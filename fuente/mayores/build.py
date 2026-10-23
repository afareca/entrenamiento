# -*- coding: utf-8 -*-
"""Vigor y Amplitud — 65+, hipertensión controlada, sin equipo, 10 a 14 min diarios.
Corre: python3 build.py  ->  dist/vigor.html y dist/amplitud.html (autocontenidos).
Imágenes en medios/<app>/<id>.mp4 | .gif | .jpg | .png (hoja de 4 cuadros se anima sola)."""
import base64, json, os, struct

def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(p, "rb").read()).decode()

def png_size(p):
    with open(p, "rb") as f:
        f.read(16); w, h = struct.unpack(">II", f.read(8))
    return w, h

def e(id, nombre, seg, cue, lados=False):
    return dict(id=id, nombre=nombre, seg=seg, cue=cue, anim=None, lados=lados)

def circuito(lista, vueltas=2):
    """Repite la lista como circuito; las vueltas siguientes llevan su número en el nombre."""
    out = list(lista)
    for v in range(2, vueltas + 1):
        out += [dict(p, nombre=f"{p['nombre']} · vuelta {v}") for p in lista]
    return out

AIRE = "Exhala en el esfuerzo. Nunca aguantes el aire."

# ======================= VIGOR · Mauricio =======================
V_FIJO = [
    e("marcha", "Marcha en el sitio", 50, "Sube las rodillas y balancea los brazos. Respira cómodo."),
    e("circulos_brazos", "Círculos de brazos", 40, "Círculos amplios hacia adelante y luego hacia atrás. Hombros abajo."),
    e("bisagra", "Bisagra de cadera", 40, "Manos en la cadera. Cadera atrás con la espalda recta, vuelve apretando glúteos."),
]
V_MOVILIDAD = [
    e("gato", "Gato–camello", 60, "En cuatro apoyos. Inhala al arquear, exhala al redondear."),
    e("abre_libro", "Libro abierto", 60, "De lado. Abre el brazo de arriba siguiéndolo con la mirada.", lados=True),
    e("pantorrilla_pared", "Pantorrilla en pared", 60, "Talón de atrás en el piso. Lleva la cadera hacia la pared.", lados=True),
    e("isquios_silla", "Isquiotibiales en silla", 60, "Pierna estirada, espalda recta. Inclínate desde la cadera.", lados=True),
    e("pecho_puerta", "Pecho en el marco de la puerta", 45, "Antebrazos en el marco. Avanza el pecho sin arquear la espalda."),
    e("flexor_cadera", "Flexor de cadera", 60, "Rodilla en un cojín, mano en la silla. Aprieta el glúteo de atrás.", lados=True),
]
VIGOR = dict(
    titulo="Vigor", trans=15, fijo=V_FIJO, rotacion=["A", "B", "C", "A", "B", "C", "D"],
    dias=dict(A="Piernas", B="Torso y brazos", C="Equilibrio y tenis", D="Movilidad"),
    fases=[
      dict(n=1, nombre="Base", semanas="1 a 4", meta="Aprender cada movimiento con control. " + AIRE,
        dias=dict(
          A=circuito([e("sentarse_pararse", "Sentarse y pararse", 45, "Brazos cruzados. Exhala al pararte, sin impulso."),
                      e("puente", "Puente de glúteo", 45, "Exhala al subir. Arriba un segundo, baja lento."),
                      e("zancada_apoyo", "Zancada con apoyo", 60, "Mano en la silla. Baja vertical, rodilla de atrás cerca del piso.", True),
                      e("elevacion_talones", "Elevación de talones", 45, "Manos en la pared. Sube en 1, baja en 3."),
                      e("escalon", "Subir escalón", 60, "Mano en la baranda. Empuja con la pierna de arriba.", True)]),
          B=circuito([e("flexion_pared", "Flexión en pared", 45, "Cuerpo en una línea. Exhala al empujar."),
                      e("remo_toalla", "Remo con toalla", 45, "Puerta bien cerrada. Tira con los codos atrás, exhala al tirar."),
                      e("angel_pared", "Ángel en pared", 45, "Espalda y cabeza en la pared. Sube los brazos sin despegarlos."),
                      e("plancha_inclinada", "Plancha inclinada", 30, "Antebrazos en la mesa. Respira normal durante toda la plancha."),
                      e("birddog", "Bird dog", 60, "Brazo y pierna contrarios. Espalda quieta. Alterna.")]),
          C=circuito([e("equilibrio_un_pie", "Equilibrio en un pie", 60, "Mano rozando la silla. Mirada al frente.", True),
                      e("talon_punta", "Caminar talón–punta", 40, "Sobre una línea, junto a una pared por si acaso."),
                      e("rotacion_tronco", "Rotación de tronco", 40, "Como un golpe de tenis lento. Gira desde el tronco, no desde los brazos."),
                      e("paso_lateral", "Desplazamiento lateral", 40, "Rodillas suaves, pasos amplios, sin cruzar los pies.")])
            + [e("abre_libro", "Libro abierto", 60, "De lado. Abre el brazo de arriba y respira.", True)],
          D=V_MOVILIDAD)),
      dict(n=2, nombre="Volumen", semanas="5 a 8", meta="Más lento y más tiempo bajo tensión: baja en 3 segundos. " + AIRE,
        dias=dict(
          A=circuito([e("sentadilla", "Sentadilla", 50, "Baja en 3 segundos, sube en 1. Exhala al subir."),
                      e("puente_una_pierna", "Puente a una pierna", 60, "La cadera no se ladea.", True),
                      e("zancada_atras", "Zancada atrás", 60, "Paso atrás controlado. Exhala al volver.", True),
                      e("escalon", "Subir escalón", 60, "Más lento: 3 segundos para bajar.", True),
                      e("elevacion_talones", "Elevación de talones", 40, "Pausa de un segundo arriba.")]),
          B=circuito([e("flexion_inclinada", "Flexión inclinada", 50, "Manos en la mesa. Baja en 3, exhala al subir."),
                      e("remo_toalla", "Remo con toalla", 50, "Más inclinado que en la fase 1. Pausa con los codos atrás."),
                      e("deadbug", "Dead bug", 60, "Lumbar pegada al piso. Exhala al extender."),
                      e("angel_pared", "Ángel en pared", 45, "Más lento."),
                      e("plancha_inclinada", "Plancha inclinada", 40, "Respira normal.")]),
          C=circuito([e("equilibrio_un_pie", "Equilibrio en un pie", 60, "Sin apoyo, la silla cerca por si acaso.", True),
                      e("reloj", "Reloj de equilibrio", 60, "Toca adelante, al lado y atrás sin apoyar el pie.", True),
                      e("rotacion_tronco", "Rotación de tronco", 40, "Más amplia, cadera acompaña."),
                      e("paso_lateral", "Desplazamiento lateral", 40, "Más bajo, como en la cancha.")])
            + [e("abre_libro", "Libro abierto", 60, "Respira largo abierto.", True)],
          D=V_MOVILIDAD)),
      dict(n=3, nombre="Control", semanas="9 a 12", meta="Variantes a una pierna y pausas: el músculo trabaja más sin agregar peso. " + AIRE,
        dias=dict(
          A=circuito([e("sentadilla_bulgara", "Sentadilla búlgara", 60, "Pie de atrás en la silla. Baja vertical, exhala al subir.", True),
                      e("pmr_libre", "Peso muerto a una pierna", 60, "Cadera atrás, espalda larga. Una mano en la pared si hace falta.", True),
                      e("puente_una_pierna", "Puente a una pierna", 60, "Pausa de 2 segundos arriba.", True),
                      e("sentadilla", "Sentadilla con pausa", 50, "Pausa de 2 segundos abajo, respirando.")]),
          B=circuito([e("flexion_rodillas", "Flexión en rodillas", 45, "Exhala al subir. Si la cadera se hunde, vuelve a la inclinada."),
                      e("remo_toalla", "Remo con toalla a una mano", 60, "Una mano, sin rotar el torso.", True),
                      e("plancha", "Plancha en antebrazos", 30, "En rodillas o en puntas. Respira normal."),
                      e("deadbug", "Dead bug", 60, "Lento y controlado."),
                      e("plancha_lateral", "Plancha lateral en rodillas", 60, "Cuerpo recto, respira normal.", True)]),
          C=circuito([e("reloj", "Reloj de equilibrio", 60, "Más lejos en cada dirección.", True),
                      e("zancada_lateral", "Zancada lateral", 60, "Cadera atrás, pie completo en el piso.", True),
                      e("split_step", "Split step", 30, "Saltito corto y caída suave. Si hay molestia en rodillas, solo el gesto sin salto."),
                      e("rotacion_tronco", "Rotación de tronco", 40, "Rápida pero controlada, como el golpe.")])
            + [e("abre_libro", "Libro abierto", 60, "Respira largo abierto.", True)],
          D=V_MOVILIDAD)),
    ],
    info="""  <ul class="lista" style="margin-top:10px">
    <li><b>Fuerza para la salud.</b> Después de los 60 el músculo se pierde si no se usa. Dos o tres días de fuerza por semana lo mantienen y hasta lo hacen crecer.</li>
    <li><b>Doce semanas con peso corporal.</b> Primero aprender los movimientos, luego más lento, luego a una pierna. Después se suman bandas elásticas.</li>
    <li><b>Rota cada día.</b> Piernas, torso y brazos, equilibrio y tenis, y un día de movilidad: A, B, C, A, B, C, D.</li>
    <li><b>Nunca aguantar el aire.</b> Con hipertensión, hacer fuerza conteniendo la respiración sube la presión. Exhala en el esfuerzo.</li>
    <li><b>El esfuerzo se mide por sensación.</b> Debe sentirse moderado: podrías hablar en frases cortas. Algunos medicamentos bajan el pulso, así que el reloj no sirve de guía.</li>
    <li><b>Del piso, despacio.</b> Al levantarte del piso, pasa primero por sentado unos segundos.</li>
  </ul>
  <div class="aviso alto" style="margin-top:16px"><b>Para y consulta</b> si hay dolor u opresión en el pecho, mareo, falta de aire fuera de lo normal o palpitaciones.</div>""",
    # Oscura, como Fuerza: tinta y papel de DCA con el azul pizarra aclarado para que lea sobre negro
    paleta="""  --fondo:#1B1B19; --tarjeta:#232421; --tinta:#F5F2EA; --suave:#A3A199; --linea:#33352F;
  --barro:#8FB0C2; --barro-claro:#28343B; --salvia:#8DA383; --alerta:#E08C76; --sintoma:#C9A55C;""",
    oscura=True, fondo="#1B1B19", icono=("#1B1B19", "#28343B", "#4F6E80", "#8FB0C2"))

