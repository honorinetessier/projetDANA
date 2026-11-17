# Data

This directory contains the data used throughout the project, from the original GeoNames dataset to the cleaned CSV files and the generated RDF representation.

## Directory Structure

```text
Data/
├── Raw/
│   └── README.md
│
├── Processed/
│   ├── france_all_features.csv
│   └── clean_france_all_features.csv
│
├── Samples/
│   └── echantillon.nt
│
└── RDF/
    ├── README.md
    └── Triplet_TTL.zip
```

## Raw Data

The `Raw/` directory documents the original GeoNames data used as the source for the project.

The raw dataset is not stored directly in the repository because of its size. The corresponding README provides information about the source data and its use in the project.

## Processed Data

The `Processed/` directory contains the CSV files obtained during the data preparation stage.

- `france_all_features.csv` — dataset containing the GeoNames features for France.
- `clean_france_all_features.csv` — cleaned version of the dataset used for the following transformation steps.

The cleaning process prepares the data for conversion into RDF.

## RDF Data

The `RDF/` directory contains the RDF representation generated from the processed dataset.

The generated RDF data is provided as a compressed archive to keep the repository size manageable.

See `Data/RDF/README.md` for more information about the RDF dataset and its generation.

## Sample Data

The `Samples/` directory contains a smaller RDF sample used for testing and development.

- `echantillon.nt` — RDF sample in N-Triples format.

The sample can be used to test queries and inference operations without loading the complete dataset.

## Data Flow

The data follows the following pipeline:

```text
Raw GeoNames data
        ↓
Data cleaning
        ↓
Processed CSV
        ↓
TARQL transformation
        ↓
RDF / Turtle
        ↓
SPARQL queries
        ↓
Inference and analysis
```

The same RDF data will also serve as the basis for the multi-dataset linking and cross-dataset queries developed in Phase 2.