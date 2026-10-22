# -*- coding: utf-8 -*-
"""Fuerza v2.0 — kettlebells 8/12 kg y bandas, 2 sesiones por semana, 8 semanas.
Edita SESIONES / SEMANAS y corre: python3 build.py  ->  dist/index.html (autocontenido)."""
import base64, json, os

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()

# ---------- ejercicios ----------
# u: 'reps' (toca Hecho al terminar) · 'seg' (temporizado) · 'max' (máximas menos 2)
# kg: carga, fija o por semana · lado: por lado · anim: tempo del orbe si no hay GIF
def ej(nombre, cue, gif=None, u="reps", n=None, kg=None, lado=False, anim=None):
    # kg: carga fija o {semana_desde: kg}, p. ej. {1: 12, 3: 16}
    if isinstance(kg, (int, float)): kg = {1: kg}
    return dict(nombre=nombre, cue=cue, gif=gif, u=u, n=n, kg=kg, lado=lado, anim=anim)

CALENTAMIENTO = [
    ej("Gato–camello", "Vértebra por vértebra. Inhala al arquear, exhala al redondear.", gif="gato", u="seg", n=35, anim="gato"),
    ej("Bisagra de cadera", "Sin peso. Cadera atrás, espalda neutra, rodillas suaves.", gif="bisagra", u="seg", n=35, anim="bisagra"),
    ej("Sentadilla profunda", "Talones en el piso. Codos abren las rodillas. Respira abajo.", gif="sentadilla", u="seg", n=40, anim="sostén"),
    ej("Rotación torácica", "En cuatro apoyos, mano en la nuca. Abre el pecho al techo. Cambia a mitad.", gif="toracica", u="seg", n=40, anim="rota", lado=True),
    ej("Apertura con banda", "Brazos rectos. Junta los omóplatos sin subir los hombros.", gif="apertura", u="seg", n=30, anim="abre"),
]

SESIONES = {
  "A": dict(nombre="Sesión A", enfoque="Bisagra y empuje", bloques=[
    dict(ej=[ej("Swing ruso", "Bisagra, no sentadilla. La pesa sube por la cadera, no por los brazos.", "swing", n=12, kg=16),
             ej("Flexiones", "Cuerpo en línea. Glúteo apretado. Si no llegas a 8, eleva las manos.", "flexion", u="max")]),
    dict(ej=[ej("Goblet squat", "Pesa pegada al pecho. Baja en 3 segundos, pausa 1, sube en 1.", "goblet", n=10, kg={1: 12, 3: 16}),
             ej("Remo a una mano", "Codo hacia la cadera, no hacia afuera. Sin rotar el torso.", "remo", n=8, kg={1: 12, 3: 16}, lado=True)]),
    dict(cierre=True, ej=[ej("Suitcase carry", "Una sola mano. Hombros nivelados. El trabajo es no inclinarte.", "carry", u="seg", n=60, kg=16, lado=True)]),
  ]),
  "B": dict(nombre="Sesión B", enfoque="Unilateral y tracción", bloques=[
    dict(ej=[ej("Peso muerto rumano a una pierna", "Pesa en la mano contraria a la pierna de apoyo. Cadera atrás.", "pmr", n=8, kg={1: 8, 5: 12}, lado=True),
             ej("Press militar a una mano", "Aprieta glúteo y abdomen antes de empujar. Sin arquear la lumbar.", "press", n=8, kg={1: 8, 5: 12}, lado=True)]),
    dict(ej=[ej("Split squat", "Pie trasero elevado. El peso adelante. Baja vertical.", "split", n=8, kg={1: 12, 5: 16}, lado=True),
             ej("Apertura posterior con banda", "Codos altos, tira hacia la cara. Compensa el escritorio.", "banda", n=20)]),
    dict(cierre=True, ej=[ej("Dead bug", "Lumbar pegada al piso todo el tiempo. Si se despega, acorta el rango.", "deadbug", n=10, lado=True)]),
  ]),
}

# ---------- progresión por semana ----------
SEMANAS = {
  1: dict(fase="Adaptación",   rondas=2, desc=45, rpe="6",     extra=0),
  2: dict(fase="Adaptación",   rondas=2, desc=45, rpe="6",     extra=0),
  3: dict(fase="Construcción", rondas=3, desc=45, rpe="7",     extra=0),
  4: dict(fase="Construcción", rondas=3, desc=45, rpe="7",     extra=0),
  5: dict(fase="Densidad",     rondas=3, desc=45, rpe="7 a 8", extra=0),
  6: dict(fase="Densidad",     rondas=3, desc=30, rpe="7 a 8", extra=0),
  7: dict(fase="Pico",         rondas=3, desc=30, rpe="8",     extra=2),
  8: dict(fase="Descarga",     rondas=2, desc=45, rpe="6",     extra=0),
}

# Medios: medios/<nombre>.mp4 (H.264) o, de respaldo, el GIF de catálogo de la versión anterior
RESPALDO = {"swing": "0549", "flexion": "0662", "goblet": "0534", "remo": "0541", "carry": "2133", "pmr": "1757",
            "press": "0361", "split": "0410", "banda": "0993", "deadbug": "0276"}
todos = [e for s in SESIONES.values() for b in s["bloques"] for e in b["ej"]] + CALENTAMIENTO
usados = sorted({e["gif"] for e in todos if e["gif"]})
MEDIA = {}
for i in usados:
    if os.path.exists(f"medios/{i}.mp4"):
        MEDIA[i] = dict(src=b64(f"medios/{i}.mp4", "video/mp4"), tipo="video")
        if os.path.exists(f"medios/{i}.poster.jpg"): MEDIA[i]["poster"] = b64(f"medios/{i}.poster.jpg", "image/jpeg")
    elif i in RESPALDO: MEDIA[i] = dict(src=b64(f"gifs/{RESPALDO[i]}.gif", "image/gif"), tipo="img")
print("Medios:", sum(1 for m in MEDIA.values() if m["tipo"] == "video"), "videos propios ·", sum(1 for m in MEDIA.values() if m["tipo"] == "img"), "GIF de respaldo")

def esc(o):
    return json.dumps(o, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")

html = open("plantilla.html", encoding="utf-8").read()
out = (html.replace("__DATA__", esc(dict(sesiones=SESIONES, semanas=SEMANAS, calentamiento=CALENTAMIENTO)))
           .replace("__MEDIA__", esc(MEDIA))
           .replace("__ICON__", b64("icon.png", "image/png")))
os.makedirs("dist", exist_ok=True)
open("dist/index.html", "w", encoding="utf-8").write(out)
print("OK dist/index.html", round(len(out.encode()) / 1e6, 2), "MB")
