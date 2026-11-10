# .opencode

Mapa de extensiones del proyecto. Cada fila es un archivo real que OpenCode
carga en esta carpeta.

| Carpeta | Archivo | Qué hace | Cómo se invoca |
| --- | --- | --- | --- |
| `agents/` | `revisor.md` | Subagente de solo lectura: revisa código y reporta hallazgos por severidad, sin editar ni ejecutar comandos. | Pídele "usa el subagente revisor". |
| `commands/` | `explicar.md` | Comando que explica un archivo en tres partes: qué hace, cómo se usa y qué podría fallar. | `/explicar gastos.py` |
| `skills/` | `correr-tests/SKILL.md` | Procedimiento para ejecutar la suite y explicar cada fallo antes de proponer cambios. | `@correr-tests` o cuando el agente lo necesita. |
| `plugins/` | `redactor/index.ts` | Hook que redacta la palabra `SECRETO` antes de que el prompt llegue al modelo. | Se carga solo al iniciar la sesión. |

## Reglas

No hay carpeta de reglas. El mecanismo es `AGENTS.md` en la raíz del repo.

## Hooks

No hay carpeta de hooks. Un hook es código dentro de un plugin, en
`plugins/<nombre>/index.ts`. El del taller está en
`plugins/redactor/index.ts` y se carga solo.

## Advertencia

Todo `.ts` dentro de `plugins/` se carga solo al iniciar la sesión. Un error de
carga afecta la sesión completa: prueba el plugin en una copia del repo antes de
dejarlo aquí.

La configuración del proyecto vive en `../opencode.jsonc`. No la dupliques aquí.
