import requests


# ==================================================
# Configuration
# ==================================================

SPARQL_ENDPOINT = "http://localhost:3030/GeoName/sparql"

OUTPUT_FILE = "void_france.ttl"

DATASET_URI = "https://github.com/honorinetessier/projetDANA/tree/main/Dataset"
URI_SPACE = "https://sws.geonames.org/"
SOURCE = "https://www.geonames.org/"


# ==================================================
# Run a SPARQL query
# ==================================================

def run_query(query):
    response = requests.get(
        SPARQL_ENDPOINT,
        params={
            "query": query,
            "format": "json"
        },
        timeout=60
    )

    response.raise_for_status()

    return response.json()["results"]["bindings"]


# ==================================================
# Get a single integer result
# ==================================================

def get_integer(query):
    results = run_query(query)
    return int(results[0]["value"]["value"])


# ==================================================
# Dataset statistics
# ==================================================

triples = get_integer("""
SELECT (COUNT(*) AS ?value)
WHERE {
    ?s ?p ?o
}
""")

entities = get_integer("""
SELECT (COUNT(DISTINCT ?s) AS ?value)
WHERE {
    ?s a ?class
}
""")

classes = get_integer("""
SELECT (COUNT(DISTINCT ?class) AS ?value)
WHERE {
    ?s a ?class
}
""")

properties = get_integer("""
SELECT (COUNT(DISTINCT ?p) AS ?value)
WHERE {
    ?s ?p ?o
}
""")

distinct_subjects = get_integer("""
SELECT (COUNT(DISTINCT ?s) AS ?value)
WHERE {
    ?s ?p ?o
}
""")

distinct_objects = get_integer("""
SELECT (COUNT(DISTINCT ?o) AS ?value)
WHERE {
    ?s ?p ?o
}
""")


# ==================================================
# Class partitions
# ==================================================

class_results = run_query("""
SELECT ?class (COUNT(?s) AS ?entities)
WHERE {
    ?s a ?class
}
GROUP BY ?class
""")


# ==================================================
# Property partitions
# ==================================================

property_results = run_query("""
SELECT ?property (COUNT(*) AS ?triples)
WHERE {
    ?s ?property ?o
}
GROUP BY ?property
""")


# ==================================================
# Generate VoID
# ==================================================

lines = [
    "@prefix void: <http://rdfs.org/ns/void#> .",
    "@prefix dcterms: <http://purl.org/dc/terms/> .",
    "@prefix gn: <https://www.geonames.org/ontology#> .",
    "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .",
    "@prefix schema: <https://schema.org/> .",
    "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .",
    "",
    f"<{DATASET_URI}>",
    "    a void:Dataset ;",
    '    dcterms:title "GeoNames France Dataset" ;',
    "",
    '    dcterms:description "A semantic RDF representation of GeoNames geographical features in France." ;',
    "",
    f"    dcterms:source <{SOURCE}> ;",
    "",
    f'    void:uriSpace "{URI_SPACE}" ;',
    "",
    f"    void:sparqlEndpoint <{SPARQL_ENDPOINT}> ;",
    "",
    f"    void:triples {triples} ;",
    "",
    f"    void:entities {entities} ;",
    "",
    f"    void:classes {classes} ;",
    "",
    f"    void:properties {properties} ;",
    "",
    f"    void:distinctSubjects {distinct_subjects} ;",
    "",
    f"    void:distinctObjects {distinct_objects} ;",
    "",
    "    void:vocabulary",
    "        <https://www.geonames.org/ontology#> ,",
    "        <http://www.w3.org/2004/02/skos/core#> ,",
    "        <https://schema.org/> ;",
    ""
]


# ==================================================
# Add class partitions
# ==================================================

for i, result in enumerate(class_results):

    class_uri = result["class"]["value"]
    count = result["entities"]["value"]

    is_last_class = i == len(class_results) - 1
    is_last_property = len(property_results) == 0

    ending = "." if is_last_class and is_last_property else ";"

    lines.extend([
        "    void:classPartition [",
        f"        void:class <{class_uri}> ;",
        f"        void:entities {count}",
        f"    ] {ending}",
        ""
    ])


# ==================================================
# Add property partitions
# ==================================================

for i, result in enumerate(property_results):

    property_uri = result["property"]["value"]
    count = result["triples"]["value"]

    is_last = i == len(property_results) - 1

    ending = "." if is_last else ";"

    lines.extend([
        "    void:propertyPartition [",
        f"        void:property <{property_uri}> ;",
        f"        void:triples {count}",
        f"    ] {ending}",
        ""
    ])


# ==================================================
# Write the VoID file
# ==================================================

with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    file.write("\n".join(lines))


# ==================================================
# Display results
# ==================================================

print("VoID file generated successfully.")
print()
print(f"Output file: {OUTPUT_FILE}")
print()
print("Dataset statistics:")
print(f"  Triples:           {triples}")
print(f"  Entities:          {entities}")
print(f"  Classes:           {classes}")
print(f"  Properties:        {properties}")
print(f"  Distinct subjects: {distinct_subjects}")
print(f"  Distinct objects:  {distinct_objects}")