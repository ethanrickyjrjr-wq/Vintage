import { createServer } from "node:http";
import { readFile, stat } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createRoomWorker } from "./room-worker.mjs";

const root = path.dirname(fileURLToPath(import.meta.url));
const port = Number(process.env.PORT || 4173);
const types = { ".html": "text/html", ".js": "text/javascript", ".css": "text/css", ".webp": "image/webp", ".png": "image/png", ".jpg": "image/jpeg", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".mp4": "video/mp4", ".mp3": "audio/mpeg" };
const worker = createRoomWorker();
createServer(async (request, response) => {
  try {
    const url = new URL(request.url, `http://127.0.0.1:${port}`);
    if (url.pathname === "/api/room-preview") {
      const init = { method: request.method, headers: request.headers };
      if (!["GET", "HEAD"].includes(request.method)) { init.body = request; init.duplex = "half"; }
      // Local preview intentionally makes no paid model calls.
      const result = await worker.fetch(new Request(url, init), {});
      response.writeHead(result.status, Object.fromEntries(result.headers));
      response.end(Buffer.from(await result.arrayBuffer())); return;
    }
    const file = path.resolve(root, `.${decodeURIComponent(url.pathname === "/" ? "/storefront.html" : url.pathname)}`);
    if (!file.startsWith(root + path.sep) || !["GET", "HEAD"].includes(request.method) || ![".html", ".js", ".css", ".webp", ".png", ".jpg", ".svg", ".woff2", ".mp4", ".mp3"].includes(path.extname(file))) { response.writeHead(404); response.end(); return; }
    const info = await stat(file);
    if (!info.isFile()) { response.writeHead(404); response.end(); return; }
    response.writeHead(200, { "content-type": types[path.extname(file)], "cache-control": "no-store" });
    response.end(request.method === "HEAD" ? undefined : await readFile(file));
  } catch { response.writeHead(404); response.end(); }
}).listen(port, "127.0.0.1", () => console.log(`Local: http://127.0.0.1:${port}`));
