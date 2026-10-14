# Entrenamiento

Dos apps web autocontenidas, publicadas con GitHub Pages.

| App | Dirección | Fuente |
|---|---|---|
| Fuerza — kettlebells, 2 sesiones/semana, 8 semanas | https://afareca.github.io/entrenamiento/ | `fuente/fuerza/` |
| Núcleo — core posparto, 10 min diarios | https://afareca.github.io/entrenamiento/core.html | `fuente/nucleo/` |
| Prueba de tonos | https://afareca.github.io/entrenamiento/tonos.html | — |

## Cambiar una rutina

1. Edita el programa en `fuente/<app>/build.py`.
2. Corre `python3 build.py` dentro de esa carpeta. Genera `dist/` con un solo HTML.
3. Copia el resultado a la raíz: `fuerza → index.html`, `nucleo → core.html`.

`index.html.html` solo redirige a `./` para que los íconos guardados antes del cambio sigan funcionando.

Los datos de cada persona se guardan en su propio teléfono, no aquí.

GIFs de ejercicios © Gym visual — https://gymvisual.com/
