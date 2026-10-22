# Entrenamiento

Dos apps web autocontenidas, publicadas con GitHub Pages.

| App | Dirección | Fuente |
|---|---|---|
| Fuerza — kettlebells, 2 sesiones/semana, 8 semanas | https://afareca.github.io/entrenamiento/ | `fuente/fuerza/` |
| Núcleo — core posparto, 10 min diarios, rutina que rota por día | https://afareca.github.io/entrenamiento/core.html | `fuente/nucleo/` |
| Vigor — fuerza 65+, peso corporal, 12 semanas | https://afareca.github.io/entrenamiento/vigor.html | `fuente/mayores/` |
| Amplitud — flexibilidad, fuerza y equilibrio 65+, 12 semanas | https://afareca.github.io/entrenamiento/amplitud.html | `fuente/mayores/` |
| Prueba de tonos | https://afareca.github.io/entrenamiento/tonos.html | — |

Para trabajar el proyecto con Claude Code, ver `CLAUDE.md`: arquitectura, cómo construir y probar, medios y pendientes.

## Cambiar una rutina

1. Edita el programa en `fuente/<app>/build.py`.
2. Corre `python3 build.py` dentro de esa carpeta. Genera `dist/` con un solo HTML.
3. Copia el resultado a la raíz: `fuerza → index.html`, `nucleo → core.html`.

## Imágenes propias de Núcleo

Pon cada imagen en `fuente/nucleo/medios/` con el nombre del ejercicio (`puente.png`, `gato.gif`…), los mismos de la página de prompts. Una hoja PNG horizontal de 4 cuadros se anima sola; un PNG normal se muestra fijo. Mientras falte una, la app usa el GIF de catálogo o la figura animada.

`index.html.html` solo redirige a `./` para que los íconos guardados antes del cambio sigan funcionando.

Los datos de cada persona se guardan en su propio teléfono, no aquí.

GIFs de ejercicios © Gym visual — https://gymvisual.com/
