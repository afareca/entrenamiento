# -*- coding: utf-8 -*-
"""Núcleo v3.0 — core posparto, 10 min diarios, rutina que rota por día.
Edita PROGRAMA y corre: python3 build.py  ->  dist/core.html (autocontenido).

Imágenes: pon el archivo en medios/ con el id del ejercicio (puente.png, gato.gif...).
  · .mp4 (H.264) -> video en bucle, sin sonido · .gif / .webp / .jpg -> se muestra tal cual
  · .png horizontal de 4 cuadros (ancho >= 3x alto) -> la app lo anima en bucle
  · .png normal -> imagen fija
Si no hay archivo en medios/, usa el GIF de catálogo de RESPALDO, luego la figura animada, luego un orbe."""
import base64, json, os, struct

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()

def png_size(p):
    with open(p, "rb") as f:
        f.read(16); w, h = struct.unpack(">II", f.read(8))
    return w, h

# ---------- ejercicios (id = nombre de archivo en medios/) ----------
# seg: duración total · lados: se parte en dos con aviso de cambio · anim: figura animada de respaldo
def e(id, nombre, seg, cue, anim=None, lados=False):
    return dict(id=id, nombre=nombre, seg=seg, cue=cue, anim=anim, lados=lados)

RESPIRA = "Boca arriba, rodillas dobladas. Inhala expandiendo costillas hacia los lados y la espalda. Exhala largo, como soplando una vela."
FIJO = [
    e("respira", "Respiración 360", 45, RESPIRA, anim="respira"),
    e("piso", "Piso pélvico lento", 45, "Al exhalar, cierra y sube como si aguantaras un gas y la orina a la vez. Sostén 5 s. Suelta del todo 5 s.", anim="piso"),
    e("piso", "Piso pélvico rápido", 20, "Aprieta y suelta rápido. Suelta completo cada vez.", anim="rapido"),
]
# Día D: movilidad, igual en las tres fases
MOVILIDAD = [
    e("gato", "Gato–camello", 60, "En cuatro apoyos. Inhala al arquear, exhala al redondear. Vértebra por vértebra."),
    e("toracica", "Rotación torácica", 60, "En cuatro apoyos, mano en la nuca. Abre el pecho hacia el techo siguiendo el codo con la mirada.", lados=True),
    e("flexor_cadera", "Flexor de cadera", 60, "Una rodilla en el piso. Aprieta el glúteo de atrás y lleva la cadera adelante. Espalda erguida.", lados=True),
    e("figura4", "Glúteo en figura 4", 60, "Tobillo sobre la rodilla contraria. Abraza el muslo hacia el pecho sin levantar la cabeza.", lados=True),
    e("isquios", "Isquiotibiales con banda", 60, "Pierna estirada al techo, banda en el pie. Tira suave, sin dolor detrás de la rodilla.", lados=True),
    e("nino", "Postura del niño", 45, "Glúteos a los talones, brazos al frente. Respira hacia la espalda baja."),
]

