# Taller: programar con IA

Taller de 2 horas para principiantes e intermedios. Practican un agente que recibe
un objetivo, lee archivos, propone cambios y ejecuta comandos. No es
autocompletado.

El código y los tests funcionan sin red, sin dependencias externas y sin git.
Solo necesitas Python 3.10 o superior y `unittest`, que viene con Python.

## Con qué herramienta empezar

| | **OpenCode** (terminal) | **Cursor** (IDE) | **Copilot** (VS Code) |
| --- | --- | --- | --- |
| Requisito extra | Proveedor de modelo configurado | Cursor + modelo en Settings | Extensión Copilot + suscripción; modelo en Settings |
| Abrir el taller | Terminal → `opencode` | **Open Folder** en Cursor | **Open Folder** en VS Code |
| Permisos del proyecto | `opencode.jsonc` | `.cursor/hooks.json` (**Trusted**) | `.vscode/settings.json` + **Manual permissions** |
| Extensiones | `.opencode/` | `.cursor/` | `.github/` |

## El repo

- `gastos.py`: librería mínima de gastos.
- `tests/test_gastos.py`: 6 pruebas de `unittest`.
- `AGENTS.md`: reglas del proyecto (todas las rutas; misión 4).
- `opencode.jsonc`: permisos shell en la ruta OpenCode.
- `.cursor/hooks.json`: permisos y bloqueo de prompt en la ruta Cursor.
- `.github/hooks/`: redacción de `SECRETO` en la ruta Copilot (**Preview**).
- `.vscode/settings.json`: auto-aprobación de `python3 -m unittest` en Copilot.

## Cómo correr los tests

Desde la raíz del repo:

```bash
python3 -m unittest discover -s tests -t .
```

Al inicio deben pasar 2 pruebas y no pasar 4. `unittest` reporta esas 4 como
errores porque las funciones lanzan `NotImplementedError` o reciben un tipo
incorrecto. Las que no pasan muestran el trabajo pendiente del taller.

## Atajos que vas a usar

| Acción | OpenCode | Cursor | Copilot (VS Code) |
| --- | --- | --- | --- |
| Archivo al contexto | `@archivo` (`@archivo#1-30`) | `@archivo` | `#file:gastos.py` o adjuntar desde el picker |
| Ejecutar shell vos | `!comando` | Terminal o agente | Terminal o agente (modo **Agent**) |
| Comandos con nombre | `/explicar`, `/undo` | `/explicar` | Prompt **explicar** en picker; `/plan` |
| Planificar sin editar | `Shift+Tab` → Plan | Plan mode | Plan (`/plan` o agente Plan) |
| Ejecutar cambios | `Shift+Tab` → Build | Agent | Agent; **Implement plan** tras Plan |
| Solo lectura (opcional) | — | Ask | Ask o Edit (diff antes de aplicar) |
| Deshacer trabajo del agente | `/undo`, `/redo` | **Revert** | **Revert** / deshacer en editor |
| Modelo | `/models` | Settings | Settings / selector de modelo Copilot |

## Las 5 misiones

Los prompts son los mismos en las tres rutas; cambian atajos y deshacer según la
herramienta.

### Misión 1: dar contexto con `@`

**Elemento que practica:** contexto.

**Objetivo:** que el agente lea el código real antes de opinar y que detectes
qué falta implementar.

**Prompt sugerido:**

```text
Lee @gastos.py y @tests/test_gastos.py. No edites nada.
Dime qué funciones están sin implementar, qué mensaje de error lanzan
y qué prueba cubre cada una.
```

**Cursor:** en la misión 1 podés usar **Ask** para reforzar que no edite.

**Copilot:** usá **Ask** o **Agent** sin editar; adjuntá archivos con `#file:…`.

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

Ejecuta los tests y observa qué cambió.

- **OpenCode:** `!python3 -m unittest discover -s tests -t .`
- **Cursor / Copilot:** terminal o pedir al agente que los ejecute.

Deshacé los cambios y confirmá el estado inicial (2 pasan, 4 no).