# ======================= AMPLITUD · Adriana =======================
A_FIJO = [
    e("respira_sentada", "Respiración lenta", 60, "Sentada, manos en las costillas. Inhala en 4, exhala en 6."),
    e("circulos_brazos", "Círculos de brazos", 40, "Círculos amplios hacia adelante y luego hacia atrás."),
    e("marcha", "Marcha en el sitio", 40, "Sube las rodillas y balancea los brazos."),
]
A_MOVILIDAD = [
    e("gato", "Gato–camello", 60, "En cuatro apoyos. Inhala al arquear, exhala al redondear."),
    e("abre_libro", "Libro abierto", 80, "De lado. Abre el brazo y respira en la postura.", True),
    e("pantorrilla_pared", "Pantorrilla en pared", 80, "Talón de atrás en el piso.", True),
    e("isquios_silla", "Isquiotibiales en silla", 80, "Espalda recta, inclínate desde la cadera.", True),
    e("pecho_puerta", "Pecho en el marco de la puerta", 60, "Avanza el pecho sin arquear la espalda."),
    e("flexor_cadera_pie", "Flexor de cadera de pie", 80, "Mano en la silla, aprieta el glúteo de atrás.", True),
]
SUAVE = "Tensión suave, nunca dolor. Respira largo."
AMPLITUD = dict(
    titulo="Amplitud", trans=10, fijo=A_FIJO, rotacion=["A", "B", "C", "A", "B", "C", "D"],
    dias=dict(A="Cadera y piernas", B="Hombros y columna", C="Fuerza y equilibrio", D="Movilidad para tenis"),
    fases=[
      dict(n=1, nombre="Soltar", semanas="1 a 4", meta="Rango cómodo y posturas cortas. " + SUAVE,
        dias=dict(
          A=[e("isquios_silla", "Isquiotibiales en silla", 80, "Pierna estirada, espalda recta.", True),
             e("flexor_cadera_pie", "Flexor de cadera de pie", 80, "Mano en la silla, cadera adelante.", True),
             e("figura4_silla", "Glúteo en figura 4 sentada", 80, "Tobillo sobre la rodilla, espalda recta.", True),
             e("pantorrilla_pared", "Pantorrilla en pared", 80, "Talón de atrás en el piso.", True),
             e("mariposa", "Mariposa", 45, "Espalda alta, rodillas caen solas."),
             e("cuadriceps", "Cuádriceps de pie", 80, "Mano en la silla, rodillas juntas.", True)],
          B=[e("pecho_puerta", "Pecho en el marco de la puerta", 60, "Avanza el pecho sin arquear la espalda."),
             e("brazo_cruzado", "Hombro con brazo cruzado", 80, "Hombros abajo, sin girar el tronco.", True),
             e("toracica_silla", "Rotación sentada", 60, "Gira desde el pecho, la cadera quieta."),
             e("gato_silla", "Gato–camello sentada", 60, "Redondea mirando al ombligo, abre el pecho al volver."),
             e("lateral_pie", "Inclinación lateral", 80, "Brazo arriba, crece antes de inclinarte.", True),
             e("angel_pared", "Ángel en pared", 60, "Sube los brazos sin despegarlos de la pared.")],
          C=circuito([e("sentarse_pararse", "Sentarse y pararse", 40, "Exhala al pararte, sin impulso."),
                      e("equilibrio_un_pie", "Equilibrio en un pie", 60, "Mano rozando la silla.", True),
                      e("flexion_pared", "Flexión en pared", 40, "Exhala al empujar."),
                      e("puente", "Puente de glúteo", 40, "Exhala al subir."),
                      e("elevacion_talones", "Elevación de talones", 40, "Manos en la pared, baja lento.")])
            + [e("talon_punta", "Caminar talón–punta", 45, "Junto a una pared por si acaso.")],
          D=A_MOVILIDAD)),
      dict(n=2, nombre="Ampliar", semanas="5 a 8", meta="Un poco más de rango y más tiempo en cada postura. " + SUAVE,
        dias=dict(
          A=[e("isquios_toalla", "Isquiotibiales con toalla", 90, "Pierna al techo, rodilla casi estirada.", True),
             e("flexor_cadera", "Flexor de cadera en rodilla", 90, "Rodilla en un cojín, mano en la silla.", True),
             e("figura4", "Glúteo en figura 4 acostada", 90, "Abraza el muslo, cabeza en el piso.", True),
             e("cuadriceps", "Cuádriceps de pie", 90, "Rodillas juntas, cadera adelante.", True),
             e("mariposa", "Mariposa", 60, "Espalda alta."),
             e("pantorrilla_pared", "Pantorrilla en pared", 90, "Rodilla de atrás estirada.", True)],
          B=[e("pecho_puerta", "Pecho en el marco de la puerta", 60, "Un paso más adelante que en la fase 1."),
             e("brazo_cruzado", "Hombro con brazo cruzado", 90, "Hombros abajo.", True),
             e("gato", "Gato–camello", 60, "En cuatro apoyos, lento."),
             e("abre_libro", "Libro abierto", 90, "Respira en la postura abierta.", True),
             e("toalla_espalda", "Hombros con toalla", 90, "Tira suave hacia arriba y hacia abajo.", True),
             e("angel_pared", "Ángel en pared", 60, "Más lento.")],
          C=circuito([e("sentarse_pararse", "Sentarse y pararse", 45, "Baja en 3 segundos."),
                      e("equilibrio_un_pie", "Equilibrio en un pie", 60, "Sin apoyo, la silla cerca.", True),
                      e("zancada_apoyo", "Zancada con apoyo", 60, "Mano en la silla, baja vertical.", True),
                      e("flexion_inclinada", "Flexión inclinada", 40, "Manos en la mesa, exhala al subir."),
                      e("puente", "Puente de glúteo", 40, "Pausa arriba.")])
            + [e("reloj", "Reloj de equilibrio", 60, "Toca adelante, al lado y atrás.", True)],
          D=A_MOVILIDAD)),
      dict(n=3, nombre="Sostener", semanas="9 a 12", meta="Posturas más profundas y equilibrio más exigente. " + SUAVE,
        dias=dict(
          A=[e("zancada_rotacion", "Zancada con rotación", 90, "Rodilla en un cojín, abre el brazo al techo.", True),
             e("isquios_toalla", "Isquiotibiales con toalla", 90, "Respira largo.", True),
             e("figura4", "Glúteo en figura 4 acostada", 90, "Abraza un poco más.", True),
             e("cuadriceps", "Cuádriceps de pie", 90, "Rodillas juntas.", True),
             e("sentadilla_sostenida", "Sentadilla sostenida con apoyo", 60, "Manos en la mesa, talones en el piso."),
             e("flexor_cadera", "Flexor de cadera en rodilla", 90, "Cadera adelante.", True)],
          B=[e("abre_libro", "Libro abierto", 90, "Abre un poco más.", True),
             e("gato", "Gato–camello", 60, "Lento."),
             e("nino", "Postura del niño", 60, "Rodillas en un cojín, respira hacia la espalda. Al subir, despacio."),
             e("toalla_espalda", "Hombros con toalla", 90, "Manos un poco más cerca.", True),
             e("pecho_puerta", "Pecho en el marco de la puerta", 60, "Brazos un poco más arriba."),
             e("lateral_pie", "Inclinación lateral", 90, "Crece antes de inclinarte.", True)],
          C=circuito([e("sentadilla", "Sentadilla", 45, "Exhala al subir."),
                      e("reloj", "Reloj de equilibrio", 60, "Más lejos en cada dirección.", True),
                      e("zancada_atras", "Zancada atrás", 60, "Mano en la silla.", True),
                      e("flexion_inclinada", "Flexión inclinada", 45, "Baja en 3 segundos."),
                      e("puente_marcha", "Puente con marcha", 45, "La cadera no se cae.")])
            + [e("equilibrio_un_pie", "Equilibrio en un pie", 60, "Sin apoyo, gira la cabeza lento.", True)],
          D=A_MOVILIDAD)),
    ],
    info="""  <ul class="lista" style="margin-top:10px">
    <li><b>Flexibilidad todos los días.</b> Cadera, piernas, hombros y columna rotan con un día de movilidad para tenis.</li>
    <li><b>Fuerza y equilibrio dos veces por semana.</b> A los 65 es lo que más previene caídas y cuida el hueso. Por eso el día C es de fuerza.</li>
    <li><b>Doce semanas.</b> Primero soltar, luego ampliar el rango, luego sostener posturas más profundas. Después se suman bandas elásticas.</li>
    <li><b>Estirar sin rebotar.</b> Llega a una tensión suave y respira ahí. El dolor no es la meta.</li>
    <li><b>Nunca aguantar el aire.</b> Con hipertensión, contener la respiración sube la presión. Exhala largo en cada postura.</li>
    <li><b>Del piso, despacio.</b> Al levantarte, pasa primero por sentada unos segundos.</li>
  </ul>
  <div class="aviso alto" style="margin-top:16px"><b>Para y consulta</b> si hay dolor u opresión en el pecho, mareo, falta de aire fuera de lo normal o palpitaciones.</div>""",
    paleta="""  --fondo:#F1F3EF; --tarjeta:#FAFBF8; --tinta:#232A26; --suave:#6B756F; --linea:#DCE3DD;
  --barro:#5F8077; --barro-claro:#CFDDD7; --salvia:#46695F; --alerta:#A8432F; --sintoma:#C9A55C;""",
    fondo="#F1F3EF", icono=("#F1F3EF", "#CFDDD7", "#93B1A8", "#5F8077"))

