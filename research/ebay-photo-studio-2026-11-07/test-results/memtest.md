# Memory across consecutive cuts (measured 2026-11-07, cloud box, 4 CPU cores, 16 GB shared limit)

Symptom: every run of cutout.py on more than one photo processed the first photo and was then killed (exit 137). Seen with birefnet-general and birefnet-general-lite, with and without decontamination.

Measurement (peak RSS from resource.getrusage, one process, birefnet-general on CPU, rembg 2.0.86, onnxruntime default options):

| step | decontaminate on | decontaminate off |
|---|---|---|
| after session load | 2065 MB | 2045 MB |
| photo 1, 1512 x 2016 | 9761 MB, 15.7 s | 9349 MB, 15.3 s |
| photo 2 | killed (137) | killed (137) |

Same, with `SessionOptions.enable_cpu_mem_arena = False` passed through `rembg.new_session(sess_opts=...)`:

| step | peak RSS | seconds |
|---|---|---|
| after session load | 2050 MB | |
| photo 1, 1512 x 2016 | 8062 MB | 18.2 |
| photo 2, 1512 x 2016 | 8116 MB | 16.0 |
| photo 3, 1932 x 2576 | 8116 MB | 16.8 |

Conclusion: the onnxruntime CPU memory arena grows on the second inference and is never returned; disabling it keeps memory flat at the cost of about two seconds per photo on CPU. tools/cutout/cutout.py now sets it off in open_session(). Scripts: memtest.py and memtest2.py in the session scratch space (not kept); the logic is three lines, reproduced in the script's docstring.
