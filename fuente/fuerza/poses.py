# -*- coding: utf-8 -*-
"""Arma la tira de 4 poses clave de cada ejercicio: medios/<id>.poses.jpg (1536 x 384).
Uso: python3 poses.py <carpeta con fuerza_<id>.gif de 48 cuadros  |  hojas <id>.png de 4 cuadros>
De un GIF interpolado toma los cuadros 0, n/4, n/2 y 3n/4, que son las poses dibujadas (sin fantasmas).
Alinea el piso entre poses para que la figura no salte al fundir."""
import sys, os, glob
from PIL import Image, ImageChops

def cuadros(ruta):
    im = Image.open(ruta)
    n = getattr(im, "n_frames", 1)
    if n > 1:
        out = []
        for j in range(4):
            im.seek(int(j * n / 4)); out.append(im.convert("RGB"))
        return out
    im = im.convert("RGB"); w, h = im.size
    return [im.crop((int(k * w / 4), 0, int((k + 1) * w / 4), h)) for k in range(4)]

def piso(im):
    fondo = Image.new("RGB", im.size, im.getpixel((2, 2)))
    caja = ImageChops.difference(im, fondo).convert("L").point(lambda v: 255 if v > 40 else 0).getbbox()
    return caja[3] if caja else im.size[1]

src = sys.argv[1]
for ruta in sorted(glob.glob(os.path.join(src, "*.gif")) + glob.glob(os.path.join(src, "*.png"))):
    i = os.path.basename(ruta).rsplit(".", 1)[0]
    i = i[7:] if i.startswith("fuerza_") else i
    fs = [f.resize((384, 384), Image.LANCZOS) for f in cuadros(ruta)]
    bajos = [piso(f) for f in fs]; ref = max(bajos)
    tira = Image.new("RGB", (1536, 384), fs[0].getpixel((2, 2)))
    for k, f in enumerate(fs):
        dy = ref - bajos[k]
        dy = dy if 0 < dy <= 20 else 0
        lienzo = Image.new("RGB", (384, 384), f.getpixel((2, 2))); lienzo.paste(f, (0, dy))
        tira.paste(lienzo, (k * 384, 0))
    tira.save(f"medios/{i}.poses.jpg", quality=84, optimize=True)
    print(i, "ajuste de piso:", [ref - b for b in bajos])