# Ajustes para las apps oscuras: la plantilla nació clara y tiene blancos fijos
OSCURA_CSS = """
.btn.pri{color:var(--fondo)}
.aviso.sube{background:#22302A;color:#B9D1C2}
.aviso.alto{background:#3A2622;color:#E8A592}
.sn button.on{background:var(--tinta);color:var(--fondo);box-shadow:none}
.sn button.on.si{background:var(--barro);color:var(--fondo)}
.media,.orbe-wrap{background:#FFFFFF;box-shadow:none}
.dias button.on{background:var(--tinta);border-color:var(--tinta);color:var(--fondo)}
.dias button.on b{color:var(--fondo)}
.ctrl button.grande{background:var(--barro);border-color:var(--barro)}
.ctrl .grande svg{fill:var(--fondo)}
.opc button.on{color:var(--fondo)}
#a-nombre{background:var(--tarjeta)!important;color:var(--tinta)}
input[type=date],input{color-scheme:dark}
"""

# ======================= construcción =======================
def icono(colores, ruta):
    from PIL import Image, ImageDraw
    S = 360; im = Image.new("RGB", (S, S), colores[0]); d = ImageDraw.Draw(im)
    for r, c in zip((132, 96, 58), colores[1:]):
        d.ellipse([S/2 - r, S/2 - r, S/2 + r, S/2 + r], fill=c)
    im.save(ruta)

