#!/bin/bash
# Hook del taller: bloquea prompts que contienen la palabra SECRETO.

set -euo pipefail

input=$(cat)
prompt=$(python3 -c 'import json,sys; print(json.load(sys.stdin).get("prompt",""))' <<<"$input")

if [[ "$prompt" == *SECRETO* ]]; then
  printf '%s\n' '{"continue":false,"user_message":"El hook bloqueó el envío: no escribas SECRETO en el prompt. En OpenCode el plugin del taller lo redacta a [redactado]."}'
  exit 0
fi

printf '%s\n' '{"continue":true}'
exit 0
