import base64, json, sys, time, urllib.request
URL = "http://127.0.0.1:11435/api/chat"
D = "/home/stanicky/social-lab/w2f/"


def run(model, prompt, imgs, num_predict=160, fmt=None):
    body = {"model": model, "stream": False, "think": False,
            "messages": [{"role": "user", "content": prompt,
                          "images": [base64.b64encode(open(p, "rb").read()).decode() for p in imgs]}],
            "options": {"num_predict": num_predict, "temperature": 0.2, "num_ctx": 4096}}
    if fmt:
        body["format"] = fmt
    t = time.time()
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
    r = json.load(urllib.request.urlopen(req, timeout=1500))
    wall = time.time() - t
    print(f"--- {model} | {[p.split('/')[-1] for p in imgs]} | wall {wall:.1f}s | prompt_tok {r.get('prompt_eval_count')} | gen_tok {r.get('eval_count')} | load {r.get('load_duration', 0) / 1e9:.1f}s | prompt_eval {r.get('prompt_eval_duration', 0) / 1e9:.1f}s | eval {r.get('eval_duration', 0) / 1e9:.1f}s")
    print(r["message"]["content"].strip())
    print(flush=True)


ALT = ("Write alt text for this photo of a vintage item for an online shop. One sentence, under 125 characters. "
       "Describe only what is visible: the object, material, colour. Do not guess brand, age or condition.")
TAG = ('List what is in this photo as JSON: {"items":[{"name":"","material":"","colour":""}],'
       '"blurry":true,"sharp_enough_for_listing":true}. Set the booleans honestly. Only what is visible.')

model, which = sys.argv[1], sys.argv[2]
if which == "alt":
    for f in ["IMG_6610_glass.jpg", "IMG_6612_boots.jpg"]:
        run(model, ALT, [D + f], 80)
elif which == "tag":
    run(model, TAG, [D + "IMG_6612_boots.jpg"], 200, "json")
    run(model, TAG, [D + "IMG_6610_glass.jpg"], 250, "json")
elif which == "vote":
    fs = ["b02_t2.0s.jpg", "b05_t7.5s.jpg", "b08_t13.5s.jpg", "b12_t20.5s.jpg"]
    run(model, "These are 4 frames from a phone video of a room, in order. Which ONE frame (1, 2, 3 or 4) would make the best Instagram Reel cover: sharp, one clear subject, uncluttered? Answer with the number and one sentence why.", [D + f for f in fs], 120)
elif which == "voterev":
    fs = ["b12_t20.5s.jpg", "b08_t13.5s.jpg", "b05_t7.5s.jpg", "b02_t2.0s.jpg"]
    run(model, "These are 4 frames from a phone video of a room, in order. Which ONE frame (1, 2, 3 or 4) would make the best Instagram Reel cover: sharp, one clear subject, uncluttered? Answer with the number and one sentence why.", [D + f for f in fs], 120)
elif which == "score":
    for f in ["b02_t2.0s.jpg", "b05_t7.5s.jpg", "b08_t13.5s.jpg", "b12_t20.5s.jpg"]:
        run(model, 'Rate this frame as an Instagram Reel cover from 1 to 10. Criteria: sharp, one clear subject, uncluttered. Reply as JSON {"subject":"","score":0}.', [D + f], 60, "json")
