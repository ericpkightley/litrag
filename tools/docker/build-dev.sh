#!/bin/bash
# tools/docker/build-dev.sh
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
docker build -f "$PROJECT_ROOT/Dockerfile.dev" -t litrag:dev "$PROJECT_ROOT"