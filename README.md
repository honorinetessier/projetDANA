# Semantic Web & Knowledge Graph — GeoNames France

A Semantic Web project for transforming geographic data into a structured RDF knowledge graph, enriching it with semantic vocabularies and inference, and connecting it with external datasets to enable integrated knowledge discovery.

The project uses **GeoNames France** as the main geographic dataset and combines data engineering, RDF modeling, ontology-based representation, SPARQL querying, semantic inference, dataset metadata and inter-dataset linking.

---

## Overview

The project explores the complete lifecycle of semantic data:

```text
Raw Geographic Data
        ↓
Data Preparation & Cleaning
        ↓
RDF Transformation
        ↓
Ontology-Based Representation
        ↓
SPARQL Querying
        ↓
Semantic Inference
        ↓
Dataset Metadata
        ↓
Inter-Dataset Linking
        ↓
Integrated Knowledge Graph
```

The objective is to transform heterogeneous geographic information into a **machine-readable, semantically structured and interconnected knowledge graph** that can be queried and enriched.

---

## Key Features

### Data Preparation

The original GeoNames data is processed using Python scripts to prepare a consistent dataset for semantic transformation.

The preprocessing workflow includes:

- source data conversion;
- geographic feature filtering;
- data cleaning;
- preparation of CSV datasets;
- extraction of smaller datasets for testing and analysis.

The processing scripts are available in:

```text
Scripts/
```

Processed datasets are stored in:

```text
Data/Processed/
```

---

### RDF Data Modeling

The processed geographic data is represented using **RDF (Resource Description Framework)**.

The project uses the **GeoNames ontology** as the main vocabulary for describing geographic entities, together with additional semantic vocabularies where appropriate.

Examples of represented information include:

- geographic names;
- populations;
- geographic coordinates;
- feature types;
- administrative and physical features;
- points of interest.

The ontology resources are available in:

```text
Ontology/
```

and the mapping resources in:

```text
Mapping/
```

---

### Tabular-to-RDF Transformation

**TARQL** is used to transform the processed CSV data into RDF.

The transformation queries define how source columns are mapped to RDF resources and properties.

```text
Processed CSV
     ↓
TARQL Mapping
     ↓
RDF Triples
     ↓
Turtle / N-Triples
```

The transformation resources are available in:

```text
Transformations/Tarql/
```

The resulting RDF dataset is stored in:

```text
Data/RDF/
```

---

### SPARQL Querying

The generated RDF graph can be explored and analysed using **SPARQL**.

The project includes queries demonstrating:

- RDF pattern matching;
- filtering and ordering;
- numerical conditions;
- geographic filtering using coordinates;
- aggregation;
- `SELECT` queries;
- `CONSTRUCT` queries;
- semantic classification analysis.

Examples include identifying:

- mountain peaks above 3,000 metres;
- the most populated localities;
- hotels around Nantes;
- highly populated places;
- frequently occurring geographic feature types.

The queries and documented results are available in:

```text
SPARQL/
```

---

### Semantic Inference

The project also explores RDF inference to derive additional knowledge from the existing semantic graph.

Inference resources, configurations, sample data and comparison results are organized in:

```text
Inference/
```

This step demonstrates how ontology-based reasoning can enrich an RDF graph beyond the information explicitly stored in the original dataset.

---

### Dataset Metadata

The RDF dataset is described using **VoID (Vocabulary of Interlinked Datasets)**.

VoID metadata provides a machine-readable description of the dataset and its RDF structure, making the dataset easier to document and integrate with other semantic datasets.

The metadata resources are available in:

```text
Metadata/VoID/
```

---

### Inter-Dataset Linking

A key aspect of the project is connecting the GeoNames knowledge graph with external RDF datasets.

The linking process involves:

- analysing external datasets and their vocabularies;
- identifying semantically corresponding entities;
- establishing RDF links between resources;
- documenting pairwise relationships;
- consolidating links between multiple datasets;
- querying the resulting interconnected graph.

The resources related to dataset integration are organized in:

```text
Linking/
├── Datasets/
├── Links/
├── Queries/
└── Results/
```

This structure supports both individual dataset relationships and larger interconnected graphs.

---

## Technologies & Standards

| Technology / Standard | Role |
|---|---|
| **RDF** | Semantic representation of data |
| **Turtle** | Human-readable RDF serialization |
| **N-Triples** | Line-based RDF serialization |
| **SPARQL** | RDF graph querying |
| **TARQL** | CSV-to-RDF transformation |
| **GeoNames Ontology** | Geographic semantic model |
| **RDFS / OWL** | Semantic reasoning and inference |
| **SKOS** | Concept and vocabulary representation |
| **Schema.org** | Additional semantic properties |
| **VoID** | Dataset metadata |
| **Python** | Data processing and preprocessing |
| **Git / GitHub** | Version control and collaboration |

---

## Repository Structure

```text
.
├── Data/
│   ├── Raw/
│   ├── Processed/
│   ├── Samples/
│   └── RDF/
│
├── Mapping/
│
├── Ontology/
│
├── Scripts/
│
├── Transformations/
│   └── Tarql/
│
├── SPARQL/
│   └── Queries/
│
├── Inference/
│   ├── Comparison/
│   └── Sample_Data/
│
├── Metadata/
│   └── VoID/
│
├── Linking/
│   ├── Datasets/
│   ├── Links/
│   ├── Queries/
│   └── Results/
│
├── README.md
├── requirements.txt
└── .gitignore
```

Each major component contains its own documentation describing its purpose, resources and workflow.

---

## Data Workflow

The complete workflow can be summarized as:

```text
GeoNames
   ↓
Data Cleaning & Filtering
   ↓
Processed Dataset
   ↓
TARQL Transformation
   ↓
RDF Knowledge Graph
   ↓
SPARQL Querying
   ↓
Semantic Inference
   ↓
VoID Metadata
   ↓
Inter-Dataset Linking
   ↓
Integrated Knowledge Graph
```

This architecture keeps data preparation, semantic modeling, querying, reasoning and dataset integration as distinct but connected components.

---

## Reproducibility

The repository is organized to make each stage of the workflow independently inspectable and reusable.

Python dependencies are listed in:

```text
requirements.txt
```

The repository also provides smaller RDF samples for testing and development without requiring the complete dataset.

Large generated RDF resources are distributed in compressed form to keep the repository manageable.

External tools such as TARQL and RDF triple-store/reasoning software are used independently of the Python environment.

---

## Project Goals

This project demonstrates practical applications of Semantic Web technologies to real-world geographic data.

It focuses on:

- transforming heterogeneous data into RDF;
- designing and applying semantic representations;
- working with ontologies and vocabularies;
- querying knowledge graphs with SPARQL;
- applying semantic inference;
- describing RDF datasets with standard metadata;
- linking independent datasets;
- performing integrated queries across interconnected knowledge graphs.

The resulting architecture provides a foundation for building **interoperable, extensible and queryable knowledge graphs from heterogeneous data sources**.