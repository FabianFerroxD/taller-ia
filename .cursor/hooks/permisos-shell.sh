#!/bin/bash
# Hook del taller: permite unittest sin aprobación; el resto pide confirmación.

set -euo pipefail

input=$(cat)
command=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("command",""))' <<<"$input")

if [[ "$command" =~ ^python3[[:space:]]+-m[[:space:]]+unittest ]]; then
  printf '%s\n' '{"permission":"allow"}'
  exit 0
fi

printf '%s\n' '{"permission":"ask","user_message":"El hook del taller pide aprobación para este comando. Solo unittest corre sin preguntar."}'
exit 0
