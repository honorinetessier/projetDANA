# Mapping

This directory contains the mapping files used to define how the source data is represented using the GeoNames ontology and converted into RDF.

## Directory Structure

```text
Mapping/
├── mappings_https.rdf
└── mappings_v3.01.rdf
```

## Mapping Files

### `mappings_https.rdf`

This mapping file defines the RDF representation of the GeoNames data using HTTPS-based namespaces.

It specifies how source data fields are associated with RDF classes and properties.

### `mappings_v3.01.rdf`

This file contains the mapping configuration used with version 3.01 of the GeoNames mapping resources.

It provides the RDF mapping information required to represent the source dataset according to the selected ontology structure.

## Role in the Project

The mapping files provide the link between the source data and its RDF representation.

The general transformation process is:

```text
Source CSV
    ↓
Mapping
    ↓
RDF triples
    ↓
Turtle / N-Triples
```

The mappings are used together with the transformation scripts and TARQL queries located in:

```text
Transformations/Tarql/
```

## Related Resources

The mapping process relies primarily on the GeoNames ontology, available in:

```text
Ontology/ontology_v3.3.rdf
```

The resulting RDF data is stored under:

```text
Data/RDF/
```

and can subsequently be queried using the SPARQL queries in:

```text
SPARQL/
```

## Project Pipeline

```text
GeoNames data
    ↓
Data cleaning
    ↓
Processed CSV
    ↓
TARQL + Mapping
    ↓
RDF representation
    ↓
SPARQL
    ↓
Inference
    ↓
Metadata and Linking
```

The mapping layer is therefore an essential step between the prepared source data and the semantic RDF representation used in the rest of the project.