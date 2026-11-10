# Guion del instructor: programar con IA

Este guion es para quien dicta el taller. El enunciado del alumnado está en
`README.md`. Hay tres rutas: **OpenCode** (terminal), **Cursor** (IDE) o
**Copilot** (VS Code).

## Checklist previo a la clase

Común a ambas rutas:

- [ ] `python3 --version` responde 3.10 o superior.
- [ ] Tests corridos una vez: `python3 -m unittest discover -s tests -t .`
      debe dar 2 pruebas que pasan y 4 que no pasan.
- [ ] Confirmado que no se necesita git ni red para ejecutar los tests.

**OpenCode:**

- [ ] OpenCode V2 instalado: `opencode --version` responde sin error.
- [ ] Proveedor autenticado: `/models` muestra al menos un modelo disponible.
- [ ] Modelo elegido y probado con un prompt corto, por ejemplo "responde OK".
- [ ] Repo abierto en una terminal con `opencode` desde la carpeta del taller.
- [ ] Terminal de la sala probada: `Ctrl+Shift+V` pega en la TUI y `Shift+Tab`
      cambia de agente.
- [ ] Permisos probados: un `ls` pide aprobación y el comando de tests no.
- [ ] Plan B: ejemplo de `opencode run` y copia local del repo.

**Cursor:**

- [ ] Cursor instalado y actualizado; modelo elegido en Settings.
- [ ] Repo abierto como carpeta; workspace marcado **Trusted** (hooks de proyecto).
- [ ] Hooks cargados: panel Hooks o canal Hooks sin error al abrir el proyecto.
- [ ] Prompt con `SECRETO` bloqueado; `ls` pide aprobación vía hook; unittest no.
- [ ] Probados `/explicar gastos.py` y "usa el subagente revisor…".
- [ ] Plan B: tests manuales y lectura de prompts sin agente.

**Copilot (VS Code):**

- [ ] VS Code + extensión GitHub Copilot; suscripción activa; modelo probado.
- [ ] Carpeta del taller abierta; permisos del chat en **Manual permissions**.
- [ ] `.vscode/settings.json` del repo cargado (unittest auto-aprobado).
- [ ] Hooks **Preview** probados: prompt con `SECRETO` → redacción; si falla, Plan B.
- [ ] `#file:gastos.py` en misión 1; Plan → Agent en misión 3.
- [ ] Agente **revisor** y prompt **explicar** en picker.
- [ ] `ls` pide confirmación; `python3 -m unittest …` con poca fricción.

## Tiempos (120 minutos)

| Bloque | Minutos |
| --- | ---: |
| Apertura | 7 |
| Modelo y contexto | 9 |
| Instrucción y modos | 9 |
| Herramientas y verificación | 10 |
| Reglas | 7 |
| Hooks | 8 |
| Extensiones | 12 |
| Demo integradora | 5 |
| Pausa | 5 |
| Práctica | 30 |
| Puesta en común y riesgos | 10 |
| Cierre | 8 |
| **Total** | **120** |

## Bloques

### Apertura (7 min)

**Decir:** El agente no es autocompletado: recibe un objetivo, lee archivos,
propone cambios y ejecuta comandos. Hoy practican los ocho elementos: modelo,
contexto, instrucción, modos, herramientas y permisos, verificación, reglas y
hooks. La alucinación es un riesgo que atacan con verificación. Los tests corren
sin red y sin git.

**Mostrar:** el árbol del repo, el `README.md` y la salida inicial de los tests
(2 pasan, 4 no).

**Mostrar (Cursor):** carpeta `.cursor/` junto a `.opencode/`; aclarar qué ruta
sigue la clase.

**Mostrar (Copilot):** `.github/` y `.vscode/settings.json`; aclarar ruta VS Code.

### Modelo y contexto (9 min)

**Decir:** el modelo se elige una vez y se puede cambiar; la calidad depende del
contexto. `@archivo` mete contenido real y evita adivinar. En OpenCode un rango
`@archivo#1-30` acota.

**Mostrar (OpenCode):** `/models`, prompt misión 1 con `@gastos.py` y
`@tests/test_gastos.py`.

**Mostrar (Cursor):** Settings → modelo; mismo prompt; opcional **Ask** en
misión 1.

**Mostrar (Copilot):** `#file:gastos.py` y `#file:tests/test_gastos.py`; **Ask**
en misión 1.

### Instrucción y modos (9 min)

**Decir:** prompt vago vs preciso. Plan separa pensar de ejecutar: en Plan no se
edita; al pasar a ejecución sí.

**Mostrar (OpenCode):** misión 2 vaga, `/undo`, preciso; `Shift+Tab` Plan → Build.

**Mostrar (Cursor):** misión 2 vaga, **Revert**, preciso; **Plan** → **Agent**.

**Mostrar (Copilot):** misma secuencia; `/plan` en misión 3.

### Herramientas y verificación (10 min)

**Decir:** la verdad la dan los tests. Los permisos del proyecto definen qué shell
pide aprobación.

**Mostrar (OpenCode):** `!python3 -m unittest discover -s tests -t .`, traceback
de `NotImplementedError`, `ls` con aprobación y `opencode.jsonc`.

**Mostrar (Cursor):** mismos tests en terminal o vía agente; `ls` con aprobación
del hook; `.cursor/hooks/permisos-shell.sh`.

**Mostrar (Copilot):** `ls` con confirmación; unittest y
`.vscode/settings.json` (`chat.tools.terminal.autoApprove`).

### Reglas (7 min)

