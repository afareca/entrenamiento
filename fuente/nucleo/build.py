# -*- coding: utf-8 -*-
"""Núcleo v2.0 — core posparto, 10 min diarios.
Edita PROGRAMA y corre: python3 build.py  ->  dist/core.html (autocontenido)."""
import base64, json, os

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()

# ---------- el programa ----------
# seg: duración total · lados: se parte en dos con aviso de cambio · anim: tempo del orbe cuando no hay GIF
def e(nombre, seg, cue, gif=None, anim=None, lados=False):
    return dict(nombre=nombre, seg=seg, cue=cue, gif=gif, anim=anim, lados=lados)

RESPIRA = "Acostada boca arriba, rodillas dobladas. Inhala expandiendo costillas hacia los lados y la espalda. Exhala largo, como soplando una vela."
PROGRAMA = [
  dict(n=1, nombre="Reconexión", semanas="1 a 4",
       meta="Volver a sentir el piso pélvico y el abdomen profundo. Nada de esfuerzo: precisión.",
       pasos=[
    e("Respiración 360", 60, RESPIRA, anim="respira"),
    e("Piso pélvico lento", 60, "Al exhalar, cierra y sube como si aguantaras un gas y la orina a la vez. Sostén 5 s. Suelta del todo 5 s.", anim="piso"),
    e("Piso pélvico rápido", 30, "Aprieta y suelta rápido. Lo importante es soltar completo cada vez.", anim="rapido"),
    e("Báscula pélvica", 45, "Exhala y aplana suave la zona lumbar contra el piso. Inhala y vuelve. Movimiento pequeño.", gif="3147"),
    e("Deslizamiento de talón", 60, "Exhala, activa el abdomen bajo y desliza un talón hasta estirar la pierna. Inhala y vuelve. Alterna.", anim="talon"),
    e("Puente de glúteo", 45, "Exhala, activa piso pélvico y sube la cadera. Inhala arriba, baja lento.", gif="3013"),
    e("Pierna lateral", 80, "De lado, cadera apilada. Sube la pierna de arriba sin rotar el pie hacia el techo.", gif="0710", lados=True),
    e("Dead bug con talón", 45, "Rodillas a 90°. Exhala y baja un talón a tocar el piso. Lumbar quieta. Alterna.", gif="0276"),
    e("Flexión en pared", 40, "Manos en la pared a la altura del pecho. Exhala al empujar. Cuerpo en una sola línea.", gif="0659"),
    e("Respiración de cierre", 30, RESPIRA, anim="respira"),
  ]),
  dict(n=2, nombre="Control", semanas="5 a 8",
       meta="Mantener el abdomen profundo activo mientras brazos y piernas se mueven.",
       pasos=[
    e("Respiración y piso pélvico", 60, "Tres respiraciones 360 y luego contracciones lentas al exhalar: 5 s arriba, 5 s suelta.", anim="piso"),
    e("Puente con marcha", 45, "Sube el puente y levanta un pie sin que la cadera se caiga. Alterna.", gif="3561"),
    e("Dead bug", 45, "Exhala y extiende brazo y pierna contrarios. Si el abdomen se abomba en la línea media, vuelve a la versión con talón.", gif="0276"),
    e("Bird dog", 60, "En cuatro apoyos. Exhala y extiende brazo y pierna contrarios sin girar la cadera. Inhala y vuelve. Alterna.", anim="bird"),
    e("Plancha lateral inclinada", 60, "Antebrazo sobre una silla o sofá, cuerpo recto. Respira normal, no aguantes el aire.", gif="3544", lados=True),
    e("Flexión inclinada", 40, "Manos sobre una mesa o sofá firme. Exhala al subir.", gif="0493"),
    e("Pallof con banda", 60, "Banda anclada a un lado. Empuja las manos al frente y resiste el giro. Exhala al extender.", gif="0979", lados=True),
    e("Sentadilla sin peso", 45, "Exhala al subir. Rodillas siguen la línea de los pies.", gif="0534"),
    e("Pierna lateral", 60, "Más lenta que en la fase 1: 3 s arriba, 3 s abajo.", gif="0710", lados=True),
    e("Respiración de cierre", 30, RESPIRA, anim="respira"),
  ]),
  dict(n=3, nombre="Fuerza", semanas="9 a 12",
       meta="Cargar. El core ya responde; ahora se construye tono con resistencia.",
       pasos=[
    e("Respiración y piso pélvico", 45, "Respiración 360 y contracciones lentas al exhalar.", anim="piso"),
    e("Sentadilla goblet", 45, "Kettlebell de 8 kg al pecho. Exhala al subir, piso pélvico activo.", gif="0534"),
    e("Puente a una pierna", 60, "Una pierna estirada. Sube sin que la cadera se ladee.", gif="3645", lados=True),
    e("Dead bug completo", 45, "Brazo y pierna contrarios, lento. Lumbar pegada al piso.", gif="0276"),
    e("Plancha lateral", 60, "Sobre rodillas si la completa abomba el abdomen o te hace aguantar el aire.", gif="0705", lados=True),
    e("Flexión en rodillas", 40, "Exhala al subir. Si se hunde la cadera, vuelve a la inclinada.", gif="3211"),
    e("Pallof con banda", 60, "Banda más tensa que en fase 2. Sostén 3 s con brazos extendidos.", gif="0979", lados=True),
    e("Plancha con toque de hombro", 40, "En rodillas. Toca el hombro contrario sin balancear la cadera.", gif="3239"),
    e("Bird dog", 40, "Pausa de 2 s extendida.", anim="bird"),
    e("Respiración de cierre", 30, RESPIRA, anim="respira"),
  ]),
]

TRANS = 10   # segundos entre ejercicios
for f in PROGRAMA:
    total = sum(p["seg"] for p in f["pasos"]) + TRANS * (len(f["pasos"]) - 1) + 5
    f["total"] = total
    print(f"Fase {f['n']} {f['nombre']}: {len(f['pasos'])} ejercicios, {total//60}:{total%60:02d}")

usados = sorted({p["gif"] for f in PROGRAMA for p in f["pasos"] if p["gif"]})
MEDIA = {i: b64(f"gifs/{i}.gif", "image/gif") for i in usados}
ICON = b64("icon.png", "image/png")

def esc(o):
    return json.dumps(o, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")

html = open("plantilla.html", encoding="utf-8").read()
out = (html.replace("__DATA__", esc(dict(programa=PROGRAMA, trans=TRANS)))
           .replace("__MEDIA__", esc(MEDIA))
           .replace("__ICON__", ICON)
           .replace("__FIGURA__", open("figura.js", encoding="utf-8").read()))
os.makedirs("dist", exist_ok=True)
open("dist/core.html", "w", encoding="utf-8").write(out)
print("OK dist/core.html", round(len(out.encode()) / 1e6, 2), "MB")
