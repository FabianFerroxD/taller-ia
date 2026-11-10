# .github (Copilot)

Mapa de extensiones del proyecto para la ruta **GitHub Copilot en VS Code**. Cada
fila es un archivo real que Copilot puede cargar desde esta carpeta.

| Carpeta | Archivo | Qué hace | Cómo se invoca |
| --- | --- | --- | --- |
| `agents/` | `revisor.md` | Agente de solo lectura: revisa código y reporta hallazgos, sin editar ni ejecutar comandos. | Elegir **revisor** en el selector de agentes del chat. |
| `prompts/` | `explicar.prompt.md` | Plantilla para explicar un archivo en tres partes. | Picker de prompts o referencia en chat. |
| `skills/` | `correr-tests/SKILL.md` | Procedimiento para ejecutar la suite y explicar cada fallo antes de proponer cambios. | Copilot la carga cuando el tema encaja; también podés pedirlo explícitamente. |
| `hooks/` | `taller.json` + `redact-secreto.sh` | Redacta `SECRETO` → `[redactado]` en el prompt que ve el modelo. | Se carga desde `hooks/*.json` (Preview en VS Code). |

## Reglas

El taller usa `AGENTS.md` en la raíz (misión 4). Copilot lo admite como
instrucciones de repo. No hay `copilot-instructions.md` duplicado a propósito.

## Permisos de terminal

La aproximación a `opencode.jsonc` / `.cursor/hooks/permisos-shell.sh` está en
[`.vscode/settings.json`](../.vscode/settings.json): `chat.tools.terminal.autoApprove`
para `python3 -m unittest`. El resto sigue pidiendo confirmación con
**Manual permissions** en el chat.

## Hooks (Preview)

Los hooks de Copilot en VS Code están en **Preview**. Si no cargan, usá el
Plan B del `GUION.md`: mostrá el script y hablá de garantía vs regla. Admití el
workspace cuando VS Code lo pida.

El evento del taller es `UserPromptTransformed` (redactar, como el plugin de
OpenCode). En Cursor el equivalente **bloquea** el envío.

## Equivalentes

| Copilot (VS Code) | OpenCode | Cursor |
| --- | --- | --- |
| `.vscode/settings.json` | `opencode.jsonc` | `.cursor/hooks/permisos-shell.sh` |
| `hooks/redact-secreto.sh` | `plugins/redactor/index.ts` | `hooks/bloquear-secreto.sh` |
