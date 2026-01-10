# Data Directory

This directory contains raw and processed data files for the demo.

## Structure

```tree
data/
├── raw/              # Downloaded source data (gitignored)
│   ├── dvf/          # DVF transaction files
│   └── insee/        # INSEE commune reference
├── processed/        # Intermediate/processed data (gitignored)
└── samples/          # Small sample files for testing (committed)
```

## Downloading Data

### DVF (Demandes de Valeurs Foncières)

**Source**: <https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/>

**Download script** (coming in Phase 1):

```bash
# Download DVF data for specific départements
python scripts/download_dvf.py --departements 75 33
```

**Manual download**:

1. Visit the data.gouv.fr link above
2. Download CSV files for desired départements
3. Place in `data/raw/dvf/`

### INSEE Commune Reference

**Source**: <https://www.insee.fr/fr/information/6800675>

Download the commune reference file (CSV) and place in `data/raw/insee/`.

## Data Not Tracked in Git

Large data files are excluded via `.gitignore`. To reproduce the demo:

1. Run download scripts (see above), or
2. Follow manual download instructions

## Sample Data

Small sample files for testing will be committed to `data/samples/` (coming soon).
