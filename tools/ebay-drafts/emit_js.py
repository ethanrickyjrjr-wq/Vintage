"""Print the javascript_tool snippet that fills the open eBay draft for one item.

Usage (2026-11-09): python -I gen_drafts.py, then python -I emit_js.py NN and run the
output in the draft tab (www.ebay.com/lstng?draftId=...). It PUTs title, SKU, description
and item specifics to Seller Hub's own draft endpoint, using the page's srt token, and reads
them back. It never lists. The footer comes from localStorage key hwvFooter (set once from
assets/ebay-shop-kit/listing-footer.html). Photos are uploaded separately with file_upload."""
import json, sys
from pathlib import Path

d = {x["num"]: x for x in json.loads(Path(__file__).with_name("drafts.json").read_text(encoding="utf-8"))}[sys.argv[1]]
payload = {k: d[k] for k in ("title", "description", "attributes")} | {"customLabel": d["sku"]}
payload["description"] = payload["description"].split('<div style="max-width:760px')[0]
print("await new Promise(r=>setTimeout(r,6000));const D=" + json.dumps(payload, ensure_ascii=False) + ";" + r"""
const F=localStorage.getItem('hwvFooter');if(!F||!F.includes('Vintage with a past'))throw new Error('footer missing');D.description+=F;
const h=document.documentElement.innerHTML;
const srt=(h.match(/\/lstng\/api\/listing_draft\/:draftId\(\\\\d\+\)&quot;:&quot;([^&]+)&quot;/)||[])[1];
const id=new URLSearchParams(location.search).get('draftId');
const api=location.origin+'/lstng/api/listing_draft/'+id+'?mode=AddItem';
const g=await (await fetch(api,{headers:{srt}})).text();
const pol=l=>{const m=g.match(new RegExp('"value":(\\d+),"label":\\{"_type":"TextualDisplay","textSpans":\\[\\{"_type":"TextSpan","text":"'+l.replace(/[|+]/g,c=>'\\'+c)+'"'));return m&&Number(m[1])};
const body={requestId:crypto.randomUUID(),removedFields:['price'],...D,paymentPolicyId:pol('HWV | eBay checkout | Immediate payment'),shippingPolicyId:pol('HWV | Parcel | Calculated | 2 business days'),requestMeta:{lastDeltaTimestamp:Date.now()}};
const r=await fetch(api,{method:'PUT',headers:{'Content-Type':'application/json',srt},body:JSON.stringify(body)});
const j=await (await fetch(api,{headers:{srt}})).json();
const A=JSON.stringify(j.ATTRIBUTES),T=document.body.innerText;
const got=Object.keys(D.attributes).filter(k=>D.attributes[k].every(v=>A.includes('"'+v+'"')));
JSON.stringify({id:id.slice(-4),put:r.status,cond:(T.match(/Item condition\n([^\n]*)/)||[])[1],cat:(T.match(/ITEM CATEGORY\nEdit\n([^\n]*)/)||[])[1],photos:(T.match(/\d+ out of 25 photos/)||['?'])[0],price:/"binPrice":\{"name":"price","value":"\d/.test(JSON.stringify(j.PRICE))?'SET':'empty',pols:[body.paymentPolicyId,body.shippingPolicyId].map(Boolean),ret:g.includes('HWV | Returns | 30 days | Buyer pays'),title:JSON.stringify(j.TITLE).includes(D.title),desc:JSON.stringify(j.DESCRIPTION).includes('Measurements, taken flat'),missing:Object.keys(D.attributes).filter(k=>!got.includes(k))})""")
