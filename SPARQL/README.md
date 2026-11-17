# SPARQL Queries

This directory contains the SPARQL queries used to explore and analyse the RDF representation of the GeoNames dataset.

The queries are executed on the generated RDF dataset and demonstrate how geographic information can be retrieved, filtered, ordered and transformed using SPARQL.

## Directory Structure

```text
SPARQL/
├── Queries/
│   ├── Altitude.rq
│   ├── Construct.rq
│   ├── Hotel.rq
│   └── Population.rq
│
├── results.md
└── README.md
```

## Queries

### 1. Altitude

`Altitude.rq` retrieves mountain peaks higher than 3,000 metres.

The query uses:

- `gn:featureCode` to identify mountain peaks;
- `gn:name` to retrieve their names;
- `schema:elevation` to retrieve elevation values.

The results are ordered by decreasing elevation and limited to the 20 highest matching features.

### 2. Construct

`Construct.rq` demonstrates the use of a SPARQL `CONSTRUCT` query.

It extracts populated places with more than 100,000 inhabitants and constructs RDF triples containing their names and population values.

This query demonstrates how SPARQL can be used not only to retrieve tabular results, but also to generate a new RDF graph from existing data.

### 3. Hotel

`Hotel.rq` retrieves hotels located in the Nantes area.

The query uses:

- the GeoNames hotel feature code (`S.HTL`);
- hotel names;
- latitude and longitude;
- geographical filtering based on latitude and longitude boundaries.

The results are ordered alphabetically by hotel name.

### 4. Population

`Population.rq` retrieves the ten most populated localities in the dataset.

The query selects GeoNames features classified as populated places (`P.PPL`), filters out entities with zero population, and orders the results by decreasing population.

## SPARQL Features Demonstrated

The queries in this directory demonstrate several fundamental SPARQL operations:

- `SELECT` queries for retrieving structured results;
- `CONSTRUCT` queries for generating RDF graphs;
- RDF pattern matching;
- filtering with `FILTER`;
- numerical comparisons;
- geographical filtering using coordinates;
- aggregation and ordering;
- result limitation with `LIMIT`;
- use of external vocabularies such as GeoNames and Schema.org.

## Results

The query results are documented in:

```text
results.md
```

The file contains both the SPARQL queries and representative results obtained from the RDF dataset.

The results include examples such as:

- mountain peaks above 3,000 metres;
- highly populated localities;
- hotels around Nantes;
- RDF triples generated using a `CONSTRUCT` query.

## Vocabularies

The queries primarily use the following vocabularies:

### GeoNames

```text
https://www.geonames.org/ontology#
```

The GeoNames ontology is used to describe geographic features, names, populations, coordinates and feature classifications.

### Schema.org

```text
https://schema.org/
```

Schema.org is used in the altitude query through the `schema:elevation` property.

## Relation to the Project Pipeline

The SPARQL queries are applied after the transformation of the cleaned tabular data into RDF.

The overall workflow is:

```text
GeoNames data
      ↓
Data cleaning
      ↓
Clean CSV dataset
      ↓
TARQL transformation
      ↓
RDF / Turtle dataset
      ↓
SPARQL queries
      ↓
Analysis and results
```

The RDF dataset produced at the previous stages therefore serves as the main input for the queries in this directory.

## Reproducibility

The query files are stored separately from their results so that they can be reused and tested on the generated RDF dataset.

The same approach will be extended in Phase 2 of the project, where SPARQL queries will combine information from multiple linked datasets.

The Phase 2 cross-dataset queries are maintained separately under:

```text
Linking/Queries/Cross_Dataset/
```