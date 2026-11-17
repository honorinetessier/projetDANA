# Scripts

This directory contains the Python scripts used to prepare and filter the GeoNames data before its transformation into RDF.

## Directory Structure

```text
Scripts/
├── Data_Cleaning.py
├── Filter_Nantes.py
├── filter_france_cities.py
└── txt_to_csv.py
```

## Scripts

### `Data_Cleaning.py`

This script is used to clean and prepare the source dataset before the RDF transformation step.

The cleaning stage removes or processes unwanted data and prepares the dataset for the following transformation steps.

### `Filter_Nantes.py`

This script filters geographic features around Nantes.

It is used to create a smaller geographical subset that can be used for local analysis and testing.

### `filter_france_cities.py`

This script filters the GeoNames data to obtain the relevant French geographic features used by the project.

It is part of the preprocessing pipeline before the data is transformed into RDF.

### `txt_to_csv.py`

This script converts the source text-based GeoNames data into CSV format.

The resulting CSV files can then be processed by the other cleaning and filtering scripts.

## Processing Pipeline

The scripts are used as part of the following workflow:

```text
GeoNames text files
        ↓
txt_to_csv.py
        ↓
CSV dataset
        ↓
filter_france_cities.py
        ↓
Data_Cleaning.py
        ↓
Clean processed dataset
        ↓
TARQL transformation
        ↓
RDF
```

`Filter_Nantes.py` can be used separately when a smaller geographical subset around Nantes is required.

## Requirements

The scripts are written in Python.

The Python dependencies used by the project are listed in:

```text
requirements.txt
```

## Role in the Project

These scripts form the preprocessing layer of the project. They make the source data suitable for semantic transformation while keeping the cleaning and filtering operations separate from the RDF generation process.

The processed datasets are stored in:

```text
Data/Processed/
```

and are subsequently used by the transformation workflow in:

```text
Transformations/Tarql/
```