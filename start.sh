#!/bin/bash

# 現在のディレクトリに移動
cd "$(dirname "$0")"
UV_PATH=/home/masato/.local/bin
$UV_PATH/uv run python -m src.graphic_recording_mcp.main 