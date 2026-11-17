
# TARQL Transformations

This directory contains the TARQL queries used to transform the cleaned GeoNames CSV data into RDF.

## Transformation Queries

Two versions of the transformation are provided:

- `tarql_v1.rq` – generates RDF using a broader set of attributes.
- `tarql_v2.rq` – focuses on GeoNames-related attributes.

## Workflow

The cleaned CSV dataset is transformed into N-Triples using TARQL:

```bash
tarql --ntriples tarql_v1.rq clean_france_all_features.csv > france_triples.nt
```

The resulting N-Triples can then be converted to Turtle using RDF tools such as `rapper`:

```bash
rapper -i ntriples -o turtle france_triples.nt > france_triples.ttl
```

The generated RDF is stored in:

```text
Data/RDF/
```

## Mapping Documentation

`MappingForTARQL.pdf` contains the documentation used to define the mapping between the CSV attributes and the RDF representation.

## Relation to the Project Pipeline

```text
Processed CSV
     ↓
TARQL mapping
     ↓
RDF / N-Triples
     ↓
Turtle dataset
     ↓
SPARQL / Inference / Linking


```