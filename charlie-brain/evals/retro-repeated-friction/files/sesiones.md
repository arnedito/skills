# Resumen de sesiones desde la última retro (exportado)

## Sesión 1
- Agente ejecutó `python -m unittest` (falló: no hay tests unittest), luego `pytest tests/` tras 4 intentos.
- Usuario: "la ecuación 5 de Einstein usa el radio, no el diámetro".
- Agente leyó los 3 ficheros de aire/ enteros para encontrar dónde estaba sedimentation_velocity.

## Sesión 2
- Agente volvió a probar `python -m unittest` antes de `pytest`.
- Usuario: "otra vez: Einstein eq. 5 es con radio r".
- Agente hizo commit con mensaje "update" y el usuario pidió reescribirlo.

## Sesión 3
- Agente cambió kB a 1.38e-23 (redondeo) sin anotarlo; el usuario lo detectó a mano comparando con el paper.
- Agente leyó CLAUDE.md, que repite las reglas del global.