- **OpenCode:** `/undo`
- **Cursor / Copilot:** **Revert** en el chat o deshacer en el editor

Ahora usa el prompt preciso:

```text
Implementa solo parsear_linea en @gastos.py.

- Formato de entrada: "AAAA-MM-DD,categoria,monto".
- Devuelve {"fecha": str, "categoria": str, "monto": float}.
- Convierte el monto con float().
- No modifiques totalizar, resumen_por_categoria ni los tests.
- Al terminar, ejecuta los tests y muéstrame el resultado.
```

**Criterio de "ya funcionó":** las 2 pruebas de `parsear_linea` pasan, el total
queda en 4 pruebas que pasan y 2 que no pasan, y la prueba de `totalizar` con
montos de texto sigue fallando. Si el agente arregló de más, deshacé y repetí con
el prompt preciso (`/undo` o **Revert**).

### Misión 3: Plan vs Build

**Elemento que practica:** modos de trabajo.

**Objetivo:** separar el diseño de la ejecución. En Plan el agente no edita; al
ejecutar sí.

- **OpenCode:** `Shift+Tab` hasta Plan, luego hasta Build.
- **Cursor:** **Plan** → **Agent**.
- **Copilot:** Plan (`/plan`) → revisar plan → **Agent** / **Implement plan**.

Presiona o elegí Plan y pide:

```text
Planifica cómo implementar resumen_por_categoria en @gastos.py
para que pase test_resumen_por_categoria. No edites archivos.
Muéstrame el plan en pasos y qué casos borde considerarías.
```

Revisa el plan. Luego pasá a Build/Agent y pide:

```text
Implementa el plan anterior en @gastos.py. No toques otras funciones
ni los tests. Ejecuta los tests al final.
```

**Criterio de "ya funcionó":** en Plan no hubo cambios en los archivos; al
ejecutar, la prueba de `resumen_por_categoria` pasa y el total queda en 5
pruebas que pasan y 1 que no pasa. La que falta es el bug de `totalizar` con
montos de texto.

### Misión 4: reglas del proyecto en `AGENTS.md`

**Elemento que practica:** `AGENTS.md`.

**Objetivo:** dar reglas permanentes al agente y comprobar que las respeta sin
repetirlas en cada prompt.

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

**Criterio de "ya funcionó":** la función se llama `gasto_mas_alto`, tiene
docstring en español, no aparece `pytest` ni una dependencia nueva, y las
pruebas existentes siguen en 5 que pasan y 1 que no pasa. Si agregó una prueba
nueva, también debe pasar.

### Misión 5 (opcional): permisos + alucinación

**Elementos que practica:** permisos y detección de alucinaciones.

**Objetivo:** ver que el agente pide aprobación para comandos y que no debes
aceptar código que usa APIs que no existen.

Para los permisos, pide:

```text
Ejecuta ls -la y dime qué archivos hay en el proyecto.
```

Debe aparecer una solicitud de aprobación. Acepta una vez. Luego pide:

```text
Ejecuta los tests del proyecto.
```

| Ruta | Comportamiento esperado |
| --- | --- |
| **OpenCode** | `opencode.jsonc`: `ls` pide aprobación; `python3 -m unittest …` no. |
| **Cursor** | `.cursor/hooks/permisos-shell.sh`: mismo criterio; Auto-run global puede variar el detalle. |
| **Copilot** | `.vscode/settings.json` (`chat.tools.terminal.autoApprove`) + nivel **Manual permissions**: unittest con poca fricción; `ls` pide confirmación. Políticas Enterprise o **Allow all** pueden cambiar el comportamiento. |

Para la alucinación, pide:

```text
Agrega una función promedio_movil(gastos) que use
statistics.promedio_movil de la biblioteca estándar.
```

Después pide una prueba y ejecuta los tests:

```text
Agrega una prueba para promedio_movil en tests/test_gastos.py
y ejecuta los tests.
```

**Criterio de "ya funcionó":** el primer comando pidió aprobación, el de tests
no, y detectaste que `statistics.promedio_movil` no existe. Puede pasar de dos
formas: el agente lo advierte antes de escribir, o la prueba falla con
`AttributeError`. En ambos casos, no aceptes la API inventada. Termina deshaciendo
cambios (`/undo` o **Revert**).

