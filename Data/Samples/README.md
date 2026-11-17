# Sample Data

This directory contains a small RDF sample extracted from the project dataset.

## File

```text id="8y1j5m"
Samples/
└── echantillon.nt
```

### `echantillon.nt`

`echantillon.nt` is an RDF sample stored in **N-Triples** format.

It provides a smaller dataset that can be used for testing and development without loading the complete RDF dataset.

## Purpose

The sample dataset is useful for:

- testing SPARQL queries;
- validating RDF structures;
- experimenting with inference;
- debugging transformation steps;
- quickly testing changes during development.

## Relation to the Full Dataset

The sample represents the same general RDF structure as the complete dataset, but on a smaller scale.

The full RDF dataset is available under:

```text id="qf7j2k"
Data/RDF/
```

The sample is also used by the inference workflow in:

```text id="5f3c8h"
Inference/
```

where it provides a lightweight dataset for testing inference rules and comparing results.