#!/bin/bash
# tools/docker/run-dev.sh
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
docker run -it \
-v "$PROJECT_ROOT/raglit:/app/raglit" \
-v "$PROJECT_ROOT/main.py:/app/main.py" \
raglit:dev \
bash