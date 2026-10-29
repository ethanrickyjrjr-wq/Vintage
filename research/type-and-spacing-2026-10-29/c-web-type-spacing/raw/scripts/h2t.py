import sys, re
from bs4 import BeautifulSoup
sys.stdin.reconfigure(encoding="utf-8", errors="replace")
html = sys.stdin.read()
s = BeautifulSoup(html, "html.parser")
for t in s(["script","style","nav","footer","noscript","svg"]): t.decompose()
root = s.find("main") or s.find("article") or s.body or s
txt = root.get_text("\n")
txt = re.sub(r"\n\s*\n+", "\n\n", txt)
sys.stdout.reconfigure(encoding="utf-8")
print(txt)
