# Project Context

## Project Name

**Showcase A — Data Quality Discovery & Remediation**

Demo showcasing a complete data quality workflow on real French open data (DVF - Demandes de Valeurs Foncières).

## Domain

French real estate transactions data quality analysis. The workflow includes:

1. Discover — Find quality issues in unfamiliar data
2. Diagnose — Understand root causes and business impact
3. Remediate — Implement automated checks
4. Monitor — Track quality over time

## Architecture

```tree
src/
├── config/      # Configuration (env.py)
├── ingest/      # Data ingestion
├── quality/     # Quality framework
├── transform/   # Data transformations
└── utils/       # Shared utilities
```

## Key Dependencies

- **Data Source**: DVF (French open data) + API Adresse (geocoding)
- **Notebooks**: Jupyter for exploration (`notebooks/`)
- **Dashboard**: Quality visualization (`dashboard/`)

## Notes

- Currently in **Phase 1: Data Exploration**
- Uses Makefile for common commands (`make dev`, `make test`, `make notebook`)
- Configuration via `.secrets.env` for sensitive values
