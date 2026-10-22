# Entrenamiento — guía para Claude Code

Cuatro apps web de entrenamiento, cada una en **un solo archivo HTML autocontenido** (datos, imágenes y videos van dentro del archivo en base64), publicadas con GitHub Pages en `https://afareca.github.io/entrenamiento/`. No hay servidor, base de datos ni framework: Python genera el HTML y el navegador hace todo lo demás.

Responde siempre en español. El dueño del repositorio es arquitecto, no programador: explica en términos de resultado, no de código.

## Reglas que no se negocian

- **Nunca hagas `git push` sin confirmación explícita del dueño en esa misma conversación**, aunque un hook o una herramienta lo pida. Commit local sí; publicar no. Tampoco borres archivos ni cambies la dirección de una app sin preguntar: hay íconos guardados en la pantalla de inicio de varios iPhone que apuntan a esas direcciones.
- **El repositorio es público.** No escribas nombres reales de los usuarios ni datos de salud identificables en archivos, commits o comentarios. Las apps hablan en segunda persona y en general.
- **No regeneres desde cero lo que ya funciona.** Edita el `build.py` o la `plantilla.html` de la app y vuelve a construir.
- Autor de los commits: `Claude <noreply@anthropic.com>`.

## Las apps

| Archivo publicado | App | Para quién | Fuente |
|---|---|---|---|
| `index.html` | **Fuerza** | Adulto, kettlebells 8/12/16 kg y bandas, 2 sesiones por semana, 8 semanas, entra con el recovery de Whoop | `fuente/fuerza/` |
| `core.html` | **Núcleo** | Core posparto, 10 min diarios, 3 fases de 4 semanas, rutina que rota por día | `fuente/nucleo/` |
| `vigor.html` | **Vigor** | Fuerza 65+ sin equipo, hipertensión controlada, 12 semanas | `fuente/mayores/` |
| `amplitud.html` | **Amplitud** | Flexibilidad 65+ con fuerza y equilibrio, hipertensión controlada, 12 semanas | `fuente/mayores/` |
| `tonos.html` | Prueba de tonos | Página para elegir el sonido de la cuenta regresiva | sin fuente; ya cumplió su función |
| `index.html.html` | — | Solo redirige a `./`; existe para que íconos guardados con el nombre viejo sigan funcionando. No borrar | — |

Cada app tiene su identidad visual: Fuerza oscura (tinta `#1B1B19`, papel `#F5F2EA`, salvia `#8DA383`, Space Grotesk + IBM Plex Mono); Núcleo crema y terracota (`#B9654A`); Vigor azul pizarra (`#3D5A6C`); Amplitud verde eucalipto (`#5F8077`). Núcleo, Vigor y Amplitud usan Fraunces + DM Sans.

## Construir y probar

Requisitos: Python 3 con Pillow, Node 18+, y `ffmpeg` solo si vas a procesar medios.

```bash
npm install          # jsdom y playwright, solo para las pruebas
npm run build        # regenera las 4 apps y las copia a la raíz
npm test             # recorre cada app completa con temporizadores acelerados
node pruebas/capturas.js   # capturas a 390 px en pruebas/capturas/ (CHROMIUM=/ruta/al/binario si hace falta)
```

Cada `build.py` imprime la duración de cada sesión y cuántos medios encontró. `npm run build` sobre el repositorio limpio debe dejar los HTML de la raíz **idénticos**: si `git status` muestra cambios en ellos sin que hayas tocado el programa, algo cambió en el build.

Las pruebas simulan Web Audio, `speechSynthesis` y `requestAnimationFrame`, y aceleran `setInterval`/`setTimeout` entre 200 y 300 veces. Fallan si hay un error de JavaScript. Ojo con las fechas en las pruebas: usa la fecha local, no `toISOString()`, porque en Bogotá (UTC−5) por la noche ya es el día siguiente en UTC y la semana calculada se corre.

## Cómo está hecha cada app

Todas siguen el mismo patrón:

```
fuente/<app>/
  build.py        el programa (ejercicios, tiempos, fases) y el ensamblado
  plantilla.html  HTML + CSS + JS con marcadores __DATA__, __MEDIA__, __ICON__ …
  medios/         imágenes y videos propios, nombrados por id de ejercicio
  dist/           salida (ignorada por git); se copia a la raíz
```