def medios(app, ids):
    M, sin = {}, []
    for i in ids:
        for ext, mime in (("mp4", "video/mp4"), ("gif", "image/gif"), ("webp", "image/webp"), ("jpg", "image/jpeg"), ("png", "image/png")):
            p = f"medios/{app}/{i}.{ext}"
            if os.path.exists(p):
                tipo = "video" if ext == "mp4" else "img"
                if ext == "png":
                    w, h = png_size(p)
                    if w >= 3 * h: tipo = "hoja"
                M[i] = dict(src=b64(p, mime), tipo=tipo)
                if tipo == "hoja": M[i]["ar"] = round(w / 4 / h, 4)
                if tipo == "video" and os.path.exists(f"medios/{app}/{i}.poster.jpg"):
                    M[i]["poster"] = b64(f"medios/{app}/{i}.poster.jpg", "image/jpeg")
                break
        else:
            sin.append(i)
    return M, sin

def esc(o):
    return json.dumps(o, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")

base = open("plantilla.html", encoding="utf-8").read()
os.makedirs("dist", exist_ok=True)
for clave, A in (("vigor", VIGOR), ("amplitud", AMPLITUD)):
    os.makedirs(f"medios/{clave}", exist_ok=True)
    fases = []
    for f in A["fases"]:
        f = dict(f); f["dias"] = dict(f["dias"]); f["dias"]["D"] = f["dias"]["D"]; f["total"] = {}
        for k, lista in f["dias"].items():
            pasos = A["fijo"] + lista
            f["dias"][k] = pasos
            f["total"][k] = sum(p["seg"] for p in pasos) + A["trans"] * (len(pasos) - 1) + 5
        fases.append(f)
        print(f"{A['titulo']} fase {f['n']} {f['nombre']}: " + " · ".join(f"{k} {t//60}:{t%60:02d}" for k, t in f["total"].items()))
    ids = sorted({p["id"] for f in fases for d in f["dias"].values() for p in d})
    M, sin = medios(clave, ids)
    print(f"  {len(ids)} ilustraciones · {len(M)} listas · faltan {len(sin)}")
    icono(A["icono"], f"icono_{clave}.png")
    out = (base.replace("__DATA__", esc(dict(programa=fases, trans=A["trans"], dias=A["dias"], rotacion=A["rotacion"])))
               .replace("__MEDIA__", esc(M))
               .replace("__ICON__", b64(f"icono_{clave}.png", "image/png"))
               .replace("__FIGURA__", open("figura.js", encoding="utf-8").read())
               .replace("__PALETA__", A["paleta"])
               .replace("__FONDO__", A["fondo"])
               .replace("__INFO__", A["info"])
               .replace("__TITULO__", A["titulo"])
               .replace("__EXTRA__", OSCURA_CSS if A.get("oscura") else "")
               .replace("__BARRA__", "black-translucent" if A.get("oscura") else "default"))
    # clave de almacenamiento propia para que no choque con Núcleo si se abre en el mismo teléfono
    out = out.replace("var CLAVE='nucleo.v2';", f"var CLAVE='{clave}.v1';")
    assert f"var CLAVE='{clave}.v1';" in out
    open(f"dist/{clave}.html", "w", encoding="utf-8").write(out)
    print("  OK", f"dist/{clave}.html", round(len(out.encode()) / 1e6, 2), "MB")
