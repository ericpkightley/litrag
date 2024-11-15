#!/bin/bash
# NOT USED RIGHT NOW
# start Ollama server
ollama serve &

# wait for server to be ready
until curl -s http://localhost:11434/api/version >/dev/null; do
  echo "Waiting for Ollama..."
  sleep 1
done

ollama pull mistral
python main.py