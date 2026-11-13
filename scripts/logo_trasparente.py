"""Rende trasparente il logo L.T. Marconi su sfondo nero e crea le varianti.

Uso: python logo_trasparente.py logo_nero.png [cartella_output]
Output: logo_lt_white.png, logo_lt_dark.png, logo_icons.png
"""
import sys
from pathlib import Path

import numpy as np
from PIL import Image

src = sys.argv[1]
out = Path(sys.argv[2] if len(sys.argv) > 2 else ".")
out.mkdir(parents=True, exist_ok=True)

a = np.asarray(Image.open(src).convert("RGB")).astype(float)
m = a.max(axis=2)
alpha = np.clip((m - 12) / (60 - 12), 0, 1)
rgb = np.clip(a / np.maximum(alpha[..., None], 1e-3), 0, 255)
o = Image.fromarray(np.dstack([rgb, alpha * 255]).astype("uint8"), "RGBA")
o = o.crop(o.getbbox())
o.save(out / "logo_lt_white.png")

# Testo scuro: scurisce solo i pixel bianchi sotto la fila di tessere,
# cosi' le icone dentro le tessere restano bianche.
d = np.asarray(o).astype(float)
sat = d[..., :3].max(2) - d[..., :3].min(2)
mask = sat < 40
mask[: int(o.height * 0.575)] = False
d[mask, 0], d[mask, 1], d[mask, 2] = 28, 28, 36
Image.fromarray(d.astype("uint8"), "RGBA").save(out / "logo_lt_dark.png")

o.crop((0, 0, o.width, int(o.height * 0.54))).save(out / "logo_icons.png")
print("Creati:", *(p.name for p in sorted(out.glob("logo_*.png"))))