PROGRAMA = [
  dict(n=1, nombre="Reconexión", semanas="1 a 4",
       meta="Volver a sentir el piso pélvico y el abdomen profundo. Nada de esfuerzo: precisión.",
       dias=dict(
    A=[e("bascula", "Báscula pélvica", 45, "Exhala y aplana suave la zona lumbar contra el piso. Inhala y vuelve. Movimiento pequeño."),
       e("talon", "Deslizamiento de talón", 60, "Exhala, activa el abdomen bajo y desliza un talón hasta estirar la pierna. Inhala y vuelve. Alterna.", anim="talon"),
       e("marcha_supina", "Marcha boca arriba", 60, "Exhala y sube una rodilla a 90° sin que la pelvis se mueva. Baja lento. Alterna."),
       e("deadbug", "Dead bug con talón", 45, "Rodillas a 90°. Exhala y baja un talón a tocar el piso. Lumbar quieta. Alterna."),
       e("birddog", "Bird dog", 60, "En cuatro apoyos. Exhala y extiende brazo y pierna contrarios sin girar la cadera. Alterna.", anim="bird"),
       e("plancha_lat_inclinada", "Plancha lateral inclinada", 60, "Antebrazo sobre el sofá, cuerpo recto. Respira normal, no aguantes el aire.", lados=True)],
    B=[e("puente", "Puente de glúteo", 60, "Exhala, activa piso pélvico y sube la cadera. Inhala arriba, baja lento."),
       e("pierna_lateral", "Pierna lateral", 80, "De lado, cadera apilada. Sube la pierna de arriba sin rotar el pie hacia el techo.", lados=True),
       e("almeja", "Almeja", 80, "De lado, rodillas dobladas. Abre la rodilla de arriba sin que la cadera ruede hacia atrás.", lados=True),
       e("sentarse_pararse", "Sentarse y pararse", 60, "Desde el borde de una silla. Exhala al pararte, sin impulso de brazos."),
       e("puente", "Puente sostenido", 45, "Sube y quédate arriba respirando. Glúteos apretados, costillas abajo.")],
    C=[e("flexion_pared", "Flexión en pared", 60, "Manos en la pared a la altura del pecho. Exhala al empujar. Cuerpo en una sola línea."),
       e("apertura_banda", "Apertura con banda", 60, "Brazos rectos. Junta los omóplatos sin subir los hombros."),
       e("angel_pared", "Ángel en pared", 60, "Espalda, cabeza y glúteos contra la pared. Sube los brazos sin despegarlos."),
       e("remo_banda", "Remo con banda", 60, "Sentada, piernas estiradas. Codos atrás, pecho alto. Exhala al tirar."),
       e("press_banda", "Press de hombro con banda", 60, "De pie sobre la banda. Exhala al empujar arriba, costillas abajo."),
       e("birddog", "Bird dog", 60, "Para cerrar: espalda larga, brazo y pierna contrarios. Alterna.", anim="bird")],
    D=MOVILIDAD)),
  dict(n=2, nombre="Control", semanas="5 a 8",
       meta="Mantener el abdomen profundo activo mientras brazos y piernas se mueven.",
       dias=dict(
    A=[e("marcha_supina", "Marcha boca arriba", 45, "Más lenta: 3 s arriba, 3 s abajo."),
       e("deadbug", "Dead bug", 60, "Exhala y extiende brazo y pierna contrarios. Si el abdomen se abomba, vuelve a la versión con talón."),
       e("birddog", "Bird dog", 60, "Pausa de 2 s extendida, sin girar la cadera.", anim="bird"),
       e("plancha_lat_inclinada", "Plancha lateral inclinada", 60, "Cuerpo recto, respiración normal.", lados=True),
       e("pallof", "Pallof con banda", 60, "Banda anclada a un lado. Empuja al frente y resiste el giro. Exhala al extender.", lados=True),
       e("toque", "Plancha con toque de hombro", 40, "En rodillas. Toca el hombro contrario sin balancear la cadera.")],
    B=[e("puente_marcha", "Puente con marcha", 60, "Sube el puente y levanta un pie sin que la cadera se caiga. Alterna."),
       e("paso_lateral", "Paso lateral con banda", 60, "Banda en las rodillas, semiflexionada. Pasos amplios, pies paralelos."),
       e("sentadilla", "Sentadilla", 60, "Exhala al subir. Rodillas siguen la línea de los pies."),
       e("zancada_atras", "Zancada atrás", 60, "Con una mano en la silla. Baja vertical, rodilla de atrás cerca del piso.", lados=True),
       e("almeja", "Almeja con banda", 60, "Banda sobre las rodillas. Abre lento, cierra más lento.", lados=True),
       e("pierna_lateral", "Pierna lateral", 40, "3 s arriba, 3 s abajo.", lados=True)],
    C=[e("flexion_inclinada", "Flexión inclinada", 60, "Manos sobre una mesa firme. Exhala al subir."),
       e("remo_banda", "Remo con banda", 60, "Pausa de 1 s con los codos atrás."),
       e("apertura_banda", "Apertura con banda", 50, "Banda más corta que en la fase 1."),
       e("press_banda", "Press de hombro con banda", 50, "Exhala al empujar. Sin arquear la lumbar."),
       e("angel_pared", "Ángel en pared", 50, "Más lento, sin despegar los codos."),
       e("birddog", "Bird dog", 60, "Pausa de 2 s extendida.", anim="bird")],
    D=MOVILIDAD)),
  dict(n=3, nombre="Fuerza", semanas="9 a 12",
       meta="Cargar. El core ya responde; ahora se construye tono con resistencia.",
       dias=dict(
    A=[e("deadbug", "Dead bug completo", 60, "Brazo y pierna contrarios, lento. Lumbar pegada al piso."),
       e("plancha_lateral", "Plancha lateral", 60, "Sobre rodillas si la completa abomba el abdomen o te hace aguantar el aire.", lados=True),
       e("pallof", "Pallof con banda", 60, "Banda más tensa. Sostén 3 s con brazos extendidos.", lados=True),
       e("toque", "Plancha con toque de hombro", 45, "Toca el hombro contrario sin balancear la cadera."),
       e("oso", "Oso sostenido", 40, "Rodillas a dos centímetros del piso, espalda plana. Respira, no aguantes el aire."),
       e("birddog", "Bird dog", 45, "Pausa de 2 s extendida.", anim="bird")],
    B=[e("goblet", "Sentadilla goblet", 60, "Kettlebell de 8 kg al pecho. Exhala al subir, piso pélvico activo."),
       e("puente_una_pierna", "Puente a una pierna", 60, "Una pierna estirada. Sube sin que la cadera se ladee.", lados=True),
       e("zancada_atras", "Zancada atrás", 60, "Sin apoyo si mantienes el equilibrio.", lados=True),
       e("peso_muerto_kb", "Peso muerto con kettlebell", 60, "8 kg con las dos manos. Cadera atrás, espalda recta. Exhala al subir."),
       e("paso_lateral", "Paso lateral con banda", 60, "Banda más tensa, más abajo."),
       e("puente_marcha", "Puente con marcha", 40, "Sin que la cadera se caiga.")],
    C=[e("rodillas", "Flexión en rodillas", 55, "Exhala al subir. Si se hunde la cadera, vuelve a la inclinada."),
       e("remo_kb", "Remo con kettlebell", 60, "8 kg, una mano y una rodilla en el banco. Codo a la cadera.", lados=True),
       e("press_banda", "Press de hombro con banda", 60, "Banda más tensa."),
       e("apertura_banda", "Apertura con banda", 55, "Pausa de 1 s abierta."),
       e("flexion_inclinada", "Flexión inclinada", 50, "Lenta: 3 s abajo."),
       e("angel_pared", "Ángel en pared", 50, "Sin despegar los codos.")],
    D=MOVILIDAD)),
]
NOMBRE_DIA = dict(A="Core profundo", B="Glúteo y piernas", C="Espalda, brazos y postura", D="Movilidad y estiramientos")
ROTACION = ["A", "B", "C", "A", "B", "C", "D"]
TRANS = 10

