#!/bin/bash
# tools/docker/run-dev.sh
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
docker run -it \
-v "$PROJECT_ROOT/litrag:/app/litrag" \
-v "$PROJECT_ROOT/main.py:/app/main.py" \
-v "$PROJECT_ROOT/data:/app/data" \
litrag:dev \
bash