# Transformations

This directory contains the resources used to transform the processed CSV data into RDF.

## Directory Structure

```text
Transformations/
└── Tarql/
    ├── MappingForTARQL.pdf
    ├── README.md
    ├── tarql_v1.rq
    └── tarql_v2.rq
```

## TARQL

The project uses **TARQL** to transform tabular data into RDF.

TARQL allows SPARQL-based transformation rules to be applied directly to CSV data. The transformation queries define how the columns of the processed dataset are converted into RDF resources, classes and properties.

## Transformation Queries

### `tarql_v1.rq`

This file contains an initial version of the TARQL transformation query.

It defines the RDF triples generated from the processed CSV dataset.

### `tarql_v2.rq`

This file contains an updated version of the TARQL transformation query.

It improves or extends the initial transformation rules used to generate the RDF representation.

Keeping both versions makes it possible to compare the evolution of the transformation process.

## Documentation

`MappingForTARQL.pdf` contains supporting documentation related to the TARQL mapping and transformation process.

Additional information about the transformation workflow is available in:

```text
Transformations/Tarql/README.md
```

## Input and Output

The transformation process connects the processed tabular data to the RDF dataset:

```text
Data/Processed/
        ↓
    TARQL query
        ↓
RDF triples
        ↓
Data/RDF/
```

The generated RDF can then be used by the SPARQL, inference and metadata stages of the project.

## Relation to Mapping and Ontology

TARQL transformations work together with the resources in:

```text
Mapping/
Ontology/
```

The mapping and ontology define the semantic structure of the RDF representation, while the TARQL queries specify how the source CSV values are converted into that representation.

## Phase 2

The transformation workflow established in Phase 1 provides the RDF datasets required for Phase 2.

During Phase 2, these RDF datasets will be linked with datasets produced by other groups, allowing more complex cross-dataset SPARQL queries to be executed.