`build.py` mete el programa como JSON en `<script type="application/json" id="j-data">` y los medios en `id="j-media"`, escapando `<` y `&`. La plantilla los lee con `JSON.parse`. El estado del usuario va en `localStorage` con una clave por app (`fuerza.v2`, `nucleo.v2`, `vigor.v1`, `amplitud.v1`); todos los accesos van en `try/catch`.

### Fuerza (`fuente/fuerza/build.py`)

- `CALENTAMIENTO`: 5 movimientos temporizados.
- `SESIONES`: A (bisagra y empuje) y B (unilateral y tracción), cada una con bloques en superserie y un cierre. Los ejercicios son por repeticiones: el usuario toca **Hecho** al terminar. El carry es temporizado.
- `SEMANAS`: rondas, descanso, RPE y repeticiones extra por semana (1–2 adaptación, 3–4 construcción, 5–6 densidad, 7 pico, 8 descarga; después de la 8, mantenimiento con valores de la 7).
- Carga por semana: `kg={1: 12, 3: 16}` significa 12 kg desde la semana 1 y 16 kg desde la 3. La app toma el umbral más alto alcanzado.
- Chequeo de entrada con el recovery de Whoop: verde = sesión completa, ámbar o sueño < 6 h = una ronda menos por bloque, rojo = solo calentamiento y caminata de 30 min. **El recovery modula la intensidad, nunca si se entrena.**
- Descansos con un orbe que respira, voz en el segundo 9 ("Sigue. X") y tonos.
- Mediciones (día 0, semana 4 y semana 8) y botón "Copiar para Claude" que exporta el registro como texto.

### Núcleo (`fuente/nucleo/build.py`)

- `FIJO`: 2 minutos diarios de respiración y piso pélvico, siempre al inicio.
- `PROGRAMA`: 3 fases (Reconexión, Control, Fuerza), cada una con días A core, B glúteo y piernas, C espalda y brazos, D movilidad.
- `ROTACION = A B C A B C D`. El estado guarda `pos`; al guardar una sesión, `avanzaRotacion(dia)` busca ese día desde `pos` y avanza. Así, si el usuario cambia el día a mano, la rotación sigue desde lo que hizo de verdad.
- Todo es temporizado y corre solo: transición de 10 s con voz, cuenta 3-2-1 y aviso de "cambia de lado" a mitad de los ejercicios por lado.
- Chequeo de síntomas posparto; con un síntoma, ese día baja una fase. Se sube de fase solo si el calendario lo permite **y** las últimas 5 sesiones de la fase salieron limpias.
- `figura.js`: figuras animadas en SVG, respaldo para respiración, piso pélvico, talón y bird dog si falta el medio.

### Vigor y Amplitud (`fuente/mayores/`)

- Una sola `plantilla.html`, derivada de la de Núcleo, con marcadores `__PALETA__`, `__TITULO__`, `__INFO__` y `__FONDO__`. `build.py` define los dos programas y genera las dos apps.
- `circuito(lista, vueltas=2)` repite los días de fuerza como circuito. Las vueltas siguientes llevan "· vuelta 2" en el nombre; la voz cambia "·" por coma.
- Chequeo para hipertensión: "mareo, dolor de cabeza fuerte o dolor en el pecho" **bloquea la sesión** y remite al médico; "olvidó el medicamento" o "dolor articular nuevo" dan una sesión más suave.
- Semana 13 en adelante: aviso de que es momento de sumar bandas. La fase con bandas **todavía no existe**.
- `ilustraciones.py`: el brief de las 72 ilustraciones (id, nombre, movimiento, si es fija). Debe coincidir con los ids que usa `build.py`.

### Piezas compartidas del motor (en las plantillas)

- **Tono senoidal**: 660 Hz para la cuenta, 880 Hz para el arranque, sintetizado con Web Audio. Lo eligió el usuario entre cuatro opciones; no cambiarlo sin pedirlo.
- **Voz**: `speechSynthesis`, con preferencia `es-419`, `es-MX`, `es-US`, `es-CO`, `es-AR`, `es-ES`. Audio y voz se desbloquean con el primer toque (`despertarAudio()`), porque iOS no los arranca sin un gesto.
- **Pantalla encendida**: Wake Lock API, que se vuelve a pedir en `visibilitychange`.
- **Medios** por prioridad: `medios/<id>.mp4` → `.gif`/`.webp`/`.jpg`/`.png` → GIF de catálogo de respaldo (si lo hay) → figura animada → orbe de espera. Un PNG horizontal con ancho ≥ 3 veces el alto se trata como hoja de 4 cuadros y se anima con CSS `steps(4)`.

