# Showcase A — Data Quality Discovery & Remediation

> **Demo**: French Real Estate Transactions (DVF + API Adresse)  
> **Status**: Phase 1 — Data Exploration  
> **Last updated**: 2026-01-10

## Overview

This demo showcases a complete data quality workflow on real French open data:

1. **Discover** — Find quality issues in unfamiliar data
2. **Diagnose** — Understand root causes and business impact
3. **Remediate** — Implement automated checks
4. **Monitor** — Track quality over time

**Why this matters**: Most "data quality" tools are sold as black boxes. We show the full process—from exploration to production—so clients understand both the methodology and the value.

## Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (fast Python package manager)

### Setup

```bash
# Install dependencies
make dev

# Copy environment template
cp .secrets.env.example .secrets.env

# Start Jupyter for exploration
make notebook
```

## Project Structure

```
showcase-a-batch/
├── docs/                    # Documentation
│   ├── architecture.md      # System design
│   ├── exploration-report.md # Phase 1 findings
│   └── quality-framework.md # How checks work
│
├── data/                    # Raw data (see data/README.md)
├── notebooks/               # Exploration & analysis
├── src/                     # Source code
│   ├── config/              # Configuration
│   ├── ingest/              # Data ingestion
│   ├── quality/             # Quality framework
│   ├── transform/           # Data transformations
│   └── utils/               # Shared utilities
│
├── tests/                   # Tests
└── dashboard/               # Quality visualization
```

## Development

### Common Commands

```bash
make help           # Show all available commands
make dev            # Install dev dependencies
make lint           # Run linter
make format         # Format code
make test           # Run all tests
make notebook       # Start Jupyter
make clean          # Clean cache files
```

### Code Quality

This project uses:

- **[uv](https://github.com/astral-sh/uv)** for fast dependency management
- **[ruff](https://github.com/astral-sh/ruff)** for linting and formatting
- **pytest** for testing

All code is formatted with `ruff format` and linted with `ruff check`.

## Phases

### Phase 1: Data Exploration (Current)

- Download DVF sample data
- Run discovery queries (see `notebooks/`)
- Document quality issues found
- **Gate**: Decide if findings justify Phase 2

### Phase 2: Quality Framework (TBD)

- Implement automated checks
- Create quality metrics
- Build alerting

### Phase 3: Dashboard & Deliverables (TBD)

- Quality scorecard
- Video walkthrough
- Sales materials

## Documentation

- [Demo Specification](../certus-docs/demo/demo-a-specs.md) — Full requirements
- [Architecture](docs/architecture.md) — System design (TBD)
- [Exploration Report](docs/exploration-report.md) — Phase 1 findings (TBD)

## License

MIT License — See [LICENSE](LICENSE)

Copyright (c) 2026 Certus-Labs
