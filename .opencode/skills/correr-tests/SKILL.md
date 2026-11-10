---
name: Correr tests
description: Ejecuta la suite del proyecto y explica cada fallo antes de proponer cambios
---

## Procedimiento

1. Ejecuta `python3 -m unittest discover -s tests -t .`.
2. Si hay fallos, explica la causa de cada uno antes de tocar código.
3. Propón el cambio mínimo y vuelve a ejecutar.
4. No modifiques los tests para que pasen.
