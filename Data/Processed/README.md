# Processed Data

This directory contains the CSV datasets obtained after processing and cleaning the original GeoNames data.

## Files

```text id="w7r2kp"
Processed/
├── france_all_features.csv
└── clean_france_all_features.csv
```

### `france_all_features.csv`

This file contains the GeoNames geographic features selected for France after the initial filtering stage.

It serves as the main tabular dataset used as input for the subsequent cleaning and transformation steps.

### `clean_france_all_features.csv`

This file contains the cleaned version of the France dataset.

The cleaning process prepares the data for conversion into RDF by removing or processing unsuitable values and ensuring that the relevant fields are ready for semantic transformation.

## Processing Workflow

The processed datasets are produced from the raw GeoNames data using the scripts in:

```text id="eqjz0x"
Scripts/
```

The workflow is:

```text id="k1d7rx"
Raw GeoNames Data
        ↓
Initial Filtering
        ↓
france_all_features.csv
        ↓
Data Cleaning
        ↓
clean_france_all_features.csv
        ↓
TARQL Transformation
        ↓
RDF Dataset
```

## Next Step

The cleaned dataset is used as input for the TARQL transformation process located in:

```text id="4y9qne"
Transformations/Tarql/
```

The resulting RDF data is stored under:

```text id="z6k8wu"
Data/RDF/
```

The processed dataset therefore forms the main bridge between the original GeoNames data and its semantic RDF representation.