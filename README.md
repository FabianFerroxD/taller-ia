# Taller: programar con IA (OpenCode · Cursor · Copilot)

Taller de 2 horas para principiantes e intermedios. El mismo repo y las mismas
misiones se practican con **una** de estas herramientas:

| Herramienta | Qué es |
| --- | --- |
| **OpenCode** | Agente en la terminal (TUI) |
| **Cursor** | Agente en el IDE Cursor |
| **Copilot** | Agente en VS Code con la extensión GitHub Copilot |

En los tres casos el agente recibe un objetivo, lee archivos, propone cambios y
ejecuta comandos. No es autocompletado.

El código y los tests funcionan sin red, sin dependencias externas y sin git.
Solo necesitas Python 3.10 o superior y `unittest`, que viene con Python.

## Con qué herramienta empezar

Elegí **una** columna y seguí el resto del README con esa ruta.

| | **OpenCode** | **Cursor** | **Copilot** |
| --- | --- | --- | --- |
| Requisito extra | Proveedor de modelo configurado | Cursor instalado; modelo en Settings | VS Code + extensión Copilot; suscripción |
| Abrir el proyecto | Terminal en esta carpeta → `opencode` | **File → Open Folder** | **File → Open Folder** |
| Arranque rápido | `opencode --version`; `/models` | Workspace **Trusted** (hooks) | Chat en **Manual permissions** |
| Permisos del proyecto | [`opencode.jsonc`](opencode.jsonc) | [`.cursor/hooks.json`](.cursor/hooks.json) | [`.vscode/settings.json`](.vscode/settings.json) |
| Mapa de extensiones | [`.opencode/README.md`](.opencode/README.md) | [`.cursor/README.md`](.cursor/README.md) | [`.github/README.md`](.github/README.md) |

## El repo

| Archivo / carpeta | OpenCode | Cursor | Copilot |
| --- | --- | --- | --- |
| `gastos.py`, `tests/` | Sí | Sí | Sí |
| [`AGENTS.md`](AGENTS.md) (reglas; misión 4) | Sí | Sí | Sí |
| [`opencode.jsonc`](opencode.jsonc) | Permisos shell | — | — |
| [`.opencode/`](.opencode/) | Agente, comando, skill, plugin | — | — |
| [`.cursor/`](.cursor/) | — | Agente, comando, skill, hooks | — |
| [`.github/`](.github/) | — | — | Agente, prompt, skill, hooks |
| [`.vscode/settings.json`](.vscode/settings.json) | — | — | Auto-aprobación de unittest |

## Cómo correr los tests

Desde la raíz del repo (cualquier herramienta):

```bash
python3 -m unittest discover -s tests -t .
```

Al inicio deben pasar 2 pruebas y no pasar 4. `unittest` reporta esas 4 como
errores porque las funciones lanzan `NotImplementedError` o reciben un tipo
incorrecto. Las que no pasan muestran el trabajo pendiente del taller.

## Atajos que vas a usar

| Acción | OpenCode | Cursor | Copilot |
| --- | --- | --- | --- |
| Archivo al contexto | `@archivo` (`@archivo#1-30`) | `@archivo` | `#file:gastos.py` o picker |
| Ejecutar shell vos | `!comando` | Terminal o agente | Terminal o agente (**Agent**) |
| Plantillas con nombre | `/explicar`, `/undo` | `/explicar` | Prompt **explicar**; `/plan` |
| Planificar sin editar | `Shift+Tab` → Plan | Plan mode | Plan o `/plan` |
| Ejecutar cambios | `Shift+Tab` → Build | Agent | Agent / **Implement plan** |
| Solo lectura (misión 1) | Modo Plan sin editar | Ask | Ask |
| Deshacer trabajo del agente | `/undo`, `/redo` | **Revert** | **Revert** / deshacer editor |
| Modelo | `/models` | Settings | Settings (Copilot) |

## Las 5 misiones

Los objetivos y criterios son **iguales** en las tres rutas. Los prompts de
abajo usan `@archivo` (OpenCode y Cursor). En **Copilot** reemplazá por
`#file:gastos.py` y `#file:tests/test_gastos.py`, o adjuntá los archivos desde
el picker.

### Misión 1: contexto (archivos reales)

**Elemento que practica:** contexto.

**Objetivo:** que el agente lea el código real antes de opinar y que detectes
qué falta implementar.

