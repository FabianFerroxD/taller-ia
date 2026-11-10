#!/bin/bash
# Hook del taller: redacta SECRETO en el prompt que ve el modelo (Copilot VS Code).

set -euo pipefail

input=$(cat)

python3 -c '
import json
import sys

data = json.load(sys.stdin)
text = (
    data.get("transformedPrompt")
    or data.get("transformed_prompt")
    or data.get("prompt")
    or ""
)
if "SECRETO" in text:
    text = text.replace("SECRETO", "[redactado]")
    print(json.dumps({"modifiedTransformedPrompt": text}))
else:
    print("{}")
' <<<"$input"
