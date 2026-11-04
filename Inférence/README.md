# Étape 3 : inférence RDFS / OWL sur les données GeoNames

Cette partie montre comment, à partir des triplets déjà présents dans nos données,
un **raisonneur** peut en **déduire de nouveaux** sans qu'ils soient écrits nulle part.
On compare ensuite les résultats de nos requêtes **sans** et **avec** inférence.

---

## 1. Le principe de l'inférence

Une inférence = un triplet **déduit** de triplets existants, grâce à une **règle**.

```
:X      rdf:type         :Singer .       <- donnée
:Singer rdfs:subClassOf  :Person .       <- règle (ontologie)
=> :X rdf:type :Person                   <- triplet déduit, jamais écrit
```

Dans notre projet, c'est la même idée avec un hôtel :

```
:hotelX    gn:featureCode   gn:S.HTL .                               <- donnée (issue de Tarql)
dbo:Hotel  owl:equivalentClass  "tout ce qui a gn:featureCode = S.HTL"  <- règle (mapping)
=> :hotelX rdf:type dbo:Hotel                                        <- triplet déduit
```

---

## 2. Les fichiers de cette partie

| Fichier | Rôle |
|---|---|
| `ontology_v3.3.rdf` | Ontologie GeoNames : le vocabulaire et ses règles internes |
| `mappings_v3.01.rdf` | Mapping d'origine : correspondances entre GeoNames et d'autres vocabulaires |
| `mappings_https.rdf` | Copie du mapping corrigée (`http://` -> `https://`, cf étape 4) |
| `echantillon.rq` / `echantillon.nt` | Requête d'extraction et échantillon de données (zone de Nantes) |
| `config_inf.ttl` | Configuration du Fuseki avec raisonneur |
| `comparaison/c1..c4_*.rq` | Requêtes de comparaison sans / avec inférence |
| `resultats_inference.md` | Requêtes et résultats (sans / avec) |

---

## 3. Les règles (ontologie et mapping)

### Rôle du mapping dans notre cas

Tarql a produit pour chaque lieu un code GeoNames, par exemple :

```
:hotelX  gn:featureCode  gn:S.HTL .
```

`S.HTL` est un code **propre à GeoNames**. Les autres jeux de données (DBpedia, schema.org,
INSEE, données des autres groupes) parlent de `schema:Hotel` ou `dbo:Hotel`.
Sans lien entre les deux, interroger `schema:Hotel` ne renvoie **rien**, alors que nos
données contiennent bien des hôtels.

Le **mapping est un dictionnaire de traduction** entre le vocabulaire GeoNames et les
vocabulaires externes. Pour l'hôtel :

```
dbo:Hotel  =  schema:Hotel  =  lgd:Hotel  =  "tout ce qui a gn:featureCode = S.HTL"
```

Il sert à :
- rendre nos données **compatibles** avec le reste du web de données (principe du Linked Data) ;
- pouvoir **interroger avec le vocabulaire de son choix**, sans connaître les codes GeoNames ;
- fournir au raisonneur les **règles** qu'il applique.

L'**ontologie** joue un rôle voisin, mais à l'intérieur de GeoNames. 
Le mapping fait le pont **vers l'extérieur**.

---

## 4. Étape 4 : préparer règles et données

### 4.1 Corriger le mapping (`http` -> `https`)

Dans `mappings_v3.01.rdf`, les adresses GeoNames sont en `http://www.geonames.org/ontology#...`,
alors que nos données (Tarql) et l'ontologie sont en `https://www.geonames.org/ontology#...`.
Pour le raisonneur ce sont deux adresses différentes : sans correction, il ne reconnaît aucun
`featureCode` et ne déduit rien. On a donc crée une copie corrigée :

```powershell
(Get-Content mappings_v3.01.rdf -Raw -Encoding UTF8) -replace 'http://www.geonames.org/ontology#','https://www.geonames.org/ontology#' | Set-Content mappings_https.rdf -Encoding UTF8
```

### 4.2 Extraire un échantillon

Le raisonneur travaille **entièrement en mémoire** : avec 1,9 million de triplets il saturerait.
On extrait donc les lieux de la zone de Nantes avec une requête `CONSTRUCT` (`echantillon.rq`) :

```sparql
PREFIX gn: <https://www.geonames.org/ontology#>
CONSTRUCT { ?f ?p ?o }
WHERE {
  ?f a gn:GeonamesFeature ; gn:lat ?lat ; gn:long ?long ; ?p ?o .
  FILTER(?lat > 46.9 && ?lat < 47.6 && ?long > -2.2 && ?long < -0.9)
}
```

Elle est exécutée sur le Fuseki principal (port 3030, dataset `Geonames`) et le résultat est
enregistré dans `echantillon.nt` (environ 2 000 lieux).

---

## 5. Étape 5 : Fuseki avec raisonneur

### Ce qu'on a ajouté