**Prompt sugerido (OpenCode / Cursor):**

```text
Lee @gastos.py y @tests/test_gastos.py. No edites nada.
Dime qué funciones están sin implementar, qué mensaje de error lanzan
y qué prueba cubre cada una.
```

**Prompt sugerido (Copilot):**

```text
Lee #file:gastos.py y #file:tests/test_gastos.py. No edites nada.
Dime qué funciones están sin implementar, qué mensaje de error lanzan
y qué prueba cubre cada una.
```

| Ruta | Refuerzo sin editar |
| --- | --- |
| OpenCode | No uses Build si solo querés lectura |
| Cursor | Modo **Ask** |
| Copilot | Modo **Ask** |

**Criterio de "ya funcionó":** la respuesta nombra `parsear_linea` y
`resumen_por_categoria`, menciona los mensajes `MISIÓN 1` y `MISIÓN 3`, y no
modificó archivos. Los tests siguen en 2 que pasan y 4 que no pasan.

### Misión 2: instrucción + verificación

**Elemento que practica:** instrucción y verificación.

**Objetivo:** comparar un prompt vago con uno preciso y comprobar el resultado
ejecutando los tests, no leyendo solo la respuesta del agente.

Primero usa el prompt vago:

```text
Arregla los tests de @tests/test_gastos.py.
```

(Copilot: `@tests/...` → `#file:tests/test_gastos.py`.)

**Ejecutar tests**

| OpenCode | Cursor | Copilot |
| --- | --- | --- |
| `!python3 -m unittest discover -s tests -t .` | Terminal o pedir al agente | Igual que Cursor |

**Deshacer**

| OpenCode | Cursor | Copilot |
| --- | --- | --- |
| `/undo` | **Revert** en el chat | **Revert** o deshacer en editor |

Confirmá estado inicial: 2 pasan, 4 no.

Prompt preciso:

```text
Implementa solo parsear_linea en @gastos.py.

- Formato de entrada: "AAAA-MM-DD,categoria,monto".
- Devuelve {"fecha": str, "categoria": str, "monto": float}.
- Convierte el monto con float().
- No modifiques totalizar, resumen_por_categoria ni los tests.
- Al terminar, ejecuta los tests y muéstrame el resultado.
```

**Criterio de "ya funcionó":** 4 pruebas pasan, 2 no; `totalizar` con montos de
texto sigue fallando. Si el agente arregló de más, deshacé y repetí con el
prompt preciso.

### Misión 3: planificar vs ejecutar

**Elemento que practica:** modos de trabajo.

**Objetivo:** separar el diseño de la ejecución. En la fase de plan no debe
haber ediciones en archivos.

| OpenCode | Cursor | Copilot |
| --- | --- | --- |
| `Shift+Tab` → Plan, luego Build | Plan → Agent | `/plan` o agente Plan → **Implement plan** → Agent |

**En planificación:**

```text
Planifica cómo implementar resumen_por_categoria en @gastos.py
para que pase test_resumen_por_categoria. No edites archivos.
Muéstrame el plan en pasos y qué casos borde considerarías.
```

**Al ejecutar:**

```text
Implementa el plan anterior en @gastos.py. No toques otras funciones
ni los tests. Ejecuta los tests al final.
```

**Criterio de "ya funcionó":** sin cambios en archivos durante el plan; después
de ejecutar, 5 pruebas pasan y 1 no (`totalizar` con montos de texto).

### Misión 4: reglas en `AGENTS.md`

**Elemento que practica:** reglas del proyecto (las tres herramientas leen
[`AGENTS.md`](AGENTS.md)).

Agrega esta línea a `AGENTS.md`:

```text
- Funciones nuevas: docstring y nombre en español. No usar pytest.
```

Después pide:

```text
Agrega gasto_mas_alto(gastos) en @gastos.py. Debe devolver el gasto
con el monto más alto. Respeta las reglas de AGENTS.md y no agregues
dependencias ni pytest. Ejecuta los tests al final.
```

**Criterio de "ya funcionó":** función `gasto_mas_alto`, docstring en español,
sin `pytest` ni dependencias nuevas; pruebas existentes en 5 pasan, 1 no.

### Misión 5 (opcional): permisos + alucinación

