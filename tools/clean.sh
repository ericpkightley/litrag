#!/bin/bash
# tools/clean.sh
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
find "$PROJECT_ROOT" -type d -name "__pycache__" -exec rm -r {} +
find "$PROJECT_ROOT" -type f -name "*.pyc" -delete