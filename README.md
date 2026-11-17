DANA – Semantic Web Project

This project was developed as part of the DANA project at Nantes Université.
The main objective is to transform geographic data about France into a structured and interoperable dataset using Semantic Web technologies.

Project Overview

The project focuses on the processing and semantic representation of geographic data from GeoNames.

The original dataset contains information about geographic features in France. We cleaned and prepared the data before transforming it into semantic data that can be used and linked with other datasets.

The project uses several Semantic Web standards and vocabularies, including:

* RDF – to represent data as triples
* SKOS – to represent concepts and controlled vocabularies
* Schema.org – to describe entities using a widely used vocabulary
* VoID – to describe and provide metadata about RDF datasets
* GeoNames Ontology – to represent geographic entities and their relationships

Data

The main source of geographic information is GeoNames.

The processed dataset contains geographic features located in France. The data was cleaned and unnecessary attributes were removed before being used for the semantic transformation.

The main data file is:

france_all_features.csv

Semantic Representation

The project converts the geographic information into RDF/Turtle data.

The generated semantic data represents geographic entities and their relationships using URIs and established Semantic Web vocabularies.

The project also includes links between the different concepts and entities so that the resulting dataset can be integrated with other Linked Data resources.


Technologies

* Python
* CSV
* RDF
* Turtle (TTL)
* SPARQL
* VoID
* GeoNames

Objective

The main goal of this project is to demonstrate how a traditional geographic dataset can be transformed into Linked Data using Semantic Web principles.

The resulting data can then be queried, connected to other datasets, and reused in a machine-readable and interoperable format.

Authors

This project was developed by students of M1 Smart Computing at Nantes Université as part of the DANA project.
