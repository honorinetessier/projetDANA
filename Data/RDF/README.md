# RDF Data

This directory contains the RDF representation of the processed GeoNames dataset.

## Contents

- `Triplet_TTL.zip` – compressed Turtle representation of the generated RDF dataset.

The RDF data was generated from the cleaned CSV dataset using the transformation queries available in:

```text
Transformations/Tarql/
```

## Representation

The dataset is represented using RDF triples and uses the GeoNames ontology together with mappings to external Semantic Web vocabularies.

The resulting RDF data can be queried using SPARQL.

## Data Generation

The transformation workflow is:

```text
GeoNames raw data
        ↓
Data cleaning
        ↓
Clean CSV dataset
        ↓
TARQL transformation
        ↓
N-Triples
        ↓
Turtle
        ↓
RDF dataset
```

The generated RDF dataset is subsequently used for SPARQL queries, metadata generation, inference and multi-dataset linking.