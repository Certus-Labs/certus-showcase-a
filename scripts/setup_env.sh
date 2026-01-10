#!/usr/bin/env bash
# Setup environment and validate configuration

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

echo "Setting up showcase-a-batch environment..."

# Check if .secrets.env exists
if [ ! -f .secrets.env ]; then
    echo "Creating .secrets.env from template..."
    cp .secrets.env.example .secrets.env
    echo "✓ .secrets.env created"
else
    echo "✓ .secrets.env already exists"
fi

# Create data directories
echo "Creating data directories..."
mkdir -p data/raw/dvf
mkdir -p data/raw/insee
mkdir -p data/processed
mkdir -p data/samples
mkdir -p outputs
echo "✓ Data directories created"

# Install dependencies with uv
if command -v uv &> /dev/null; then
    echo "Installing dependencies with uv..."
    uv sync --all-extras
    echo "✓ Dependencies installed"
else
    echo "⚠ uv not found. Please install uv: https://github.com/astral-sh/uv"
    exit 1
fi

echo ""
echo "Setup complete! 🎉"
echo ""
echo "Next steps:"
echo "  1. Review .secrets.env and adjust if needed"
echo "  2. Run 'make notebook' to start exploring"
echo "  3. See data/README.md for data download instructions"
