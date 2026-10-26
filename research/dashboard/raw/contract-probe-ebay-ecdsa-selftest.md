# contract probe: eBay notification signature algorithm self-test under Deno, 2026-10-26

Algorithm source (eBay's own SDK, https://github.com/eBay/event-notification-nodejs-sdk, files lib/validator.js, lib/client.js, lib/constants.js, fetched today into raw/contract-gh-ebay-notif-sdk-*):
1. `sig = JSON.parse(Buffer.from(headers['x-ebay-signature'], 'base64').toString('ascii'))` -> uses `sig.kid` and `sig.signature`
2. GET `https://api.ebay.com/commerce/notification/v1/public_key/{kid}` with `Authorization: Bearer <application token>` (client-credentials) -> `{algorithm, digest, key}`; cache by kid (SDK: LRU 100; eBay docs: about 1 hour)
3. PEM = `-----BEGIN PUBLIC KEY-----\n` + key + `\n-----END PUBLIC KEY-----` (SDK inserts the header/footer around the bare key string)
4. `crypto.createVerify('ssl3-sha1')`; `.update(JSON.stringify(parsedBody))`; `.verify(PEM, sig.signature, 'base64')`
   -> 204 on success, 412 on failure (SDK behaviour)
Note the SDK verifies over `JSON.stringify(req.body)` (parsed then re-serialised), not over the raw bytes.

Self-test (local Deno 2.7.13, a locally generated P-256 key; NOT an eBay key, NOT the Supabase Edge Runtime):
```
// Self-test (no eBay data): does the algorithm used by eBay's own SDK work under Deno?
// SDK: crypto.createVerify('ssl3-sha1'); verifier.update(JSON.stringify(message)); verifier.verify(pemKey, signatureB64, 'base64')
import { createSign, createVerify, generateKeyPairSync } from "node:crypto";
const { publicKey, privateKey } = generateKeyPairSync("ec", { namedCurve: "prime256v1" });
const msg = JSON.stringify({ metadata: { topic: "X" }, notification: { n: 1 } });
// 1) node:crypto path exactly as the SDK, DER signature
const sig = createSign("ssl3-sha1").update(msg).sign(privateKey, "base64");
console.log("node:crypto ssl3-sha1 verify (DER sig):", createVerify("ssl3-sha1").update(msg).verify(publicKey, sig, "base64"));
// 2) key formatting as SDK does it: strip PEM header/footer to bare base64, then re-add
const pem = publicKey.export({ type: "spki", format: "pem" }) as string;
const bare = pem.replace(/-----(BEGIN|END) PUBLIC KEY-----/g, "").replace(/\s+/g, "");
const rebuilt = bare.replace(/^/, "-----BEGIN PUBLIC KEY-----\n").replace(/$/, "\n-----END PUBLIC KEY-----");
console.log("verify with SDK-style rebuilt PEM:", createVerify("ssl3-sha1").update(msg).verify(rebuilt, sig, "base64"));
// 3) WebCrypto path: ECDSA + SHA-1 needs raw r||s (P1363), not DER
const p1363 = createSign("sha1").update(msg).sign({ key: privateKey, dsaEncoding: "ieee-p1363" });
const spki = Uint8Array.from(atob(bare), (c) => c.charCodeAt(0));
const k = await crypto.subtle.importKey("spki", spki, { name: "ECDSA", namedCurve: "P-256" }, false, ["verify"]);
console.log("WebCrypto ECDSA/SHA-1 verify (P1363 sig):", await crypto.subtle.verify({ name: "ECDSA", hash: "SHA-1" }, k, p1363, new TextEncoder().encode(msg)));
// 4) WebCrypto with DER sig directly (expected to fail -> builder must convert DER to r||s)
const der = Uint8Array.from(atob(sig), (c) => c.charCodeAt(0));
console.log("WebCrypto verify with DER sig (expect false/throw):", await crypto.subtle.verify({ name: "ECDSA", hash: "SHA-1" }, k, der, new TextEncoder().encode(msg)).catch((e) => "throws: " + e.message));
```

Output:
```
node:crypto ssl3-sha1 verify (DER sig): true
verify with SDK-style rebuilt PEM: true
WebCrypto ECDSA/SHA-1 verify (P1363 sig): true
WebCrypto verify with DER sig (expect false/throw): false
```

Reading: (1) `node:crypto` `createVerify('ssl3-sha1')` works in Deno and accepts a DER ECDSA signature exactly as the SDK uses it. (2) The SDK-style PEM rebuild works. (3) WebCrypto `ECDSA` + `SHA-1` works only with a raw r||s (IEEE P1363) signature. (4) WebCrypto with the DER signature returns false, so if the builder uses `crypto.subtle` it must convert DER to r||s first. Prefer `node:crypto` (npm-compat) to mirror the SDK.
Unverified: the curve of eBay's real key (`PublicKey.algorithm` is documented only as "such as ... ECDSA", `digest` "such as ... SHA1"); whether eBay signs the raw body bytes or the re-serialised JSON; whether `node:crypto` `createVerify('ssl3-sha1')` exists in Supabase's Edge Runtime.
