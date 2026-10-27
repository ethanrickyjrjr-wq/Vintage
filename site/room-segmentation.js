// Runs only in a dedicated module worker. The room pixels never leave this worker.
// Model/runtime downloads are public, with no token or photo in any request.
const LIBRARY_URL = 'https://cdn.jsdelivr.net/npm/@huggingface/transformers@4.3.1/dist/transformers.min.js';
const MODEL = 'Xenova/detr-resnet-50-panoptic';
const REVISION = 'ea24b2d4e0bfae31f0a1299ba3fb892a2df064de';
let library;
let segmenterPromise;
let activeRequestId;
let phase = 'initializing';

function progress(message, value) {
  self.postMessage({ requestId: activeRequestId, type: 'progress', message, ...(Number.isFinite(value) ? { progress: value } : {}) });
}

async function loadSegmenter() {
  if (!segmenterPromise) {
    segmenterPromise = (async () => {
      progress('Loading room tools…');
      phase = 'library';
      library = await import(LIBRARY_URL);
      const { env, pipeline } = library;
      env.allowLocalModels = false;
      // No SharedArrayBuffer or cross-origin isolation is required. The editor
      // stays responsive because this entire pipeline runs outside its thread.
      env.backends.onnx.wasm.numThreads = 1;
      env.backends.onnx.wasm.proxy = false;
      phase = 'model';
      progress('Loading the room model…');
      const segmenter = await pipeline('image-segmentation', MODEL, {
        revision: REVISION,
        dtype: 'q8',
        device: 'wasm',
        progress_callback(event) {
          if (event.status === 'progress' && event.file?.endsWith('.onnx')) {
            progress('Downloading room model…', Math.round(event.progress));
          }
        },
      });
      // Verified against 4.3.1's ImageProcessor.resize() and real inference.
      // The stock 800/1333 setting costs substantially more memory and time.
      segmenter.processor.image_processor.size = { shortest_edge: 512, longest_edge: 768 };
      return segmenter;
    })().catch(error => {
      segmenterPromise = null;
      throw error;
    });
  }
  return segmenterPromise;
}

self.onmessage = async ({ data }) => {
  const { requestId, width, height, pixels } = data ?? {};
  activeRequestId = requestId;
  try {
    if (!Number.isInteger(width) || !Number.isInteger(height) || width < 1 || height < 1 ||
      width > 4096 || height > 4096 || width / height < .2 || width / height > 5 ||
      !(pixels instanceof ArrayBuffer) || pixels.byteLength !== width * height * 4) {
      throw new Error('Invalid room pixels');
    }
    const segmenter = await loadSegmenter();
    phase = 'inference';
    progress('Finding the room’s surfaces…');
    const gridWidth = 160;
    const gridHeight = Math.max(1, Math.round(gridWidth * height / width));
    const image = new library.RawImage(new Uint8ClampedArray(pixels), width, height, 4);
    // Do not pass subtask: 4.3.1's explicit subtask branch fails to bind its
    // postprocessor. Auto-detection selects panoptic segmentation correctly.
    const results = await segmenter(image, {
      threshold: .6,
      mask_threshold: .5,
      overlap_mask_area_threshold: .5,
      label_ids_to_fuse: [],
      target_sizes: [[gridHeight, gridWidth]],
    });
    const segments = results.map(result => ({
      label: result.label,
      score: result.score,
      mask: new Uint8Array(result.mask.data),
    }));
    self.postMessage({ requestId, type: 'result', width: gridWidth, height: gridHeight, segments },
      segments.map(segment => segment.mask.buffer));
  } catch (error) {
    // Diagnostic text contains library errors only; strip asset URLs (including
    // signed download queries). Never include pixels, tensors or user content.
    const diagnostic = String(error?.message || error?.name || 'Unknown error')
      .replace(/https?:\/\/\S+/g, '[asset]').replace(/\[[\s\S]*\]/g, '[details]').slice(0, 220);
    const retryable = phase === 'library' || phase === 'model' && /fetch|network|download|connection|timeout|401|403|404|502|503/i.test(String(error?.message));
    self.postMessage({ requestId, type: 'error', phase, diagnostic, retryable, message: 'Room suggestions could not load on this device. You can still drag your picks into place.' });
  }
};
