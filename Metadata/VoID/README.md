# VoID Metadata

This directory contains the VoID description of the RDF dataset generated from the GeoNames data.

VoID (Vocabulary of Interlinked Datasets) is used to provide metadata about the dataset and its RDF structure.

## Directory Structure

```text id="q6y5kx"
VoID/
├── Help.pdf
├── void_france.nt
└── void_france.ttl
```

## VoID Files

### `void_france.ttl`

The VoID description in Turtle format.

This file provides a human-readable RDF representation of the dataset metadata and can be inspected or queried using standard RDF tools.

### `void_france.nt`

The same VoID description represented in N-Triples format.

The N-Triples version can be useful for tools and workflows that require a line-based RDF serialization.

### `Help.pdf`

Supporting documentation for the VoID metadata and its construction.

## Purpose

The VoID description provides metadata about the RDF dataset, helping to document its structure and make it easier to integrate with other datasets.

It can describe information such as:

- the dataset itself;
- RDF classes used in the dataset;
- properties used to describe resources;
- dataset statistics;
- relationships between datasets.

## Role in the Project

The VoID metadata is created after the RDF transformation:

```text id="g6n6j8"
GeoNames Data
      ↓
Data Cleaning
      ↓
TARQL Transformation
      ↓
RDF Dataset
      ↓
VoID Description
```

The resulting metadata complements the RDF dataset without changing the underlying geographic data.

## Phase 2

In Phase 2, several datasets produced by different groups will be connected.

VoID metadata can help document these datasets and their characteristics before and during the linking process.

The linked datasets will ultimately be used for cross-dataset SPARQL queries.