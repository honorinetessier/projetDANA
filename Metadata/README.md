# Metadata

This directory contains the metadata describing the RDF dataset produced by the project.

Metadata provides information about the dataset itself, such as its identity, structure, vocabulary and provenance.

## Directory Structure

```text
Metadata/
└── VoID/
    ├── Help.pdf
    ├── void_france.nt
    └── void_france.ttl
```

## VoID

The project uses **VoID (Vocabulary of Interlinked Datasets)** to describe the RDF dataset.

VoID provides a standard vocabulary for describing RDF datasets and their characteristics, including information about datasets, classes and links between datasets.

The VoID description is available in both N-Triples and Turtle formats.

## Files

### `void_france.ttl`

The Turtle representation of the VoID metadata describing the France dataset.

### `void_france.nt`

The same VoID metadata represented in N-Triples format.

### `Help.pdf`

Supporting documentation used during the creation and understanding of the VoID description.

## Role in the Project

The metadata layer describes the RDF dataset generated during Phase 1:

```text
Processed Data
      ↓
RDF Dataset
      ↓
VoID Metadata
      ↓
Dataset Description
```

This makes the dataset easier to understand, document and integrate with other RDF datasets.

## Relation to Phase 2

VoID becomes particularly useful when several datasets are combined.

During Phase 2, the project will link the GeoNames dataset with datasets produced by other groups. Metadata can help describe the different datasets and their relationships, supporting the construction of a larger interconnected RDF graph.

The linked datasets will then be queried using cross-dataset SPARQL queries.