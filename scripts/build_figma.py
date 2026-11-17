"""Unisce gli artboard di un canvas Design in un unico HTML autonomo per html_to_figma.

Uso:
  python build_figma.py <cartella project> <output.html> <mappa.json> [Board1 Board2 ...]

<mappa.json> associa ogni id di asset caricato sul canvas al file locale:
  {"6727b21f36ca01222cb0c8c5b68f3252": "/percorso/foto.jpg", ...}
(gli id sono la parte dopo /_blob/ negli url restituiti da upload_asset).

Senza nomi di board usa: Main Slide2 Slide3 Banner (salta quelli che non esistono).
Le foto vengono ridotte a max 1200 px e incorporate in base64: html_to_figma non
scarica risorse esterne e risponde 500 se l'HTML è troppo pesante.
Ogni artboard diventa un frame Figma (cssSelector ".board").
"""
import base64
import io
import json
import re
import sys
from pathlib import Path

from PIL import Image

proj, out, mappa = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
names = sys.argv[4:] or ["Main", "Slide2", "Slide3", "Banner"]
blobs = json.loads(mappa.read_text())


def data_uri(path):
    p = Path(path)
    if p.suffix.lower() == ".svg":
        return "data:image/svg+xml;base64," + base64.b64encode(p.read_bytes()).decode()
    im = Image.open(p)
    buf = io.BytesIO()
    if p.suffix.lower() == ".png" or im.mode in ("RGBA", "P"):
        im = im.convert("RGBA")
        im.thumbnail((1600, 1600))
        im.save(buf, "PNG", optimize=True)
        mime = "image/png"
    else:
        im = im.convert("RGB")
        im.thumbnail((1200, 1200))
        im.save(buf, "JPEG", quality=82)
        mime = "image/jpeg"
    return f"data:{mime};base64," + base64.b64encode(buf.getvalue()).decode()


boards = []
for name in names:
    f = proj / f"{name}.dc.html"
    if not f.exists():
        continue
    src = f.read_text()
    body = re.search(r"<x-dc>(.*)</x-dc>", src, re.S).group(1)
    body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
    # sostituisce i {{segnaposto}} con i default dichiarati in data-props
    props = re.search(r"data-props='(\{.*?\})'", src, re.S)
    defaults = {}
    if props:
        for k, v in json.loads(props.group(1)).items():
            if isinstance(v, dict) and "default" in v:
                defaults[k] = v["default"]
    body = re.sub(r"\{\{(\w+)\}\}", lambda m: str(defaults.get(m.group(1), "")), body)
    for bid, path in blobs.items():
        if f"/_blob/{bid}" in body:
            body = body.replace(f"/_blob/{bid}", data_uri(path))
    missing = re.findall(r"/_blob/(\w+)", body)
    if missing:
        sys.exit(f"{name}: asset senza file locale nella mappa: {sorted(set(missing))}")
    body = body.replace('<div style="width: ', f'<div class="board" data-name="{name}" style="width: ', 1)
    boards.append(body)

html = (
    '<!doctype html><html lang="it"><head><meta charset="utf-8"><title>Export</title>'
    "<style>body{margin:0;background:#ddd;display:flex;gap:80px;padding:80px;"
    "align-items:flex-start;width:max-content}</style></head><body>"
    + "".join(boards)
    + "</body></html>"
)
out.write_text(html)
print(f"{out}: {len(boards)} board, {len(html) // 1024} KB")