## Hooks: ejemplo del taller

Las reglas piden; los hooks garantizan. Un hook es código que el producto ejecuta
en un punto del flujo, sin depender de que el modelo lo recuerde.

### OpenCode: plugin que redacta

```ts
// Hook del taller. Se carga solo desde .opencode/plugins/redactor/index.ts.

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

Prueba escribir `SECRETO` en un prompt: debe llegar al modelo como `[redactado]`.

### Cursor: hook que bloquea

En Cursor, `beforeSubmitPrompt` no puede reescribir el texto; solo permite o
bloquea el envío. El taller usa `.cursor/hooks/bloquear-secreto.sh`: si el prompt
contiene `SECRETO`, no se envía y ves un mensaje del hook.

Prueba escribir `SECRETO` en un prompt: debe bloquearse antes de enviar.

### Copilot: hook que redacta (Preview)

Copilot en VS Code usa `UserPromptTransformed` en `.github/hooks/taller.json` y
`.github/hooks/redact-secreto.sh`: `SECRETO` llega al modelo como `[redactado]`
(más parecido a OpenCode). Los hooks Copilot en VS Code están en **Preview**; si
no cargan, leé el script en clase y explicá garantía vs regla.

Responde (las tres rutas):

1. ¿En qué momento del flujo interviene?
2. ¿Qué hace con la palabra `SECRETO`?
3. ¿Por qué esto no se logra solo con una regla en `AGENTS.md`?

## Extensiones del proyecto

| Extensión | OpenCode | Cursor | Copilot | Cómo se invoca |
| --- | --- | --- | --- | --- |
| Agente | `.opencode/agents/revisor.md` | `.cursor/agents/revisor.md` | `.github/agents/revisor.md` | Agente **revisor** o pedir revisión solo lectura |
| Comando / prompt | `.opencode/commands/explicar.md` | `.cursor/commands/explicar.md` | `.github/prompts/explicar.prompt.md` | `/explicar` o picker **explicar** |
| Skill | `.opencode/skills/correr-tests/` | `.cursor/skills/correr-tests/` | `.github/skills/correr-tests/` | Mencionar tests o dejar que Copilot cargue la skill |
| Hook / permisos | plugin redactor + `opencode.jsonc` | `hooks.json` + scripts | `hooks/taller.json` + `.vscode/settings.json` | `SECRETO`: redacta (OC/Copilot) o bloquea (Cursor) |

Un agente cambia quién responde; un comando cambia cómo pides; una skill cambia
cómo trabaja; un hook cambia qué pasa siempre.

## Mapa de misiones y elementos

| Elemento | OpenCode | Cursor | Copilot | Qué se practica |
| --- | --- | --- | --- | --- |
| Modelo | `/models` | Settings | Settings | Elegir y cambiar modelo |
| Contexto | Misión 1, `@` | Misión 1, `@` | Misión 1, `#file` | Archivos reales antes de editar |
| Instrucción | Misión 2 | Misión 2 | Misión 2 | Cambio acotado con límites |
| Modos | Plan/Build | Plan/Agent | Plan/Agent | Planificar sin editar, luego ejecutar |
| Herramientas y permisos | `opencode.jsonc` | hook shell | `settings.json` | Aprobar comandos; unittest sin fricción |
| Verificación | Misión 2 | Misión 2 | Misión 2 | Tests vs criterio |
| Reglas | `AGENTS.md` | `AGENTS.md` | `AGENTS.md` | Reglas permanentes observables |
| Hooks | Plugin redactor | bloquear | redactar (Preview) | Garantía del sistema vs sugerencia |

Las reglas las interpreta el modelo; los hooks los ejecuta el producto. La
alucinación no es un elemento: es un riesgo que se detecta con la verificación.

**Deshacer sin git:** OpenCode usa `/undo` y `/redo`. En Cursor y Copilot usá
**Revert** / deshacer en el editor; git es opcional.