**Decir:** `AGENTS.md` guarda reglas permanentes; conviene que sean observables.

**Mostrar:** regla de docstring en español, pedir `gasto_mas_alto`, revisar
nombre y docstring. Al terminar, quitar regla agregada y deshacer la función
(`/undo` o **Revert**).

**Mostrar (Cursor):** mencionar que también existe `.cursor/rules/` para reglas
por archivo; en este taller alcanza `AGENTS.md`.

**Mostrar (Copilot):** Copilot lee `AGENTS.md` sin `copilot-instructions.md`
duplicado.

### Hooks (8 min)

**Decir:** los hooks los ejecuta el producto, no el modelo: garantía, no
sugerencia.

**Mostrar (OpenCode):** `.opencode/plugins/redactor/index.ts`, prompt con
`SECRETO` → `[redactado]` en lo que ve el modelo.

**Mostrar (Cursor):** `.cursor/hooks/bloquear-secreto.sh` y `hooks.json`; prompt
con `SECRETO` → **bloqueo** con mensaje. Explicar: misma lección (el sistema
interviene), distinto efecto (redactar vs impedir envío). Canal **Hooks** si hace
falta depurar.

**Mostrar (Copilot):** `.github/hooks/redact-secreto.sh`; `SECRETO` →
`[redactado]` como OpenCode. Avisar **Preview**; si no corre, enseñar el script.
No confundir con `UserPromptSubmitted` (no reescribe en command hooks).

### Extensiones (12 min)

**Decir:** agente, comando, skill y hook empaquetan los ocho elementos.

**Mostrar (OpenCode):** árbol `.opencode/`, `/explicar gastos.py`, skill de tests,
subagente revisor, `SECRETO` con plugin.

**Mostrar (Cursor):** árbol `.cursor/`, mismas invocaciones; `SECRETO` con bloqueo.

**Mostrar (Copilot):** árbol `.github/`; agente **revisor**, prompt **explicar**;
skill de tests; `SECRETO` con redacción.

### Demo integradora (5 min)

**Decir:** ciclo completo hasta 6/6 tests y vuelta al estado inicial.

**Mostrar:** prompt integrador del README; 6/6; deshacer hasta 2/4 (`/undo` o
**Revert**).

### Pausa (5 min)

**Decir:** pausa corta; repo en estado inicial (2 pasan, 4 no).

### Práctica (30 min)

**Decir:** misiones 1 a 4 (5 opcional); no copiar prompts sin leerlos; deshacer
si algo se rompe.

**Mostrar:** lista de misiones y temporizador; pedir salida de tests, no solo
texto del agente.

### Puesta en común y riesgos (10 min)

**Decir:** prompts que funcionaron; momentos de alucinación o exceso; tabla de
riesgos.

**Mostrar:** diff real, permisos (`opencode.jsonc`, hooks Cursor o
`.vscode/settings.json`) y tabla del `README.md`.

### Cierre (8 min)

**Decir:** ciclo contexto → instrucción → plan → ejecución → verificación. Reglas
piden; hooks garantizan.

**Mostrar:** tabla final del `README.md` y tests en estado inicial.

## Los 8 elementos

1. **Modelo:** OpenCode `/models`; Cursor/Copilot Settings.
2. **Contexto:** `@` (OC/Cursor) o `#file` (Copilot).
3. **Instrucción:** cambio acotado con límites y criterio.
4. **Modos:** Plan/Build, Plan/Agent o Plan+Implement (Copilot).
5. **Herramientas y permisos:** unittest sin fricción; el resto con aprobación.
6. **Verificación:** tests vs expectativa.
7. **Reglas:** `AGENTS.md`.
8. **Hooks:** OpenCode plugin; Cursor bloqueo; Copilot redacción (Preview).

Las reglas las interpreta el modelo. Los hooks los ejecuta el producto. Regla =
probabilidad; hook = garantía.

La alucinación no es un elemento: es un riesgo que se detecta con el elemento 6.

## Riesgos

| Riesgo | Ejemplo | Qué hacer |
| --- | --- | --- |
| Alucinación | `statistics.promedio_movil` no existe | Verificar con tests o documentación antes de aceptar |
| Secretos en el prompt | Pegar un token o una clave en el chat | No pegar secretos; usar configuración del entorno y revocar si se filtró |
| Aceptar sin leer | Aprobar un cambio o un comando sin revisar | Leer la diferencia y ejecutar los tests antes de aprobar |
| Dependencias inventadas | Importar una librería que no está instalada | Respetar `AGENTS.md`: solo biblioteca estándar |
| Licencias | Copiar código de otro proyecto sin revisar su licencia | Verificar el origen y la licencia antes de reutilizar |

## Plan B

**OpenCode**

- Interfaz caída pero proveedor OK: `opencode run "Lee gastos.py y explica qué falta"`.
- Sin red o sin proveedor: guion + repo + tests a mano + discusión de prompts.

**Cursor**

- Sin agente o sin red: mismos tests y `gastos.py` a mano; leer misiones del README.
- Hooks no cargan: workspace no trusted o reiniciar Cursor; si persiste, enseñar
  permisos con la configuración global y seguir con verificación manual.

**Copilot**

- Hooks Preview no cargan: mostrar `redact-secreto.sh` y comparar con reglas.
- Sin red o sin Copilot: tests a mano y discusión de prompts (igual que otras rutas).
- **Allow all** en sesión: recordar riesgo; volver a **Manual permissions**.

En todos los casos: sin red, la práctica de tests sigue; el agente no.
