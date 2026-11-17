# Ontology

This directory contains the ontology resources used to describe the geographic entities in the project.

## Directory Structure

```text
Ontology/
└── ontology_v3.3.rdf
```

## GeoNames Ontology

The project uses the **GeoNames ontology** to represent geographic features and their relationships in RDF.

The ontology provides classes and properties for describing entities such as:

- populated places;
- administrative areas;
- mountains and other physical features;
- hotels and other points of interest;
- geographic coordinates;
- population;
- feature classifications.

The ontology is used to give semantic meaning to the data rather than representing it only as CSV fields.

## Ontology Resource

`ontology_v3.3.rdf` contains the ontology resource used by the project.

It provides the vocabulary referenced by the mapping and RDF transformation steps.

For example, the generated RDF data uses GeoNames properties such as:

```text
gn:name
gn:population
gn:featureCode
gn:lat
gn:long
```

with the GeoNames namespace:

```text
https://www.geonames.org/ontology#
```

Other vocabularies, such as Schema.org and SKOS, are also used where appropriate in the project.

## Role in the Project

The ontology is used throughout the RDF pipeline:

```text
Source Data
    ↓
Data Cleaning
    ↓
Processed CSV
    ↓
Mapping / TARQL
    ↓
RDF using the GeoNames ontology
    ↓
SPARQL Queries
    ↓
RDFS / OWL Inference
```

It also provides the semantic basis for linking the GeoNames dataset with other datasets during Phase 2.

## Related Resources

The ontology is used together with the mapping files located in:

```text
Mapping/
```

and the transformation queries located in:

```text
Transformations/Tarql/
```

The generated RDF dataset is available under:

```text
Data/RDF/
```

and is queried through:

```text
SPARQL/
```