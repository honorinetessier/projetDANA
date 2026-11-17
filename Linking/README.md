# Multi-Dataset Linking

This directory contains the resources developed for Phase 2 of the project.

The objective of this phase is to integrate our GeoNames-based dataset with datasets produced by other project groups and to enable semantic queries across multiple datasets.

## Objectives

The linking phase aims to:

- identify common concepts and entities across different datasets;
- establish semantic links between heterogeneous datasets;
- reuse existing ontologies and vocabularies whenever possible;
- make the different datasets interoperable;
- formulate SPARQL queries that combine information from multiple datasets.

## Structure

```text
Linking/
├── Datasets/
│   ├── Group_01/
│   ├── Group_02/
│   └── ...
│
├── Links/
│   ├── Pairwise/
│   └── Global/
│
├── Queries/
│   └── Cross_Dataset/
│
└── Results/
```

### Datasets

The `Datasets/` directory contains information and, when necessary, local copies of the datasets used for the integration.

Each group should be documented separately, including the dataset source, namespaces, main classes, properties and concepts relevant for linking.

### Links

The `Links/` directory contains the semantic links established between the datasets.

Pairwise links can be stored in `Links/Pairwise/`, while links involving several datasets or the complete integration can be stored in `Links/Global/`.

The links may use properties such as `owl:sameAs`, `rdfs:seeAlso` or other appropriate semantic relations depending on the nature of the relationship.

### Cross-Dataset Queries

The `Queries/Cross_Dataset/` directory contains SPARQL queries that combine information from multiple datasets.

The queries are designed to demonstrate that the datasets can be accessed through a common semantic layer rather than being treated as isolated sources.

### Results

The `Results/` directory contains the results and observations associated with the cross-dataset queries.

## Integration Approach

The integration process follows these main steps:

1. Analyse the datasets provided by the different groups.
2. Identify common entities, concepts and vocabularies.
3. Compare namespaces, classes and properties.
4. Define appropriate semantic links.
5. Store and document the links.
6. Test the links with SPARQL queries.
7. Build increasingly complex queries combining several datasets.
8. Analyse and document the results.

## Multi-Dataset Queries

A key objective of this phase is to construct queries involving several datasets.

The final queries should demonstrate how information from different groups can be combined to answer questions that cannot be answered using a single dataset alone.

The number of datasets involved in each query and the concepts used for linking will be documented with the corresponding query.

## Reproducibility

All linking files and SPARQL queries should be documented so that the integration process can be understood and reproduced from the repository.