# GIFs de catálogo que ya usaba la versión anterior: respaldo mientras llegan las imágenes propias
RESPALDO = {"bascula": "3147", "puente": "3013", "pierna_lateral": "0710", "deadbug": "0276", "flexion_pared": "0659",
            "puente_marcha": "3561", "plancha_lat_inclinada": "3544", "flexion_inclinada": "0493", "pallof": "0979",
            "goblet": "0534", "puente_una_pierna": "3645", "plancha_lateral": "0705", "rodillas": "3211", "toque": "3239"}

# ---------- medios ----------
ids = sorted({p["id"] for f in PROGRAMA for d in f["dias"].values() for p in d} | {p["id"] for p in FIJO})
MEDIA, propias, respaldo, sin = {}, [], [], []
for i in ids:
    hecho = False
    for ext, mime in (("mp4", "video/mp4"), ("gif", "image/gif"), ("webp", "image/webp"), ("jpg", "image/jpeg"), ("png", "image/png")):
        p = f"medios/{i}.{ext}"
        if os.path.exists(p):
            tipo = "video" if ext == "mp4" else "img"
            if ext == "png":
                w, h = png_size(p)
                if w >= 3 * h: tipo = "hoja"
            MEDIA[i] = dict(src=b64(p, mime), tipo=tipo)
            if tipo == "video" and os.path.exists(f"medios/{i}.poster.jpg"): MEDIA[i]["poster"] = b64(f"medios/{i}.poster.jpg", "image/jpeg")
            if tipo == "hoja": MEDIA[i]["ar"] = round(w / 4 / h, 4)
            propias.append(i); hecho = True; break
    if not hecho and i in RESPALDO:
        MEDIA[i] = dict(src=b64(f"gifs/{RESPALDO[i]}.gif", "image/gif"), tipo="img"); respaldo.append(i); hecho = True
    if not hecho: sin.append(i)

for f in PROGRAMA:
    f["total"] = {}
    for k, lista in f["dias"].items():
        pasos = FIJO + lista
        f["dias"][k] = pasos
        f["total"][k] = sum(p["seg"] for p in pasos) + TRANS * (len(pasos) - 1) + 5
    print(f"Fase {f['n']} {f['nombre']}: " + " · ".join(f"{k} {t//60}:{t%60:02d}" for k, t in f["total"].items()))
print(f"Imágenes propias: {len(propias)} · respaldo catálogo: {len(respaldo)} · sin imagen: {len(sin)} {sin}")

def esc(o):
    return json.dumps(o, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")

html = open("plantilla.html", encoding="utf-8").read()
out = (html.replace("__DATA__", esc(dict(programa=PROGRAMA, trans=TRANS, dias=NOMBRE_DIA, rotacion=ROTACION)))
           .replace("__MEDIA__", esc(MEDIA))
           .replace("__ICON__", b64("icon.png", "image/png"))
           .replace("__FIGURA__", open("figura.js", encoding="utf-8").read()))
os.makedirs("dist", exist_ok=True)
open("dist/core.html", "w", encoding="utf-8").write(out)
print("OK dist/core.html", round(len(out.encode()) / 1e6, 2), "MB")