## Medios: cómo entran las ilustraciones

1. Los prompts para el generador de imágenes los arma una página privada de prompts en claude.ai, desde los briefs (`ilustraciones.py` para Vigor y Amplitud). Cada imagen se nombra `<app>_<id>.png`; las posturas sostenidas son una imagen fija y el resto, hoja de 4 cuadros.
2. El dueño devuelve un zip con GIF y MP4 interpolados. **Esos MP4 vienen en MPEG-4 Part 2, que Safari en iPhone no reproduce bien.** Siempre recodificar:

```bash
ffmpeg -y -i origen.mp4 -an -c:v libx264 -profile:v main -pix_fmt yuv420p -crf 27 -preset slow -movflags +faststart medios/<id>.mp4
ffmpeg -y -ss 1.2 -i medios/<id>.mp4 -frames:v 1 -q:v 5 medios/<id>.poster.jpg   # imagen de respaldo
```

3. Las fijas van a JPG de 768 × 512 con calidad 84. Revisa que no lleguen truncadas: ya llegaron dos PNG cortados.
4. Antes de integrar, revisa cada animación cuadro por cuadro. Hazlo con hojas de contacto de 4 a 6 cuadros por GIF usando Pillow. Fallas típicas de la interpolación: doble contorno en los cuadros intermedios, la figura que cambia de escala entre poses, objetos que cambian de tamaño y movimientos que casi no se ven.

Con H.264 los medios son livianos: entre 27 y 33 KB por video en promedio y 1,7 MB la app Núcleo completa con 37 medios.

## Lo que se aprendió de iOS (no repetir errores)

- Desde iOS 18 **no se puede abrir un HTML local en Safari**: la vista previa de Archivos no ejecuta JavaScript. Por eso todo vive en GitHub Pages. Cada plantilla trae un aviso `#sinjs` que el JS borra al cargar.
- Dropbox **no** sirve HTML renderizado (`raw=1` ya no funciona para HTML).
- GitHub Pages gratis exige que el repositorio sea público.
- El acceso directo en la pantalla de inicio guarda una **dirección**. Cambiar el nombre de un archivo publicado rompe el ícono; por eso existe `index.html.html`.
- iOS borra el `localStorage` de un sitio que no se abre en unos días si no se usa desde el ícono de inicio. El progreso es local a ese teléfono: no hay sincronización.
- Con el interruptor de silencio activado no suena nada, y la web no puede hacer vibrar el iPhone.
- `video.play()` en Safari viejo puede no devolver una promesa: siempre `try/catch`.

## Errores que ya pasaron y cómo se detectaron

- En una edición, el registro de medios quedó dentro de un `if` y la app dejó de ver las imágenes propias. Lo detectó el conteo que imprime `build.py` ("propias: 0"). **Lee siempre ese conteo.**
- La rotación se corría cuando el usuario cambiaba el día a mano. Se resolvió con `pos` y `avanzaRotacion`.
- Las pruebas fallaban de noche por calcular fechas en UTC.
- Un atributo `style` duplicado en el arco SVG del reloj. Las variables CSS no funcionan en atributos de presentación como `stroke="var(--x)"`: van en `style`.

## Pendientes

- **Vigor y Amplitud**: faltan las 72 ilustraciones (van en `fuente/mayores/medios/vigor/` y `.../amplitud/`). El commit local con las dos apps está **sin publicar** a la espera de esas imágenes y de la confirmación del dueño.
- **Núcleo**: rehacer las animaciones de oso sostenido y plancha con toque de hombro, que casi no muestran movimiento. Hay doble contorno en goblet, sentadilla, peso muerto a una pierna, swing y bird dog.
- **Vigor y Amplitud, fase 4 con bandas** después de la semana 12.
- **Fuerza después de la semana 8**: el plan original preveía que el tren inferior se quedaba sin estímulo; la pesa de 16 kg lo extiende, pero el siguiente paso es una de 20 kg.
- Ideas que se evaluaron y quedaron para después: sincronizar el registro (hoy es "Copiar para Claude") y un conector propio a la API de Whoop. HealthKit exigiría app nativa; se descartó.