Un **second serveur Fuseki** (port 3031), démarré avec un fichier de configuration
`config_inf.ttl`, à côté du premier (port 3030) qui garde la grosse base sans inférence.

```
 ontology_v3.3.rdf   --+
 mappings_https.rdf  --+-->  modelBase  (règles + faits chargés en mémoire)
 echantillon.nt      --+          |
                                  +----------------------->  service "GeonamesBase"
                                  |                           (lecture telle quelle)
                                  v
                        modelInf = modelBase + RAISONNEUR
                                  |
                                  +----------------------->  service "GeonamesInf"
                                                              (lecture + triplets déduits)
```

### Les trois éléments de la configuration

- **`modelBase`** : une boîte en mémoire (`ja:MemoryModel`) dans laquelle Fuseki charge les
  trois fichiers au démarrage. Règles et faits sont mélangés (ce sont tous des triplets).
  Aucune déduction à ce stade.
- **`modelInf`** :
-:modelInf a ja:InfModel ;
    ja:baseModel :modelBase ;
    ja:reasoner [ ja:reasonerURL <...OWLMicroFBRuleReasoner> ] .
  Quand on l'interroge, il lit les règles, les applique aux faits et ajoute les triplets déduits.
- **Deux services** : `GeonamesBase` interroge `modelBase` directement ; `GeonamesInf`
  passe par `modelInf`. Les deux regardent **les mêmes données** : la seule différence entre
  leurs réponses est donc l'inférence.

### Rôle du raisonneur

Le raisonneur est le **programme qui applique les règles**. Le mapping contient la règle
(« `S.HTL` = `schema:Hotel` ») mais c'est le raisonneur qui l'exécute sur chaque lieu et crée
le triplet `:hotelX rdf:type schema:Hotel`. Sans lui (service `GeonamesBase`), le mapping est
chargé mais ignoré.

### Lancement

```powershell
cd <dossier de Fuseki>
.\fuseki-server.bat --port=3031 --config=<chemin>\Partie_3\config_inf.ttl
```

Endpoints obtenus :
- `http://localhost:3031/GeonamesBase/query` (sans inférence)
- `http://localhost:3031/GeonamesInf/query` (avec inférence)

---

## 6. Étape 6 : comparer sans / avec inférence

Quatre requêtes (dossier `comparaison/`) posent des questions sur des **classes que les données
n'écrivent jamais** :

| Requête | Question |
|---|---|
| `c1_feature` | Combien d'entités sont des `gn:Feature` ? (règle RDFS de l'ontologie) |
| `c2_hotels_schema` | Combien d'entités sont des `schema:Hotel` ? (règle OWL du mapping) |
| `c3_classes` | Combien de `schema:City`, `schema:Mountain`, `insee:Commune`, `dbo:Airport` ? |
| `c4_types_hotel` | Quels sont tous les types d'un même hôtel ? |

Un script PowerShell envoie chaque requête aux **deux** services et écrit requête + résultat
sans inférence + résultat avec inférence dans `resultats_inference.md`.

---

## 7. Résultats

| Requête | Sans inférence | Avec inférence |
|---|---|---|
| c1 : `gn:Feature` | 0 | 1955 |
| c2 : `schema:Hotel` | 0 | 173 |
| c3 : `dbo:Airport` | 0 | 5 |
| c3 : `schema:City`, `insee:Commune`, `schema:Mountain` | 0 | 0 |
| c4 : types d'un hôtel | 1 (`gn:GeonamesFeature`) | une vingtaine (`schema:Hotel`, `dbo:Hotel`, `lgd:Hotel`, `gn:Feature`, `owl:Thing`...) |
| Requêtes de l'étape 1 (hôtels, population) | résultats | **identiques** |

---

## 8. Ce que l'on constate

1. **Sans inférence**, les requêtes sur des classes de haut niveau (`gn:Feature`, `schema:Hotel`...)
   ne renvoient rien. **Avec**, elles retrouvent les entités.
2. Les requêtes de l'étape 1, qui n'utilisent que des triplets explicites, donnent les
   **mêmes résultats** : l'inférence enrichit les données, elle ne modifie pas l'existant.
3. **Seuls les mappings en `owl:equivalentClass` produisent des déductions.** Hôtels et
   aéroports sont déclarés ainsi. En revanche `schema:City` et `insee:Commune` sont déclarés
   avec `rdfs:subClassOf` : cela signifie « toute `City` a le code `P.PPL` » mais pas
   « tout lieu de code `P.PPL` est une `City` ». Le raisonneur ne peut donc pas classer nos
   localités (0 résultat). Piste d'amélioration : les passer en équivalence.
4. `schema:Mountain` renvoie 0 car l'échantillon (zone de Nantes) ne contient pas de montagne.
5. Le raisonneur ne déduit que des **classes** : le mapping n'aligne aucune propriété
   (par exemple `gn:name` avec `schema:name`).
6. **Limite** : le raisonneur travaille en mémoire, d'où l'usage d'un échantillon
   plutôt que des 1,9 million de triplets.