**Permisos:** pedí primero `Ejecuta ls -la y dime qué archivos hay en el
proyecto.` (debe pedir aprobación) y luego `Ejecuta los tests del proyecto.`

| Ruta | Configuración del taller |
| --- | --- |
| **OpenCode** | [`opencode.jsonc`](opencode.jsonc): `ls` pide aprobación; `python3 -m unittest …` no |
| **Cursor** | [`.cursor/hooks/permisos-shell.sh`](.cursor/hooks/permisos-shell.sh); workspace **Trusted** |
| **Copilot** | [`.vscode/settings.json`](.vscode/settings.json) + **Manual permissions**; Enterprise / **Allow all** pueden cambiar el detalle |

**Alucinación:** pedí `statistics.promedio_movil` (no existe), luego una prueba y
tests. No aceptes la API inventada. Deshacé (`/undo` o **Revert**).

## Hooks: las tres rutas

Las reglas piden; los hooks garantizan. Comportamiento de `SECRETO` en el prompt:

| Ruta | Archivo | Efecto con `SECRETO` |
| --- | --- | --- |
| **OpenCode** | [`.opencode/plugins/redactor/index.ts`](.opencode/plugins/redactor/index.ts) | Redacta → `[redactado]` |
| **Cursor** | [`.cursor/hooks/bloquear-secreto.sh`](.cursor/hooks/bloquear-secreto.sh) | Bloquea el envío |
| **Copilot** | [`.github/hooks/redact-secreto.sh`](.github/hooks/redact-secreto.sh) | Redacta → `[redactado]` (**Preview** en VS Code) |

Detalle OpenCode (plugin):

```ts
import { Plugin } from "@opencode/plugin"

export default Plugin.define({
  id: "taller.redactor",
  async setup(ctx) {
    await ctx.session.hook("prompt", (event) => {
      event.prompt.text = event.prompt.text.replaceAll("SECRETO", "[redactado]")
    })
  },
})
```

Responde con la ruta que uses:

1. ¿En qué momento del flujo interviene?
2. ¿Qué hace con la palabra `SECRETO`?
3. ¿Por qué no alcanza con una regla en `AGENTS.md`?

## Extensiones del proyecto

| Tipo | OpenCode | Cursor | Copilot |
| --- | --- | --- | --- |
| Agente revisor | `.opencode/agents/revisor.md` | `.cursor/agents/revisor.md` | `.github/agents/revisor.md` |
| Explicar archivo | `.opencode/commands/explicar.md` | `.cursor/commands/explicar.md` | `.github/prompts/explicar.prompt.md` |
| Correr tests | `.opencode/skills/correr-tests/` | `.cursor/skills/correr-tests/` | `.github/skills/correr-tests/` |
| Hook / permisos | plugin + `opencode.jsonc` | `hooks.json` + scripts | `hooks/taller.json` + `.vscode/settings.json` |

| Tipo | Cómo invocarlo |
| --- | --- |
| Agente | OpenCode: «usa el subagente revisor…» · Cursor: igual · Copilot: agente **revisor** en el selector |
| Explicar | OpenCode/Cursor: `/explicar gastos.py` · Copilot: prompt **explicar** en el picker |
| Skill tests | Mencioná correr tests o dejá que el agente cargue la skill del repo |

## Mapa de los 8 elementos

| Elemento | OpenCode | Cursor | Copilot |
| --- | --- | --- | --- |
| Modelo | `/models` | Settings | Settings |
| Contexto | `@` (misión 1) | `@` | `#file` |
| Instrucción | Misión 2 | Misión 2 | Misión 2 |
| Modos | Plan / Build | Plan / Agent | Plan / Agent |
| Permisos | `opencode.jsonc` | hook shell | `settings.json` |
| Verificación | Misión 2 (tests) | Igual | Igual |
| Reglas | `AGENTS.md` | `AGENTS.md` | `AGENTS.md` |
| Hooks | Plugin (redacta) | Script (bloquea) | Script (redacta, Preview) |

Las reglas las interpreta el modelo; los hooks los ejecuta el producto. La
alucinación no es un elemento del mapa: es un riesgo que se detecta con la
verificación (tests).

**Deshacer sin git:** OpenCode → `/undo`, `/redo`. Cursor y Copilot → **Revert**
en el chat o deshacer en el editor.

**Instructor:** el guion por herramienta está en [`GUION.md`](GUION.md).
