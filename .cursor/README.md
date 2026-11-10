# .cursor

Mapa de extensiones del proyecto para la ruta **Cursor**. Cada fila es un archivo
real que Cursor carga desde esta carpeta.

| Carpeta | Archivo | Qué hace | Cómo se invoca |
| --- | --- | --- | --- |
| `agents/` | `revisor.md` | Subagente de solo lectura: revisa código y reporta hallazgos por severidad, sin editar ni ejecutar comandos. | "Usa el subagente revisor para revisar gastos.py". |
| `commands/` | `explicar.md` | Comando que explica un archivo en tres partes: qué hace, cómo se usa y qué podría fallar. | `/explicar gastos.py` |
| `skills/` | `correr-tests/SKILL.md` | Procedimiento para ejecutar la suite y explicar cada fallo antes de proponer cambios. | Menciona correr tests o invoca la skill si aparece en el menú. |
| `hooks/` | `permisos-shell.sh` + `bloquear-secreto.sh` | Permisos de shell (aprox. `opencode.jsonc`) y bloqueo de prompts con `SECRETO`. | Se cargan solos vía `hooks.json`. |

## Reglas

No hay carpeta de reglas en este taller. El mecanismo compartido es `AGENTS.md` en
la raíz del repo. Cursor también puede usar `.cursor/rules/*.mdc` para reglas por
archivo; aquí no hace falta para las misiones.

## Hooks

La configuración vive en `hooks.json`. Los scripts están en `hooks/` y se ejecutan
desde la raíz del proyecto.

- **`beforeShellExecution`** (`permisos-shell.sh`): permite `python3 -m unittest …`
  sin pedir aprobación; el resto pide confirmación.
- **`beforeSubmitPrompt`** (`bloquear-secreto.sh`): bloquea el envío si el prompt
  contiene la palabra `SECRETO` (en OpenCode el plugin equivalente la redacta a
  `[redactado]`).

Marcá el workspace como **Trusted** para que los hooks de proyecto se ejecuten.

## Equivalente OpenCode

| Cursor | OpenCode |
| --- | --- |
| `hooks.json` + `hooks/permisos-shell.sh` | `opencode.jsonc` |
| `hooks/bloquear-secreto.sh` | `.opencode/plugins/redactor/index.ts` |

La configuración de permisos de OpenCode no se duplica aquí: está en `../opencode.jsonc`.
