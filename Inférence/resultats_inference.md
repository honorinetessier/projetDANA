# Comparaison sans / avec inférence

## echantillon

```sparql
PREFIX gn: <https://www.geonames.org/ontology#>
CONSTRUCT { ?f ?p ?o }
WHERE {
  ?f a gn:GeonamesFeature ; gn:lat ?lat ; gn:long ?long ; ?p ?o .
  FILTER(?lat > 46.9 && ?lat < 47.6 && ?long > -2.2 && ?long < -0.9)
}
```

**SANS inférence**

```
PREFIX adms:    <http://www.w3.org/ns/adms#>
PREFIX cc:      <https://creativecommons.org/ns#>
PREFIX dc:      <http://purl.org/dc/terms/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX foaf:    <http://xmlns.com/foaf/0.1/>
PREFIX gn:      <https://www.geonames.org/ontology#>
PREFIX mrel:    <http://id.loc.gov/vocabulary/relators/>
PREFIX ns:      <http://creativecommons.org/ns#>
PREFIX owl:     <http://www.w3.org/2002/07/owl#>
PREFIX rdf:     <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs:    <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos:    <http://www.w3.org/2004/02/skos/core#>
PREFIX spatial: <http://geovocab.org/spatial#>
PREFIX vann:    <http://purl.org/vocab/vann/>
PREFIX xsd:     <http://www.w3.org/2001/XMLSchema#>

<https://sws.geonames.org/2970293/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2970293;
        gn:lat           47.55459;
        gn:long          -1.70172;
        gn:name          "Vay";
        gn:population    1333 .

<https://sws.geonames.org/12312956/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Joneliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312956;
        gn:lat           47.2551;
        gn:long          -1.54716;
        gn:name          "La Jonelière";
        gn:population    0 .

<https://sws.geonames.org/2979873/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Gereon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979873;
        gn:lat           47.3696;
        gn:long          -1.19854;
        gn:name          "Saint-Géréon";
        gn:population    2727 .

<https://sws.geonames.org/12313143/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Ville Henri";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313143;
        gn:lat           47.16162;
        gn:long          -1.43775;
        gn:name          "La Ville Henri";
        gn:population    0 .

<https://sws.geonames.org/8292948/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Gorges";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292948;
        gn:lat           47.10219;
        gn:long          -1.30489;
        gn:name          "Bureau de Poste de Gorges";
        gn:population    0 .

<https://sws.geonames.org/2974680/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sevre Nantaise";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2974680;
        gn:lat           47.19655;
        gn:long          -1.54679;
        gn:name          "Sèvre Nantaise";
        gn:population    0 .

<https://sws.geonames.org/3007587/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Noe Guy";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007587;
        gn:lat           47.41726;
        gn:long          -1.49441;
        gn:name          "La Noe Guy";
        gn:population    0 .

<https://sws.geonames.org/12313148/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Jarrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313148;
        gn:lat           47.05665;
        gn:long          -1.47702;
        gn:name          "La Jarrie";
        gn:population    0 .

<https://sws.geonames.org/3013457/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Heric";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3013457;
        gn:lat           47.41299;
        gn:long          -1.65234;
        gn:name          "Héric";
        gn:population    4286 .

<https://sws.geonames.org/8292987/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Pornic Principal";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292987;
        gn:lat           47.1154;
        gn:long          -2.09998;
        gn:name          "Bureau de Poste de Pornic Principal";
        gn:population    0 .

<https://sws.geonames.org/6434553/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Treillieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434553;
        gn:lat           47.33083;
        gn:long          -1.62667;
        gn:name          "Treillières";
        gn:population    8978 .

<https://sws.geonames.org/2998826/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Vieux Bourg";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998826;
        gn:lat           47.39393;
        gn:long          -1.46976;
        gn:name          "Le Vieux Bourg";
        gn:population    0 .

<https://sws.geonames.org/12312934/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Basloirs";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312934;
        gn:lat           47.34508;
        gn:long          -1.40647;
        gn:name          "Les Basloirs";
        gn:population    0 .

<https://sws.geonames.org/6516654/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Novotel Nantes Cite Congres";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6516654;
        gn:lat           47.21353;
        gn:long          -1.54402;
        gn:name          "Novotel Nantes Cite Congres";
        gn:population    0 .

<https://sws.geonames.org/8293024/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Savenay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293024;
        gn:lat           47.3593;
        gn:long          -1.94459;
        gn:name          "Bureau de Poste de Savenay";
        gn:population    0 .

<https://sws.geonames.org/6434558/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vertou";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434558;
        gn:lat           47.16806;
        gn:long          -1.47139;
        gn:name          "Vertou";
        gn:population    23581 .

<https://sws.geonames.org/3007208/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Porcherais Casso";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007208;
        gn:lat           47.48869;
        gn:long          -2.07584;
        gn:name          "La Porcherais Casso";
        gn:population    0 .

<https://sws.geonames.org/12310623/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Valleterie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310623;
        gn:lat           46.96034;
        gn:long          -1.12031;
        gn:name          "La Valleterie";
        gn:population    0 .

<https://sws.geonames.org/2969717/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ruisseau Verret";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2969717;
        gn:lat           47.13503;
        gn:long          -1.23758;
        gn:name          "Ruisseau Verret";
        gn:population    0 .

<https://sws.geonames.org/2998816/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Vieux Marillais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998816;
        gn:lat           47.37184;
        gn:long          -1.02334;
        gn:name          "Le Vieux Marillais";
        gn:population    0 .

<https://sws.geonames.org/3008096/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Montagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008096;
        gn:lat           47.18987;
        gn:long          -1.68395;
        gn:name          "La Montagne";
        gn:population    6012 .

<https://sws.geonames.org/12312981/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Colle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312981;
        gn:lat           47.35548;
        gn:long          -1.86319;
        gn:name          "La Colle";
        gn:population    0 .

<https://sws.geonames.org/6435215/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Freigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435215;
        gn:lat           47.54861;
        gn:long          -1.12222;
        gn:name          "Freigné";
        gn:population    1164 .

<https://sws.geonames.org/12313134/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Ville Au Blanc";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313134;
        gn:lat           47.18182;
        gn:long          -1.45415;
        gn:name          "La Ville Au Blanc";
        gn:population    0 .

<https://sws.geonames.org/8292973/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292973;
        gn:lat           47.21764;
        gn:long          -1.55883;
        gn:name          "Bureau de Poste de Nantes Bretagne";
        gn:population    0 .

<https://sws.geonames.org/3008820/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Guyonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008820;
        gn:lat           46.96476;
        gn:long          -1.25059;
        gn:name          "La Guyonnière";
        gn:population    2629 .

<https://sws.geonames.org/2981295/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Brevin-l'Ocean";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981295;
        gn:lat           47.23023;
        gn:long          -2.17202;
        gn:name          "Saint-Brévin-l'Océan";
        gn:population    0 .

<https://sws.geonames.org/3021093/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Donges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3021093;
        gn:lat           47.31824;
        gn:long          -2.07538;
        gn:name          "Donges";
        gn:population    6749 .

<https://sws.geonames.org/8297444/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Gervais";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297444;
        gn:lat           46.9027;
        gn:long          -1.99894;
        gn:name          "Bureau de Poste de Saint Gervais";
        gn:population    0 .

<https://sws.geonames.org/6455301/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beaurepaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6455301;
        gn:lat           46.91056;
        gn:long          -1.08889;
        gn:name          "Beaurepaire";
        gn:population    2368 .

<https://sws.geonames.org/12305884/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gesvrine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305884;
        gn:lat           47.26789;
        gn:long          -1.55093;
        gn:name          "Gesvrine";
        gn:population    0 .

<https://sws.geonames.org/3037797/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ancenis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLA3;
        gn:geonamesID    3037797;
        gn:lat           47.36667;
        gn:long          -1.16667;
        gn:name          "Ancenis";
        gn:population    7840 .

<https://sws.geonames.org/2983237/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Etang du Rocher";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.LK;
        gn:geonamesID    2983237;
        gn:lat           47.54353;
        gn:long          -2.10676;
        gn:name          "Étang du Rocher";
        gn:population    0 .

<https://sws.geonames.org/3233409/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nor Aigu";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233409;
        gn:lat           47.07917;
        gn:long          -2.08472;
        gn:name          "Nor Aigu";
        gn:population    0 .

<https://sws.geonames.org/3233459/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Ternais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233459;
        gn:lat           47.25401;
        gn:long          -1.98722;
        gn:name          "La Ternais";
        gn:population    0 .

<https://sws.geonames.org/2972364/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de Touffou";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2972364;
        gn:lat           47.12709;
        gn:long          -1.48773;
        gn:name          "Forêt de Touffou";
        gn:population    0 .

<https://sws.geonames.org/2989310/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gare de Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    2989310;
        gn:lat           47.21756;
        gn:long          -1.54183;
        gn:name          "Gare de Nantes";
        gn:population    0 .

<https://sws.geonames.org/3021286/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Dodineau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3021286;
        gn:lat           47.37637;
        gn:long          -0.90897;
        gn:name          "Dodineau";
        gn:population    0 .

<https://sws.geonames.org/6434515/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Herblain";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434515;
        gn:lat           47.21139;
        gn:long          -1.65111;
        gn:name          "Saint-Herblain";
        gn:population    46603 .

<https://sws.geonames.org/3015241/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grande Brosse";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3015241;
        gn:lat           46.99154;
        gn:long          -1.41691;
        gn:name          "Grande Brosse";
        gn:population    0 .

<https://sws.geonames.org/3015009/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grand Reservoir de Vioreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.RSV;
        gn:geonamesID    3015009;
        gn:lat           47.52357;
        gn:long          -1.42309;
        gn:name          "Grand Réservoir de Vioreau";
        gn:population    0 .

<https://sws.geonames.org/6614417/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Cellier";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614417;
        gn:lat           47.31944;
        gn:long          -1.34639;
        gn:name          "Le Cellier";
        gn:population    3698 .

<https://sws.geonames.org/2971939/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tregouet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2971939;
        gn:lat           47.57943;
        gn:long          -1.89705;
        gn:name          "Trégouet";
        gn:population    0 .

<https://sws.geonames.org/2989696/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ognon";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2989696;
        gn:lat           47.10295;
        gn:long          -1.648;
        gn:name          "Ognon";
        gn:population    0 .

<https://sws.geonames.org/3008534/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Landelle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008534;
        gn:lat           47.23655;
        gn:long          -1.36631;
        gn:name          "La Landelle";
        gn:population    0 .

<https://sws.geonames.org/7535062/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Golf Savenay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RECG;
        gn:geonamesID    7535062;
        gn:lat           47.3607;
        gn:long          -1.9143;
        gn:name          "Golf Savenay";
        gn:population    0 .

<https://sws.geonames.org/3008985/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grande Maison";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008985;
        gn:lat           47.43595;
        gn:long          -1.60833;
        gn:name          "La Grande Maison";
        gn:population    0 .

<https://sws.geonames.org/9177212/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inter-Hotel La Verriaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177212;
        gn:lat           46.94564;
        gn:long          -0.98185;
        gn:name          "Inter-Hotel La Verriaire";
        gn:population    0 .

<https://sws.geonames.org/3023315/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Couffe";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3023315;
        gn:lat           47.39191;
        gn:long          -1.29151;
        gn:name          "Couffé";
        gn:population    1936 .

<https://sws.geonames.org/12312954/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bois Raguenet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312954;
        gn:lat           47.26963;
        gn:long          -1.59596;
        gn:name          "Le Bois Raguenet";
        gn:population    0 .

<https://sws.geonames.org/6615238/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vritz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6615238;
        gn:lat           47.58167;
        gn:long          -1.06972;
        gn:name          "Vritz";
        gn:population    732 .

<https://sws.geonames.org/3008884/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grigonnais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008884;
        gn:lat           47.52704;
        gn:long          -1.66749;
        gn:name          "La Grigonnais";
        gn:population    1314 .

<https://sws.geonames.org/2990969/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLA;
        gn:geonamesID    2990969;
        gn:lat           47.21725;
        gn:long          -1.55336;
        gn:name          "Nantes";
        gn:population    325070 .

<https://sws.geonames.org/3007232/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Poitriere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007232;
        gn:lat           47.39777;
        gn:long          -0.98388;
        gn:name          "La Poitrière";
        gn:population    0 .

<https://sws.geonames.org/2985226/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Etang de la Provostiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.LK;
        gn:geonamesID    2985226;
        gn:lat           47.52691;
        gn:long          -1.33683;
        gn:name          "Étang de la Provostière";
        gn:population    0 .

<https://sws.geonames.org/6456915/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chevroliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456915;
        gn:lat           47.09083;
        gn:long          -1.61194;
        gn:name          "La Chevrolière";
        gn:population    5490 .

<https://sws.geonames.org/12312899/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Sinandiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312899;
        gn:lat           47.40143;
        gn:long          -1.20066;
        gn:name          "La Sinandière";
        gn:population    0 .

<https://sws.geonames.org/3005338/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Ebaupin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005338;
        gn:lat           47.43333;
        gn:long          -1.98333;
        gn:name          "L'Ebaupin";
        gn:population    0 .

<https://sws.geonames.org/2978529/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Mars-de-Coutais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978529;
        gn:lat           47.11266;
        gn:long          -1.73552;
        gn:name          "Saint-Mars-de-Coutais";
        gn:population    2360 .

<https://sws.geonames.org/8287011/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Savenay Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287011;
        gn:lat           47.35889;
        gn:long          -1.95238;
        gn:name          "Savenay Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8293027/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Les Sorinieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293027;
        gn:lat           47.14853;
        gn:long          -1.5331;
        gn:name          "Bureau de Poste de Les Sorinieres";
        gn:population    0 .

<https://sws.geonames.org/12310626/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Poteries";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310626;
        gn:lat           46.93298;
        gn:long          -1.88792;
        gn:name          "Les Poteries";
        gn:population    0 .

<https://sws.geonames.org/12313096/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Trinite";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313096;
        gn:lat           47.08869;
        gn:long          -1.27755;
        gn:name          "La Trinité";
        gn:population    0 .

<https://sws.geonames.org/3233416/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe aux Chevaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    3233416;
        gn:lat           47.1097;
        gn:long          -2.12132;
        gn:name          "Pointe aux Chevaux";
        gn:population    0 .

<https://sws.geonames.org/3233619/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Roches Alluard";
        <https://schema.org/elevation>  8.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:T;
        gn:featureCode                  gn:T.RKS;
        gn:geonamesID                   3233619;
        gn:lat                          47.285;
        gn:long                         -2.08139;
        gn:name                         "Roches Alluard";
        gn:population                   0 .

<https://sws.geonames.org/6456089/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Salle-et-Chapelle-Aubry";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456089;
        gn:lat           47.2554;
        gn:long          -0.9847;
        gn:name          "La Salle-et-Chapelle-Aubry";
        gn:population    1251 .

<https://sws.geonames.org/3007163/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Poupiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007163;
        gn:lat           47.40202;
        gn:long          -1.49703;
        gn:name          "La Poupinière";
        gn:population    0 .

<https://sws.geonames.org/3008470/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Limouziniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008470;
        gn:lat           46.99346;
        gn:long          -1.59726;
        gn:name          "La Limouzinière";
        gn:population    1518 .

<https://sws.geonames.org/3015078/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lac de Grand-Lieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.LK;
        gn:geonamesID    3015078;
        gn:lat           47.09537;
        gn:long          -1.67209;
        gn:name          "Lac de Grand-Lieu";
        gn:population    0 .

<https://sws.geonames.org/12746923/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ecole des Beaux-Arts de Nantes Saint-Nazaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.UNIV;
        gn:geonamesID    12746923;
        gn:lat           47.20654;
        gn:long          -1.55998;
        gn:name          "École des Beaux-Arts de Nantes Saint-Nazaire";
        gn:population    0 .

<https://sws.geonames.org/12312946/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Hulonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312946;
        gn:lat           47.27012;
        gn:long          -1.44546;
        gn:name          "La Hulonnière";
        gn:population    0 .

<https://sws.geonames.org/3012662/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Issoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3012662;
        gn:lat           47.00289;
        gn:long          -1.54184;
        gn:name          "Issoire";
        gn:population    0 .

<https://sws.geonames.org/3007262/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Plaine-sur-Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007262;
        gn:lat           47.13718;
        gn:long          -2.19172;
        gn:name          "La Plaine-sur-Mer";
        gn:population    2711 .

<https://sws.geonames.org/9539818/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Du Beryl Saint Brevin L'Ocean";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539818;
        gn:lat           47.22922;
        gn:long          -2.17609;
        gn:name          "Du Beryl Saint Brevin L'Ocean";
        gn:population    0 .

<https://sws.geonames.org/12313108/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Caillaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313108;
        gn:lat           47.16911;
        gn:long          -1.41456;
        gn:name          "La Caillaudière";
        gn:population    0 .

<https://sws.geonames.org/3006999/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Remaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006999;
        gn:lat           47.23774;
        gn:long          -1.24367;
        gn:name          "La Remaudière";
        gn:population    1068 .

<https://sws.geonames.org/3233386/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Epronai";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233386;
        gn:lat           47.00316;
        gn:long          -2.10338;
        gn:name          "L'Epronai";
        gn:population    0 .

<https://sws.geonames.org/3011090/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bernerie-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011090;
        gn:lat           47.08135;
        gn:long          -2.0372;
        gn:name          "La Bernerie-en-Retz";
        gn:population    2296 .

<https://sws.geonames.org/6434545/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Severac";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434545;
        gn:lat           47.55;
        gn:long          -2.07667;
        gn:name          "Sévérac";
        gn:population    1628 .

<https://sws.geonames.org/3005281/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bignon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005281;
        gn:lat           47.47393;
        gn:long          -1.96405;
        gn:name          "Le Bignon";
        gn:population    0 .

<https://sws.geonames.org/3030970/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bourgneuf-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3030970;
        gn:lat           47.04294;
        gn:long          -1.95292;
        gn:name          "Bourgneuf-en-Retz";
        gn:population    2591 .

<https://sws.geonames.org/3009626/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Dourie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009626;
        gn:lat           47.10872;
        gn:long          -1.24429;
        gn:name          "La Dourie";
        gn:population    0 .

<https://sws.geonames.org/6434560/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vigneux-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434560;
        gn:lat           47.32611;
        gn:long          -1.73833;
        gn:name          "Vigneux-de-Bretagne";
        gn:population    5923 .

<https://sws.geonames.org/3005640/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Verrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005640;
        gn:lat           46.96076;
        gn:long          -0.99522;
        gn:name          "La Verrie";
        gn:population    3613 .

<https://sws.geonames.org/6614870/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Landes-Genusson";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614870;
        gn:lat           46.96556;
        gn:long          -1.11833;
        gn:name          "Les Landes-Genusson";
        gn:population    2344 .

<https://sws.geonames.org/2981033/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Colomban";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981033;
        gn:lat           47.0093;
        gn:long          -1.58377;
        gn:name          "Saint-Colomban";
        gn:population    0 .

<https://sws.geonames.org/12312971/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Siniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312971;
        gn:lat           47.22423;
        gn:long          -1.67637;
        gn:name          "La Sinière";
        gn:population    0 .

<https://sws.geonames.org/3010632/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Calvernais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010632;
        gn:lat           47.57634;
        gn:long          -1.71196;
        gn:name          "La Calvernais";
        gn:population    0 .

<https://sws.geonames.org/10297826/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inn Nantes Centre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297826;
        gn:lat           47.20701;
        gn:long          -1.54845;
        gn:name          "Inn Nantes Centre";
        gn:population    0 .

<https://sws.geonames.org/3008829/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Guiltiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008829;
        gn:lat           47.13286;
        gn:long          -1.22657;
        gn:name          "La Guiltière";
        gn:population    0 .

<https://sws.geonames.org/3006168/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Tremblais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006168;
        gn:lat           47.35381;
        gn:long          -2.01059;
        gn:name          "La Tremblais";
        gn:population    0 .

<https://sws.geonames.org/6449435/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chaudron-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6449435;
        gn:lat           47.2875;
        gn:long          -0.98472;
        gn:name          "Chaudron-en-Mauges";
        gn:population    1443 .

<https://sws.geonames.org/6619291/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fresne-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    6619291;
        gn:lat           47.40091;
        gn:long          -0.92834;
        gn:name          "Le Fresne-sur-Loire";
        gn:population    700 .

<https://sws.geonames.org/12310631/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Puyravault";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310631;
        gn:lat           46.95139;
        gn:long          -1.18556;
        gn:name          "Puyravault";
        gn:population    0 .

<https://sws.geonames.org/6615510/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Geneston";
        <https://schema.org/elevation>  14.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:P;
        gn:featureCode                  gn:P.PPL;
        gn:geonamesID                   6615510;
        gn:lat                          47.05639;
        gn:long                         -1.51139;
        gn:name                         "Geneston";
        gn:population                   2217 .

<https://sws.geonames.org/3010842/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bouvardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010842;
        gn:lat           47.32119;
        gn:long          -1.6944;
        gn:name          "La Bouvardière";
        gn:population    0 .

<https://sws.geonames.org/8286985/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Moutiers en Retz Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286985;
        gn:lat           47.06194;
        gn:long          -2.00167;
        gn:name          "Les Moutiers en Retz Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12313007/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Thenot";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313007;
        gn:lat           47.56211;
        gn:long          -2.00318;
        gn:name          "Le Thénot";
        gn:population    0 .

<https://sws.geonames.org/3010990/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boissiere-de-Montaigu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010990;
        gn:lat           46.95078;
        gn:long          -1.19177;
        gn:name          "La Boissière-de-Montaigu";
        gn:population    1683 .

<https://sws.geonames.org/3020847/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Drain";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3020847;
        gn:lat           47.33655;
        gn:long          -1.20773;
        gn:name          "Drain";
        gn:population    1757 .

<https://sws.geonames.org/7116362/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Polytech'Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.SCH;
        gn:geonamesID    7116362;
        gn:lat           47.28265;
        gn:long          -1.51663;
        gn:name          "Polytech'Nantes";
        gn:population    0 .

<https://sws.geonames.org/2987041/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bras de Pirmil";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STMA;
        gn:geonamesID    2987041;
        gn:lat           47.1981;
        gn:long          -1.57297;
        gn:name          "Bras de Pirmil";
        gn:population    0 .

<https://sws.geonames.org/12312973/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Troche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312973;
        gn:lat           47.39032;
        gn:long          -1.73622;
        gn:name          "La Troche";
        gn:population    0 .

<https://sws.geonames.org/3016167/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Geste";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3016167;
        gn:lat           47.18179;
        gn:long          -1.10917;
        gn:name          "Gesté";
        gn:population    2471 .

<https://sws.geonames.org/8293075/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Beausejour";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293075;
        gn:lat           47.23506;
        gn:long          -1.58287;
        gn:name          "Bureau de Poste de Nantes Beausejour";
        gn:population    0 .

<https://sws.geonames.org/13592130/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "PARC Artotheque de Nantes (Fermee)";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.MUS;
        gn:geonamesID    13592130;
        gn:lat           47.21439;
        gn:long          -1.56269;
        gn:name          "PARC Artothèque de Nantes (Fermée)";
        gn:population    0 .

<https://sws.geonames.org/11073027/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe de la Casie";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    11073027;
        gn:lat           46.92626;
        gn:long          -2.14723;
        gn:name          "Pointe de la Casie";
        gn:population    0 .

<https://sws.geonames.org/12312939/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Barthelemy";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312939;
        gn:lat           47.26032;
        gn:long          -1.36058;
        gn:name          "Saint-Barthélemy";
        gn:population    0 .

<https://sws.geonames.org/12313165/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Guenegaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313165;
        gn:lat           47.08949;
        gn:long          -1.52429;
        gn:name          "Guénégaud";
        gn:population    0 .

<https://sws.geonames.org/6616810/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Indre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616810;
        gn:lat           47.1987;
        gn:long          -1.6705;
        gn:name          "Indre";
        gn:population    3915 .

<https://sws.geonames.org/8292921/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Carquefou";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292921;
        gn:lat           47.29698;
        gn:long          -1.49114;
        gn:name          "Bureau de Poste de Carquefou";
        gn:population    0 .

<https://sws.geonames.org/3233461/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cheminandais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233461;
        gn:lat           47.25833;
        gn:long          -1.92849;
        gn:name          "La Cheminandais";
        gn:population    0 .

<https://sws.geonames.org/3008817/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008817;
        gn:lat           47.28976;
        gn:long          -1.54524;
        gn:name          "La Haie";
        gn:population    0 .

<https://sws.geonames.org/3004184/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fouy";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004184;
        gn:lat           47.58025;
        gn:long          -1.40575;
        gn:name          "Le Fouy";
        gn:population    0 .

<https://sws.geonames.org/3005727/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lavau-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005727;
        gn:lat           47.30706;
        gn:long          -1.9672;
        gn:name          "Lavau-sur-Loire";
        gn:population    670 .

<https://sws.geonames.org/10281143/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appart City Nantes Le Viarme";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10281143;
        gn:lat           47.21944;
        gn:long          -1.56158;
        gn:name          "Appart City Nantes Le Viarme";
        gn:population    0 .

<https://sws.geonames.org/8293371/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Ingrandes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293371;
        gn:lat           47.40468;
        gn:long          -0.92123;
        gn:name          "Bureau de Poste de Ingrandes";
        gn:population    0 .

<https://sws.geonames.org/9224798/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Graslin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9224798;
        gn:lat           47.21227;
        gn:long          -1.56176;
        gn:name          "Hotel Graslin";
        gn:population    0 .

<https://sws.geonames.org/6449083/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cheix-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449083;
        gn:lat           47.18167;
        gn:long          -1.81556;
        gn:name          "Cheix-en-Retz";
        gn:population    1047 .

<https://sws.geonames.org/9178623/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quintessia & Spa (Ex Domaine D'Orvault)";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178623;
        gn:lat           47.25992;
        gn:long          -1.58913;
        gn:name          "Quintessia & Spa (Ex Domaine D'Orvault)";
        gn:population    0 .

<https://sws.geonames.org/12312961/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grehandiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312961;
        gn:lat           47.32658;
        gn:long          -1.64284;
        gn:name          "La Gréhandière";
        gn:population    0 .

<https://sws.geonames.org/8287001/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montoir-de-Bretagne Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287001;
        gn:lat           47.32065;
        gn:long          -2.16254;
        gn:name          "Montoir-de-Bretagne Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8293063/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Vieux Doulon";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293063;
        gn:lat           47.23611;
        gn:long          -1.50492;
        gn:name          "Bureau de Poste de Nantes Vieux Doulon";
        gn:population    0 .

<https://sws.geonames.org/12313156/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Houssais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313156;
        gn:lat           47.17349;
        gn:long          -1.55562;
        gn:name          "La Houssais";
        gn:population    0 .

<https://sws.geonames.org/3007577/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Noue";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.FRM;
        gn:geonamesID    3007577;
        gn:lat           47.10953;
        gn:long          -1.19381;
        gn:name          "La Noüe";
        gn:population    0 .

<https://sws.geonames.org/9177258/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inter-Hotel Le Surcouf";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177258;
        gn:lat           47.2173;
        gn:long          -1.54652;
        gn:name          "Inter-Hotel Le Surcouf";
        gn:population    0 .

<https://sws.geonames.org/3008803/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haie-Trois-Sous";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008803;
        gn:lat           47.12286;
        gn:long          -1.40381;
        gn:name          "La Haie-Trois-Sous";
        gn:population    0 .

<https://sws.geonames.org/3233389/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Banc de Bourgneuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.SHOL;
        gn:geonamesID    3233389;
        gn:lat           47.025;
        gn:long          -2.10417;
        gn:name          "Banc de Bourgneuf";
        gn:population    0 .

<https://sws.geonames.org/9173745/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes Reze";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173745;
        gn:lat           47.19391;
        gn:long          -1.57447;
        gn:name          "Campanile Nantes Reze";
        gn:population    0 .

<https://sws.geonames.org/3011093/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bernardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011093;
        gn:lat           47.04937;
        gn:long          -1.26648;
        gn:name          "La Bernardière";
        gn:population    1252 .

<https://sws.geonames.org/12313076/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Recouvrance";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313076;
        gn:lat           47.07574;
        gn:long          -1.24147;
        gn:name          "Recouvrance";
        gn:population    0 .

<https://sws.geonames.org/3233498/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Quatretais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233498;
        gn:lat           47.22449;
        gn:long          -2.14849;
        gn:name          "Le Quatretais";
        gn:population    0 .

<https://sws.geonames.org/2998831/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Vieille Ville";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998831;
        gn:lat           47.59142;
        gn:long          -2.00181;
        gn:name          "Le Vieille Ville";
        gn:population    0 .

<https://sws.geonames.org/3024683/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Clegreue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3024683;
        gn:lat           47.556;
        gn:long          -1.72219;
        gn:name          "Clegreue";
        gn:population    0 .

<https://sws.geonames.org/6491386/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes St Herblain";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6491386;
        gn:lat           47.2274;
        gn:long          -1.6349;
        gn:name          "Campanile Nantes St Herblain";
        gn:population    0 .

<https://sws.geonames.org/3000745/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Grisons";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000745;
        gn:lat           47.45715;
        gn:long          -1.69321;
        gn:name          "Les Grisons";
        gn:population    0 .

<https://sws.geonames.org/12313091/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Morandiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313091;
        gn:lat           47.13049;
        gn:long          -1.31121;
        gn:name          "La Morandière";
        gn:population    0 .

<https://sws.geonames.org/6614116/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois-de-Cene";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614116;
        gn:lat           46.93806;
        gn:long          -1.88528;
        gn:name          "Bois-de-Céné";
        gn:population    1991 .

<https://sws.geonames.org/8297456/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Tiffauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297456;
        gn:lat           47.01119;
        gn:long          -1.11561;
        gn:name          "Bureau de Poste de Tiffauges";
        gn:population    0 .

<https://sws.geonames.org/3032380/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Blanche-Lande";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3032380;
        gn:lat           47.35369;
        gn:long          -1.2569;
        gn:name          "Blanche-Lande";
        gn:population    0 .

<https://sws.geonames.org/3032462/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Blain";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3032462;
        gn:lat           47.47563;
        gn:long          -1.76449;
        gn:name          "Blain";
        gn:population    8274 .

<https://sws.geonames.org/2979707/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Gervais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979707;
        gn:lat           46.90258;
        gn:long          -1.99907;
        gn:name          "Saint-Gervais";
        gn:population    1763 .

<https://sws.geonames.org/8286988/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Machecoul Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286988;
        gn:lat           46.99032;
        gn:long          -1.82247;
        gn:name          "Machecoul Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12313081/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Riniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313081;
        gn:lat           47.20935;
        gn:long          -1.27489;
        gn:name          "La Rinière";
        gn:population    0 .

<https://sws.geonames.org/9178229/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Park And Suites Confort Nantes Saint Herblain";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178229;
        gn:lat           47.22711;
        gn:long          -1.65028;
        gn:name          "Park And Suites Confort Nantes Saint Herblain";
        gn:population    0 .

<https://sws.geonames.org/2986956/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plaine de la Poupiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.LK;
        gn:geonamesID    2986956;
        gn:lat           47.39179;
        gn:long          -1.49476;
        gn:name          "Plaine de la Poupinière";
        gn:population    0 .

<https://sws.geonames.org/12312976/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Babiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312976;
        gn:lat           47.2939;
        gn:long          -1.72383;
        gn:name          "La Babinière";
        gn:population    0 .

<https://sws.geonames.org/3010396/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Basse-Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010396;
        gn:lat           47.27203;
        gn:long          -1.3384;
        gn:name          "La Chapelle-Basse-Mer";
        gn:population    4595 .

<https://sws.geonames.org/12310638/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Michellerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310638;
        gn:lat           46.92638;
        gn:long          -1.83891;
        gn:name          "La Michellerie";
        gn:population    0 .

<https://sws.geonames.org/2999766/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Rivieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999766;
        gn:lat           47.11667;
        gn:long          -1.13333;
        gn:name          "Les Rivières";
        gn:population    0 .

<https://sws.geonames.org/6613997/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Brevin-les-Pins";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6613997;
        gn:lat           47.24639;
        gn:long          -2.16694;
        gn:name          "Saint-Brevin-les-Pins";
        gn:population    13778 .

<https://sws.geonames.org/8293078/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Eraudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293078;
        gn:lat           47.24175;
        gn:long          -1.53247;
        gn:name          "Bureau de Poste de Nantes Eraudiere";
        gn:population    0 .

<https://sws.geonames.org/2971815/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trentemoult";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2971815;
        gn:lat           47.1945;
        gn:long          -1.57722;
        gn:name          "Trentemoult";
        gn:population    0 .

<https://sws.geonames.org/6434505/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rouans";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434505;
        gn:lat           47.18528;
        gn:long          -1.85972;
        gn:name          "Rouans";
        gn:population    2913 .

<https://sws.geonames.org/3006029/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Launay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006029;
        gn:lat           47.33226;
        gn:long          -1.37857;
        gn:name          "Launay";
        gn:population    0 .

<https://sws.geonames.org/12310628/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Port du Bec";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310628;
        gn:lat           46.93698;
        gn:long          -2.07384;
        gn:name          "Port du Bec";
        gn:population    0 .

<https://sws.geonames.org/3003195/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Moulin-Eve";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003195;
        gn:lat           47.53952;
        gn:long          -1.61705;
        gn:name          "Le Moulin-Eve";
        gn:population    0 .

<https://sws.geonames.org/3028428/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Casson";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3028428;
        gn:lat           47.38647;
        gn:long          -1.55809;
        gn:name          "Casson";
        gn:population    1432 .

<https://sws.geonames.org/9173374/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brit Hotel Azur";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173374;
        gn:lat           47.09382;
        gn:long          -1.00327;
        gn:name          "Brit Hotel Azur";
        gn:population    0 .

<https://sws.geonames.org/3001308/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Couets";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3001308;
        gn:lat           47.18512;
        gn:long          -1.59119;
        gn:name          "Les Couêts";
        gn:population    0 .

<https://sws.geonames.org/6449118/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Maumusson";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6449118;
        gn:lat           47.48278;
        gn:long          -1.10556;
        gn:name          "Maumusson";
        gn:population    989 .

<https://sws.geonames.org/2981095/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Clair";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981095;
        gn:lat           47.52705;
        gn:long          -1.95152;
        gn:name          "Saint-Clair";
        gn:population    0 .

<https://sws.geonames.org/7778638/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Basse Lande transmitter";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RUIN;
        gn:geonamesID    7778638;
        gn:lat           47.17075;
        gn:long          -1.69501;
        gn:name          "Basse Lande transmitter";
        gn:population    0 .

<https://sws.geonames.org/6434485/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Notre-Dame-des-Landes";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434485;
        gn:lat           47.38083;
        gn:long          -1.71;
        gn:name          "Notre-Dame-des-Landes";
        gn:population    2144 .

<https://sws.geonames.org/8292940/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Donges";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292940;
        gn:lat           47.3148;
        gn:long          -2.06444;
        gn:name          "Bureau de Poste de Donges";
        gn:population    0 .

<https://sws.geonames.org/12313101/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Brillaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313101;
        gn:lat           47.17652;
        gn:long          -1.41084;
        gn:name          "La Brillaudière";
        gn:population    0 .

<https://sws.geonames.org/3009676/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Davelais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009676;
        gn:lat           47.3819;
        gn:long          -2.07;
        gn:name          "La Davelais";
        gn:population    0 .

<https://sws.geonames.org/10297833/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel La Perouse";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297833;
        gn:lat           47.21668;
        gn:long          -1.55648;
        gn:name          "Hôtel La Pérouse";
        gn:population    0 .

<https://sws.geonames.org/6473718/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grand Hotel Mercure Nantes Central";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6473718;
        gn:lat           47.2139;
        gn:long          -1.5568;
        gn:name          "Grand Hotel Mercure Nantes Central";
        gn:population    0 .

<https://sws.geonames.org/8292993/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Rouans";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292993;
        gn:lat           47.18561;
        gn:long          -1.8585;
        gn:name          "Bureau de Poste de Rouans";
        gn:population    0 .

<https://sws.geonames.org/3035266/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Balasson";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3035266;
        gn:lat           47.4425;
        gn:long          -2.03857;
        gn:name          "Balasson";
        gn:population    0 .

<https://sws.geonames.org/6434511/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Etienne-de-Montluc";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434511;
        gn:lat           47.27639;
        gn:long          -1.78028;
        gn:name          "Saint-Étienne-de-Montluc";
        gn:population    6952 .

<https://sws.geonames.org/12312968/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bastille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312968;
        gn:lat           47.25832;
        gn:long          -1.67917;
        gn:name          "La Bastille";
        gn:population    0 .

<https://sws.geonames.org/12313151/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Barbin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313151;
        gn:lat           46.97146;
        gn:long          -1.42457;
        gn:name          "Le Barbin";
        gn:population    0 .

<https://sws.geonames.org/12313212/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Maisons Neuves";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313212;
        gn:lat           47.06389;
        gn:long          -1.99098;
        gn:name          "Les Maisons Neuves";
        gn:population    0 .

<https://sws.geonames.org/8293018/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Pere En Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293018;
        gn:lat           47.20749;
        gn:long          -2.04439;
        gn:name          "Bureau de Poste de Saint Pere En Retz";
        gn:population    0 .

<https://sws.geonames.org/3006325/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Tanniais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006325;
        gn:lat           47.27226;
        gn:long          -1.97523;
        gn:name          "La Tanniais";
        gn:population    0 .

<https://sws.geonames.org/6501003/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel De France Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6501003;
        gn:lat           47.2133;
        gn:long          -1.5615;
        gn:name          "Hotel De France Nantes";
        gn:population    0 .

<https://sws.geonames.org/3233426/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rocher de la Cormorane";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233426;
        gn:lat           47.16366;
        gn:long          -2.1955;
        gn:name          "Rocher de la Cormorane";
        gn:population    0 .

<https://sws.geonames.org/13192642/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Eglise Saint-Nicolas";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.CH;
        gn:geonamesID    13192642;
        gn:lat           46.94442;
        gn:long          -2.18132;
        gn:name          "Église Saint-Nicolas";
        gn:population    0 .

<https://sws.geonames.org/6437373/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Dolay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6437373;
        gn:lat           47.54472;
        gn:long          -2.15444;
        gn:name          "Saint-Dolay";
        gn:population    2465 .

<https://sws.geonames.org/3033243/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Berreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3033243;
        gn:lat           47.46881;
        gn:long          -2.11167;
        gn:name          "Berreau";
        gn:population    0 .

<https://sws.geonames.org/3010862/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bourgonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSEC;
        gn:geonamesID    3010862;
        gn:lat           47.34796;
        gn:long          -1.09304;
        gn:name          "La Bourgonnière";
        gn:population    0 .

<https://sws.geonames.org/6458670/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boissiere-sur-Evre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6458670;
        gn:lat           47.30167;
        gn:long          -1.08;
        gn:name          "La Boissière-sur-Èvre";
        gn:population    413 .

<https://sws.geonames.org/3026592/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois des Charmeraies";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    3026592;
        gn:lat           47.49572;
        gn:long          -0.98405;
        gn:name          "Bois des Charmeraies";
        gn:population    0 .

<https://sws.geonames.org/3026302/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arrondissement de Chateaubriant";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM3H;
        gn:geonamesID    3026302;
        gn:lat           47.58333;
        gn:long          -1.66667;
        gn:name          "Arrondissement de Châteaubriant";
        gn:population    124748 .

<https://sws.geonames.org/3015205/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grande Maine";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3015205;
        gn:lat           46.95117;
        gn:long          -1.3029;
        gn:name          "Grande Maine";
        gn:population    0 .

<https://sws.geonames.org/3008730/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Hinchere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008730;
        gn:lat           47.00317;
        gn:long          -1.26571;
        gn:name          "La Hinchère";
        gn:population    0 .

<https://sws.geonames.org/6299461/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Nantes Atlantique Airport";
        <https://schema.org/elevation>  27.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:S;
        gn:featureCode                  gn:S.AIRP;
        gn:geonamesID                   6299461;
        gn:lat                          47.15319;
        gn:long                         -1.61072;
        gn:name                         "Nantes Atlantique Airport";
        gn:population                   0 .

<https://sws.geonames.org/12313116/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Metairie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313116;
        gn:lat           47.1433;
        gn:long          -1.40422;
        gn:name          "La Métairie";
        gn:population    0 .

<https://sws.geonames.org/6616807/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau-Thebaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616807;
        gn:lat           47.1249;
        gn:long          -1.4185;
        gn:name          "Château-Thébaud";
        gn:population    3007 .

<https://sws.geonames.org/3016473/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret du Gavre";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    3016473;
        gn:lat           47.53035;
        gn:long          -1.79453;
        gn:name          "Forêt du Gavre";
        gn:population    0 .

<https://sws.geonames.org/3007961/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mulotais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007961;
        gn:lat           47.25868;
        gn:long          -2.09964;
        gn:name          "La Mulotais";
        gn:population    0 .

<https://sws.geonames.org/2978670/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Lumine-de-Clisson";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978670;
        gn:lat           47.08284;
        gn:long          -1.33716;
        gn:name          "Saint-Lumine-de-Clisson";
        gn:population    1451 .

<https://sws.geonames.org/3233412/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grand Ve";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233412;
        gn:lat           47.08417;
        gn:long          -2.08667;
        gn:name          "Grand Vé";
        gn:population    0 .

<https://sws.geonames.org/6434530/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vallons-de-l'Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434530;
        gn:lat           47.52528;
        gn:long          -1.18472;
        gn:name          "Vallons-de-l'Erdre";
        gn:population    6589 .

<https://sws.geonames.org/3003392/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Mesnil-en-Vallee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003392;
        gn:lat           47.36551;
        gn:long          -0.93485;
        gn:name          "Le Mesnil-en-Vallée";
        gn:population    1364 .

<https://sws.geonames.org/2986195/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Esnaut";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2986195;
        gn:lat           47.41667;
        gn:long          -1.3;
        gn:name          "Pont Esnaut";
        gn:population    0 .

<https://sws.geonames.org/3030603/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brains";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3030603;
        gn:lat           47.16915;
        gn:long          -1.72283;
        gn:name          "Brains";
        gn:population    2325 .

<https://sws.geonames.org/7116364/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ecole de design";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.SCH;
        gn:geonamesID    7116364;
        gn:lat           47.28325;
        gn:long          -1.51762;
        gn:name          "Ecole de design";
        gn:population    0 .

<https://sws.geonames.org/3233649/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Foucauderie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233649;
        gn:lat           47.27643;
        gn:long          -2.00167;
        gn:name          "La Foucauderie";
        gn:population    0 .

<https://sws.geonames.org/8293967/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Dolay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293967;
        gn:lat           47.545;
        gn:long          -2.15955;
        gn:name          "Bureau de Poste de Saint Dolay";
        gn:population    0 .

<https://sws.geonames.org/6449091/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Donges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449091;
        gn:lat           47.3229;
        gn:long          -2.0755;
        gn:name          "Donges";
        gn:population    7852 .

<https://sws.geonames.org/10297841/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Des Trois Marchands";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297841;
        gn:lat           47.21839;
        gn:long          -1.55605;
        gn:name          "Des Trois Marchands";
        gn:population    0 .

<https://sws.geonames.org/2977603/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Philbert-de-Bouaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977603;
        gn:lat           46.98748;
        gn:long          -1.51961;
        gn:name          "Saint-Philbert-de-Bouaine";
        gn:population    2413 .

<https://sws.geonames.org/2984038/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Remouille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2984038;
        gn:lat           47.05589;
        gn:long          -1.37729;
        gn:name          "Remouillé";
        gn:population    1558 .

<https://sws.geonames.org/9177031/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ibis Styles Nantes Centre Place Royale";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177031;
        gn:lat           47.21423;
        gn:long          -1.55742;
        gn:name          "Ibis Styles Nantes Centre Place Royale";
        gn:population    0 .

<https://sws.geonames.org/12305893/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pe de Vignard";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305893;
        gn:lat           47.14097;
        gn:long          -1.34443;
        gn:name          "Pé de Vignard";
        gn:population    0 .

<https://sws.geonames.org/6435301/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sevremoine";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6435301;
        gn:lat           47.12389;
        gn:long          -0.99167;
        gn:name          "Sèvremoine";
        gn:population    25681 .

<https://sws.geonames.org/12312900/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cite des Etourneaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312900;
        gn:lat           47.39979;
        gn:long          -1.2168;
        gn:name          "Cité des Étourneaux";
        gn:population    0 .

<https://sws.geonames.org/8292958/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Ligne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292958;
        gn:lat           47.4125;
        gn:long          -1.37431;
        gn:name          "Bureau de Poste de Ligne";
        gn:population    0 .

<https://sws.geonames.org/9177239/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inter-Hotel Le Logis D'Elbee";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177239;
        gn:lat           47.20854;
        gn:long          -0.98165;
        gn:name          "Inter-Hotel Le Logis D'Elbee";
        gn:population    0 .

<https://sws.geonames.org/8292904/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Abbaretz";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292904;
        gn:lat           47.5521;
        gn:long          -1.53467;
        gn:name          "Bureau de Poste de Abbaretz";
        gn:population    0 .

<https://sws.geonames.org/2979551/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Hilaire-de-Clisson";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979551;
        gn:lat           47.06197;
        gn:long          -1.30946;
        gn:name          "Saint-Hilaire-de-Clisson";
        gn:population    1754 .

<https://sws.geonames.org/8292943/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Fay De Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292943;
        gn:lat           47.41408;
        gn:long          -1.79073;
        gn:name          "Bureau de Poste de Fay De Bretagne";
        gn:population    0 .

<https://sws.geonames.org/3006237/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Touche Boissaie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006237;
        gn:lat           47.57981;
        gn:long          -1.55076;
        gn:name          "La Touche Boissaie";
        gn:population    0 .

<https://sws.geonames.org/12313104/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roseraie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313104;
        gn:lat           47.1757;
        gn:long          -1.36946;
        gn:name          "La Roseraie";
        gn:population    0 .

<https://sws.geonames.org/6452325/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Aigrefeuille-sur-Maine";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6452325;
        gn:lat           47.07667;
        gn:long          -1.40056;
        gn:name          "Aigrefeuille-sur-Maine";
        gn:population    3763 .

<https://sws.geonames.org/3024376/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Coisnaute";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3024376;
        gn:lat           47.55162;
        gn:long          -1.98933;
        gn:name          "Coisnauté";
        gn:population    0 .

<https://sws.geonames.org/9178795/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Residence Cerise Nantes La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178795;
        gn:lat           47.25341;
        gn:long          -1.52835;
        gn:name          "Residence Cerise Nantes La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/12313177/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Halbrandiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313177;
        gn:lat           47.12071;
        gn:long          -1.6153;
        gn:name          "L'Halbrandière";
        gn:population    0 .

<https://sws.geonames.org/3013766/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Haute-Goulaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3013766;
        gn:lat           47.19904;
        gn:long          -1.43012;
        gn:name          "Haute-Goulaine";
        gn:population    5290 .

<https://sws.geonames.org/12313012/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boulaie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313012;
        gn:lat           47.5356;
        gn:long          -1.99157;
        gn:name          "La Boulaie";
        gn:population    0 .

<https://sws.geonames.org/12312963/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Buron";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312963;
        gn:lat           47.2944;
        gn:long          -1.69359;
        gn:name          "Le Buron";
        gn:population    0 .

<https://sws.geonames.org/12060744/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Babiniere Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    12060744;
        gn:lat           47.25802;
        gn:long          -1.54548;
        gn:name          "Babinière Railway Station";
        gn:population    0 .

<https://sws.geonames.org/2992054/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montrevault";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2992054;
        gn:lat           47.26145;
        gn:long          -1.04579;
        gn:name          "Montrevault";
        gn:population    1267 .

<https://sws.geonames.org/8287008/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Coueron Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287008;
        gn:lat           47.22217;
        gn:long          -1.72469;
        gn:name          "Couéron Railway Station";
        gn:population    0 .

<https://sws.geonames.org/6452360/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Andreze";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6452360;
        gn:lat           47.17139;
        gn:long          -0.95333;
        gn:name          "Andrezé";
        gn:population    1814 .

<https://sws.geonames.org/8293080/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Malakoff";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293080;
        gn:lat           47.2144;
        gn:long          -1.5274;
        gn:name          "Bureau de Poste de Nantes Malakoff";
        gn:population    0 .

<https://sws.geonames.org/12313155/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rousseliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313155;
        gn:lat           47.17591;
        gn:long          -1.51873;
        gn:name          "La Rousselière";
        gn:population    0 .

<https://sws.geonames.org/2982023/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saffre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2982023;
        gn:lat           47.50145;
        gn:long          -1.57882;
        gn:name          "Saffré";
        gn:population    2884 .

<https://sws.geonames.org/3009045/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gouachere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009045;
        gn:lat           47.325;
        gn:long          -1.43726;
        gn:name          "La Gouachère";
        gn:population    0 .

<https://sws.geonames.org/12310645/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Genetais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310645;
        gn:lat           46.92308;
        gn:long          -1.39192;
        gn:name          "Le Genétais";
        gn:population    0 .

<https://sws.geonames.org/8436196/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont de Chevire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436196;
        gn:lat           47.19288;
        gn:long          -1.6136;
        gn:name          "Pont de Cheviré";
        gn:population    0 .

<https://sws.geonames.org/3233493/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Menhir";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233493;
        gn:lat           47.20464;
        gn:long          -2.14538;
        gn:name          "Le Menhir";
        gn:population    0 .

<https://sws.geonames.org/12313219/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Trois Croix";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313219;
        gn:lat           47.1245;
        gn:long          -2.09561;
        gn:name          "Les Trois Croix";
        gn:population    0 .

<https://sws.geonames.org/2997861/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Loire-Atlantique";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM2;
        gn:geonamesID    2997861;
        gn:lat           47.32863;
        gn:long          -1.65764;
        gn:name          "Loire-Atlantique";
        gn:population    1473156 .

<https://sws.geonames.org/8293036/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Varades";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293036;
        gn:lat           47.38668;
        gn:long          -1.03232;
        gn:name          "Bureau de Poste de Varades";
        gn:population    0 .

<https://sws.geonames.org/8436210/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont General-Audibert";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436210;
        gn:lat           47.20788;
        gn:long          -1.54918;
        gn:name          "Pont Général-Audibert";
        gn:population    0 .

<https://sws.geonames.org/3038520/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Aigrefeuille-sur-Maine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3038520;
        gn:lat           47.08008;
        gn:long          -1.40419;
        gn:name          "Aigrefeuille-sur-Maine";
        gn:population    2355 .

<https://sws.geonames.org/6435222/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ingrandes-le-Fresne-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6435222;
        gn:lat           47.40222;
        gn:long          -0.92333;
        gn:name          "Ingrandes-le-Fresne-sur-Loire";
        gn:population    2601 .

<https://sws.geonames.org/3022041/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Curette";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3022041;
        gn:lat           47.3606;
        gn:long          -1.63155;
        gn:name          "Curette";
        gn:population    0 .

<https://sws.geonames.org/3008842/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Guibretiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008842;
        gn:lat           47.44416;
        gn:long          -1.2744;
        gn:name          "La Guibretière";
        gn:population    0 .

<https://sws.geonames.org/8292985/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Pontchateau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292985;
        gn:lat           47.43493;
        gn:long          -2.08897;
        gn:name          "Bureau de Poste de Pontchateau";
        gn:population    0 .

<https://sws.geonames.org/12313146/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Barbiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313146;
        gn:lat           47.16135;
        gn:long          -1.48144;
        gn:name          "La Barbinière";
        gn:population    0 .

<https://sws.geonames.org/3005424/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Vriere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005424;
        gn:lat           47.28202;
        gn:long          -1.55595;
        gn:name          "La Vrière";
        gn:population    0 .

<https://sws.geonames.org/3031219/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roches de Bouin";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.RF;
        gn:geonamesID    3031219;
        gn:lat           47.00234;
        gn:long          -2.058;
        gn:name          "Roches de Bouin";
        gn:population    0 .

<https://sws.geonames.org/3029076/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Camais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3029076;
        gn:lat           47.32131;
        gn:long          -2.12786;
        gn:name          "Camais";
        gn:population    0 .

<https://sws.geonames.org/3023696/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Etier de Cordemais";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3023696;
        gn:lat           47.28417;
        gn:long          -1.89107;
        gn:name          "Étier de Cordemais";
        gn:population    0 .

<https://sws.geonames.org/12313004/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Retaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313004;
        gn:lat           47.5535;
        gn:long          -2.02759;
        gn:name          "Rétaud";
        gn:population    0 .

<https://sws.geonames.org/8293008/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Sainte Luce Sur Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293008;
        gn:lat           47.24982;
        gn:long          -1.48442;
        gn:name          "Bureau de Poste de Sainte Luce Sur Loire";
        gn:population    0 .

<https://sws.geonames.org/3009285/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Frandiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009285;
        gn:lat           46.92119;
        gn:long          -2.16561;
        gn:name          "La Frandière";
        gn:population    0 .

<https://sws.geonames.org/2980993/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Crespin-sur-Moine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980993;
        gn:lat           47.09968;
        gn:long          -1.18651;
        gn:name          "Saint-Crespin-sur-Moine";
        gn:population    1474 .

<https://sws.geonames.org/12312881/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haute Meilleraie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312881;
        gn:lat           47.37111;
        gn:long          -1.02012;
        gn:name          "La Haute Meilleraie";
        gn:population    0 .

<https://sws.geonames.org/9177479/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Kyriad Prestige Saint Nazaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177479;
        gn:lat           47.3178;
        gn:long          -2.18912;
        gn:name          "Kyriad Prestige Saint Nazaire";
        gn:population    0 .

<https://sws.geonames.org/6434557/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434557;
        gn:lat           47.55472;
        gn:long          -1.70111;
        gn:name          "Vay";
        gn:population    2060 .

<https://sws.geonames.org/6614481/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bonnœuvre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6614481;
        gn:lat           47.5275;
        gn:long          -1.23611;
        gn:name          "Bonnœuvre";
        gn:population    560 .

<https://sws.geonames.org/8292971/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Montoir De Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292971;
        gn:lat           47.3194;
        gn:long          -2.16236;
        gn:name          "Bureau de Poste de Montoir De Bretagne";
        gn:population    0 .

<https://sws.geonames.org/9259163/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Adagio Acces Nantes Viarme";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9259163;
        gn:lat           47.22308;
        gn:long          -1.56266;
        gn:name          "Adagio Acces Nantes Viarme";
        gn:population    0 .

<https://sws.geonames.org/9177085/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inter-Hotel Agora";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177085;
        gn:lat           47.25211;
        gn:long          -1.6189;
        gn:name          "Inter-Hotel Agora";
        gn:population    0 .

<https://sws.geonames.org/7521333/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mairie de Doulon";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    7521333;
        gn:lat           47.22679;
        gn:long          -1.51873;
        gn:name          "Mairie de Doulon";
        gn:population    0 .

<https://sws.geonames.org/10297838/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Du Tourisme";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297838;
        gn:lat           47.21736;
        gn:long          -1.55673;
        gn:name          "Hotel Du Tourisme";
        gn:population    0 .

<https://sws.geonames.org/3233929/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bras de Cordemais";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STMA;
        gn:geonamesID    3233929;
        gn:lat           47.28306;
        gn:long          -1.89667;
        gn:name          "Bras de Cordemais";
        gn:population    0 .

<https://sws.geonames.org/8297447/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Hilaire De Loulay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297447;
        gn:lat           47.00326;
        gn:long          -1.33156;
        gn:name          "Bureau de Poste de Saint Hilaire De Loulay";
        gn:population    0 .

<https://sws.geonames.org/3037795/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret d'Ancenis";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    3037795;
        gn:lat           47.54642;
        gn:long          -1.3185;
        gn:name          "Forêt d'Ancenis";
        gn:population    0 .

<https://sws.geonames.org/8292977/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Orvault";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292977;
        gn:lat           47.25321;
        gn:long          -1.59664;
        gn:name          "Bureau de Poste de Orvault";
        gn:population    0 .

<https://sws.geonames.org/12310643/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Dauniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310643;
        gn:lat           46.93213;
        gn:long          -1.28158;
        gn:name          "La Daunière";
        gn:population    0 .

<https://sws.geonames.org/8293049/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Chantenay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293049;
        gn:lat           47.20049;
        gn:long          -1.58923;
        gn:name          "Bureau de Poste de Nantes Chantenay";
        gn:population    0 .

<https://sws.geonames.org/12313019/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Vallee Mismi";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313019;
        gn:lat           47.36706;
        gn:long          -1.96104;
        gn:name          "La Vallée Mismi";
        gn:population    0 .

<https://sws.geonames.org/3009111/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Geriais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009111;
        gn:lat           47.51023;
        gn:long          -2.14774;
        gn:name          "La Gériais";
        gn:population    0 .

<https://sws.geonames.org/12305810/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Midi";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305810;
        gn:lat           46.9494;
        gn:long          -2.18937;
        gn:name          "Le Midi";
        gn:population    0 .

<https://sws.geonames.org/2978917/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Laurent-des-Autels";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978917;
        gn:lat           47.28524;
        gn:long          -1.18881;
        gn:name          "Saint-Laurent-des-Autels";
        gn:population    1590 .

<https://sws.geonames.org/12305901/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont James";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305901;
        gn:lat           47.01433;
        gn:long          -1.57036;
        gn:name          "Pont James";
        gn:population    0 .

<https://sws.geonames.org/12305883/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Housseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305883;
        gn:lat           47.28332;
        gn:long          -1.49646;
        gn:name          "Le Housseau";
        gn:population    0 .

<https://sws.geonames.org/8297410/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Gaubretiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297410;
        gn:lat           46.94347;
        gn:long          -1.06305;
        gn:name          "Bureau de Poste de La Gaubretiere";
        gn:population    0 .

<https://sws.geonames.org/8436213/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Resal";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436213;
        gn:lat           47.212;
        gn:long          -1.53418;
        gn:name          "Pont Résal";
        gn:population    0 .

<https://sws.geonames.org/12305888/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Brebionniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305888;
        gn:lat           47.10712;
        gn:long          -1.27437;
        gn:name          "La Brébionnière";
        gn:population    0 .

<https://sws.geonames.org/3007230/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Polhaie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007230;
        gn:lat           47.51708;
        gn:long          -2.01736;
        gn:name          "La Polhaie";
        gn:population    0 .

<https://sws.geonames.org/12312896/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Riffaudieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312896;
        gn:lat           47.47003;
        gn:long          -1.20222;
        gn:name          "Les Riffaudières";
        gn:population    0 .

<https://sws.geonames.org/3233428/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Moutons";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233428;
        gn:lat           47.18333;
        gn:long          -2.18167;
        gn:name          "Les Moutons";
        gn:population    0 .

<https://sws.geonames.org/3031370/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031370;
        gn:lat           47.35595;
        gn:long          -1.58821;
        gn:name          "Bouché";
        gn:population    0 .

<https://sws.geonames.org/2981149/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Christophe-du-Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981149;
        gn:lat           47.02911;
        gn:long          -0.94518;
        gn:name          "Saint-Christophe-du-Bois";
        gn:population    2667 .

<https://sws.geonames.org/13494802/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Phare de la Noeveillard";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.LTHSE;
        gn:geonamesID    13494802;
        gn:lat           47.11032;
        gn:long          -2.1154;
        gn:name          "Phare de la Noëveillard";
        gn:population    0 .

<https://sws.geonames.org/8292930/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Chauve";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292930;
        gn:lat           47.1507;
        gn:long          -1.98701;
        gn:name          "Bureau de Poste de Chauve";
        gn:population    0 .

<https://sws.geonames.org/12308496/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Blottieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308496;
        gn:lat           47.24418;
        gn:long          -1.11272;
        gn:name          "Les Blottières";
        gn:population    0 .

<https://sws.geonames.org/3002783/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Epine de Fay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002783;
        gn:lat           47.37048;
        gn:long          -1.70369;
        gn:name          "L'Épine de Fay";
        gn:population    0 .

<https://sws.geonames.org/2988288/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pays de la Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.RGN;
        gn:geonamesID    2988288;
        gn:lat           47.5;
        gn:long          -1.0;
        gn:name          "Pays de la Loire";
        gn:population    0 .

<https://sws.geonames.org/3012727/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Isac";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3012727;
        gn:lat           47.45977;
        gn:long          -1.63012;
        gn:name          "Isac";
        gn:population    0 .

<https://sws.geonames.org/6434501/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Puceul";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434501;
        gn:lat           47.52194;
        gn:long          -1.61694;
        gn:name          "Puceul";
        gn:population    1119 .

<https://sws.geonames.org/12312958/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Petit Chantilly";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312958;
        gn:lat           47.25068;
        gn:long          -1.59919;
        gn:name          "Le Petit Chantilly";
        gn:population    0 .

<https://sws.geonames.org/12312916/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cotiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312916;
        gn:lat           47.45866;
        gn:long          -1.34091;
        gn:name          "La Cotinière";
        gn:population    0 .

<https://sws.geonames.org/2981568/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Aubin-des-Ormeaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981568;
        gn:lat           46.99194;
        gn:long          -1.04316;
        gn:name          "Saint-Aubin-des-Ormeaux";
        gn:population    1232 .

<https://sws.geonames.org/12313229/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Sandier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313229;
        gn:lat           47.12123;
        gn:long          -2.11056;
        gn:name          "Le Sandier";
        gn:population    0 .

<https://sws.geonames.org/12312884/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Courtais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312884;
        gn:lat           47.59196;
        gn:long          -1.18072;
        gn:name          "La Courtais";
        gn:population    0 .

<https://sws.geonames.org/6614376/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Herbergement";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614376;
        gn:lat           46.90917;
        gn:long          -1.37694;
        gn:name          "L'Herbergement";
        gn:population    3145 .

<https://sws.geonames.org/6434481/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mouzeil";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434481;
        gn:lat           47.44806;
        gn:long          -1.34806;
        gn:name          "Mouzeil";
        gn:population    1874 .

<https://sws.geonames.org/3003661/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Loroux-Bottereau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003661;
        gn:lat           47.23797;
        gn:long          -1.34963;
        gn:name          "Le Loroux-Bottereau";
        gn:population    5326 .

<https://sws.geonames.org/10297848/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Apts Adagio Access Nantes La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297848;
        gn:lat           47.2514;
        gn:long          -1.53154;
        gn:name          "Apts Adagio Access Nantes La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/6435217/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Geste";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435217;
        gn:lat           47.18056;
        gn:long          -1.11083;
        gn:name          "Gesté";
        gn:population    2547 .

<https://sws.geonames.org/2993692/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Missillac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2993692;
        gn:lat           47.48217;
        gn:long          -2.15926;
        gn:name          "Missillac";
        gn:population    4180 .

<https://sws.geonames.org/3011326/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Barre-Theberge";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011326;
        gn:lat           47.48857;
        gn:long          -1.35143;
        gn:name          "La Barre-Theberge";
        gn:population    0 .

<https://sws.geonames.org/8293031/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Thouare Sur Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293031;
        gn:lat           47.26723;
        gn:long          -1.4404;
        gn:name          "Bureau de Poste de Thouare Sur Loire";
        gn:population    0 .

<https://sws.geonames.org/12313106/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Verrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313106;
        gn:lat           47.17296;
        gn:long          -1.42546;
        gn:name          "La Verrie";
        gn:population    0 .

<https://sws.geonames.org/2979930/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Georges-de-Montaigu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979930;
        gn:lat           46.94655;
        gn:long          -1.29262;
        gn:name          "Saint-Georges-de-Montaigu";
        gn:population    3598 .

<https://sws.geonames.org/3009272/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fremiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009272;
        gn:lat           47.34047;
        gn:long          -1.7594;
        gn:name          "La Fremière";
        gn:population    0 .

<https://sws.geonames.org/12313121/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Mortier Mainguet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313121;
        gn:lat           47.0821;
        gn:long          -1.34676;
        gn:name          "Le Mortier Mainguet";
        gn:population    0 .

<https://sws.geonames.org/6612550/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Gereon";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6612550;
        gn:lat           47.36917;
        gn:long          -1.19833;
        gn:name          "Saint-Géréon";
        gn:population    2668 .

<https://sws.geonames.org/6616812/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Aignan-Grandlieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616812;
        gn:lat           47.124;
        gn:long          -1.63;
        gn:name          "Saint-Aignan-Grandlieu";
        gn:population    3912 .

<https://sws.geonames.org/2990071/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plateau de Notre-Dame";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    2990071;
        gn:lat           47.09044;
        gn:long          -2.13854;
        gn:name          "Plateau de Notre-Dame";
        gn:population    0 .

<https://sws.geonames.org/6473350/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mercure Ile de Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6473350;
        gn:lat           47.2062;
        gn:long          -1.5285;
        gn:name          "Mercure Ile de Nantes";
        gn:population    0 .

<https://sws.geonames.org/2977166/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Roch";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977166;
        gn:lat           47.45405;
        gn:long          -1.76928;
        gn:name          "Saint-Roch";
        gn:population    0 .

<https://sws.geonames.org/6445214/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Martin-des-Tilleuls";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6445214;
        gn:lat           46.97389;
        gn:long          -1.05111;
        gn:name          "Saint-Martin-des-Tilleuls";
        gn:population    1062 .

<https://sws.geonames.org/12313071/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Peltiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313071;
        gn:lat           47.04679;
        gn:long          -1.14869;
        gn:name          "La Peltière";
        gn:population    0 .

<https://sws.geonames.org/8287025/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ingrandes sur Loire Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287025;
        gn:lat           47.40594;
        gn:long          -0.92053;
        gn:name          "Ingrandes sur Loire Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3008281/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Marne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008281;
        gn:lat           47.0;
        gn:long          -1.73333;
        gn:name          "La Marne";
        gn:population    0 .

<https://sws.geonames.org/6434517/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Hilaire-de-Chaleons";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434517;
        gn:lat           47.10306;
        gn:long          -1.865;
        gn:name          "Saint-Hilaire-de-Chaléons";
        gn:population    2265 .

<https://sws.geonames.org/12308528/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Blouere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308528;
        gn:lat           47.15655;
        gn:long          -1.05453;
        gn:name          "La Blouère";
        gn:population    0 .

<https://sws.geonames.org/8297459/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Verrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297459;
        gn:lat           46.9602;
        gn:long          -0.99663;
        gn:name          "Bureau de Poste de La Verrie";
        gn:population    0 .

<https://sws.geonames.org/9176888/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Les Archers";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9176888;
        gn:lat           46.92952;
        gn:long          -0.98764;
        gn:name          "Hotel Les Archers";
        gn:population    0 .

<https://sws.geonames.org/3006852/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Robiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006852;
        gn:lat           47.3325;
        gn:long          -1.36464;
        gn:name          "La Robinière";
        gn:population    0 .

<https://sws.geonames.org/3002608/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pommain";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002608;
        gn:lat           47.45773;
        gn:long          -1.63428;
        gn:name          "Le Pommain";
        gn:population    0 .

<https://sws.geonames.org/2978632/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Malo-du-Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978632;
        gn:lat           46.92891;
        gn:long          -0.90004;
        gn:name          "Saint-Malô-du-Bois";
        gn:population    1291 .

<https://sws.geonames.org/2987714/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Petite Maine";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2987714;
        gn:lat           46.95063;
        gn:long          -1.30419;
        gn:name          "Petite Maine";
        gn:population    0 .

<https://sws.geonames.org/3006857/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Robertiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006857;
        gn:lat           47.53647;
        gn:long          -1.46486;
        gn:name          "La Robertière";
        gn:population    0 .

<https://sws.geonames.org/9172997/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Balladins Nantes Saint Herblain";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9172997;
        gn:lat           47.22954;
        gn:long          -1.6337;
        gn:name          "Balladins Nantes Saint Herblain";
        gn:population    0 .

<https://sws.geonames.org/2985488/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Prefoure";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2985488;
        gn:lat           47.41584;
        gn:long          -1.41441;
        gn:name          "Préfoure";
        gn:population    0 .

<https://sws.geonames.org/3000205/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Moutiers-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000205;
        gn:lat           47.06375;
        gn:long          -1.999;
        gn:name          "Les Moutiers-en-Retz";
        gn:population    1145 .

<https://sws.geonames.org/3020828/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Dreffeac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3020828;
        gn:lat           47.476;
        gn:long          -2.05783;
        gn:name          "Drefféac";
        gn:population    1452 .

<https://sws.geonames.org/10281898/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Premiere Classe Nantes St Herblain";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10281898;
        gn:lat           47.21179;
        gn:long          -1.65403;
        gn:name          "Premiere Classe Nantes St Herblain";
        gn:population    0 .

<https://sws.geonames.org/12313163/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bourie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313163;
        gn:lat           47.13231;
        gn:long          -1.58295;
        gn:name          "La Bourie";
        gn:population    0 .

<https://sws.geonames.org/2986705/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plongeon";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2986705;
        gn:lat           47.46881;
        gn:long          -1.72238;
        gn:name          "Plongeon";
        gn:population    0 .

<https://sws.geonames.org/6435335/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tillieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435335;
        gn:lat           47.14444;
        gn:long          -1.16444;
        gn:name          "Tillières";
        gn:population    1744 .

<https://sws.geonames.org/3003710/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Lavoir";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003710;
        gn:lat           47.37584;
        gn:long          -1.50599;
        gn:name          "Le Lavoir";
        gn:population    0 .

<https://sws.geonames.org/12313006/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Cougou";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313006;
        gn:lat           47.54393;
        gn:long          -2.0095;
        gn:name          "Le Cougou";
        gn:population    0 .

<https://sws.geonames.org/12310635/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Petit Saint-Andre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310635;
        gn:lat           46.93664;
        gn:long          -1.40681;
        gn:name          "Le Petit Saint-André";
        gn:population    0 .

<https://sws.geonames.org/9178692/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Relais Du Silence Domaine Le Martinet";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178692;
        gn:lat           46.97426;
        gn:long          -1.99848;
        gn:name          "Relais Du Silence Domaine Le Martinet";
        gn:population    0 .

<https://sws.geonames.org/8293021/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Viaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293021;
        gn:lat           47.25594;
        gn:long          -2.01856;
        gn:name          "Bureau de Poste de Saint Viaud";
        gn:population    0 .

<https://sws.geonames.org/3233500/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fief";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233500;
        gn:lat           47.23227;
        gn:long          -2.16496;
        gn:name          "Le Fief";
        gn:population    0 .

<https://sws.geonames.org/12310650/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boisseliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310650;
        gn:lat           46.91631;
        gn:long          -1.36017;
        gn:name          "La Boisselière";
        gn:population    0 .

<https://sws.geonames.org/6456064/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fuilet";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456064;
        gn:lat           47.28111;
        gn:long          -1.11583;
        gn:name          "Le Fuilet";
        gn:population    1872 .

<https://sws.geonames.org/10110273/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Duquesne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10110273;
        gn:lat           47.21867;
        gn:long          -1.55673;
        gn:name          "Hotel Duquesne";
        gn:population    0 .

<https://sws.geonames.org/3233616/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe de l'Imperlay";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    3233616;
        gn:lat           47.27406;
        gn:long          -2.13205;
        gn:name          "Pointe de l'Imperlay";
        gn:population    0 .

<https://sws.geonames.org/12320392/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cran";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12320392;
        gn:lat           47.57692;
        gn:long          -2.13038;
        gn:name          "Cran";
        gn:population    0 .

<https://sws.geonames.org/12313190/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Ardillets";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313190;
        gn:lat           47.21346;
        gn:long          -1.71628;
        gn:name          "Les Ardillets";
        gn:population    0 .

<https://sws.geonames.org/2969316/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vieillevigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2969316;
        gn:lat           46.97152;
        gn:long          -1.43446;
        gn:name          "Vieillevigne";
        gn:population    3529 .

<https://sws.geonames.org/12308535/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Boisselieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308535;
        gn:lat           47.12667;
        gn:long          -1.16759;
        gn:name          "Les Boisselières";
        gn:population    0 .

<https://sws.geonames.org/12305735/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle Aubry";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305735;
        gn:lat           47.24435;
        gn:long          -0.95783;
        gn:name          "La Chapelle Aubry";
        gn:population    0 .

<https://sws.geonames.org/3000834/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Grandes Landes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000834;
        gn:lat           47.4656;
        gn:long          -1.5725;
        gn:name          "Les Grandes Landes";
        gn:population    0 .

<https://sws.geonames.org/2973219/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Teille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2973219;
        gn:lat           47.4617;
        gn:long          -1.2781;
        gn:name          "Teillé";
        gn:population    1407 .

<https://sws.geonames.org/2996445/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Malescot";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2996445;
        gn:lat           47.51667;
        gn:long          -1.63333;
        gn:name          "Malescot";
        gn:population    0 .

<https://sws.geonames.org/2987756/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile du Petit Carnet";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    2987756;
        gn:lat           47.28107;
        gn:long          -1.97608;
        gn:name          "Île du Petit Carnet";
        gn:population    0 .

<https://sws.geonames.org/6434478/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montoir-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434478;
        gn:lat           47.32833;
        gn:long          -2.14917;
        gn:name          "Montoir-de-Bretagne";
        gn:population    7079 .

<https://sws.geonames.org/12313230/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Carres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313230;
        gn:lat           47.07831;
        gn:long          -2.02944;
        gn:name          "Les Carrés";
        gn:population    0 .

<https://sws.geonames.org/2979682/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sapins de Saint-Gildas";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2979682;
        gn:lat           47.53333;
        gn:long          -2.01667;
        gn:name          "Sapins de Saint-Gildas";
        gn:population    0 .

<https://sws.geonames.org/2983869/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pays de Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.RGN;
        gn:geonamesID    2983869;
        gn:lat           47.11667;
        gn:long          -1.96667;
        gn:name          "Pays de Retz";
        gn:population    0 .

<https://sws.geonames.org/2969612/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vertou";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2969612;
        gn:lat           47.16878;
        gn:long          -1.4729;
        gn:name          "Vertou";
        gn:population    22921 .

<https://sws.geonames.org/11746354/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arcades du Gue de la Roche";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNLA;
        gn:geonamesID    11746354;
        gn:lat           47.49117;
        gn:long          -1.46808;
        gn:name          "Arcades du Gué de la Roche";
        gn:population    0 .

<https://sws.geonames.org/12313074/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chalousiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313074;
        gn:lat           47.16055;
        gn:long          -1.22252;
        gn:name          "La Chalousière";
        gn:population    0 .

<https://sws.geonames.org/3233388/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roche des Fleurs";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233388;
        gn:lat           47.02;
        gn:long          -2.11333;
        gn:name          "Roche des Fleurs";
        gn:population    0 .

<https://sws.geonames.org/6455120/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ligne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6455120;
        gn:lat           47.41167;
        gn:long          -1.37722;
        gn:name          "Ligné";
        gn:population    5143 .

<https://sws.geonames.org/3015658/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gorges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3015658;
        gn:lat           47.10112;
        gn:long          -1.30267;
        gn:name          "Gorges";
        gn:population    3087 .

<https://sws.geonames.org/2982492/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roussay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2982492;
        gn:lat           47.09011;
        gn:long          -1.06417;
        gn:name          "Roussay";
        gn:population    1060 .

<https://sws.geonames.org/3003730/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Landreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003730;
        gn:lat           47.20443;
        gn:long          -1.30546;
        gn:name          "Le Landreau";
        gn:population    2674 .

<https://sws.geonames.org/8292961/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Machecoul";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292961;
        gn:lat           46.99359;
        gn:long          -1.8218;
        gn:name          "Bureau de Poste de Machecoul";
        gn:population    0 .

<https://sws.geonames.org/6490782/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Premiere Classe Nantes est - Saint Sebastien sur Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6490782;
        gn:lat           47.2116;
        gn:long          -1.4871;
        gn:name          "Premiere Classe Nantes est - Saint Sebastien sur Loire";
        gn:population    0 .

<https://sws.geonames.org/2998659/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois du Lezay";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2998659;
        gn:lat           47.53647;
        gn:long          -2.12152;
        gn:name          "Bois du Lezay";
        gn:population    0 .

<https://sws.geonames.org/6639990/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bataille de Blain 843";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.BTL;
        gn:geonamesID    6639990;
        gn:lat           47.46245;
        gn:long          -1.73807;
        gn:name          "Bataille de Blain 843";
        gn:population    0 .

<https://sws.geonames.org/3006290/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Terreliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006290;
        gn:lat           47.05286;
        gn:long          -1.01084;
        gn:name          "La Terrelière";
        gn:population    0 .

<https://sws.geonames.org/10297850/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abat Jour";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297850;
        gn:lat           47.22179;
        gn:long          -1.54854;
        gn:name          "Abat Jour";
        gn:population    0 .

<https://sws.geonames.org/9172611/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Adagio Nantes Centre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9172611;
        gn:lat           47.21691;
        gn:long          -1.54621;
        gn:name          "Adagio Nantes Centre";
        gn:population    0 .

<https://sws.geonames.org/9179084/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sejours & Affaires Nantes Ducs De Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9179084;
        gn:lat           47.21382;
        gn:long          -1.54551;
        gn:name          "Séjours & Affaires Nantes Ducs De Bretagne";
        gn:population    0 .

<https://sws.geonames.org/3029976/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brive";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3029976;
        gn:lat           47.36209;
        gn:long          -2.1837;
        gn:name          "Brivé";
        gn:population    0 .

<https://sws.geonames.org/6456912/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Launay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456912;
        gn:lat           47.3725;
        gn:long          -1.97194;
        gn:name          "La Chapelle-Launay";
        gn:population    2983 .

<https://sws.geonames.org/3010237/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010237;
        gn:lat           47.29964;
        gn:long          -1.55239;
        gn:name          "La Chapelle-sur-Erdre";
        gn:population    18481 .

<https://sws.geonames.org/12313180/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Passay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313180;
        gn:lat           47.09648;
        gn:long          -1.63582;
        gn:name          "Passay";
        gn:population    0 .

<https://sws.geonames.org/3001608/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Escarpiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3001608;
        gn:lat           47.0919;
        gn:long          -1.18825;
        gn:name          "L'Escarpière";
        gn:population    0 .

<https://sws.geonames.org/6435310/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Philbert-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435310;
        gn:lat           47.15111;
        gn:long          -1.01722;
        gn:name          "Saint-Philbert-en-Mauges";
        gn:population    375 .

<https://sws.geonames.org/12493353/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Moulin de La Brousse";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.ML;
        gn:geonamesID    12493353;
        gn:lat           47.57254;
        gn:long          -1.8226;
        gn:name          "Moulin de La Brousse";
        gn:population    0 .

<https://sws.geonames.org/3015357/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grand-Auverne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3015357;
        gn:lat           47.59172;
        gn:long          -1.32953;
        gn:name          "Grand-Auverné";
        gn:population    0 .

<https://sws.geonames.org/3005032/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Breil";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005032;
        gn:lat           47.28714;
        gn:long          -1.67678;
        gn:name          "Le Breil";
        gn:population    0 .

<https://sws.geonames.org/6434497/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Port-Saint-Pere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434497;
        gn:lat           47.13306;
        gn:long          -1.74833;
        gn:name          "Port-Saint-Père";
        gn:population    2910 .

<https://sws.geonames.org/12313009/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Branleix";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313009;
        gn:lat           47.55464;
        gn:long          -2.04281;
        gn:name          "Branleix";
        gn:population    0 .

<https://sws.geonames.org/12313113/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Halopiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313113;
        gn:lat           47.13243;
        gn:long          -1.37224;
        gn:name          "La Halopière";
        gn:population    0 .

<https://sws.geonames.org/3000970/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Friches";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000970;
        gn:lat           47.48964;
        gn:long          -1.48191;
        gn:name          "Les Friches";
        gn:population    0 .

<https://sws.geonames.org/3233503/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roches des Rochelets";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233503;
        gn:lat           47.21581;
        gn:long          -2.17067;
        gn:name          "Roches des Rochelets";
        gn:population    0 .

<https://sws.geonames.org/12313222/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Port Cheri";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313222;
        gn:lat           47.11804;
        gn:long          -2.07744;
        gn:name          "Le Port Chéri";
        gn:population    0 .

<https://sws.geonames.org/12312975/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Primaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312975;
        gn:lat           47.37926;
        gn:long          -1.71447;
        gn:name          "La Primaudière";
        gn:population    0 .

<https://sws.geonames.org/6434523/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Leger-les-Vignes";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434523;
        gn:lat           47.13611;
        gn:long          -1.73222;
        gn:name          "Saint-Léger-les-Vignes";
        gn:population    1776 .

<https://sws.geonames.org/12313021/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tarambon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313021;
        gn:lat           47.59892;
        gn:long          -2.07216;
        gn:name          "Tarambon";
        gn:population    0 .

<https://sws.geonames.org/2980259/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Etienne-de-Montluc";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980259;
        gn:lat           47.27622;
        gn:long          -1.78013;
        gn:name          "Saint-Étienne-de-Montluc";
        gn:population    6809 .

<https://sws.geonames.org/12305896/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bourchiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305896;
        gn:lat           47.15194;
        gn:long          -1.42954;
        gn:name          "La Bourchinière";
        gn:population    0 .

<https://sws.geonames.org/12312886/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Basses Places";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312886;
        gn:lat           47.53349;
        gn:long          -1.16937;
        gn:name          "Les Basses Places";
        gn:population    0 .

<https://sws.geonames.org/6456956/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chaussaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456956;
        gn:lat           47.20139;
        gn:long          -1.14639;
        gn:name          "La Chaussaire";
        gn:population    777 .

<https://sws.geonames.org/12312995/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Haute Abbaye";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312995;
        gn:lat           47.59752;
        gn:long          -2.0396;
        gn:name          "Haute Abbaye";
        gn:population    0 .

<https://sws.geonames.org/8286992/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pallet Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286992;
        gn:lat           47.14423;
        gn:long          -1.34779;
        gn:name          "Le Pallet Railway Station";
        gn:population    0 .

<https://sws.geonames.org/2970808/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vandel";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2970808;
        gn:lat           47.33083;
        gn:long          -1.32714;
        gn:name          "Vandel";
        gn:population    0 .

<https://sws.geonames.org/12313171/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bouguiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313171;
        gn:lat           47.1731;
        gn:long          -1.63411;
        gn:name          "La Bouguinière";
        gn:population    0 .

<https://sws.geonames.org/3010726/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bruffiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010726;
        gn:lat           47.0138;
        gn:long          -1.19795;
        gn:name          "La Bruffière";
        gn:population    3320 .

<https://sws.geonames.org/2990688/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Etang Neuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.LK;
        gn:geonamesID    2990688;
        gn:lat           46.91667;
        gn:long          -1.13333;
        gn:name          "L'Étang Neuf";
        gn:population    0 .

<https://sws.geonames.org/6452328/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chaumes-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6452328;
        gn:lat           47.11639;
        gn:long          -1.93861;
        gn:name          "Chaumes-en-Retz";
        gn:population    6691 .

<https://sws.geonames.org/3006446/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Seilleraye";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSEC;
        gn:geonamesID    3006446;
        gn:lat           47.29917;
        gn:long          -1.43273;
        gn:name          "La Seilleraye";
        gn:population    0 .

<https://sws.geonames.org/2983103/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rohars";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2983103;
        gn:lat           47.29488;
        gn:long          -1.92036;
        gn:name          "Rohars";
        gn:population    0 .

<https://sws.geonames.org/12320409/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Broussais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12320409;
        gn:lat           47.5655;
        gn:long          -2.14715;
        gn:name          "Le Broussais";
        gn:population    0 .

<https://sws.geonames.org/3006805/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roche-Blanche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006805;
        gn:lat           47.4405;
        gn:long          -1.14028;
        gn:name          "La Roche-Blanche";
        gn:population    929 .

<https://sws.geonames.org/3009905/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cornuaille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009905;
        gn:lat           47.51087;
        gn:long          -0.98432;
        gn:name          "La Cornuaille";
        gn:population    837 .

<https://sws.geonames.org/3005763/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Varenne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005763;
        gn:lat           47.31107;
        gn:long          -1.31976;
        gn:name          "La Varenne";
        gn:population    1451 .

<https://sws.geonames.org/2979680/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Gildas-des-Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979680;
        gn:lat           47.51622;
        gn:long          -2.03659;
        gn:name          "Saint-Gildas-des-Bois";
        gn:population    3239 .

<https://sws.geonames.org/12312966/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Hauts de Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312966;
        gn:lat           47.25802;
        gn:long          -1.67471;
        gn:name          "Les Hauts de Loire";
        gn:population    0 .

<https://sws.geonames.org/3010983/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boissiere-sur-Evre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010983;
        gn:lat           47.30101;
        gn:long          -1.08002;
        gn:name          "La Boissière-sur-Èvre";
        gn:population    0 .

<https://sws.geonames.org/2984009/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rendreux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2984009;
        gn:lat           47.47202;
        gn:long          -2.09714;
        gn:name          "Rendreux";
        gn:population    0 .

<https://sws.geonames.org/2977415/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Pierre-Montlimart";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977415;
        gn:lat           47.26976;
        gn:long          -1.02738;
        gn:name          "Saint-Pierre-Montlimart";
        gn:population    3238 .

<https://sws.geonames.org/8293068/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Saint Jacques";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293068;
        gn:lat           47.19408;
        gn:long          -1.53125;
        gn:name          "Bureau de Poste de Nantes Saint Jacques";
        gn:population    0 .

<https://sws.geonames.org/12313088/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haute Reciviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313088;
        gn:lat           47.12199;
        gn:long          -1.26221;
        gn:name          "La Haute Recivière";
        gn:population    0 .

<https://sws.geonames.org/6456560/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Guyonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456560;
        gn:lat           46.96556;
        gn:long          -1.24972;
        gn:name          "La Guyonnière";
        gn:population    2674 .

<https://sws.geonames.org/12308468/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Guloliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308468;
        gn:lat           47.31508;
        gn:long          -1.30205;
        gn:name          "La Gulolière";
        gn:population    0 .

<https://sws.geonames.org/12313158/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Blordiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313158;
        gn:lat           47.18026;
        gn:long          -1.53688;
        gn:name          "La Blordière";
        gn:population    0 .

<https://sws.geonames.org/2976401/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Etier de la Salle";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2976401;
        gn:lat           47.0;
        gn:long          -1.91667;
        gn:name          "Étier de la Salle";
        gn:population    0 .

<https://sws.geonames.org/12313128/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Louee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313128;
        gn:lat           47.18421;
        gn:long          -1.43235;
        gn:name          "La Louée";
        gn:population    0 .

<https://sws.geonames.org/12312921/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mabonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312921;
        gn:lat           47.3582;
        gn:long          -1.28171;
        gn:name          "La Mabonnière";
        gn:population    0 .

<https://sws.geonames.org/8293011/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Pornic Ste Marie Sur Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293011;
        gn:lat           47.11296;
        gn:long          -2.13074;
        gn:name          "Bureau de Poste de Pornic Ste Marie Sur Mer";
        gn:population    0 .

<https://sws.geonames.org/7290119/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Parc du grand blottereau";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.PRK;
        gn:geonamesID    7290119;
        gn:lat           47.2284;
        gn:long          -1.50903;
        gn:name          "Parc du grand blottereau";
        gn:population    0 .

<https://sws.geonames.org/6616819/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Geneston";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616819;
        gn:lat           47.0556;
        gn:long          -1.5121;
        gn:name          "Geneston";
        gn:population    3638 .

<https://sws.geonames.org/6456024/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Plaine-sur-Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456024;
        gn:lat           47.1375;
        gn:long          -2.18972;
        gn:name          "La Plaine-sur-Mer";
        gn:population    4164 .

<https://sws.geonames.org/12313078/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Eraudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313078;
        gn:lat           47.05359;
        gn:long          -1.17146;
        gn:name          "L'Éraudière";
        gn:population    0 .

<https://sws.geonames.org/8286980/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouaye Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286980;
        gn:lat           47.13778;
        gn:long          -1.67982;
        gn:name          "Bouaye Railway Station";
        gn:population    0 .

<https://sws.geonames.org/2991292/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mouzeil";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2991292;
        gn:lat           47.44835;
        gn:long          -1.34819;
        gn:name          "Mouzeil";
        gn:population    1306 .

<https://sws.geonames.org/6614540/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Limouziniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614540;
        gn:lat           46.9935;
        gn:long          -1.5958;
        gn:name          "La Limouzinière";
        gn:population    2401 .

<https://sws.geonames.org/3233497/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Neuvillette";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233497;
        gn:lat           47.22318;
        gn:long          -2.16553;
        gn:name          "Neuvillette";
        gn:population    0 .

<https://sws.geonames.org/6449108/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Joue-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449108;
        gn:lat           47.49556;
        gn:long          -1.42028;
        gn:name          "Joué-sur-Erdre";
        gn:population    2434 .

<https://sws.geonames.org/3005094/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bourg-Chevreuil";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005094;
        gn:lat           47.5125;
        gn:long          -1.34368;
        gn:name          "Le Bourg-Chevreuil";
        gn:population    0 .

<https://sws.geonames.org/3233931/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile Nouvelle";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISLX;
        gn:geonamesID    3233931;
        gn:lat           47.25;
        gn:long          -1.6;
        gn:name          "Île Nouvelle";
        gn:population    0 .

<https://sws.geonames.org/8293375/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Lire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293375;
        gn:lat           47.34237;
        gn:long          -1.16414;
        gn:name          "Bureau de Poste de Lire";
        gn:population    0 .

<https://sws.geonames.org/3010062/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chebuette";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010062;
        gn:lat           47.26726;
        gn:long          -1.40751;
        gn:name          "La Chebuette";
        gn:population    0 .

<https://sws.geonames.org/10111591/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau De La Tremblaye";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10111591;
        gn:lat           47.02268;
        gn:long          -0.90162;
        gn:name          "Chateau De La Tremblaye";
        gn:population    0 .

<https://sws.geonames.org/2970382/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2970382;
        gn:lat           47.46536;
        gn:long          -1.48083;
        gn:name          "Vaux";
        gn:population    0 .

<https://sws.geonames.org/12313111/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fevrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313111;
        gn:lat           47.1408;
        gn:long          -1.38263;
        gn:name          "La Févrie";
        gn:population    0 .

<https://sws.geonames.org/12312912/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Meilleraie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312912;
        gn:lat           47.53305;
        gn:long          -1.34094;
        gn:name          "La Meilleraie";
        gn:population    0 .

<https://sws.geonames.org/8293002/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Herblain Principal";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293002;
        gn:lat           47.2183;
        gn:long          -1.61384;
        gn:name          "Bureau de Poste de Saint Herblain Principal";
        gn:population    0 .

<https://sws.geonames.org/8292916/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Bouguenais Principal";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292916;
        gn:lat           47.17933;
        gn:long          -1.62062;
        gn:name          "Bureau de Poste de Bouguenais Principal";
        gn:population    0 .

<https://sws.geonames.org/12313220/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fontaine Aux Bretons";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313220;
        gn:lat           47.10429;
        gn:long          -2.06611;
        gn:name          "La Fontaine Aux Bretons";
        gn:population    0 .

<https://sws.geonames.org/2971706/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois du Triage";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2971706;
        gn:lat           47.51297;
        gn:long          -1.15071;
        gn:name          "Bois du Triage";
        gn:population    0 .

<https://sws.geonames.org/3008596/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Jaunais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008596;
        gn:lat           47.5949;
        gn:long          -1.72509;
        gn:name          "La Jaunais";
        gn:population    0 .

<https://sws.geonames.org/3008172/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Menardais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008172;
        gn:lat           47.30786;
        gn:long          -1.61821;
        gn:name          "La Menardais";
        gn:population    0 .

<https://sws.geonames.org/12310601/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Antieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310601;
        gn:lat           47.06571;
        gn:long          -1.24486;
        gn:name          "Antières";
        gn:population    0 .

<https://sws.geonames.org/8293041/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Zola";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293041;
        gn:lat           47.21411;
        gn:long          -1.58745;
        gn:name          "Bureau de Poste de Nantes Zola";
        gn:population    0 .

<https://sws.geonames.org/12312985/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Touche Robin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312985;
        gn:lat           47.53434;
        gn:long          -1.96447;
        gn:name          "La Touche Robin";
        gn:population    0 .

<https://sws.geonames.org/6449110/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lavau-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449110;
        gn:lat           47.30694;
        gn:long          -1.96694;
        gn:name          "Lavau-sur-Loire";
        gn:population    766 .

<https://sws.geonames.org/12313225/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Goheliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313225;
        gn:lat           47.11378;
        gn:long          -2.08731;
        gn:name          "La Gohelière";
        gn:population    0 .

<https://sws.geonames.org/8292980/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Le Pallet";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292980;
        gn:lat           47.138;
        gn:long          -1.33785;
        gn:name          "Bureau de Poste de Le Pallet";
        gn:population    0 .

<https://sws.geonames.org/3008866/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Guay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008866;
        gn:lat           47.32476;
        gn:long          -1.83547;
        gn:name          "La Guay";
        gn:population    0 .

<https://sws.geonames.org/10117601/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Du Beryl Standing Sea View 14Km From Saint-Nazaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10117601;
        gn:lat           47.22922;
        gn:long          -2.17609;
        gn:name          "Du Beryl Standing Sea View 14Km From Saint-Nazaire";
        gn:population    0 .

<https://sws.geonames.org/6451590/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bazoges-en-Paillers";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6451590;
        gn:lat           46.90722;
        gn:long          -1.13417;
        gn:name          "Bazoges-en-Paillers";
        gn:population    1393 .

<https://sws.geonames.org/2980393/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Emilien";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980393;
        gn:lat           47.43369;
        gn:long          -1.71036;
        gn:name          "Saint-Emilien";
        gn:population    0 .

<https://sws.geonames.org/6476171/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mercure Gd Htl Nantes Ctre 4";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6476171;
        gn:lat           47.214;
        gn:long          -1.557;
        gn:name          "Mercure Gd Htl Nantes Ctre 4";
        gn:population    0 .

<https://sws.geonames.org/6612545/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montbert";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6612545;
        gn:lat           47.05778;
        gn:long          -1.48889;
        gn:name          "Montbert";
        gn:population    3097 .

<https://sws.geonames.org/2997471/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Ouche-Mouchand";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2997471;
        gn:lat           46.97395;
        gn:long          -2.02852;
        gn:name          "L'Ouche-Mouchand";
        gn:population    0 .

<https://sws.geonames.org/3025627/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cheix-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3025627;
        gn:lat           47.18197;
        gn:long          -1.8139;
        gn:name          "Cheix-en-Retz";
        gn:population    573 .

<https://sws.geonames.org/8293058/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Tharon Plage";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293058;
        gn:lat           47.16486;
        gn:long          -2.16411;
        gn:name          "Bureau de Poste de Tharon Plage";
        gn:population    0 .

<https://sws.geonames.org/12305891/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Croix Moriceau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305891;
        gn:lat           47.15741;
        gn:long          -1.38229;
        gn:name          "La Croix Moriceau";
        gn:population    0 .

<https://sws.geonames.org/3002623/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pointeau";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    3002623;
        gn:lat           47.23291;
        gn:long          -2.18155;
        gn:name          "Le Pointeau";
        gn:population    0 .

<https://sws.geonames.org/10297845/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brit Hotel Belfort";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297845;
        gn:lat           47.21123;
        gn:long          -1.54459;
        gn:name          "Brit Hotel Belfort";
        gn:population    0 .

<https://sws.geonames.org/12313175/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Epinais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313175;
        gn:lat           47.13631;
        gn:long          -1.6076;
        gn:name          "Les Épinais";
        gn:population    0 .

<https://sws.geonames.org/3009688/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Culiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009688;
        gn:lat           47.46655;
        gn:long          -1.33809;
        gn:name          "La Culière";
        gn:population    0 .

<https://sws.geonames.org/3031313/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031313;
        gn:lat           47.32023;
        gn:long          -1.91014;
        gn:name          "Bouée";
        gn:population    713 .

<https://sws.geonames.org/6449101/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Guenrouet";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449101;
        gn:lat           47.51917;
        gn:long          -1.95528;
        gn:name          "Guenrouet";
        gn:population    3335 .

<https://sws.geonames.org/6449095/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Fegreac";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449095;
        gn:lat           47.58472;
        gn:long          -2.04444;
        gn:name          "Fégréac";
        gn:population    2447 .

<https://sws.geonames.org/8436222/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ponts de Thouare";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436222;
        gn:lat           47.25785;
        gn:long          -1.42784;
        gn:name          "Ponts de Thouaré";
        gn:population    0 .

<https://sws.geonames.org/12123740/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Musee de l'imprimerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.MUS;
        gn:geonamesID    12123740;
        gn:lat           47.21085;
        gn:long          -1.56211;
        gn:name          "Musée de l'imprimerie";
        gn:population    0 .

<https://sws.geonames.org/11906049/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Parc du Crapa";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.PRK;
        gn:geonamesID    11906049;
        gn:lat           47.21252;
        gn:long          -1.52012;
        gn:name          "Parc du Crapa";
        gn:population    0 .

<https://sws.geonames.org/2983242/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rochementru";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2983242;
        gn:lat           47.56808;
        gn:long          -1.11692;
        gn:name          "Rochementru";
        gn:population    0 .

<https://sws.geonames.org/6449080/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Casson";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449080;
        gn:lat           47.38583;
        gn:long          -1.55944;
        gn:name          "Casson";
        gn:population    2217 .

<https://sws.geonames.org/8292995/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saffre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292995;
        gn:lat           47.50152;
        gn:long          -1.57822;
        gn:name          "Bureau de Poste de Saffre";
        gn:population    0 .

<https://sws.geonames.org/12305809/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Pere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305809;
        gn:lat           47.00833;
        gn:long          -1.2057;
        gn:name          "Saint-Père";
        gn:population    0 .

<https://sws.geonames.org/6434487/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Orvault";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434487;
        gn:lat           47.27083;
        gn:long          -1.62361;
        gn:name          "Orvault";
        gn:population    25931 .

<https://sws.geonames.org/12313103/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Martin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313103;
        gn:lat           47.19041;
        gn:long          -1.4226;
        gn:name          "Saint-Martin";
        gn:population    0 .

<https://sws.geonames.org/6456908/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Divatte-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456908;
        gn:lat           47.27167;
        gn:long          -1.33806;
        gn:name          "Divatte-sur-Loire";
        gn:population    6713 .

<https://sws.geonames.org/3031268/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouguenais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031268;
        gn:lat           47.17941;
        gn:long          -1.62468;
        gn:name          "Bouguenais";
        gn:population    16824 .

<https://sws.geonames.org/6456091/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Seguiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456091;
        gn:lat           47.06306;
        gn:long          -0.93972;
        gn:name          "La Séguinière";
        gn:population    4092 .

<https://sws.geonames.org/3009114/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Geraudais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009114;
        gn:lat           47.41405;
        gn:long          -2.06143;
        gn:name          "La Géraudais";
        gn:population    0 .

<https://sws.geonames.org/6489822/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Beautour";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6489822;
        gn:lat           47.18202;
        gn:long          -1.51408;
        gn:name          "Hotel Beautour";
        gn:population    0 .

<https://sws.geonames.org/12310640/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Dragonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310640;
        gn:lat           46.92828;
        gn:long          -1.2402;
        gn:name          "La Dragonnière";
        gn:population    0 .

<https://sws.geonames.org/6497396/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel & Casino Le Beryl";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6497396;
        gn:lat           47.2291;
        gn:long          -2.1758;
        gn:name          "Hôtel & Casino Le Béryl";
        gn:population    0 .

<https://sws.geonames.org/10344045/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appartcity Nantes Quai de Loir";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10344045;
        gn:lat           47.20939;
        gn:long          -1.56803;
        gn:name          "Appartcity Nantes Quai de Loir";
        gn:population    0 .

<https://sws.geonames.org/3233606/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roches de Vila";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233606;
        gn:lat           47.25889;
        gn:long          -2.17278;
        gn:name          "Roches de Vila";
        gn:population    0 .

<https://sws.geonames.org/12313016/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Clas";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313016;
        gn:lat           47.39736;
        gn:long          -2.01396;
        gn:name          "Clas";
        gn:population    0 .

<https://sws.geonames.org/12308486/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Croix des Victoires";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308486;
        gn:lat           47.28232;
        gn:long          -1.13185;
        gn:name          "La Croix des Victoires";
        gn:population    0 .

<https://sws.geonames.org/2995089/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Maumusson";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2995089;
        gn:lat           47.48214;
        gn:long          -1.10559;
        gn:name          "Maumusson";
        gn:population    874 .

<https://sws.geonames.org/12308505/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Villeneuve";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308505;
        gn:lat           47.22476;
        gn:long          -1.05817;
        gn:name          "Villeneuve";
        gn:population    0 .

<https://sws.geonames.org/3007661/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Languin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007661;
        gn:lat           47.45726;
        gn:long          -1.53988;
        gn:name          "Languin";
        gn:population    0 .

<https://sws.geonames.org/2975192/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sem";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2975192;
        gn:lat           47.3569;
        gn:long          -2.02702;
        gn:name          "Sem";
        gn:population    0 .

<https://sws.geonames.org/3009044/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gouairie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009044;
        gn:lat           47.35321;
        gn:long          -1.9125;
        gn:name          "La Gouairie";
        gn:population    0 .

<https://sws.geonames.org/8436195/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont de Saint-Nazaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436195;
        gn:lat           47.27477;
        gn:long          -2.16383;
        gn:name          "Pont de Saint-Nazaire";
        gn:population    0 .

<https://sws.geonames.org/3015229/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grande Crume";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3015229;
        gn:lat           47.01797;
        gn:long          -1.11536;
        gn:name          "Grande Crûme";
        gn:population    0 .

<https://sws.geonames.org/6445224/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Philbert-de-Bouaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6445224;
        gn:lat           46.98528;
        gn:long          -1.52083;
        gn:name          "Saint-Philbert-de-Bouaine";
        gn:population    3375 .

<https://sws.geonames.org/8292933/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Pornic La Birochere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292933;
        gn:lat           47.10992;
        gn:long          -2.0902;
        gn:name          "Bureau de Poste de Pornic La Birochere";
        gn:population    0 .

<https://sws.geonames.org/12312893/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grande Haie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312893;
        gn:lat           47.57494;
        gn:long          -1.28109;
        gn:name          "La Grande Haie";
        gn:population    0 .

<https://sws.geonames.org/6458672/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Varenne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6458672;
        gn:lat           47.31278;
        gn:long          -1.32194;
        gn:name          "La Varenne";
        gn:population    1719 .

<https://sws.geonames.org/12313002/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Madeleine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313002;
        gn:lat           47.58057;
        gn:long          -2.04548;
        gn:name          "La Madeleine";
        gn:population    0 .

<https://sws.geonames.org/3003807/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Haut Luc";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003807;
        gn:lat           47.5539;
        gn:long          -1.75076;
        gn:name          "Le Haut Luc";
        gn:population    0 .

<https://sws.geonames.org/8292983/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Plaine Sur Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292983;
        gn:lat           47.13788;
        gn:long          -2.19089;
        gn:name          "Bureau de Poste de La Plaine Sur Mer";
        gn:population    0 .

<https://sws.geonames.org/2977826/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Ouen";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977826;
        gn:lat           47.50274;
        gn:long          -1.29214;
        gn:name          "Saint-Ouen";
        gn:population    0 .

<https://sws.geonames.org/3006986/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Renaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006986;
        gn:lat           47.12012;
        gn:long          -1.05869;
        gn:name          "La Renaudière";
        gn:population    836 .

<https://sws.geonames.org/12313118/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Hauts Mortiers";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313118;
        gn:lat           47.10096;
        gn:long          -1.34602;
        gn:name          "Les Hauts Mortiers";
        gn:population    0 .

<https://sws.geonames.org/10125021/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quality Hotel Et Suites Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10125021;
        gn:lat           47.25369;
        gn:long          -1.51355;
        gn:name          "Quality Hotel Et Suites Nantes";
        gn:population    0 .

<https://sws.geonames.org/6616809/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grandchamp-des-Fontaines";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616809;
        gn:lat           47.3652;
        gn:long          -1.6048;
        gn:name          "Grandchamp-des-Fontaines";
        gn:population    5841 .

<https://sws.geonames.org/6451593/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beauvoir-sur-Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6451593;
        gn:lat           46.91611;
        gn:long          -2.04278;
        gn:name          "Beauvoir-sur-Mer";
        gn:population    3925 .

<https://sws.geonames.org/3233612/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Tourteau";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233612;
        gn:lat           47.28889;
        gn:long          -2.17806;
        gn:name          "Le Grand Tourteau";
        gn:population    0 .

<https://sws.geonames.org/2985854/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pouille-les-Coteaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2985854;
        gn:lat           47.45587;
        gn:long          -1.16226;
        gn:name          "Pouillé-les-Côteaux";
        gn:population    761 .

<https://sws.geonames.org/3005684/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Verdiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005684;
        gn:lat           47.41096;
        gn:long          -1.60845;
        gn:name          "La Verdinière";
        gn:population    0 .

<https://sws.geonames.org/6434532/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Michel-Chef-Chef";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434532;
        gn:lat           47.18083;
        gn:long          -2.14861;
        gn:name          "Saint-Michel-Chef-Chef";
        gn:population    4813 .

<https://sws.geonames.org/8292989/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Port St Pere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292989;
        gn:lat           47.13454;
        gn:long          -1.74736;
        gn:name          "Bureau de Poste de Port St Pere";
        gn:population    0 .

<https://sws.geonames.org/12310655/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Belletiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310655;
        gn:lat           46.90695;
        gn:long          -1.04133;
        gn:name          "La Belletière";
        gn:population    0 .

<https://sws.geonames.org/3038799/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaretz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3038799;
        gn:lat           47.55254;
        gn:long          -1.53301;
        gn:name          "Abbaretz";
        gn:population    1627 .

<https://sws.geonames.org/3007161/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Poutiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007161;
        gn:lat           47.00333;
        gn:long          -1.1389;
        gn:name          "La Poutière";
        gn:population    0 .

<https://sws.geonames.org/2977280/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Quentin-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977280;
        gn:lat           47.2913;
        gn:long          -0.91191;
        gn:name          "Saint-Quentin-en-Mauges";
        gn:population    1047 .

<https://sws.geonames.org/3008169/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Menie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008169;
        gn:lat           46.96072;
        gn:long          -0.93631;
        gn:name          "La Ménie";
        gn:population    0 .

<https://sws.geonames.org/2990085/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nort-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2990085;
        gn:lat           47.4399;
        gn:long          -1.49909;
        gn:name          "Nort-sur-Erdre";
        gn:population    6461 .

<https://sws.geonames.org/12718932/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaye Notre-Dame";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSTS;
        gn:geonamesID    12718932;
        gn:lat           46.93301;
        gn:long          -1.90895;
        gn:name          "Abbaye Notre-Dame";
        gn:population    0 .

<https://sws.geonames.org/3033108/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Besne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3033108;
        gn:lat           47.39738;
        gn:long          -2.09137;
        gn:name          "Besné";
        gn:population    2212 .

<https://sws.geonames.org/12305895/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Hautiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305895;
        gn:lat           47.13909;
        gn:long          -1.39563;
        gn:name          "La Hautière";
        gn:population    0 .

<https://sws.geonames.org/3019268/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Evre";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3019268;
        gn:lat           47.36337;
        gn:long          -1.03315;
        gn:name          "Evre";
        gn:population    0 .

<https://sws.geonames.org/2986106/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont-Saint-Martin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2986106;
        gn:lat           47.12421;
        gn:long          -1.58476;
        gn:name          "Pont-Saint-Martin";
        gn:population    5114 .

<https://sws.geonames.org/6445194/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Georges-de-Montaigu";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6445194;
        gn:lat           46.94694;
        gn:long          -1.29472;
        gn:name          "Saint-Georges-de-Montaigu";
        gn:population    3805 .

<https://sws.geonames.org/2992624/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montfaucon-Montigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2992624;
        gn:lat           47.1;
        gn:long          -1.11667;
        gn:name          "Montfaucon-Montigné";
        gn:population    1756 .

<https://sws.geonames.org/8292952/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Haye Fouassiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292952;
        gn:lat           47.15631;
        gn:long          -1.39955;
        gn:name          "Bureau de Poste de La Haye Fouassiere";
        gn:population    0 .

<https://sws.geonames.org/3012783/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ingrandes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3012783;
        gn:lat           47.4051;
        gn:long          -0.92275;
        gn:name          "Ingrandes";
        gn:population    1503 .

<https://sws.geonames.org/8292906/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Ancenis";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292906;
        gn:lat           47.36597;
        gn:long          -1.1787;
        gn:name          "Bureau de Poste de Ancenis";
        gn:population    0 .

<https://sws.geonames.org/2983245/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roche-Maurice";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2983245;
        gn:lat           47.2;
        gn:long          -1.61667;
        gn:name          "Roche-Maurice";
        gn:population    0 .

<https://sws.geonames.org/6506044/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mercure Nantes Gare Sud 3";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6506044;
        gn:lat           47.21572;
        gn:long          -1.54284;
        gn:name          "Mercure Nantes Gare Sud 3";
        gn:population    0 .

<https://sws.geonames.org/3017259/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Freigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3017259;
        gn:lat           47.54858;
        gn:long          -1.12274;
        gn:name          "Freigné";
        gn:population    1045 .

<https://sws.geonames.org/3031403/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouaye";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031403;
        gn:lat           47.14343;
        gn:long          -1.68902;
        gn:name          "Bouaye";
        gn:population    5673 .

<https://sws.geonames.org/2976853/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sulpice-des-Landes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2976853;
        gn:lat           47.57595;
        gn:long          -1.20678;
        gn:name          "Saint-Sulpice-des-Landes";
        gn:population    651 .

<https://sws.geonames.org/8292923/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Chapelle Basse Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292923;
        gn:lat           47.27299;
        gn:long          -1.33589;
        gn:name          "Bureau de Poste de La Chapelle Basse Mer";
        gn:population    0 .

<https://sws.geonames.org/3024648/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Clermont";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSEC;
        gn:geonamesID    3024648;
        gn:lat           47.32621;
        gn:long          -1.33422;
        gn:name          "Clermont";
        gn:population    0 .

<https://sws.geonames.org/8286946/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "St-Gildas-des-Bois Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286946;
        gn:lat           47.5164;
        gn:long          -2.04405;
        gn:name          "St-Gildas-des-Bois Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8411058/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Sicaudais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    8411058;
        gn:lat           47.18715;
        gn:long          -1.94724;
        gn:name          "La Sicaudais";
        gn:population    0 .

<https://sws.geonames.org/6508831/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ibis Nantes Treillieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6508831;
        gn:lat           47.3303;
        gn:long          -1.6256;
        gn:name          "Ibis Nantes Treillieres";
        gn:population    0 .

<https://sws.geonames.org/8293048/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Jules Verne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293048;
        gn:lat           47.248;
        gn:long          -1.52196;
        gn:name          "Bureau de Poste de Nantes Jules Verne";
        gn:population    0 .

<https://sws.geonames.org/2990057/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Notre-Dame-de-Grace";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2990057;
        gn:lat           47.48738;
        gn:long          -1.9275;
        gn:name          "Notre-Dame-de-Grâce";
        gn:population    0 .

<https://sws.geonames.org/3008490/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Aleu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008490;
        gn:lat           47.36881;
        gn:long          -0.95027;
        gn:name          "L'Aleu";
        gn:population    0 .

<https://sws.geonames.org/12310647/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pontreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310647;
        gn:lat           46.90786;
        gn:long          -2.04928;
        gn:name          "Le Pontreau";
        gn:population    0 .

<https://sws.geonames.org/3233403/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chenal de la Pierre";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CHN;
        gn:geonamesID    3233403;
        gn:lat           47.08021;
        gn:long          -2.14209;
        gn:name          "Chenal de la Pierre";
        gn:population    0 .

<https://sws.geonames.org/8286982/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Pazanne Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286982;
        gn:lat           47.10508;
        gn:long          -1.81431;
        gn:name          "Sainte-Pazanne Railway Station";
        gn:population    0 .

<https://sws.geonames.org/2972696/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Thouare-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2972696;
        gn:lat           47.26957;
        gn:long          -1.44354;
        gn:name          "Thouaré-sur-Loire";
        gn:population    7172 .

<https://sws.geonames.org/3233441/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Rochelets";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233441;
        gn:lat           47.21771;
        gn:long          -2.15833;
        gn:name          "Les Rochelets";
        gn:population    0 .

<https://sws.geonames.org/8293033/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Trignac";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293033;
        gn:lat           47.31759;
        gn:long          -2.18847;
        gn:name          "Bureau de Poste de Trignac";
        gn:population    0 .

<https://sws.geonames.org/3005132/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Boulay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005132;
        gn:lat           47.43159;
        gn:long          -1.33258;
        gn:name          "Le Boulay";
        gn:population    0 .

<https://sws.geonames.org/6456076/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Mesnil-en-Vallee";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456076;
        gn:lat           47.36583;
        gn:long          -0.93556;
        gn:name          "Le Mesnil-en-Vallée";
        gn:population    1463 .

<https://sws.geonames.org/12305900/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Viais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305900;
        gn:lat           47.11939;
        gn:long          -1.53771;
        gn:name          "Viais";
        gn:population    0 .

<https://sws.geonames.org/3233446/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile Saint-Nicolas";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3233446;
        gn:lat           47.28008;
        gn:long          -2.10778;
        gn:name          "Île Saint-Nicolas";
        gn:population    0 .

<https://sws.geonames.org/8436212/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Willy-Brandt";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436212;
        gn:lat           47.21165;
        gn:long          -1.5359;
        gn:name          "Pont Willy-Brandt";
        gn:population    0 .

<https://sws.geonames.org/8293053/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Rollin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293053;
        gn:lat           47.20896;
        gn:long          -1.57473;
        gn:name          "Bureau de Poste de Nantes Rollin";
        gn:population    0 .

<https://sws.geonames.org/8436217/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Georges-Clemenceau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436217;
        gn:lat           47.20168;
        gn:long          -1.53517;
        gn:name          "Pont Georges-Clemenceau";
        gn:population    0 .

<https://sws.geonames.org/13494801/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau de Pornic";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.CSTL;
        gn:geonamesID    13494801;
        gn:lat           47.1139;
        gn:long          -2.10561;
        gn:name          "Château de Pornic";
        gn:population    0 .

<https://sws.geonames.org/2991495/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mouline";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2991495;
        gn:lat           47.32178;
        gn:long          -1.54952;
        gn:name          "Mouline";
        gn:population    0 .

<https://sws.geonames.org/6456086/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Puiset-Dore";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456086;
        gn:lat           47.23222;
        gn:long          -1.11556;
        gn:name          "Le Puiset-Doré";
        gn:population    1120 .

<https://sws.geonames.org/3032062/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois-de-Cene";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3032062;
        gn:lat           46.93769;
        gn:long          -1.8861;
        gn:name          "Bois-de-Céné";
        gn:population    1364 .

<https://sws.geonames.org/12310600/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Fradet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310600;
        gn:lat           47.0669;
        gn:long          -1.24064;
        gn:name          "Fradet";
        gn:population    0 .

<https://sws.geonames.org/12313227/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Mousseaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313227;
        gn:lat           47.11655;
        gn:long          -2.11322;
        gn:name          "Les Mousseaux";
        gn:population    0 .

<https://sws.geonames.org/3005751/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile de Lavau";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3005751;
        gn:lat           47.30047;
        gn:long          -1.95559;
        gn:name          "Île de Lavau";
        gn:population    0 .

<https://sws.geonames.org/10154841/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Citea Residentiel Nantes La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10154841;
        gn:lat           47.26034;
        gn:long          -1.49657;
        gn:name          "Citea Residentiel Nantes La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/3233921/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile Chevalier";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISLX;
        gn:geonamesID    3233921;
        gn:lat           47.30445;
        gn:long          -1.99964;
        gn:name          "Île Chevalier";
        gn:population    0 .

<https://sws.geonames.org/6454152/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plesse";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6454152;
        gn:lat           47.54167;
        gn:long          -1.88694;
        gn:name          "Plessé";
        gn:population    5241 .

<https://sws.geonames.org/6434539/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Reine-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434539;
        gn:lat           47.44056;
        gn:long          -2.19389;
        gn:name          "Sainte-Reine-de-Bretagne";
        gn:population    2353 .

<https://sws.geonames.org/9173051/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Best Western  Plus Le Colisee Hotel & Spa";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173051;
        gn:lat           47.23412;
        gn:long          -1.65368;
        gn:name          "Best Western  Plus Le Colisee Hotel & Spa";
        gn:population    0 .

<https://sws.geonames.org/6455117/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campbon";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6455117;
        gn:lat           47.41194;
        gn:long          -1.96861;
        gn:name          "Campbon";
        gn:population    4018 .

<https://sws.geonames.org/3018781/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Fegreac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3018781;
        gn:lat           47.58464;
        gn:long          -2.04458;
        gn:name          "Fégréac";
        gn:population    2156 .

<https://sws.geonames.org/3030718/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouvron";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3030718;
        gn:lat           47.41774;
        gn:long          -1.84938;
        gn:name          "Bouvron";
        gn:population    2618 .

<https://sws.geonames.org/3002625/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Point du Jour";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002625;
        gn:lat           47.35488;
        gn:long          -1.88678;
        gn:name          "Le Point du Jour";
        gn:population    0 .

<https://sws.geonames.org/6434529/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Mars-de-Coutais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434529;
        gn:lat           47.1125;
        gn:long          -1.73583;
        gn:name          "Saint-Mars-de-Coutais";
        gn:population    2630 .

<https://sws.geonames.org/12358518/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaye de Sainte-Radegonde";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSTS;
        gn:geonamesID    12358518;
        gn:lat           47.2598;
        gn:long          -1.27483;
        gn:name          "Abbaye de Sainte-Radegonde";
        gn:population    0 .

<https://sws.geonames.org/3023324/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Coueron";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3023324;
        gn:lat           47.21473;
        gn:long          -1.72452;
        gn:name          "Couëron";
        gn:population    19466 .

<https://sws.geonames.org/6616815/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Corcoue-sur-Logne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616815;
        gn:lat           46.9656;
        gn:long          -1.576;
        gn:name          "Corcoué-sur-Logne";
        gn:population    2873 .

<https://sws.geonames.org/12313197/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Pele";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313197;
        gn:lat           47.15694;
        gn:long          -1.73547;
        gn:name          "Le Grand Pêle";
        gn:population    0 .

<https://sws.geonames.org/3019929/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3019929;
        gn:lat           47.21223;
        gn:long          -1.53984;
        gn:name          "Erdre";
        gn:population    0 .

<https://sws.geonames.org/6493474/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appart'city Nantes Chateau des Ducs";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6493474;
        gn:lat           47.2144;
        gn:long          -1.546;
        gn:name          "Appart'city Nantes Château des Ducs";
        gn:population    0 .

<https://sws.geonames.org/3009987/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Coindassiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009987;
        gn:lat           47.32786;
        gn:long          -1.28893;
        gn:name          "La Coindassière";
        gn:population    0 .

<https://sws.geonames.org/12313125/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Riviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313125;
        gn:lat           47.21437;
        gn:long          -1.4759;
        gn:name          "La Rivière";
        gn:population    0 .

<https://sws.geonames.org/3008117/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Moissonnaie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008117;
        gn:lat           47.31667;
        gn:long          -1.81667;
        gn:name          "La Moissonnaie";
        gn:population    0 .

<https://sws.geonames.org/12305903/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Croix Jeannette";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305903;
        gn:lat           47.17262;
        gn:long          -1.62421;
        gn:name          "La Croix Jeannette";
        gn:population    0 .

<https://sws.geonames.org/12313018/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Menais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313018;
        gn:lat           47.40783;
        gn:long          -2.0402;
        gn:name          "La Menais";
        gn:population    0 .

<https://sws.geonames.org/12313033/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bellevue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313033;
        gn:lat           47.30674;
        gn:long          -2.17975;
        gn:name          "Bellevue";
        gn:population    0 .

<https://sws.geonames.org/2994838/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile de Mazin";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    2994838;
        gn:lat           47.39381;
        gn:long          -2.19631;
        gn:name          "Île de Mazin";
        gn:population    0 .

<https://sws.geonames.org/8297412/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de L Herbergement";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297412;
        gn:lat           46.91006;
        gn:long          -1.37589;
        gn:name          "Bureau de Poste de L Herbergement";
        gn:population    0 .

<https://sws.geonames.org/2978057/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Meme-le-Tenu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978057;
        gn:lat           47.02089;
        gn:long          -1.79409;
        gn:name          "Saint-Même-le-Tenu";
        gn:population    1138 .

<https://sws.geonames.org/2987712/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Petite Menuere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2987712;
        gn:lat           47.38333;
        gn:long          -1.01667;
        gn:name          "Petite Menuère";
        gn:population    0 .

<https://sws.geonames.org/12312898/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mondaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312898;
        gn:lat           47.41875;
        gn:long          -1.18925;
        gn:name          "La Mondaire";
        gn:population    0 .

<https://sws.geonames.org/2976678/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Viaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2976678;
        gn:lat           47.25626;
        gn:long          -2.01859;
        gn:name          "Saint-Viaud";
        gn:population    1992 .

<https://sws.geonames.org/2978669/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Lumine-de-Coutais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978669;
        gn:lat           47.05471;
        gn:long          -1.7269;
        gn:name          "Saint-Lumine-de-Coutais";
        gn:population    1770 .

<https://sws.geonames.org/10342677/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Novotel Nantes Cite Des Congre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10342677;
        gn:lat           47.214;
        gn:long          -1.543;
        gn:name          "Novotel Nantes Cite Des Congre";
        gn:population    0 .

<https://sws.geonames.org/12313183/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Benate";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313183;
        gn:lat           46.95501;
        gn:long          -1.60494;
        gn:name          "La Bénate";
        gn:population    0 .

<https://sws.geonames.org/2979590/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Herblain";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979590;
        gn:lat           47.21154;
        gn:long          -1.651;
        gn:name          "Saint-Herblain";
        gn:population    46898 .

<https://sws.geonames.org/3233390/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chenal du Centre";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CHN;
        gn:geonamesID    3233390;
        gn:lat           47.04306;
        gn:long          -2.13333;
        gn:name          "Chenal du Centre";
        gn:population    0 .

<https://sws.geonames.org/6445246/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tiffauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6445246;
        gn:lat           47.01361;
        gn:long          -1.11139;
        gn:name          "Tiffauges";
        gn:population    1597 .

<https://sws.geonames.org/2996905/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Machecoul";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2996905;
        gn:lat           46.99336;
        gn:long          -1.82298;
        gn:name          "Machecoul";
        gn:population    6054 .

<https://sws.geonames.org/3005035/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bredeloup";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005035;
        gn:lat           47.39964;
        gn:long          -1.72881;
        gn:name          "Le Bredeloup";
        gn:population    0 .

<https://sws.geonames.org/8292913/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Le Bignon";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292913;
        gn:lat           47.09851;
        gn:long          -1.49075;
        gn:name          "Bureau de Poste de Le Bignon";
        gn:population    0 .

<https://sws.geonames.org/11876726/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.PRT;
        gn:geonamesID    11876726;
        gn:lat           47.19618;
        gn:long          -1.58904;
        gn:name          "Nantes";
        gn:population    0 .

<https://sws.geonames.org/3021310/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Divatte";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3021310;
        gn:lat           47.30095;
        gn:long          -1.34476;
        gn:name          "Divatte";
        gn:population    0 .

<https://sws.geonames.org/12313161/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ragon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313161;
        gn:lat           47.1667;
        gn:long          -1.54188;
        gn:name          "Ragon";
        gn:population    0 .

<https://sws.geonames.org/12313189/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Jariais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313189;
        gn:lat           47.21218;
        gn:long          -1.71648;
        gn:name          "La Jariais";
        gn:population    0 .

<https://sws.geonames.org/10173560/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nantes Est Saint SBastien Sur Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10173560;
        gn:lat           47.212;
        gn:long          -1.487;
        gn:name          "Nantes Est Saint SBastien Sur Loire";
        gn:population    0 .

<https://sws.geonames.org/12312918/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Richerais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312918;
        gn:lat           47.43442;
        gn:long          -1.30217;
        gn:name          "La Richerais";
        gn:population    0 .

<https://sws.geonames.org/12313024/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Savinais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313024;
        gn:lat           47.37548;
        gn:long          -2.06838;
        gn:name          "La Savinais";
        gn:population    0 .

<https://sws.geonames.org/3007568/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Noue Peguille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007568;
        gn:lat           47.47857;
        gn:long          -1.6194;
        gn:name          "La Noue Peguille";
        gn:population    0 .

<https://sws.geonames.org/3001340/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Coniers";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3001340;
        gn:lat           47.3726;
        gn:long          -1.08688;
        gn:name          "Les Coniers";
        gn:population    0 .

<https://sws.geonames.org/3026847/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gare de Chantenay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    3026847;
        gn:lat           47.2;
        gn:long          -1.61667;
        gn:name          "Gare de Chantenay";
        gn:population    0 .

<https://sws.geonames.org/12310607/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Poiron Badonneau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310607;
        gn:lat           47.03088;
        gn:long          -1.3214;
        gn:name          "Le Poiron Badonneau";
        gn:population    0 .

<https://sws.geonames.org/3010459/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chambre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010459;
        gn:lat           47.30845;
        gn:long          -1.5194;
        gn:name          "La Chambre";
        gn:population    0 .

<https://sws.geonames.org/12313097/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Malonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313097;
        gn:lat           47.22024;
        gn:long          -1.39595;
        gn:name          "La Malonnière";
        gn:population    0 .

<https://sws.geonames.org/3007004/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Regrippiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007004;
        gn:lat           47.1815;
        gn:long          -1.17636;
        gn:name          "La Regrippière";
        gn:population    1167 .

<https://sws.geonames.org/8297382/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Beauvoir Sur Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297382;
        gn:lat           46.91569;
        gn:long          -2.04368;
        gn:name          "Bureau de Poste de Beauvoir Sur Mer";
        gn:population    0 .

<https://sws.geonames.org/12313167/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Favet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313167;
        gn:lat           46.96017;
        gn:long          -1.57402;
        gn:name          "Favet";
        gn:population    0 .

<https://sws.geonames.org/6434554/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trignac";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434554;
        gn:lat           47.31806;
        gn:long          -2.18917;
        gn:name          "Trignac";
        gn:population    7871 .

<https://sws.geonames.org/12305730/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Plairie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305730;
        gn:lat           47.5386;
        gn:long          -1.01353;
        gn:name          "La Plairie";
        gn:population    0 .

<https://sws.geonames.org/3007204/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Pordais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007204;
        gn:lat           47.26738;
        gn:long          -2.00928;
        gn:name          "La Pordais";
        gn:population    0 .

<https://sws.geonames.org/6434483/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434483;
        gn:lat           47.21722;
        gn:long          -1.55389;
        gn:name          "Nantes";
        gn:population    306694 .

<https://sws.geonames.org/8293404/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Germain Sur Moine";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293404;
        gn:lat           47.11804;
        gn:long          -1.12476;
        gn:name          "Bureau de Poste de Saint Germain Sur Moine";
        gn:population    0 .

<https://sws.geonames.org/2973162/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tenu";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2973162;
        gn:lat           47.12598;
        gn:long          -1.72568;
        gn:name          "Tenu";
        gn:population    0 .

<https://sws.geonames.org/2978330/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Martin-des-Tilleuls";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978330;
        gn:lat           46.97382;
        gn:long          -1.05088;
        gn:name          "Saint-Martin-des-Tilleuls";
        gn:population    879 .

<https://sws.geonames.org/3010805/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bretonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010805;
        gn:lat           47.51747;
        gn:long          -1.68681;
        gn:name          "La Bretonnière";
        gn:population    0 .

<https://sws.geonames.org/3029918/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brossay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3029918;
        gn:lat           47.34702;
        gn:long          -1.93607;
        gn:name          "Brossay";
        gn:population    0 .

<https://sws.geonames.org/3010044/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chevallerais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010044;
        gn:lat           47.46798;
        gn:long          -1.6716;
        gn:name          "La Chevallerais";
        gn:population    704 .

<https://sws.geonames.org/3002082/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Sausais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002082;
        gn:lat           47.10349;
        gn:long          -1.25159;
        gn:name          "Le Sausais";
        gn:population    0 .

<https://sws.geonames.org/2986128/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Pietin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSEC;
        gn:geonamesID    2986128;
        gn:lat           47.46519;
        gn:long          -1.82479;
        gn:name          "Pont Piétin";
        gn:population    0 .

<https://sws.geonames.org/12313130/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gare";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313130;
        gn:lat           47.18697;
        gn:long          -1.47746;
        gn:name          "La Gare";
        gn:population    0 .

<https://sws.geonames.org/12312909/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Sablonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312909;
        gn:lat           47.56971;
        gn:long          -1.32789;
        gn:name          "La Sablonnière";
        gn:population    0 .

<https://sws.geonames.org/9224792/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inter-Hotel Grand Hotel De Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9224792;
        gn:lat           47.21262;
        gn:long          -1.56024;
        gn:name          "Inter-Hotel Grand Hotel De Nantes";
        gn:population    0 .

<https://sws.geonames.org/12312888/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mesliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312888;
        gn:lat           47.48811;
        gn:long          -1.17692;
        gn:name          "La Meslière";
        gn:population    0 .

<https://sws.geonames.org/6434540/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sebastien-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434540;
        gn:lat           47.20766;
        gn:long          -1.50337;
        gn:name          "Saint-Sébastien-sur-Loire";
        gn:population    26872 .

<https://sws.geonames.org/6456027/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Regrippiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456027;
        gn:lat           47.18167;
        gn:long          -1.17611;
        gn:name          "La Regrippière";
        gn:population    1525 .

<https://sws.geonames.org/12308354/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Availles";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308354;
        gn:lat           47.54861;
        gn:long          -0.90339;
        gn:name          "Les Availlés";
        gn:population    0 .

<https://sws.geonames.org/3011142/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Belinais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011142;
        gn:lat           47.44773;
        gn:long          -1.89487;
        gn:name          "La Belinais";
        gn:population    0 .

<https://sws.geonames.org/12313234/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Porteau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313234;
        gn:lat           47.11672;
        gn:long          -2.14876;
        gn:name          "Le Porteau";
        gn:population    0 .

<https://sws.geonames.org/12313073/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Courreres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313073;
        gn:lat           47.19545;
        gn:long          -1.24195;
        gn:name          "Les Courrères";
        gn:population    0 .

<https://sws.geonames.org/3233405/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Mauvaise";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.SHOL;
        gn:geonamesID    3233405;
        gn:lat           47.06722;
        gn:long          -2.09139;
        gn:name          "Le Mauvaise";
        gn:population    0 .

<https://sws.geonames.org/3233455/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Buzay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233455;
        gn:lat           47.20726;
        gn:long          -1.82631;
        gn:name          "Buzay";
        gn:population    0 .

<https://sws.geonames.org/3003977/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Merimont";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003977;
        gn:lat           47.36239;
        gn:long          -1.79154;
        gn:name          "Le Grand Merimont";
        gn:population    0 .

<https://sws.geonames.org/3023512/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Corsept";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3023512;
        gn:lat           47.27678;
        gn:long          -2.06062;
        gn:name          "Corsept";
        gn:population    2116 .

<https://sws.geonames.org/12313093/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Magasin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313093;
        gn:lat           47.11399;
        gn:long          -1.29256;
        gn:name          "Le Magasin";
        gn:population    0 .

<https://sws.geonames.org/6616805/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bignon";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616805;
        gn:lat           47.0988;
        gn:long          -1.4896;
        gn:name          "Le Bignon";
        gn:population    3718 .

<https://sws.geonames.org/12312879/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gautellerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312879;
        gn:lat           47.4305;
        gn:long          -1.05498;
        gn:name          "La Gautellerie";
        gn:population    0 .

<https://sws.geonames.org/12312988/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Oisilliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312988;
        gn:lat           47.35594;
        gn:long          -1.92772;
        gn:name          "L'Oisillière";
        gn:population    0 .

<https://sws.geonames.org/3035046/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Barbatre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3035046;
        gn:lat           46.94359;
        gn:long          -2.17981;
        gn:name          "Barbâtre";
        gn:population    1517 .

<https://sws.geonames.org/8436219/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont ferroviaire de Pirmil";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436219;
        gn:lat           47.19818;
        gn:long          -1.54972;
        gn:name          "Pont ferroviaire de Pirmil";
        gn:population    0 .

<https://sws.geonames.org/12313187/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Noe";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313187;
        gn:lat           47.19517;
        gn:long          -1.712;
        gn:name          "La Noë";
        gn:population    0 .

<https://sws.geonames.org/11073022/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe de Biochon";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    11073022;
        gn:lat           47.12224;
        gn:long          -2.19156;
        gn:name          "Pointe de Biochon";
        gn:population    0 .

<https://sws.geonames.org/6449113/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Machecoul-Saint-Meme";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449113;
        gn:lat           46.99306;
        gn:long          -1.82278;
        gn:name          "Machecoul-Saint-Même";
        gn:population    7393 .

<https://sws.geonames.org/3004204/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fosse-Neuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004204;
        gn:lat           47.35666;
        gn:long          -1.12035;
        gn:name          "Le Fossé-Neuf";
        gn:population    0 .

<https://sws.geonames.org/8286531/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sebastien Pas Enchantes Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286531;
        gn:lat           47.20699;
        gn:long          -1.51126;
        gn:name          "Saint-Sébastien Pas Enchantés Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3036679/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arthon-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3036679;
        gn:lat           47.11655;
        gn:long          -1.9392;
        gn:name          "Arthon-en-Retz";
        gn:population    2888 .

<https://sws.geonames.org/10297827/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Saint Patrick";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297827;
        gn:lat           47.21496;
        gn:long          -1.55748;
        gn:name          "Hôtel Saint Patrick";
        gn:population    0 .

<https://sws.geonames.org/6456911/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Heulin";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456911;
        gn:lat           47.17639;
        gn:long          -1.34056;
        gn:name          "La Chapelle-Heulin";
        gn:population    3265 .

<https://sws.geonames.org/3017373/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Franchaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3017373;
        gn:lat           47.50416;
        gn:long          -1.48024;
        gn:name          "Franchaud";
        gn:population    0 .

<https://sws.geonames.org/12312978/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rouillonnais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312978;
        gn:lat           47.26516;
        gn:long          -1.76368;
        gn:name          "La Rouillonnais";
        gn:population    0 .

<https://sws.geonames.org/12313206/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pont Beranger";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313206;
        gn:lat           47.1291;
        gn:long          -1.83241;
        gn:name          "Le Pont Béranger";
        gn:population    0 .

<https://sws.geonames.org/2998825/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Vieux-Bourg";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998825;
        gn:lat           47.58258;
        gn:long          -1.19233;
        gn:name          "Le Vieux-Bourg";
        gn:population    0 .

<https://sws.geonames.org/9173038/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Best Hotel Nantes   Graslin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173038;
        gn:lat           47.2122;
        gn:long          -1.56244;
        gn:name          "Best Hotel Nantes   Graslin";
        gn:population    0 .

<https://sws.geonames.org/3006894/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Riviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006894;
        gn:lat           47.50473;
        gn:long          -2.03191;
        gn:name          "La Rivière";
        gn:population    0 .

<https://sws.geonames.org/8293023/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Sautron";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293023;
        gn:lat           47.26121;
        gn:long          -1.66396;
        gn:name          "Bureau de Poste de Sautron";
        gn:population    0 .

<https://sws.geonames.org/3233502/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Rang";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233502;
        gn:lat           47.23974;
        gn:long          -2.18159;
        gn:name          "Le Grand Rang";
        gn:population    0 .

<https://sws.geonames.org/12310622/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bellevue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310622;
        gn:lat           46.96689;
        gn:long          -1.1155;
        gn:name          "Bellevue";
        gn:population    0 .

<https://sws.geonames.org/2984566/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ragon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2984566;
        gn:lat           47.28179;
        gn:long          -1.5981;
        gn:name          "Ragon";
        gn:population    0 .

<https://sws.geonames.org/11048613/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaye de Buzay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RUIN;
        gn:geonamesID    11048613;
        gn:lat           47.20731;
        gn:long          -1.82678;
        gn:name          "Abbaye de Buzay";
        gn:population    0 .

<https://sws.geonames.org/12312941/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Caherault";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312941;
        gn:lat           47.24255;
        gn:long          -1.41585;
        gn:name          "Cahérault";
        gn:population    0 .

<https://sws.geonames.org/8297389/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Bruffiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297389;
        gn:lat           47.0182;
        gn:long          -1.19972;
        gn:name          "Bureau de Poste de La Bruffiere";
        gn:population    0 .

<https://sws.geonames.org/6457158/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gaubretiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6457158;
        gn:lat           46.94333;
        gn:long          -1.06472;
        gn:name          "La Gaubretière";
        gn:population    3034 .

<https://sws.geonames.org/2999950/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Placieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999950;
        gn:lat           47.54791;
        gn:long          -1.54324;
        gn:name          "Les Placières";
        gn:population    0 .

<https://sws.geonames.org/8436225/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont suspendu d'Ancenis";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436225;
        gn:lat           47.36211;
        gn:long          -1.17659;
        gn:name          "Pont suspendu d'Ancenis";
        gn:population    0 .

<https://sws.geonames.org/12313133/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grammoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313133;
        gn:lat           47.18302;
        gn:long          -1.47141;
        gn:name          "La Grammoire";
        gn:population    0 .

<https://sws.geonames.org/2993819/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Banc de Mindin";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.BNK;
        gn:geonamesID    2993819;
        gn:lat           47.25819;
        gn:long          -2.19243;
        gn:name          "Banc de Mindin";
        gn:population    0 .

<https://sws.geonames.org/12313170/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beauregard";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313170;
        gn:lat           47.20876;
        gn:long          -1.6615;
        gn:name          "Beauregard";
        gn:population    0 .

<https://sws.geonames.org/2990038/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Notre-Dame-des-Langueurs";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2990038;
        gn:lat           47.51762;
        gn:long          -1.47488;
        gn:name          "Notre-Dame-des-Langueurs";
        gn:population    0 .

<https://sws.geonames.org/2977920/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arrondissement de Saint-Nazaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM3;
        gn:geonamesID    2977920;
        gn:lat           47.33846;
        gn:long          -2.12397;
        gn:name          "Arrondissement de Saint-Nazaire";
        gn:population    350369 .

<https://sws.geonames.org/7535059/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Golf Nantes Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RECG;
        gn:geonamesID    7535059;
        gn:lat           47.2618;
        gn:long          -1.582;
        gn:name          "Golf Nantes Erdre";
        gn:population    0 .

<https://sws.geonames.org/3001581/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Chabossieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3001581;
        gn:lat           47.17321;
        gn:long          -1.22155;
        gn:name          "Les Chabossières";
        gn:population    0 .

<https://sws.geonames.org/8293014/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Michel Chef Chef";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293014;
        gn:lat           47.18184;
        gn:long          -2.1519;
        gn:name          "Bureau de Poste de Saint Michel Chef Chef";
        gn:population    0 .

<https://sws.geonames.org/10118622/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Residence De L'ocean La Tranche Sur Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10118622;
        gn:lat           47.20252;
        gn:long          -1.54299;
        gn:name          "Residence De L'ocean La Tranche Sur Mer";
        gn:population    0 .

<https://sws.geonames.org/12310613/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pre Gestin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310613;
        gn:lat           47.00132;
        gn:long          -1.32616;
        gn:name          "Le Pré Gestin";
        gn:population    0 .

<https://sws.geonames.org/12313232/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Corbeliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313232;
        gn:lat           47.12526;
        gn:long          -2.13887;
        gn:name          "La Corbélière";
        gn:population    0 .

<https://sws.geonames.org/12313083/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gobiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313083;
        gn:lat           47.18383;
        gn:long          -1.31945;
        gn:name          "La Gobinière";
        gn:population    0 .

<https://sws.geonames.org/9173239/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Best Western Plus Hotel De La Regate";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173239;
        gn:lat           47.29344;
        gn:long          -1.52665;
        gn:name          "Best Western Plus Hotel De La Regate";
        gn:population    0 .

<https://sws.geonames.org/3233609/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Nez de Chien";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233609;
        gn:lat           47.26765;
        gn:long          -2.17115;
        gn:name          "Le Nez de Chien";
        gn:population    0 .

<https://sws.geonames.org/13192380/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Musee Jules-Verne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.MUS;
        gn:geonamesID    13192380;
        gn:lat           47.20177;
        gn:long          -1.57739;
        gn:name          "Musée Jules-Verne";
        gn:population    0 .

<https://sws.geonames.org/2977204/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Remy-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977204;
        gn:lat           47.27202;
        gn:long          -1.07499;
        gn:name          "Saint-Rémy-en-Mauges";
        gn:population    1298 .

<https://sws.geonames.org/3233408/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nor Sauvage";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233408;
        gn:lat           47.07639;
        gn:long          -2.075;
        gn:name          "Nor Sauvage";
        gn:population    0 .

<https://sws.geonames.org/12313127/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chevrue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313127;
        gn:lat           47.17881;
        gn:long          -1.43389;
        gn:name          "La Chevrue";
        gn:population    0 .

<https://sws.geonames.org/10277071/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes Ouest Rl";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10277071;
        gn:lat           47.22656;
        gn:long          -1.6301;
        gn:name          "Campanile Nantes Ouest Rl";
        gn:population    0 .

<https://sws.geonames.org/2976984/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sebastien-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2976984;
        gn:lat           47.20768;
        gn:long          -1.50332;
        gn:name          "Saint-Sébastien-sur-Loire";
        gn:population    29238 .

<https://sws.geonames.org/3000519/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Landes-Genusson";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000519;
        gn:lat           46.96378;
        gn:long          -1.1194;
        gn:name          "Les Landes-Genusson";
        gn:population    2138 .

<https://sws.geonames.org/12308562/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Vallee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308562;
        gn:lat           47.01655;
        gn:long          -1.10951;
        gn:name          "La Vallée";
        gn:population    0 .

<https://sws.geonames.org/3007143/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Preoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3007143;
        gn:lat           47.00234;
        gn:long          -2.13424;
        gn:name          "La Préoire";
        gn:population    0 .

<https://sws.geonames.org/6525608/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau De La Colaissiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6525608;
        gn:lat           47.287;
        gn:long          -1.256;
        gn:name          "Chateau De La Colaissiere";
        gn:population    0 .

<https://sws.geonames.org/9177444/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Kyriad Nantes Bouaye - Aeroport";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177444;
        gn:lat           47.14369;
        gn:long          -1.66071;
        gn:name          "Kyriad Nantes Bouaye - Aeroport";
        gn:population    0 .

<https://sws.geonames.org/11746347/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Carriere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.MNQ;
        gn:geonamesID    11746347;
        gn:lat           47.49253;
        gn:long          -1.46533;
        gn:name          "La Carrière";
        gn:population    0 .

<https://sws.geonames.org/2990968/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arrondissement de Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM3;
        gn:geonamesID    2990968;
        gn:lat           47.13934;
        gn:long          -1.56967;
        gn:name          "Arrondissement de Nantes";
        gn:population    888845 .

<https://sws.geonames.org/7535089/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Golf de l'Ile d'Or";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RECG;
        gn:geonamesID    7535089;
        gn:lat           47.32556;
        gn:long          -1.32222;
        gn:name          "Golf de l'Île d'Or";
        gn:population    0 .

<https://sws.geonames.org/8292964/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Mauves Sur Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292964;
        gn:lat           47.29758;
        gn:long          -1.39437;
        gn:name          "Bureau de Poste de Mauves Sur Loire";
        gn:population    0 .

<https://sws.geonames.org/6456914/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456914;
        gn:lat           47.29889;
        gn:long          -1.55278;
        gn:name          "La Chapelle-sur-Erdre";
        gn:population    19348 .

<https://sws.geonames.org/2986060/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pornic";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2986060;
        gn:lat           47.11581;
        gn:long          -2.10331;
        gn:name          "Pornic";
        gn:population    12897 .

<https://sws.geonames.org/12312911/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Croix Aux Camus";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312911;
        gn:lat           47.54867;
        gn:long          -1.36098;
        gn:name          "La Croix Aux Camus";
        gn:population    0 .

<https://sws.geonames.org/3006983/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Renouere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006983;
        gn:lat           47.19584;
        gn:long          -1.29048;
        gn:name          "La Renouère";
        gn:population    0 .

<https://sws.geonames.org/12313115/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bretonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313115;
        gn:lat           47.12309;
        gn:long          -1.4044;
        gn:name          "La Bretonnière";
        gn:population    0 .

<https://sws.geonames.org/8293040/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Geneston";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293040;
        gn:lat           47.05527;
        gn:long          -1.51558;
        gn:name          "Bureau de Poste de Geneston";
        gn:population    0 .

<https://sws.geonames.org/3037559/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chenal d'Anjoubert";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CHNM;
        gn:geonamesID    3037559;
        gn:lat           46.96632;
        gn:long          -2.17985;
        gn:name          "Chenal d'Anjoubert";
        gn:population    0 .

<https://sws.geonames.org/3004238/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fief-Sauvin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004238;
        gn:lat           47.22143;
        gn:long          -1.04214;
        gn:name          "Le Fief-Sauvin";
        gn:population    1407 .

<https://sws.geonames.org/12313224/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Pagotiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313224;
        gn:lat           47.11977;
        gn:long          -2.09696;
        gn:name          "La Pagotière";
        gn:population    0 .

<https://sws.geonames.org/8292935/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Cordemais";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292935;
        gn:lat           47.2918;
        gn:long          -1.87693;
        gn:name          "Bureau de Poste de Cordemais";
        gn:population    0 .

<https://sws.geonames.org/6434525/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Lumine-de-Clisson";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434525;
        gn:lat           47.08361;
        gn:long          -1.33694;
        gn:name          "Saint-Lumine-de-Clisson";
        gn:population    2109 .

<https://sws.geonames.org/9539751/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Residence Le Hameau Du Golf";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539751;
        gn:lat           47.11906;
        gn:long          -2.11719;
        gn:name          "Residence Le Hameau Du Golf";
        gn:population    0 .

<https://sws.geonames.org/6490216/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grand Hotel de Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6490216;
        gn:lat           47.21288;
        gn:long          -1.56002;
        gn:name          "Grand Hotel de Nantes";
        gn:population    0 .

<https://sws.geonames.org/12305898/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Neustrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305898;
        gn:lat           47.17587;
        gn:long          -1.59167;
        gn:name          "La Neustrie";
        gn:population    0 .

<https://sws.geonames.org/12308512/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Martin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308512;
        gn:lat           47.2029;
        gn:long          -0.9803;
        gn:name          "Saint-Martin";
        gn:population    0 .

<https://sws.geonames.org/3031808/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bon Garand";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031808;
        gn:lat           47.2806;
        gn:long          -1.6956;
        gn:name          "Bon Garand";
        gn:population    0 .

<https://sws.geonames.org/3002699/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Plessis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002699;
        gn:lat           47.43333;
        gn:long          -1.95;
        gn:name          "Le Plessis";
        gn:population    0 .

<https://sws.geonames.org/9539830/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cerise Nantes La Beaujoire (Residence Studinn)";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539830;
        gn:lat           47.25348;
        gn:long          -1.52881;
        gn:name          "Cerise Nantes La Beaujoire (Residence Studinn)";
        gn:population    0 .

<https://sws.geonames.org/8286994/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Clisson Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286994;
        gn:lat           47.08585;
        gn:long          -1.28675;
        gn:name          "Clisson Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8292955/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Heric";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292955;
        gn:lat           47.4166;
        gn:long          -1.65416;
        gn:name          "Bureau de Poste de Heric";
        gn:population    0 .

<https://sws.geonames.org/12310629/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Oncheres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310629;
        gn:lat           46.93268;
        gn:long          -2.17116;
        gn:name          "Les Onchères";
        gn:population    0 .

<https://sws.geonames.org/6612549/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Etienne-de-Mer-Morte";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6612549;
        gn:lat           46.92972;
        gn:long          -1.74278;
        gn:name          "Saint-Étienne-de-Mer-Morte";
        gn:population    1715 .

<https://sws.geonames.org/12313173/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roche Ballue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313173;
        gn:lat           47.18732;
        gn:long          -1.66751;
        gn:name          "Roche Ballue";
        gn:population    0 .

<https://sws.geonames.org/12308411/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fief Egare";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308411;
        gn:lat           47.40795;
        gn:long          -0.92689;
        gn:name          "Le Fief Égaré";
        gn:population    0 .

<https://sws.geonames.org/12312948/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Vallees";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312948;
        gn:lat           47.22743;
        gn:long          -1.46143;
        gn:name          "Les Vallées";
        gn:population    0 .

<https://sws.geonames.org/2993245/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Monnieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2993245;
        gn:lat           47.1319;
        gn:long          -1.35648;
        gn:name          "Monnières";
        gn:population    1659 .

<https://sws.geonames.org/2997872/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2997872;
        gn:lat           47.26952;
        gn:long          -2.18349;
        gn:name          "Loire";
        gn:population    0 .

<https://sws.geonames.org/8292945/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Frossay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292945;
        gn:lat           47.2433;
        gn:long          -1.93506;
        gn:name          "Bureau de Poste de Frossay";
        gn:population    0 .

<https://sws.geonames.org/6449100/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grand-Auverne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449100;
        gn:lat           47.59139;
        gn:long          -1.33056;
        gn:name          "Grand-Auverné";
        gn:population    772 .

<https://sws.geonames.org/12313179/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chaussee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313179;
        gn:lat           47.09938;
        gn:long          -1.61013;
        gn:name          "La Chaussée";
        gn:population    0 .

<https://sws.geonames.org/12313014/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Coisnongle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313014;
        gn:lat           47.46484;
        gn:long          -2.0176;
        gn:name          "Coisnongle";
        gn:population    0 .

<https://sws.geonames.org/6509061/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Novotel Nantes Carquefou";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6509061;
        gn:lat           47.2829;
        gn:long          -1.4539;
        gn:name          "Novotel Nantes Carquefou";
        gn:population    0 .

<https://sws.geonames.org/3002812/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3002812;
        gn:lat           47.35;
        gn:long          -2.16667;
        gn:name          "Le Pin";
        gn:population    649 .

<https://sws.geonames.org/2971899/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trelan";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2971899;
        gn:lat           47.5601;
        gn:long          -1.80714;
        gn:name          "Trelan";
        gn:population    0 .

<https://sws.geonames.org/12308503/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Dore";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308503;
        gn:lat           47.22816;
        gn:long          -1.18041;
        gn:name          "Le Doré";
        gn:population    0 .

<https://sws.geonames.org/2981758/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Andre-de-la-Marche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981758;
        gn:lat           47.09952;
        gn:long          -0.99441;
        gn:name          "Saint-André-de-la-Marche";
        gn:population    2701 .

<https://sws.geonames.org/12313152/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bourserie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313152;
        gn:lat           46.96248;
        gn:long          -1.42242;
        gn:name          "La Bourserie";
        gn:population    0 .

<https://sws.geonames.org/8292999/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Corcoue Sur Logne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292999;
        gn:lat           46.9661;
        gn:long          -1.57641;
        gn:name          "Bureau de Poste de Corcoue Sur Logne";
        gn:population    0 .

<https://sws.geonames.org/3022300/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Crossac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3022300;
        gn:lat           47.41235;
        gn:long          -2.16758;
        gn:name          "Crossac";
        gn:population    2329 .

<https://sws.geonames.org/8287002/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Donges Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287002;
        gn:lat           47.30884;
        gn:long          -2.07253;
        gn:name          "Donges Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3233624/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mabilais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233624;
        gn:lat           47.27262;
        gn:long          -2.08841;
        gn:name          "La Mabilais";
        gn:population    0 .

<https://sws.geonames.org/3029217/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Caharel";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3029217;
        gn:lat           47.51797;
        gn:long          -1.53571;
        gn:name          "Caharel";
        gn:population    0 .

<https://sws.geonames.org/6449395/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beaupreau-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449395;
        gn:lat           47.20194;
        gn:long          -0.99444;
        gn:name          "Beaupréau-en-Mauges";
        gn:population    23146 .

<https://sws.geonames.org/10127364/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Residhome Nantes Berges De La Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10127364;
        gn:lat           47.21223;
        gn:long          -1.53816;
        gn:name          "Residhome Nantes Berges De La Loire";
        gn:population    0 .

<https://sws.geonames.org/3010878/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bourdiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010878;
        gn:lat           47.49393;
        gn:long          -1.22571;
        gn:name          "La Bourdinière";
        gn:population    0 .

<https://sws.geonames.org/12323951/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bellevue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12323951;
        gn:lat           47.23632;
        gn:long          -1.47336;
        gn:name          "Bellevue";
        gn:population    0 .

<https://sws.geonames.org/3009153/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gaubretiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009153;
        gn:lat           46.94275;
        gn:long          -1.06482;
        gn:name          "La Gaubretière";
        gn:population    2689 .

<https://sws.geonames.org/3003637/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Maffay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003637;
        gn:lat           47.55476;
        gn:long          -1.43925;
        gn:name          "Le Maffay";
        gn:population    0 .

<https://sws.geonames.org/9036654/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Aeropuerto de Saint Nazaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.AIRP;
        gn:geonamesID    9036654;
        gn:lat           47.31485;
        gn:long          -2.15379;
        gn:name          "Aeropuerto de Saint Nazaire";
        gn:population    0 .

<https://sws.geonames.org/6435273/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roussay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435273;
        gn:lat           47.09056;
        gn:long          -1.06472;
        gn:name          "Roussay";
        gn:population    1150 .

<https://sws.geonames.org/2979545/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Hilaire-de-Loulay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979545;
        gn:lat           47.0019;
        gn:long          -1.33079;
        gn:name          "Saint-Hilaire-de-Loulay";
        gn:population    3840 .

<https://sws.geonames.org/2986118/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gare de Pont-Rousseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    2986118;
        gn:lat           47.2;
        gn:long          -1.55;
        gn:name          "Gare de Pont-Rousseau";
        gn:population    0 .

<https://sws.geonames.org/6449070/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Belligne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6449070;
        gn:lat           47.4675;
        gn:long          -1.02806;
        gn:name          "Belligné";
        gn:population    1750 .

<https://sws.geonames.org/8293050/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Doulon";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293050;
        gn:lat           47.22597;
        gn:long          -1.52953;
        gn:name          "Bureau de Poste de Nantes Doulon";
        gn:population    0 .

<https://sws.geonames.org/12312914/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Linieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312914;
        gn:lat           47.48373;
        gn:long          -1.31587;
        gn:name          "Les Linières";
        gn:population    0 .

<https://sws.geonames.org/8292918/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Bouvron";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292918;
        gn:lat           47.41804;
        gn:long          -1.84776;
        gn:name          "Bureau de Poste de Bouvron";
        gn:population    0 .

<https://sws.geonames.org/6449115/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Malville";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449115;
        gn:lat           47.36111;
        gn:long          -1.86389;
        gn:name          "Malville";
        gn:population    3429 .

<https://sws.geonames.org/8286984/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bourgneuf en Retz Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286984;
        gn:lat           47.04687;
        gn:long          -1.95494;
        gn:name          "Bourgneuf en Retz Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12312987/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gavalais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312987;
        gn:lat           47.39063;
        gn:long          -1.90746;
        gn:name          "Gavalais";
        gn:population    0 .

<https://sws.geonames.org/6456032/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chevallerais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456032;
        gn:lat           47.4675;
        gn:long          -1.67139;
        gn:name          "La Chevallerais";
        gn:population    1556 .

<https://sws.geonames.org/10281591/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appart City Nantes Cite Des Congres";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10281591;
        gn:lat           47.21944;
        gn:long          -1.56158;
        gn:name          "Appart City Nantes Cite Des Congres";
        gn:population    0 .

<https://sws.geonames.org/9178389/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Park & Suites Elegance Nantes Hotel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178389;
        gn:lat           47.21516;
        gn:long          -1.55221;
        gn:name          "Park & Suites Elegance Nantes Hotel";
        gn:population    0 .

<https://sws.geonames.org/3233463/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pontreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233463;
        gn:lat           47.3031;
        gn:long          -1.85234;
        gn:name          "Le Pontreau";
        gn:population    0 .

<https://sws.geonames.org/3008849/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Guesne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008849;
        gn:lat           47.38422;
        gn:long          -2.13485;
        gn:name          "La Guesne";
        gn:population    0 .

<https://sws.geonames.org/3030855/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bourun";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3030855;
        gn:lat           47.58067;
        gn:long          -1.93952;
        gn:name          "Bourun";
        gn:population    0 .

<https://sws.geonames.org/2978743/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Louis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978743;
        gn:lat           47.49679;
        gn:long          -1.31631;
        gn:name          "Saint-Louis";
        gn:population    0 .

<https://sws.geonames.org/8293369/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Geste";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293369;
        gn:lat           47.18184;
        gn:long          -1.11287;
        gn:name          "Bureau de Poste de Geste";
        gn:population    0 .

<https://sws.geonames.org/3034697/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Indre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3034697;
        gn:lat           47.2;
        gn:long          -1.66667;
        gn:name          "Indre";
        gn:population    3897 .

<https://sws.geonames.org/6497876/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel des Colonies";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6497876;
        gn:lat           47.215;
        gn:long          -1.5603;
        gn:name          "Hotel des Colonies";
        gn:population    0 .

<https://sws.geonames.org/2983735/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Riaille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2983735;
        gn:lat           47.51917;
        gn:long          -1.29598;
        gn:name          "Riaillé";
        gn:population    1916 .

<https://sws.geonames.org/8292950/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Guenrouet";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292950;
        gn:lat           47.51939;
        gn:long          -1.95475;
        gn:name          "Bureau de Poste de Guenrouet";
        gn:population    0 .

<https://sws.geonames.org/8286975/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mauves sur Loire Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286975;
        gn:lat           47.29281;
        gn:long          -1.38928;
        gn:name          "Mauves sur Loire Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3021913/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Etier du Dain";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3021913;
        gn:lat           46.93984;
        gn:long          -2.07494;
        gn:name          "Étier du Dain";
        gn:population    0 .

<https://sws.geonames.org/3008994/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grande Haie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008994;
        gn:lat           47.37416;
        gn:long          -1.63345;
        gn:name          "La Grande Haie";
        gn:population    0 .

<https://sws.geonames.org/6497195/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Residences Lagrange Classic Saint Michel Chef Chef";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6497195;
        gn:lat           47.1811;
        gn:long          -2.14;
        gn:name          "Les Résidences Lagrange Classic Saint Michel Chef Chef";
        gn:population    0 .

<https://sws.geonames.org/6449103/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Haute-Goulaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449103;
        gn:lat           47.19889;
        gn:long          -1.42861;
        gn:name          "Haute-Goulaine";
        gn:population    5755 .

<https://sws.geonames.org/6449085/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cordemais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449085;
        gn:lat           47.29028;
        gn:long          -1.87889;
        gn:name          "Cordemais";
        gn:population    3692 .

<https://sws.geonames.org/8436224/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont de Champtoceaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436224;
        gn:lat           47.34099;
        gn:long          -1.27847;
        gn:name          "Pont de Champtoceaux";
        gn:population    0 .

<https://sws.geonames.org/6613984/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Mars-du-Desert";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6613984;
        gn:lat           47.36639;
        gn:long          -1.40583;
        gn:name          "Saint-Mars-du-Désert";
        gn:population    4787 .

<https://sws.geonames.org/8293065/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Vertou Beautour";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293065;
        gn:lat           47.1839;
        gn:long          -1.50564;
        gn:name          "Bureau de Poste de Vertou Beautour";
        gn:population    0 .

<https://sws.geonames.org/9539815/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Adagio Access Nantes Viarme";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539815;
        gn:lat           47.22294;
        gn:long          -1.56288;
        gn:name          "Adagio Access Nantes Viarme";
        gn:population    0 .

<https://sws.geonames.org/12313192/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Sables Rouges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313192;
        gn:lat           47.18565;
        gn:long          -1.69389;
        gn:name          "Les Sables Rouges";
        gn:population    0 .

<https://sws.geonames.org/3233451/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Penhoet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233451;
        gn:lat           47.29578;
        gn:long          -2.19188;
        gn:name          "Penhoët";
        gn:population    0 .

<https://sws.geonames.org/3004597/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Chiron";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004597;
        gn:lat           47.23333;
        gn:long          -1.41667;
        gn:name          "Le Chiron";
        gn:population    0 .

<https://sws.geonames.org/9173252/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Best Western Pornic";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173252;
        gn:lat           47.12574;
        gn:long          -2.11693;
        gn:name          "Best Western Pornic";
        gn:population    0 .

<https://sws.geonames.org/2985161/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Puceul";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2985161;
        gn:lat           47.52204;
        gn:long          -1.61715;
        gn:name          "Puceul";
        gn:population    682 .

<https://sws.geonames.org/11279881/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Park And Suites Nantes Ouest Saint Herblain";
        <https://schema.org/elevation>  0.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:S;
        gn:featureCode                  gn:S.HTL;
        gn:geonamesID                   11279881;
        gn:lat                          47.22086;
        gn:long                         -1.62767;
        gn:name                         "Park And Suites Nantes Ouest Saint Herblain";
        gn:population                   0 .

<https://sws.geonames.org/6449105/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Heric";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449105;
        gn:lat           47.4125;
        gn:long          -1.65167;
        gn:name          "Héric";
        gn:population    5930 .

<https://sws.geonames.org/6519216/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appart City Nantes Chateau Des";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6519216;
        gn:lat           47.2102;
        gn:long          -1.5471;
        gn:name          "Appart City Nantes Chateau Des";
        gn:population    0 .

<https://sws.geonames.org/8297379/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Barbatre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297379;
        gn:lat           46.94229;
        gn:long          -2.17875;
        gn:name          "Bureau de Poste de Barbatre";
        gn:population    0 .

<https://sws.geonames.org/8436215/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont de la Vendee";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436215;
        gn:lat           47.21377;
        gn:long          -1.51735;
        gn:name          "Pont de la Vendée";
        gn:population    0 .

<https://sws.geonames.org/3233673/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Corbinais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233673;
        gn:lat           47.26639;
        gn:long          -1.99016;
        gn:name          "La Corbinais";
        gn:population    0 .

<https://sws.geonames.org/10297823/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quick Palace Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297823;
        gn:lat           47.25305;
        gn:long          -1.51285;
        gn:name          "Quick Palace Nantes";
        gn:population    0 .

<https://sws.geonames.org/6449073/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouaye";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449073;
        gn:lat           47.14361;
        gn:long          -1.68889;
        gn:name          "Bouaye";
        gn:population    7620 .

<https://sws.geonames.org/13494804/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plage de la Noeveillard";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.BCH;
        gn:geonamesID    13494804;
        gn:lat           47.11016;
        gn:long          -2.11711;
        gn:name          "Plage de la Noëveillard";
        gn:population    0 .

<https://sws.geonames.org/3233445/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Banc des Brillantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.SHOL;
        gn:geonamesID    3233445;
        gn:lat           47.29166;
        gn:long          -2.07215;
        gn:name          "Banc des Brillantes";
        gn:population    0 .

<https://sws.geonames.org/3022827/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Coutable";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3022827;
        gn:lat           47.39655;
        gn:long          -1.91762;
        gn:name          "Coutable";
        gn:population    0 .

<https://sws.geonames.org/3007259/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Planche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007259;
        gn:lat           47.01675;
        gn:long          -1.43533;
        gn:name          "La Planche";
        gn:population    2239 .

<https://sws.geonames.org/12313202/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Messan";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313202;
        gn:lat           47.1923;
        gn:long          -1.85302;
        gn:name          "Messan";
        gn:population    0 .

<https://sws.geonames.org/11467722/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Prieure de Freny";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSTS;
        gn:geonamesID    11467722;
        gn:lat           47.35281;
        gn:long          -2.14251;
        gn:name          "Prieuré de Frény";
        gn:population    0 .

<https://sws.geonames.org/3021704/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Dastres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3021704;
        gn:lat           47.58857;
        gn:long          -1.74991;
        gn:name          "Dastres";
        gn:population    0 .

<https://sws.geonames.org/3008615/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Jametrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008615;
        gn:lat           47.31047;
        gn:long          -1.70119;
        gn:name          "La Jametrie";
        gn:population    0 .

<https://sws.geonames.org/10125023/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Hotel De Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10125023;
        gn:lat           47.21266;
        gn:long          -1.56021;
        gn:name          "Le Grand Hotel De Nantes";
        gn:population    0 .

<https://sws.geonames.org/6434537/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Pere-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434537;
        gn:lat           47.20694;
        gn:long          -2.04472;
        gn:name          "Saint-Père-en-Retz";
        gn:population    4553 .

<https://sws.geonames.org/9178513/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Premiere Classe Nantes Reze";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178513;
        gn:lat           47.21837;
        gn:long          -1.55362;
        gn:name          "Premiere Classe Nantes Reze";
        gn:population    0 .

<https://sws.geonames.org/6513382/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ibis Nantes Centre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6513382;
        gn:lat           47.2189;
        gn:long          -1.5609;
        gn:name          "Ibis Nantes Centre";
        gn:population    0 .

<https://sws.geonames.org/3233611/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Plessis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233611;
        gn:lat           47.2545;
        gn:long          -2.15079;
        gn:name          "Le Plessis";
        gn:population    0 .

<https://sws.geonames.org/12312933/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Volerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312933;
        gn:lat           47.4645;
        gn:long          -1.41175;
        gn:name          "La Volerie";
        gn:population    0 .

<https://sws.geonames.org/8292937/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Couffe";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292937;
        gn:lat           47.39041;
        gn:long          -1.29442;
        gn:name          "Bureau de Poste de Couffe";
        gn:population    0 .

<https://sws.geonames.org/6520008/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Domaine D Orvault";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6520008;
        gn:lat           47.265;
        gn:long          -1.6288;
        gn:name          "Le Domaine D Orvault";
        gn:population    0 .

<https://sws.geonames.org/3008992/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grande Huttiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008992;
        gn:lat           47.43093;
        gn:long          -0.95848;
        gn:name          "La Grande Huttière";
        gn:population    0 .

<https://sws.geonames.org/10173584/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nantes Centre Saint Jacques";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10173584;
        gn:lat           47.196;
        gn:long          -1.531;
        gn:name          "Nantes Centre Saint Jacques";
        gn:population    0 .

<https://sws.geonames.org/7116365/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ecole Superieure du Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.SCH;
        gn:geonamesID    7116365;
        gn:lat           47.28368;
        gn:long          -1.51472;
        gn:name          "Ecole Supérieure du Bois";
        gn:population    0 .

<https://sws.geonames.org/6454151/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nozay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6454151;
        gn:lat           47.56444;
        gn:long          -1.62528;
        gn:name          "Nozay";
        gn:population    4130 .

<https://sws.geonames.org/3008238/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mauvaisiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSEC;
        gn:geonamesID    3008238;
        gn:lat           47.33167;
        gn:long          -1.09857;
        gn:name          "La Mauvaisinière";
        gn:population    0 .

<https://sws.geonames.org/12312980/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bas Tremar";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312980;
        gn:lat           47.53929;
        gn:long          -1.84452;
        gn:name          "Le Bas Trémar";
        gn:population    0 .

<https://sws.geonames.org/9539867/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brit Hotel Alantel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539867;
        gn:lat           47.29924;
        gn:long          -1.77637;
        gn:name          "Brit Hotel Alantel";
        gn:population    0 .

<https://sws.geonames.org/8286979/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ancenis Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286979;
        gn:lat           47.36947;
        gn:long          -1.17759;
        gn:name          "Ancenis Railway Station";
        gn:population    0 .

<https://sws.geonames.org/2972584/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tillieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2972584;
        gn:lat           47.14397;
        gn:long          -1.16334;
        gn:name          "Tillières";
        gn:population    1343 .

<https://sws.geonames.org/3002629/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Epoids";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002629;
        gn:lat           46.93373;
        gn:long          -2.05823;
        gn:name          "L'Époids";
        gn:population    0 .

<https://sws.geonames.org/12313100/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Basse Canterie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313100;
        gn:lat           47.17883;
        gn:long          -1.42784;
        gn:name          "Basse Canterie";
        gn:population    0 .

<https://sws.geonames.org/2998165/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998165;
        gn:lat           47.34322;
        gn:long          -1.16536;
        gn:name          "Liré";
        gn:population    2365 .

<https://sws.geonames.org/6694757/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Montaigu - Saint-Georges";
        <https://schema.org/elevation>  56.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:S;
        gn:featureCode                  gn:S.AIRP;
        gn:geonamesID                   6694757;
        gn:lat                          46.933;
        gn:long                         -1.326;
        gn:name                         "Montaigu - Saint-Georges";
        gn:population                   0 .

<https://sws.geonames.org/12313195/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Barbotiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313195;
        gn:lat           47.16788;
        gn:long          -1.74801;
        gn:name          "La Barbotinière";
        gn:population    0 .

<https://sws.geonames.org/11073019/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plage de la Birochere";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.BCH;
        gn:geonamesID    11073019;
        gn:lat           47.10469;
        gn:long          -2.09126;
        gn:name          "Plage de la Birochère";
        gn:population    0 .

<https://sws.geonames.org/12313123/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Champ du Pont";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313123;
        gn:lat           47.05763;
        gn:long          -1.37365;
        gn:name          "Le Champ du Pont";
        gn:population    0 .

<https://sws.geonames.org/6616814/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Colomban";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616814;
        gn:lat           47.0088;
        gn:long          -1.5823;
        gn:name          "Saint-Colomban";
        gn:population    3333 .

<https://sws.geonames.org/6449122/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Missillac";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449122;
        gn:lat           47.48222;
        gn:long          -2.15889;
        gn:name          "Missillac";
        gn:population    5271 .

<https://sws.geonames.org/3008809/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haie-Fouassiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008809;
        gn:lat           47.15546;
        gn:long          -1.39927;
        gn:name          "La Haie-Fouassière";
        gn:population    4047 .

<https://sws.geonames.org/9253702/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Nazaire, Nantes Port";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.PRT;
        gn:geonamesID    9253702;
        gn:lat           47.29539;
        gn:long          -2.16044;
        gn:name          "Saint-Nazaire, Nantes Port";
        gn:population    0 .

<https://sws.geonames.org/3233626/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Petolais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233626;
        gn:lat           47.26988;
        gn:long          -2.11;
        gn:name          "La Pétolais";
        gn:population    0 .

<https://sws.geonames.org/3233458/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Migron";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233458;
        gn:lat           47.25536;
        gn:long          -1.91599;
        gn:name          "Le Migron";
        gn:population    0 .

<https://sws.geonames.org/12310619/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Riviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310619;
        gn:lat           46.9496;
        gn:long          -1.87416;
        gn:name          "La Rivière";
        gn:population    0 .

<https://sws.geonames.org/12308489/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Barbotin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308489;
        gn:lat           47.28026;
        gn:long          -1.17341;
        gn:name          "Le Barbotin";
        gn:population    0 .

<https://sws.geonames.org/3022153/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cugand";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3022153;
        gn:lat           47.06353;
        gn:long          -1.25463;
        gn:name          "Cugand";
        gn:population    3189 .

<https://sws.geonames.org/3233448/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Treveneuc";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233448;
        gn:lat           47.32488;
        gn:long          -2.105;
        gn:name          "Tréveneuc";
        gn:population    0 .

<https://sws.geonames.org/6434495/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont-Saint-Martin";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434495;
        gn:lat           47.12361;
        gn:long          -1.58444;
        gn:name          "Pont-Saint-Martin";
        gn:population    5877 .

<https://sws.geonames.org/12312953/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gergaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312953;
        gn:lat           47.29083;
        gn:long          -1.58361;
        gn:name          "La Gergaudière";
        gn:population    0 .

<https://sws.geonames.org/6615237/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boussay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6615237;
        gn:lat           47.04417;
        gn:long          -1.18639;
        gn:name          "Boussay";
        gn:population    2632 .

<https://sws.geonames.org/3027335/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chambretaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3027335;
        gn:lat           46.92178;
        gn:long          -0.96559;
        gn:name          "Chambretaud";
        gn:population    1377 .

<https://sws.geonames.org/3007231/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Poivetiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007231;
        gn:lat           47.21215;
        gn:long          -1.35381;
        gn:name          "La Poivetière";
        gn:population    0 .

<https://sws.geonames.org/3010107/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chaussee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010107;
        gn:lat           47.48238;
        gn:long          -1.79273;
        gn:name          "La Chaussée";
        gn:population    0 .

<https://sws.geonames.org/8293055/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Brevin L Ocean";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293055;
        gn:lat           47.22987;
        gn:long          -2.17504;
        gn:name          "Bureau de Poste de Saint Brevin L Ocean";
        gn:population    0 .

<https://sws.geonames.org/6457135/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boissiere-de-Montaigu";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6457135;
        gn:lat           46.95083;
        gn:long          -1.19139;
        gn:name          "La Boissière-de-Montaigu";
        gn:population    2261 .

<https://sws.geonames.org/12323978/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Tardiviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12323978;
        gn:lat           47.56674;
        gn:long          -1.64165;
        gn:name          "La Tardivière";
        gn:population    0 .

<https://sws.geonames.org/12313142/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Portillon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313142;
        gn:lat           47.14958;
        gn:long          -1.46759;
        gn:name          "Portillon";
        gn:population    0 .

<https://sws.geonames.org/12312931/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312931;
        gn:lat           47.51139;
        gn:long          -1.38403;
        gn:name          "Le Bois";
        gn:population    0 .

<https://sws.geonames.org/3233411/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Petit Ve";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233411;
        gn:lat           47.08472;
        gn:long          -2.085;
        gn:name          "Petit Vé";
        gn:population    0 .

<https://sws.geonames.org/8287010/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cordemais Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287010;
        gn:lat           47.30202;
        gn:long          -1.84617;
        gn:name          "Cordemais Railway Station";
        gn:population    0 .

<https://sws.geonames.org/6520562/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Citea Residentiel Nantes Aubini";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6520562;
        gn:lat           47.2456;
        gn:long          -1.5693;
        gn:name          "Citea Residentiel Nantes Aubini";
        gn:population    0 .

<https://sws.geonames.org/6456034/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grigonnais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456034;
        gn:lat           47.52667;
        gn:long          -1.6675;
        gn:name          "La Grigonnais";
        gn:population    1657 .

<https://sws.geonames.org/12312936/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Guineau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312936;
        gn:lat           47.26841;
        gn:long          -1.35675;
        gn:name          "Le Guineau";
        gn:population    0 .

<https://sws.geonames.org/6434502/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quilly";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434502;
        gn:lat           47.46167;
        gn:long          -1.95333;
        gn:name          "Quilly";
        gn:population    1379 .

<https://sws.geonames.org/3034111/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beaupreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3034111;
        gn:lat           47.20214;
        gn:long          -0.99471;
        gn:name          "Beaupréau";
        gn:population    6932 .

<https://sws.geonames.org/12310625/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Noue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310625;
        gn:lat           46.95322;
        gn:long          -1.1932;
        gn:name          "La Noue";
        gn:population    0 .

<https://sws.geonames.org/8287049/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Herbergement-Les Brouzils Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287049;
        gn:lat           46.90641;
        gn:long          -1.37179;
        gn:name          "L'Herbergement-Les Brouzils Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12313095/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grande Galussiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313095;
        gn:lat           47.09571;
        gn:long          -1.30814;
        gn:name          "La Grande Galussière";
        gn:population    0 .

<https://sws.geonames.org/6474236/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Amiral";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6474236;
        gn:lat           47.21404;
        gn:long          -1.56259;
        gn:name          "Amiral";
        gn:population    0 .

<https://sws.geonames.org/3233926/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bazillais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233926;
        gn:lat           47.29655;
        gn:long          -1.8902;
        gn:name          "La Bazillais";
        gn:population    0 .

<https://sws.geonames.org/3034423/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bazoges-en-Paillers";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3034423;
        gn:lat           46.90861;
        gn:long          -1.13678;
        gn:name          "Bazoges-en-Paillers";
        gn:population    898 .

<https://sws.geonames.org/3003586/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Marillais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003586;
        gn:lat           47.35749;
        gn:long          -1.07693;
        gn:name          "Le Marillais";
        gn:population    707 .

<https://sws.geonames.org/6449407/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouzille";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6449407;
        gn:lat           47.3375;
        gn:long          -1.11111;
        gn:name          "Bouzillé";
        gn:population    1451 .

<https://sws.geonames.org/10106136/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Domaine De La Bretesche";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10106136;
        gn:lat           47.5124;
        gn:long          -2.06578;
        gn:name          "Domaine De La Bretesche";
        gn:population    0 .

<https://sws.geonames.org/3233618/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Basse Meyner";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233618;
        gn:lat           47.28528;
        gn:long          -2.13694;
        gn:name          "Basse Meyner";
        gn:population    0 .

<https://sws.geonames.org/8287061/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Torfou Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287061;
        gn:lat           47.033;
        gn:long          -1.11717;
        gn:name          "Torfou Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8293407/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Macaire En Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293407;
        gn:lat           47.1237;
        gn:long          -0.99073;
        gn:name          "Bureau de Poste de Saint Macaire En Mauges";
        gn:population    0 .

<https://sws.geonames.org/6526211/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mercure Nantes Nord 2m";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6526211;
        gn:lat           47.3303;
        gn:long          -1.6256;
        gn:name          "Mercure Nantes Nord 2m";
        gn:population    0 .

<https://sws.geonames.org/2967993/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vioreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2967993;
        gn:lat           47.53133;
        gn:long          -1.43683;
        gn:name          "Vioreau";
        gn:population    0 .

<https://sws.geonames.org/12308352/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Gilles";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308352;
        gn:lat           47.55612;
        gn:long          -1.03478;
        gn:name          "Saint-Gilles";
        gn:population    0 .

<https://sws.geonames.org/6616817/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Suce-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616817;
        gn:lat           47.3445;
        gn:long          -1.5283;
        gn:name          "Sucé-sur-Erdre";
        gn:population    6958 .

<https://sws.geonames.org/6449120/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mesanger";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449120;
        gn:lat           47.43306;
        gn:long          -1.23139;
        gn:name          "Mésanger";
        gn:population    4686 .

<https://sws.geonames.org/2995088/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois de Maumusson";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2995088;
        gn:lat           47.49905;
        gn:long          -1.14738;
        gn:name          "Bois de Maumusson";
        gn:population    0 .

<https://sws.geonames.org/6456022/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pallet";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456022;
        gn:lat           47.13833;
        gn:long          -1.33583;
        gn:name          "Le Pallet";
        gn:population    3236 .

<https://sws.geonames.org/6613025/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Getigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6613025;
        gn:lat           47.07556;
        gn:long          -1.24944;
        gn:name          "Gétigné";
        gn:population    3621 .

<https://sws.geonames.org/12313199/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Breuil";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313199;
        gn:lat           46.99816;
        gn:long          -1.69084;
        gn:name          "Le Breuil";
        gn:population    0 .

<https://sws.geonames.org/10297839/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel de La Gare de Nantes Citotel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297839;
        gn:lat           47.21771;
        gn:long          -1.54395;
        gn:name          "Hotel de La Gare de Nantes Citotel";
        gn:population    0 .

<https://sws.geonames.org/3004478/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Coudray";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004478;
        gn:lat           47.55828;
        gn:long          -1.83933;
        gn:name          "Le Coudray";
        gn:population    0 .

<https://sws.geonames.org/3233453/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bourdiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233453;
        gn:lat           47.2276;
        gn:long          -1.75617;
        gn:name          "La Bourdinière";
        gn:population    0 .

<https://sws.geonames.org/8293045/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Reze Chateau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293045;
        gn:lat           47.18455;
        gn:long          -1.5591;
        gn:name          "Bureau de Poste de Reze Chateau";
        gn:population    0 .

<https://sws.geonames.org/3004504/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Cormier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004504;
        gn:lat           47.15478;
        gn:long          -2.17639;
        gn:name          "Le Cormier";
        gn:population    0 .

<https://sws.geonames.org/6434544/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Savenay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434544;
        gn:lat           47.36111;
        gn:long          -1.94194;
        gn:name          "Savenay";
        gn:population    8448 .

<https://sws.geonames.org/12313218/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gelletiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313218;
        gn:lat           47.13567;
        gn:long          -2.08184;
        gn:name          "La Gelletière";
        gn:population    0 .

<https://sws.geonames.org/10112804/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Kyriad Nantes Sud Bouaye Aeroport";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10112804;
        gn:lat           47.143;
        gn:long          -1.662;
        gn:name          "Kyriad Nantes Sud Bouaye Aeroport";
        gn:population    0 .

<https://sws.geonames.org/3006088/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Turpinais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006088;
        gn:lat           47.42083;
        gn:long          -1.97643;
        gn:name          "La Turpinais";
        gn:population    0 .

<https://sws.geonames.org/10297825/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Logis Beaujoire Hotel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297825;
        gn:lat           47.25773;
        gn:long          -1.52928;
        gn:name          "Logis Beaujoire Hôtel";
        gn:population    0 .

<https://sws.geonames.org/6449075/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouguenais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449075;
        gn:lat           47.17917;
        gn:long          -1.62472;
        gn:name          "Bouguenais";
        gn:population    19049 .

<https://sws.geonames.org/2991782/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Morisseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2991782;
        gn:lat           47.15763;
        gn:long          -1.38179;
        gn:name          "Morisseau";
        gn:population    0 .

<https://sws.geonames.org/2979344/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Jean-de-Boiseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979344;
        gn:lat           47.19424;
        gn:long          -1.72485;
        gn:name          "Saint-Jean-de-Boiseau";
        gn:population    4906 .

<https://sws.geonames.org/12310630/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Sauvagere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310630;
        gn:lat           46.94925;
        gn:long          -1.06609;
        gn:name          "La Sauvagère";
        gn:population    0 .

<https://sws.geonames.org/12312878/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gree Saint-Jacques";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312878;
        gn:lat           47.56413;
        gn:long          -1.04656;
        gn:name          "La Grée Saint-Jacques";
        gn:population    0 .

<https://sws.geonames.org/8293070/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Champ De Mars";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293070;
        gn:lat           47.21367;
        gn:long          -1.54522;
        gn:name          "Bureau de Poste de Nantes Champ De Mars";
        gn:population    0 .

<https://sws.geonames.org/12313204/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Tancherie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313204;
        gn:lat           47.17911;
        gn:long          -1.80065;
        gn:name          "La Tancherie";
        gn:population    0 .

<https://sws.geonames.org/12313182/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Touche Monnet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313182;
        gn:lat           46.99023;
        gn:long          -1.61458;
        gn:name          "La Touche Monnet";
        gn:population    0 .

<https://sws.geonames.org/10281170/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Escale Oceania Nantes Bouguenais Hotel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10281170;
        gn:lat           47.1729;
        gn:long          -1.6189;
        gn:name          "Escale Oceania Nantes Bouguenais Hotel";
        gn:population    0 .

<https://sws.geonames.org/12313209/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Port";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313209;
        gn:lat           47.1129;
        gn:long          -1.97158;
        gn:name          "Port";
        gn:population    0 .

<https://sws.geonames.org/10117424/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Jules Verne Nantes Prochainement All Seasons";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10117424;
        gn:lat           47.21455;
        gn:long          -1.5576;
        gn:name          "Hotel Jules Verne Nantes Prochainement All Seasons";
        gn:population    0 .

<https://sws.geonames.org/9180242/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vvf Villages Noirmoutier";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9180242;
        gn:lat           46.90508;
        gn:long          -2.1571;
        gn:name          "Vvf Villages Noirmoutier";
        gn:population    0 .

<https://sws.geonames.org/12310620/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois Gaudin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310620;
        gn:lat           46.94039;
        gn:long          -2.17678;
        gn:name          "Bois Gaudin";
        gn:population    0 .

<https://sws.geonames.org/10112829/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes Est Saint Sebastien Sur Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10112829;
        gn:lat           47.21197;
        gn:long          -1.4865;
        gn:name          "Campanile Nantes Est Saint Sebastien Sur Loire";
        gn:population    0 .

<https://sws.geonames.org/12313149/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Getiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313149;
        gn:lat           47.0028;
        gn:long          -1.46123;
        gn:name          "La Gétière";
        gn:population    0 .

<https://sws.geonames.org/12313026/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Pommeraie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313026;
        gn:lat           47.35248;
        gn:long          -2.10155;
        gn:name          "La Pommeraie";
        gn:population    0 .

<https://sws.geonames.org/2982611/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois de Rouge";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2982611;
        gn:lat           47.49465;
        gn:long          -1.01328;
        gn:name          "Bois de Rougé";
        gn:population    0 .

<https://sws.geonames.org/6434559/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vieillevigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434559;
        gn:lat           46.97111;
        gn:long          -1.43333;
        gn:name          "Vieillevigne";
        gn:population    3961 .

<https://sws.geonames.org/3031890/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boistuaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031890;
        gn:lat           47.33916;
        gn:long          -1.86845;
        gn:name          "Boistuaud";
        gn:population    0 .

<https://sws.geonames.org/8292920/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Campbon";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292920;
        gn:lat           47.4127;
        gn:long          -1.96836;
        gn:name          "Bureau de Poste de Campbon";
        gn:population    0 .

<https://sws.geonames.org/12312880/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Madeleine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312880;
        gn:lat           47.38211;
        gn:long          -1.02292;
        gn:name          "La Madeleine";
        gn:population    0 .

<https://sws.geonames.org/8436220/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont des Trois-Continents";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436220;
        gn:lat           47.19818;
        gn:long          -1.56182;
        gn:name          "Pont des Trois-Continents";
        gn:population    0 .

<https://sws.geonames.org/9173412/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brit Hotel Les Alizes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173412;
        gn:lat           47.11379;
        gn:long          -2.09423;
        gn:name          "Brit Hotel Les Alizes";
        gn:population    0 .

<https://sws.geonames.org/2972056/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trans-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2972056;
        gn:lat           47.47658;
        gn:long          -1.37374;
        gn:name          "Trans-sur-Erdre";
        gn:population    734 .

<https://sws.geonames.org/2978896/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Laurent-du-Mottay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978896;
        gn:lat           47.35107;
        gn:long          -0.94937;
        gn:name          "Saint-Laurent-du-Mottay";
        gn:population    746 .

<https://sws.geonames.org/3025826/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chauve";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3025826;
        gn:lat           47.15199;
        gn:long          -1.98666;
        gn:name          "Chauvé";
        gn:population    1822 .

<https://sws.geonames.org/11048617/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "La petorie";
        <https://schema.org/elevation>  73.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:P;
        gn:featureCode                  gn:P.PPL;
        gn:geonamesID                   11048617;
        gn:lat                          47.30644;
        gn:long                         -1.42623;
        gn:name                         "La pètorie";
        gn:population                   0 .

<https://sws.geonames.org/12312945/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Charbonneau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312945;
        gn:lat           47.3017;
        gn:long          -1.48921;
        gn:name          "Le Charbonneau";
        gn:population    0 .

<https://sws.geonames.org/12312960/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roulais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312960;
        gn:lat           47.5171;
        gn:long          -1.67807;
        gn:name          "La Roulais";
        gn:population    0 .

<https://sws.geonames.org/12313137/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Denillere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313137;
        gn:lat           47.16546;
        gn:long          -1.43399;
        gn:name          "La Denillère";
        gn:population    0 .

<https://sws.geonames.org/8293062/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Coueron La Chabossiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293062;
        gn:lat           47.2147;
        gn:long          -1.6821;
        gn:name          "Bureau de Poste de Coueron La Chabossiere";
        gn:population    0 .

<https://sws.geonames.org/3037215/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de l'Arche";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    3037215;
        gn:lat           47.56238;
        gn:long          -1.44516;
        gn:name          "Forêt de l'Arche";
        gn:population    0 .

<https://sws.geonames.org/8292976/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nozay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292976;
        gn:lat           47.56563;
        gn:long          -1.62685;
        gn:name          "Bureau de Poste de Nozay";
        gn:population    0 .

<https://sws.geonames.org/9177962/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mercure Nantes Centre Gare";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177962;
        gn:lat           47.21614;
        gn:long          -1.54398;
        gn:name          "Mercure Nantes Centre Gare";
        gn:population    0 .

<https://sws.geonames.org/3011092/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bernardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011092;
        gn:lat           47.17;
        gn:long          -1.3694;
        gn:name          "La Bernardière";
        gn:population    0 .

<https://sws.geonames.org/6456029/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rouxiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456029;
        gn:lat           47.44278;
        gn:long          -1.06778;
        gn:name          "La Rouxière";
        gn:population    985 .

<https://sws.geonames.org/12312923/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Epine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312923;
        gn:lat           47.29027;
        gn:long          -1.34518;
        gn:name          "L'Épine";
        gn:population    0 .

<https://sws.geonames.org/2987055/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile Pipy";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    2987055;
        gn:lat           47.29429;
        gn:long          -1.94202;
        gn:name          "Île Pipy";
        gn:population    0 .

<https://sws.geonames.org/12313075/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Corbeillieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313075;
        gn:lat           47.14393;
        gn:long          -1.22791;
        gn:name          "Les Corbeillières";
        gn:population    0 .

<https://sws.geonames.org/2989058/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Oudon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2989058;
        gn:lat           47.34692;
        gn:long          -1.28659;
        gn:name          "Oudon";
        gn:population    2845 .

<https://sws.geonames.org/12310612/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Avenir";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310612;
        gn:lat           47.00631;
        gn:long          -1.33369;
        gn:name          "L'Avenir";
        gn:population    0 .

<https://sws.geonames.org/12313236/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Guerches";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313236;
        gn:lat           47.11604;
        gn:long          -2.12709;
        gn:name          "Les Guerches";
        gn:population    0 .

<https://sws.geonames.org/11746345/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cormerais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    11746345;
        gn:lat           47.49691;
        gn:long          -1.46645;
        gn:name          "La Cormerais";
        gn:population    0 .

<https://sws.geonames.org/3034249/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile Beaulieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3034249;
        gn:lat           47.20452;
        gn:long          -1.54381;
        gn:name          "Île Beaulieu";
        gn:population    0 .

<https://sws.geonames.org/12312970/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bazillere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312970;
        gn:lat           47.22618;
        gn:long          -1.69304;
        gn:name          "La Bazillère";
        gn:population    0 .

<https://sws.geonames.org/6435204/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Drain";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435204;
        gn:lat           47.3391;
        gn:long          -1.2061;
        gn:name          "Drain";
        gn:population    1877 .

<https://sws.geonames.org/8287026/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Varades Saint-Florent le Vieil Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287026;
        gn:lat           47.37437;
        gn:long          -1.01968;
        gn:name          "Varades Saint-Florent le Vieil Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8292962/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Maisdon Sur Sevre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292962;
        gn:lat           47.09906;
        gn:long          -1.38523;
        gn:name          "Bureau de Poste de Maisdon Sur Sevre";
        gn:population    0 .

<https://sws.geonames.org/2980449/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Marie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980449;
        gn:lat           47.11485;
        gn:long          -2.13106;
        gn:name          "Sainte-Marie";
        gn:population    0 .

<https://sws.geonames.org/8292967/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Missillac";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292967;
        gn:lat           47.48231;
        gn:long          -2.16164;
        gn:name          "Bureau de Poste de Missillac";
        gn:population    0 .

<https://sws.geonames.org/12166923/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaye de Saint-Gildas-des-Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSTS;
        gn:geonamesID    12166923;
        gn:lat           47.51649;
        gn:long          -2.03708;
        gn:name          "Abbaye de Saint-Gildas-des-Bois";
        gn:population    0 .

<https://sws.geonames.org/3010844/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boutouchere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010844;
        gn:lat           47.32905;
        gn:long          -0.99333;
        gn:name          "La Boutouchère";
        gn:population    0 .

<https://sws.geonames.org/2999190/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Thiemay";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSEC;
        gn:geonamesID    2999190;
        gn:lat           47.35083;
        gn:long          -1.80083;
        gn:name          "Le Thiémay";
        gn:population    0 .

<https://sws.geonames.org/8286987/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pornic Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286987;
        gn:lat           47.11453;
        gn:long          -2.09766;
        gn:name          "Pornic Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12313080/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Petiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313080;
        gn:lat           47.18127;
        gn:long          -1.27225;
        gn:name          "La Pétinière";
        gn:population    0 .

<https://sws.geonames.org/2986955/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plaine de Mazerolles";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.LK;
        gn:geonamesID    2986955;
        gn:lat           47.3619;
        gn:long          -1.50135;
        gn:name          "Plaine de Mazerolles";
        gn:population    0 .

<https://sws.geonames.org/11054416/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaye Notre-Dame de Melleray";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.MSTY;
        gn:geonamesID    11054416;
        gn:lat           47.54888;
        gn:long          -1.3775;
        gn:name          "Abbaye Notre-Dame de Melleray";
        gn:population    0 .

<https://sws.geonames.org/11073021/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe de Gourmalon";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    11073021;
        gn:lat           47.10849;
        gn:long          -2.10723;
        gn:name          "Pointe de Gourmalon";
        gn:population    0 .

<https://sws.geonames.org/8293077/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Ancenis Arcades";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293077;
        gn:lat           47.37053;
        gn:long          -1.17751;
        gn:name          "Bureau de Poste de Ancenis Arcades";
        gn:population    0 .

<https://sws.geonames.org/9177178/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inter-Hotel Du Grand Monarque";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177178;
        gn:lat           47.22161;
        gn:long          -1.54744;
        gn:name          "Inter-Hotel Du Grand Monarque";
        gn:population    0 .

<https://sws.geonames.org/6456918/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haie-Fouassiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456918;
        gn:lat           47.15556;
        gn:long          -1.39917;
        gn:name          "La Haie-Fouassière";
        gn:population    4648 .

<https://sws.geonames.org/3008399/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Lucrais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008399;
        gn:lat           47.59781;
        gn:long          -1.87019;
        gn:name          "La Lucrais";
        gn:population    0 .

<https://sws.geonames.org/12312938/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Simon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312938;
        gn:lat           47.29035;
        gn:long          -1.36951;
        gn:name          "Saint-Simon";
        gn:population    0 .

<https://sws.geonames.org/2987944/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Perno";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2987944;
        gn:lat           47.46655;
        gn:long          -2.17738;
        gn:name          "Perno";
        gn:population    0 .

<https://sws.geonames.org/6434504/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Riaille";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434504;
        gn:lat           47.51889;
        gn:long          -1.29556;
        gn:name          "Riaillé";
        gn:population    2319 .

<https://sws.geonames.org/2996116/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ruisseau des Marais de Gree";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2996116;
        gn:lat           47.36988;
        gn:long          -1.1681;
        gn:name          "Ruisseau des Marais de Grée";
        gn:population    0 .

<https://sws.geonames.org/2986271/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pontchateau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2986271;
        gn:lat           47.43868;
        gn:long          -2.09422;
        gn:name          "Pontchâteau";
        gn:population    8474 .

<https://sws.geonames.org/12313164/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Benetiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313164;
        gn:lat           47.11194;
        gn:long          -1.53348;
        gn:name          "La Benêtière";
        gn:population    0 .

<https://sws.geonames.org/12310627/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Port";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310627;
        gn:lat           46.92879;
        gn:long          -2.05204;
        gn:name          "Le Port";
        gn:population    0 .

<https://sws.geonames.org/6612547/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Oudon";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6612547;
        gn:lat           47.34639;
        gn:long          -1.28694;
        gn:name          "Oudon";
        gn:population    3763 .

<https://sws.geonames.org/3008811/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haie de Ligne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008811;
        gn:lat           47.39845;
        gn:long          -1.40476;
        gn:name          "La Haie de Ligné";
        gn:population    0 .

<https://sws.geonames.org/2979169/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Joseph";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979169;
        gn:lat           47.26854;
        gn:long          -1.5197;
        gn:name          "Saint-Joseph";
        gn:population    0 .

<https://sws.geonames.org/3233460/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fontaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233460;
        gn:lat           47.31175;
        gn:long          -1.98186;
        gn:name          "La Fontaine";
        gn:population    0 .

<https://sws.geonames.org/12312943/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Georges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312943;
        gn:lat           47.44003;
        gn:long          -1.48971;
        gn:name          "Saint-Georges";
        gn:population    0 .

<https://sws.geonames.org/6449092/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Dreffeac";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449092;
        gn:lat           47.4768;
        gn:long          -2.0557;
        gn:name          "Drefféac";
        gn:population    2188 .

<https://sws.geonames.org/8436227/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont d'Ingrandes-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436227;
        gn:lat           47.40089;
        gn:long          -0.91884;
        gn:name          "Pont d'Ingrandes-sur-Loire";
        gn:population    0 .

<https://sws.geonames.org/8297424/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Mortagne Sur Sevre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297424;
        gn:lat           46.99203;
        gn:long          -0.95261;
        gn:name          "Bureau de Poste de Mortagne Sur Sevre";
        gn:population    0 .

<https://sws.geonames.org/12320393/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Petit Bezo";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12320393;
        gn:lat           47.57486;
        gn:long          -2.15714;
        gn:name          "Le Petit Bézo";
        gn:population    0 .

<https://sws.geonames.org/3007878/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Landemont";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007878;
        gn:lat           47.26536;
        gn:long          -1.23989;
        gn:name          "Landemont";
        gn:population    1568 .

<https://sws.geonames.org/3002701/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Plessis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002701;
        gn:lat           47.35381;
        gn:long          -1.30024;
        gn:name          "Le Plessis";
        gn:population    0 .

<https://sws.geonames.org/10281142/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Adagio Access Nantes La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10281142;
        gn:lat           47.21944;
        gn:long          -1.56158;
        gn:name          "Adagio Access Nantes La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/6449082/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chauve";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449082;
        gn:lat           47.15111;
        gn:long          -1.98611;
        gn:name          "Chauvé";
        gn:population    2814 .

<https://sws.geonames.org/12718883/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Marais breton vendeen";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.MRSH;
        gn:geonamesID    12718883;
        gn:lat           46.90124;
        gn:long          -2.01867;
        gn:name          "Marais breton vendéen";
        gn:population    0 .

<https://sws.geonames.org/9173744/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes Ouest - Saint Herblain";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173744;
        gn:lat           47.22656;
        gn:long          -1.6301;
        gn:name          "Campanile Nantes Ouest - Saint Herblain";
        gn:population    0 .

<https://sws.geonames.org/12310615/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Marionniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310615;
        gn:lat           46.97894;
        gn:long          -1.33379;
        gn:name          "La Marionnière";
        gn:population    0 .

<https://sws.geonames.org/12313085/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Dorices";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313085;
        gn:lat           47.17216;
        gn:long          -1.26224;
        gn:name          "Les Dorices";
        gn:population    0 .

<https://sws.geonames.org/12313211/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Auviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313211;
        gn:lat           47.09065;
        gn:long          -1.99044;
        gn:name          "L'Auvière";
        gn:population    0 .

<https://sws.geonames.org/2985319/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Prigny";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2985319;
        gn:lat           47.06673;
        gn:long          -1.9808;
        gn:name          "Prigny";
        gn:population    0 .

<https://sws.geonames.org/3030555/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Branducas";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3030555;
        gn:lat           47.45524;
        gn:long          -2.0594;
        gn:name          "Branducas";
        gn:population    0 .

<https://sws.geonames.org/3005282/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bignon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005282;
        gn:lat           47.09854;
        gn:long          -1.49103;
        gn:name          "Le Bignon";
        gn:population    2793 .

<https://sws.geonames.org/6451619/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cugand-la-Bernardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6451619;
        gn:lat           47.0625;
        gn:long          -1.25444;
        gn:name          "Cugand-la-Bernardière";
        gn:population    3466 .

<https://sws.geonames.org/3007437/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Papiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007437;
        gn:lat           47.07583;
        gn:long          -1.07798;
        gn:name          "La Papinière";
        gn:population    0 .

<https://sws.geonames.org/3014496/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de la Groulais";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    3014496;
        gn:lat           47.45333;
        gn:long          -1.73952;
        gn:name          "Forêt de la Groulais";
        gn:population    0 .

<https://sws.geonames.org/6614024/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sigismond";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6614024;
        gn:lat           47.45361;
        gn:long          -0.94278;
        gn:name          "Saint-Sigismond";
        gn:population    375 .

<https://sws.geonames.org/2994981/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mauves-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2994981;
        gn:lat           47.29671;
        gn:long          -1.39138;
        gn:name          "Mauves-sur-Loire";
        gn:population    2579 .

<https://sws.geonames.org/12313090/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Massonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313090;
        gn:lat           47.14571;
        gn:long          -1.30918;
        gn:name          "La Massonnière";
        gn:population    0 .

<https://sws.geonames.org/12305742/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Poterie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305742;
        gn:lat           47.15194;
        gn:long          -1.14162;
        gn:name          "La Poterie";
        gn:population    0 .

<https://sws.geonames.org/3233967/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Port-Launay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233967;
        gn:lat           47.21218;
        gn:long          -1.74386;
        gn:name          "Le Port-Launay";
        gn:population    0 .

<https://sws.geonames.org/6449399/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Begrolles-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449399;
        gn:lat           47.14056;
        gn:long          -0.94139;
        gn:name          "Bégrolles-en-Mauges";
        gn:population    2040 .

<https://sws.geonames.org/3025311/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile Chevire";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3025311;
        gn:lat           47.18333;
        gn:long          -1.8;
        gn:name          "Île Cheviré";
        gn:population    0 .

<https://sws.geonames.org/3003801/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Haut Ros";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003801;
        gn:lat           47.39991;
        gn:long          -2.15259;
        gn:name          "Le Haut Ros";
        gn:population    0 .

<https://sws.geonames.org/6456950/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-du-Genet";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456950;
        gn:lat           47.18306;
        gn:long          -1.01944;
        gn:name          "La Chapelle-du-Genêt";
        gn:population    1202 .

<https://sws.geonames.org/6434507/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saffre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434507;
        gn:lat           47.50167;
        gn:long          -1.57861;
        gn:name          "Saffré";
        gn:population    3860 .

<https://sws.geonames.org/10278540/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sajours and Affaires Nantes Ducs de Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10278540;
        gn:lat           47.21382;
        gn:long          -1.54551;
        gn:name          "Sajours and Affaires Nantes Ducs de Bretagne";
        gn:population    0 .

<https://sws.geonames.org/3009918/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Corbiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009918;
        gn:lat           47.57591;
        gn:long          -1.42575;
        gn:name          "La Corbière";
        gn:population    0 .

<https://sws.geonames.org/9173736/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes Centre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173736;
        gn:lat           47.19439;
        gn:long          -1.52971;
        gn:name          "Campanile Nantes Centre";
        gn:population    0 .

<https://sws.geonames.org/3023697/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cordemais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3023697;
        gn:lat           47.2914;
        gn:long          -1.87887;
        gn:name          "Cordemais";
        gn:population    2747 .

<https://sws.geonames.org/3011038/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bignanais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011038;
        gn:lat           47.3;
        gn:long          -1.9;
        gn:name          "La Bignanais";
        gn:population    0 .

<https://sws.geonames.org/6612866/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rocheserviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6612866;
        gn:lat           46.93889;
        gn:long          -1.50917;
        gn:name          "Rocheservière";
        gn:population    3299 .

<https://sws.geonames.org/3004600/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Chillon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004600;
        gn:lat           47.48432;
        gn:long          -0.91926;
        gn:name          "Le Chillon";
        gn:population    0 .

<https://sws.geonames.org/9178388/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Park & Suites Elegance Nantes Atlantis";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178388;
        gn:lat           47.22257;
        gn:long          -1.62613;
        gn:name          "Park & Suites Elegance Nantes Atlantis";
        gn:population    0 .

<https://sws.geonames.org/12305892/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cornillere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305892;
        gn:lat           47.16519;
        gn:long          -1.42302;
        gn:name          "La Cornillère";
        gn:population    0 .

<https://sws.geonames.org/3233467/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Verriere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233467;
        gn:lat           47.27726;
        gn:long          -2.01635;
        gn:name          "La Verrière";
        gn:population    0 .

<https://sws.geonames.org/3006820/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006820;
        gn:lat           47.30059;
        gn:long          -1.7244;
        gn:name          "La Roche";
        gn:population    0 .

<https://sws.geonames.org/6452324/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaretz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6452324;
        gn:lat           47.5525;
        gn:long          -1.53167;
        gn:name          "Abbaretz";
        gn:population    2068 .

<https://sws.geonames.org/10297835/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Saint Yves";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297835;
        gn:lat           47.22628;
        gn:long          -1.54329;
        gn:name          "Hotel Saint Yves";
        gn:population    0 .

<https://sws.geonames.org/3008786/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haudeliniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008786;
        gn:lat           47.49178;
        gn:long          -1.50155;
        gn:name          "La Haudelinière";
        gn:population    0 .

<https://sws.geonames.org/8286974/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Thouare Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286974;
        gn:lat           47.26512;
        gn:long          -1.44093;
        gn:name          "Thouaré Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12313176/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trejet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313176;
        gn:lat           47.11243;
        gn:long          -1.60671;
        gn:name          "Tréjet";
        gn:population    0 .

<https://sws.geonames.org/12313011/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Chene";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313011;
        gn:lat           47.56075;
        gn:long          -2.04299;
        gn:name          "Le Chêne";
        gn:population    0 .

<https://sws.geonames.org/11073016/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe des Poloux";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    11073016;
        gn:lat           47.00949;
        gn:long          -2.02861;
        gn:name          "Pointe des Poloux";
        gn:population    0 .

<https://sws.geonames.org/12312962/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Muzon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312962;
        gn:lat           47.33145;
        gn:long          -1.66846;
        gn:name          "Muzon";
        gn:population    0 .

<https://sws.geonames.org/8292992/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Riaille";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292992;
        gn:lat           47.5171;
        gn:long          -1.29463;
        gn:name          "Bureau de Poste de Riaille";
        gn:population    0 .

<https://sws.geonames.org/3233941/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Canal de Buzay";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    3233941;
        gn:lat           47.19441;
        gn:long          -1.85288;
        gn:name          "Canal de Buzay";
        gn:population    0 .

<https://sws.geonames.org/12313214/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Port du Collet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313214;
        gn:lat           47.02932;
        gn:long          -1.97589;
        gn:name          "Port du Collet";
        gn:population    0 .

<https://sws.geonames.org/6449089/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Crossac";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449089;
        gn:lat           47.41139;
        gn:long          -2.16833;
        gn:name          "Crossac";
        gn:population    2926 .

<https://sws.geonames.org/12313139/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Billardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313139;
        gn:lat           47.17375;
        gn:long          -1.4553;
        gn:name          "La Billardière";
        gn:population    0 .

<https://sws.geonames.org/3034029/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beausse";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3034029;
        gn:lat           47.32035;
        gn:long          -0.92726;
        gn:name          "Beausse";
        gn:population    382 .

<https://sws.geonames.org/2994280/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mesanger";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2994280;
        gn:lat           47.43281;
        gn:long          -1.23122;
        gn:name          "Mésanger";
        gn:population    3435 .

<https://sws.geonames.org/6613988/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Malo-du-Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6613988;
        gn:lat           46.92861;
        gn:long          -0.90056;
        gn:name          "Saint-Malô-du-Bois";
        gn:population    1605 .

<https://sws.geonames.org/12313154/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beaulieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313154;
        gn:lat           47.20902;
        gn:long          -1.53299;
        gn:name          "Beaulieu";
        gn:population    0 .

<https://sws.geonames.org/8292959/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Le Loroux Bottereau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292959;
        gn:lat           47.23883;
        gn:long          -1.34844;
        gn:name          "Bureau de Poste de Le Loroux Bottereau";
        gn:population    0 .

<https://sws.geonames.org/6434549/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Thouare-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434549;
        gn:lat           47.2675;
        gn:long          -1.44056;
        gn:name          "Thouaré-sur-Loire";
        gn:population    9778 .

<https://sws.geonames.org/3233492/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Malfiches";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233492;
        gn:lat           47.20051;
        gn:long          -2.17433;
        gn:name          "Les Malfiches";
        gn:population    0 .

<https://sws.geonames.org/3006522/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Sanglaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006522;
        gn:lat           47.22158;
        gn:long          -1.3705;
        gn:name          "La Sanglaire";
        gn:population    0 .

<https://sws.geonames.org/8292910/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Basse Goulaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292910;
        gn:lat           47.21684;
        gn:long          -1.46549;
        gn:name          "Bureau de Poste de Basse Goulaine";
        gn:population    0 .

<https://sws.geonames.org/6435297/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Laurent-du-Mottay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435297;
        gn:lat           47.35;
        gn:long          -0.95;
        gn:name          "Saint-Laurent-du-Mottay";
        gn:population    782 .

<https://sws.geonames.org/2968587/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Villeneuve";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2968587;
        gn:lat           47.56642;
        gn:long          -1.30275;
        gn:name          "Villeneuve";
        gn:population    0 .

<https://sws.geonames.org/2994817/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Etier de Mean";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    2994817;
        gn:lat           47.28929;
        gn:long          -2.17432;
        gn:name          "Étier de Méan";
        gn:population    0 .

<https://sws.geonames.org/2971908/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Treillieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2971908;
        gn:lat           47.33117;
        gn:long          -1.62684;
        gn:name          "Treillières";
        gn:population    6572 .

<https://sws.geonames.org/8293035/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Vallet";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293035;
        gn:lat           47.1617;
        gn:long          -1.26624;
        gn:name          "Bureau de Poste de Vallet";
        gn:population    0 .

<https://sws.geonames.org/3030720/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ruisseau du Bouvreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3030720;
        gn:lat           46.93896;
        gn:long          -1.29259;
        gn:name          "Ruisseau du Bouvreau";
        gn:population    0 .

<https://sws.geonames.org/2992925/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montbert";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2992925;
        gn:lat           47.05778;
        gn:long          -1.48873;
        gn:name          "Montbert";
        gn:population    2481 .

<https://sws.geonames.org/12312950/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Vieux Bourg";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312950;
        gn:lat           47.56732;
        gn:long          -1.61332;
        gn:name          "Le Vieux Bourg";
        gn:population    0 .

<https://sws.geonames.org/12313145/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grassiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313145;
        gn:lat           47.16609;
        gn:long          -1.50791;
        gn:name          "La Grassinière";
        gn:population    0 .

<https://sws.geonames.org/8292984/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Plesse";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292984;
        gn:lat           47.5418;
        gn:long          -1.88441;
        gn:name          "Bureau de Poste de Plesse";
        gn:population    0 .

<https://sws.geonames.org/8293052/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Talensac";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293052;
        gn:lat           47.22008;
        gn:long          -1.55588;
        gn:name          "Bureau de Poste de Nantes Talensac";
        gn:population    0 .

<https://sws.geonames.org/10246254/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Atlantys Hatel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10246254;
        gn:lat           47.22797;
        gn:long          -1.63271;
        gn:name          "Atlantys Hatel";
        gn:population    0 .

<https://sws.geonames.org/6435299/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Leger-sous-Cholet";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6435299;
        gn:lat           47.09306;
        gn:long          -0.90972;
        gn:name          "Saint-Léger-sous-Cholet";
        gn:population    2817 .

<https://sws.geonames.org/8292947/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Getigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292947;
        gn:lat           47.07574;
        gn:long          -1.24956;
        gn:name          "Bureau de Poste de Getigne";
        gn:population    0 .

<https://sws.geonames.org/3027008/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Champtoceaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3027008;
        gn:lat           47.33665;
        gn:long          -1.26602;
        gn:name          "Champtoceaux";
        gn:population    1840 .

<https://sws.geonames.org/12313221/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Caradouere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313221;
        gn:lat           47.11564;
        gn:long          -2.07481;
        gn:name          "La Caradouère";
        gn:population    0 .

<https://sws.geonames.org/3037583/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Angrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3037583;
        gn:lat           47.57032;
        gn:long          -0.97445;
        gn:name          "Angrie";
        gn:population    712 .

<https://sws.geonames.org/3017197/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Fresnay-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3017197;
        gn:lat           47.02447;
        gn:long          -1.87596;
        gn:name          "Fresnay-en-Retz";
        gn:population    929 .

<https://sws.geonames.org/3233648/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cannelais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233648;
        gn:lat           47.27385;
        gn:long          -2.00841;
        gn:name          "La Cannelais";
        gn:population    0 .

<https://sws.geonames.org/10297840/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Chateaubriand";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297840;
        gn:lat           47.22199;
        gn:long          -1.55469;
        gn:name          "Hotel Chateaubriand";
        gn:population    0 .

<https://sws.geonames.org/3233465/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bellevue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233465;
        gn:lat           47.25377;
        gn:long          -1.94702;
        gn:name          "Bellevue";
        gn:population    0 .

<https://sws.geonames.org/2978636/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Malo-de-Guersac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978636;
        gn:lat           47.35121;
        gn:long          -2.17962;
        gn:name          "Saint-Malo-de-Guersac";
        gn:population    3408 .

<https://sws.geonames.org/3003615/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Maire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003615;
        gn:lat           47.55752;
        gn:long          -1.58514;
        gn:name          "Le Maire";
        gn:population    0 .

<https://sws.geonames.org/6464553/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Stars Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6464553;
        gn:lat           47.2473;
        gn:long          -1.5039;
        gn:name          "Hotel Stars Nantes";
        gn:population    0 .

<https://sws.geonames.org/3031220/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile de Bouin";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3031220;
        gn:lat           46.96667;
        gn:long          -2.0;
        gn:name          "Île de Bouin";
        gn:population    0 .

<https://sws.geonames.org/6434526/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Lumine-de-Coutais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434526;
        gn:lat           47.05444;
        gn:long          -1.72639;
        gn:name          "Saint-Lumine-de-Coutais";
        gn:population    2128 .

<https://sws.geonames.org/3034699/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Basse-Goulaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3034699;
        gn:lat           47.2151;
        gn:long          -1.46598;
        gn:name          "Basse-Goulaine";
        gn:population    8160 .

<https://sws.geonames.org/6452327/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Anetz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6452327;
        gn:lat           47.38222;
        gn:long          -1.10278;
        gn:name          "Anetz";
        gn:population    1872 .

<https://sws.geonames.org/3031293/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouffere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031293;
        gn:lat           46.96179;
        gn:long          -1.33965;
        gn:name          "Boufféré";
        gn:population    1892 .

<https://sws.geonames.org/6454806/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montaigu-Vendee";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6454806;
        gn:lat           46.9728;
        gn:long          -1.3087;
        gn:name          "Montaigu-Vendée";
        gn:population    20084 .

<https://sws.geonames.org/8286977/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boussay La Bruffiere Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286977;
        gn:lat           47.05061;
        gn:long          -1.18351;
        gn:name          "Boussay La Bruffière Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3028535/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Carquefou";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3028535;
        gn:lat           47.29722;
        gn:long          -1.4921;
        gn:name          "Carquefou";
        gn:population    18056 .

<https://sws.geonames.org/2993092/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montaigu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2993092;
        gn:lat           46.97462;
        gn:long          -1.31067;
        gn:name          "Montaigu";
        gn:population    5070 .

<https://sws.geonames.org/6449087/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Coueron";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449087;
        gn:lat           47.21472;
        gn:long          -1.72389;
        gn:name          "Couëron";
        gn:population    20900 .

<https://sws.geonames.org/12312965/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Plessis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312965;
        gn:lat           47.2565;
        gn:long          -1.66359;
        gn:name          "Le Plessis";
        gn:population    0 .

<https://sws.geonames.org/3008110/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Moncoillere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008110;
        gn:lat           47.13309;
        gn:long          -1.0131;
        gn:name          "La Moncoillère";
        gn:population    0 .

<https://sws.geonames.org/3233928/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Etier de la Coquerais";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.DTCHD;
        gn:geonamesID    3233928;
        gn:lat           47.28417;
        gn:long          -1.90587;
        gn:name          "Étier de la Coquerais";
        gn:population    0 .

<https://sws.geonames.org/8293067/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Reze Pont Rousseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293067;
        gn:lat           47.18932;
        gn:long          -1.55013;
        gn:name          "Bureau de Poste de Reze Pont Rousseau";
        gn:population    0 .

<https://sws.geonames.org/12306350/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Poterie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12306350;
        gn:lat           47.10809;
        gn:long          -1.43823;
        gn:name          "La Poterie";
        gn:population    0 .

<https://sws.geonames.org/12123737/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cathedrale Saint-Pierre-et-Saint-Paul";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.CH;
        gn:geonamesID    12123737;
        gn:lat           47.21851;
        gn:long          -1.55061;
        gn:name          "Cathédrale Saint-Pierre-et-Saint-Paul";
        gn:population    0 .

<https://sws.geonames.org/3012803/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Indret";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3012803;
        gn:lat           47.1967;
        gn:long          -1.68214;
        gn:name          "Indret";
        gn:population    0 .

<https://sws.geonames.org/9177352/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Kyriad  Nantes Est - Carquefou";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177352;
        gn:lat           47.26916;
        gn:long          -1.48523;
        gn:name          "Kyriad  Nantes Est - Carquefou";
        gn:population    0 .

<https://sws.geonames.org/12313194/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Landas";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313194;
        gn:lat           47.19243;
        gn:long          -1.7216;
        gn:name          "Le Landas";
        gn:population    0 .

<https://sws.geonames.org/12902693/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau de la Chardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.CSTL;
        gn:geonamesID    12902693;
        gn:lat           46.90146;
        gn:long          -1.23276;
        gn:name          "Château de la Chardière";
        gn:population    0 .

<https://sws.geonames.org/2982022/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de Saffre";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2982022;
        gn:lat           47.50095;
        gn:long          -1.52631;
        gn:name          "Forêt de Saffré";
        gn:population    0 .

<https://sws.geonames.org/3002483/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Puiset-Dore";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002483;
        gn:lat           47.23143;
        gn:long          -1.11523;
        gn:name          "Le Puiset-Doré";
        gn:population    981 .

<https://sws.geonames.org/6498280/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appart'City Sanitat";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6498280;
        gn:lat           47.2097;
        gn:long          -1.5672;
        gn:name          "Appart'City Sanitat";
        gn:population    0 .

<https://sws.geonames.org/2979109/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Julien-de-Concelles";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979109;
        gn:lat           47.2536;
        gn:long          -1.38568;
        gn:name          "Saint-Julien-de-Concelles";
        gn:population    6758 .

<https://sws.geonames.org/2971903/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Treize-Septiers";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2971903;
        gn:lat           46.985;
        gn:long          -1.23029;
        gn:name          "Treize-Septiers";
        gn:population    2561 .

<https://sws.geonames.org/8293038/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Vieillevigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293038;
        gn:lat           46.9728;
        gn:long          -1.43205;
        gn:name          "Bureau de Poste de Vieillevigne";
        gn:population    0 .

<https://sws.geonames.org/6434514/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Gildas-des-Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434514;
        gn:lat           47.51639;
        gn:long          -2.03833;
        gn:name          "Saint-Gildas-des-Bois";
        gn:population    3776 .

<https://sws.geonames.org/12308487/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fosse A l'Ane";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308487;
        gn:lat           47.27246;
        gn:long          -1.13035;
        gn:name          "La Fosse À l'Âne";
        gn:population    0 .

<https://sws.geonames.org/3233427/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Port de Comberge";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.HBR;
        gn:geonamesID    3233427;
        gn:lat           47.17583;
        gn:long          -2.16549;
        gn:name          "Port de Comberge";
        gn:population    0 .

<https://sws.geonames.org/3233675/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Babinais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233675;
        gn:lat           47.30861;
        gn:long          -1.90393;
        gn:name          "La Babinais";
        gn:population    0 .

<https://sws.geonames.org/2998626/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Herbergement";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998626;
        gn:lat           46.90892;
        gn:long          -1.37648;
        gn:name          "L'Herbergement";
        gn:population    0 .

<https://sws.geonames.org/12253606/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Hayes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12253606;
        gn:lat           47.17432;
        gn:long          -0.93766;
        gn:name          "Les Hayes";
        gn:population    0 .

<https://sws.geonames.org/3003023/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pasbou";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    3003023;
        gn:lat           47.48366;
        gn:long          -1.28856;
        gn:name          "Le Pasbou";
        gn:population    0 .

<https://sws.geonames.org/8293001/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Gildas Des Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293001;
        gn:lat           47.51575;
        gn:long          -2.03833;
        gn:name          "Bureau de Poste de Saint Gildas Des Bois";
        gn:population    0 .

<https://sws.geonames.org/6434500/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Prinquiau";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434500;
        gn:lat           47.36278;
        gn:long          -2.01111;
        gn:name          "Prinquiau";
        gn:population    3476 .

<https://sws.geonames.org/6458673/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Christophe-la-Couperie";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6458673;
        gn:lat           47.25429;
        gn:long          -1.18042;
        gn:name          "Saint-Christophe-la-Couperie";
        gn:population    757 .

<https://sws.geonames.org/12313140/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grande Noe";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313140;
        gn:lat           47.16338;
        gn:long          -1.45213;
        gn:name          "La Grande Noë";
        gn:population    0 .

<https://sws.geonames.org/12312957/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312957;
        gn:lat           47.25851;
        gn:long          -1.52637;
        gn:name          "La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/3003912/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Egreniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003912;
        gn:lat           47.00921;
        gn:long          -1.42634;
        gn:name          "L'Égrenière";
        gn:population    0 .

<https://sws.geonames.org/12313003/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Hotel Menant";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313003;
        gn:lat           47.57269;
        gn:long          -2.04793;
        gn:name          "L'Hôtel Ménant";
        gn:population    0 .

<https://sws.geonames.org/8293007/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Decre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293007;
        gn:lat           47.21586;
        gn:long          -1.55441;
        gn:name          "Bureau de Poste de Nantes Decre";
        gn:population    0 .

<https://sws.geonames.org/2986590/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pocazet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2986590;
        gn:lat           47.43548;
        gn:long          -2.01238;
        gn:name          "Pocazet";
        gn:population    0 .

<https://sws.geonames.org/3028851/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cande";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3028851;
        gn:lat           47.56077;
        gn:long          -1.03739;
        gn:name          "Candé";
        gn:population    2755 .

<https://sws.geonames.org/3006739/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Romagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006739;
        gn:lat           47.0611;
        gn:long          -1.02167;
        gn:name          "La Romagne";
        gn:population    1652 .

<https://sws.geonames.org/2998593/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Hommetiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998593;
        gn:lat           46.96821;
        gn:long          -1.42238;
        gn:name          "L'Hommetière";
        gn:population    0 .

<https://sws.geonames.org/9178557/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quality Hotel & Suites Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178557;
        gn:lat           47.25225;
        gn:long          -1.51182;
        gn:name          "Quality Hotel & Suites Nantes";
        gn:population    0 .

<https://sws.geonames.org/6457139/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bruffiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6457139;
        gn:lat           47.01306;
        gn:long          -1.19778;
        gn:name          "La Bruffière";
        gn:population    3921 .

<https://sws.geonames.org/12312883/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Clancheliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312883;
        gn:lat           47.57015;
        gn:long          -1.18585;
        gn:name          "La Clanchelière";
        gn:population    0 .

<https://sws.geonames.org/12312935/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Simonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312935;
        gn:lat           47.31892;
        gn:long          -1.38989;
        gn:name          "La Simonnière";
        gn:population    0 .

<https://sws.geonames.org/3233415/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tapis Vert";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233415;
        gn:lat           47.08333;
        gn:long          -2.09917;
        gn:name          "Tapis Vert";
        gn:population    0 .

<https://sws.geonames.org/8293400/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Christophe Du Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293400;
        gn:lat           47.02694;
        gn:long          -0.9478;
        gn:name          "Bureau de Poste de Saint Christophe Du Bois";
        gn:population    0 .

<https://sws.geonames.org/2988520/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Parignac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2988520;
        gn:lat           47.42789;
        gn:long          -1.80474;
        gn:name          "Parignac";
        gn:population    0 .

<https://sws.geonames.org/3009145/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gautrais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009145;
        gn:lat           47.38056;
        gn:long          -2.11497;
        gn:name          "La Gautrais";
        gn:population    0 .

<https://sws.geonames.org/2999828/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Railleres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999828;
        gn:lat           47.18631;
        gn:long          -1.31179;
        gn:name          "Les Raillères";
        gn:population    0 .

<https://sws.geonames.org/2993619/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Moine";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2993619;
        gn:lat           47.08666;
        gn:long          -1.2775;
        gn:name          "Moine";
        gn:population    0 .

<https://sws.geonames.org/6456088/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Renaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456088;
        gn:lat           47.12056;
        gn:long          -1.05972;
        gn:name          "La Renaudière";
        gn:population    937 .

<https://sws.geonames.org/2999937/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Planches";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999937;
        gn:lat           47.24917;
        gn:long          -1.40285;
        gn:name          "Les Planches";
        gn:population    0 .

<https://sws.geonames.org/6434556/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Loireauxence";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434556;
        gn:lat           47.38444;
        gn:long          -1.03;
        gn:name          "Loireauxence";
        gn:population    7540 .

<https://sws.geonames.org/6449097/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Frossay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449097;
        gn:lat           47.24389;
        gn:long          -1.93417;
        gn:name          "Frossay";
        gn:population    3227 .

<https://sws.geonames.org/2979166/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Joseph";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    2979166;
        gn:lat           47.23333;
        gn:long          -1.55;
        gn:name          "Saint-Joseph";
        gn:population    0 .

<https://sws.geonames.org/10297847/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Apts Adagio Access Nantes Sextant";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297847;
        gn:lat           47.20669;
        gn:long          -1.57929;
        gn:name          "Apts Adagio Access Nantes Sextant";
        gn:population    0 .

<https://sws.geonames.org/2988582/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret du Parc";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2988582;
        gn:lat           47.55619;
        gn:long          -1.88114;
        gn:name          "Forêt du Parc";
        gn:population    0 .

<https://sws.geonames.org/2994668/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Melleray-Abbaye";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2994668;
        gn:lat           47.54833;
        gn:long          -1.3775;
        gn:name          "Melleray-Abbaye";
        gn:population    0 .

<https://sws.geonames.org/8292970/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Montbert";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292970;
        gn:lat           47.05587;
        gn:long          -1.48766;
        gn:name          "Bureau de Poste de Montbert";
        gn:population    0 .

<https://sws.geonames.org/3033802/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Belebat";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3033802;
        gn:lat           47.34607;
        gn:long          -1.97703;
        gn:name          "Belébat";
        gn:population    0 .

<https://sws.geonames.org/11906048/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Parc de Proce";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.PRK;
        gn:geonamesID    11906048;
        gn:lat           47.22437;
        gn:long          -1.58238;
        gn:name          "Parc de Procé";
        gn:population    0 .

<https://sws.geonames.org/12313105/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Paradis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313105;
        gn:lat           47.17417;
        gn:long          -1.39058;
        gn:name          "Le Paradis";
        gn:population    0 .

<https://sws.geonames.org/2967992/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de Vioreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2967992;
        gn:lat           47.54367;
        gn:long          -1.41567;
        gn:name          "Forêt de Vioreau";
        gn:population    0 .

<https://sws.geonames.org/3006433/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Sennetiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLX;
        gn:geonamesID    3006433;
        gn:lat           47.07468;
        gn:long          -2.02389;
        gn:name          "La Sennetière";
        gn:population    0 .

<https://sws.geonames.org/8292979/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Paimboeuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292979;
        gn:lat           47.2853;
        gn:long          -2.02489;
        gn:name          "Bureau de Poste de Paimboeuf";
        gn:population    0 .

<https://sws.geonames.org/6445176/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Aubin-des-Ormeaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6445176;
        gn:lat           46.99139;
        gn:long          -1.04333;
        gn:name          "Saint-Aubin-des-Ormeaux";
        gn:population    1341 .

<https://sws.geonames.org/8292907/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Arthon En Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292907;
        gn:lat           47.1168;
        gn:long          -1.94417;
        gn:name          "Bureau de Poste de Arthon En Retz";
        gn:population    0 .

<https://sws.geonames.org/6456921/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Meilleraye-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456921;
        gn:lat           47.55972;
        gn:long          -1.40139;
        gn:name          "La Meilleraye-de-Bretagne";
        gn:population    1512 .

<https://sws.geonames.org/12308435/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Vieux Bourg";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308435;
        gn:lat           47.36202;
        gn:long          -1.03466;
        gn:name          "Le Vieux Bourg";
        gn:population    0 .

<https://sws.geonames.org/12310642/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Templerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310642;
        gn:lat           46.93158;
        gn:long          -1.30344;
        gn:name          "La Templerie";
        gn:population    0 .

<https://sws.geonames.org/12313216/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chalopiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313216;
        gn:lat           47.12596;
        gn:long          -2.07928;
        gn:name          "La Chalopinière";
        gn:population    0 .

<https://sws.geonames.org/8286996/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montaigu-Vendee Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286996;
        gn:lat           46.98375;
        gn:long          -1.31648;
        gn:name          "Montaigu-Vendée Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12312999/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Touche Saint-Armel";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312999;
        gn:lat           47.57274;
        gn:long          -2.01245;
        gn:name          "La Touche Saint-Armel";
        gn:population    0 .

<https://sws.geonames.org/3233385/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roches de la Preoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233385;
        gn:lat           47.00582;
        gn:long          -2.10834;
        gn:name          "Roches de la Préoire";
        gn:population    0 .

<https://sws.geonames.org/3006653/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roussellerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006653;
        gn:lat           47.19572;
        gn:long          -2.15226;
        gn:name          "La Roussellerie";
        gn:population    0 .

<https://sws.geonames.org/3233494/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roches de la Banche";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233494;
        gn:lat           47.20472;
        gn:long          -2.15889;
        gn:name          "Roches de la Banche";
        gn:population    0 .

<https://sws.geonames.org/3009628/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Douettee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009628;
        gn:lat           47.50285;
        gn:long          -1.91845;
        gn:name          "La Douettée";
        gn:population    0 .

<https://sws.geonames.org/12305882/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Madeleine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305882;
        gn:lat           47.277;
        gn:long          -1.48435;
        gn:name          "La Madeleine";
        gn:population    0 .

<https://sws.geonames.org/2972613/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tiffauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2972613;
        gn:lat           47.01288;
        gn:long          -1.11173;
        gn:name          "Tiffauges";
        gn:population    1437 .

<https://sws.geonames.org/3011001/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boissiere-du-Dore";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011001;
        gn:lat           47.23333;
        gn:long          -1.21667;
        gn:name          "La Boissière-du-Doré";
        gn:population    0 .

<https://sws.geonames.org/3004329/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Doucet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004329;
        gn:lat           47.2775;
        gn:long          -1.63345;
        gn:name          "Le Doucet";
        gn:population    0 .

<https://sws.geonames.org/3031754/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bonne Fontaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031754;
        gn:lat           47.16047;
        gn:long          -1.30393;
        gn:name          "Bonne Fontaine";
        gn:population    0 .

<https://sws.geonames.org/2969111/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vigneux-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2969111;
        gn:lat           47.32545;
        gn:long          -1.73732;
        gn:name          "Vigneux-de-Bretagne";
        gn:population    5095 .

<https://sws.geonames.org/3010321/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Heulin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010321;
        gn:lat           47.1768;
        gn:long          -1.3407;
        gn:name          "La Chapelle-Heulin";
        gn:population    1997 .

<https://sws.geonames.org/3233457/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Peille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233457;
        gn:lat           47.27683;
        gn:long          -1.85929;
        gn:name          "La Peille";
        gn:population    0 .

<https://sws.geonames.org/8292932/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Chevroliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292932;
        gn:lat           47.09213;
        gn:long          -1.61208;
        gn:name          "Bureau de Poste de La Chevroliere";
        gn:population    0 .

<https://sws.geonames.org/2999231/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Tertre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999231;
        gn:lat           47.28619;
        gn:long          -1.85916;
        gn:name          "Le Tertre";
        gn:population    0 .

<https://sws.geonames.org/12494116/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Graslin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLX;
        gn:geonamesID    12494116;
        gn:lat           47.21375;
        gn:long          -1.56331;
        gn:name          "Graslin";
        gn:population    0 .

<https://sws.geonames.org/3030822/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boussay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3030822;
        gn:lat           47.04389;
        gn:long          -1.18697;
        gn:name          "Boussay";
        gn:population    2553 .

<https://sws.geonames.org/2973748/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Suce-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2973748;
        gn:lat           47.33333;
        gn:long          -1.53333;
        gn:name          "Sucé-sur-Erdre";
        gn:population    6335 .

<https://sws.geonames.org/12313001/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trenneban";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313001;
        gn:lat           47.59252;
        gn:long          -2.03155;
        gn:name          "Trenneban";
        gn:population    0 .

<https://sws.geonames.org/2988797/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Paimboeuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2988797;
        gn:lat           47.28654;
        gn:long          -2.03048;
        gn:name          "Paimboeuf";
        gn:population    3015 .

<https://sws.geonames.org/6499327/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Kyriad - Nantes Centre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6499327;
        gn:lat           47.2175;
        gn:long          -1.5443;
        gn:name          "Kyriad - Nantes Centre";
        gn:population    0 .

<https://sws.geonames.org/10297829/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Renova";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297829;
        gn:lat           47.21488;
        gn:long          -1.5553;
        gn:name          "Hôtel Renova";
        gn:population    0 .

<https://sws.geonames.org/6449079/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Carquefou";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449079;
        gn:lat           47.29694;
        gn:long          -1.49278;
        gn:name          "Carquefou";
        gn:population    19384 .

<https://sws.geonames.org/2980345/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Reine-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980345;
        gn:lat           47.44071;
        gn:long          -2.19393;
        gn:name          "Sainte-Reine-de-Bretagne";
        gn:population    1829 .

<https://sws.geonames.org/12312972/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Primais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312972;
        gn:lat           47.41143;
        gn:long          -1.72357;
        gn:name          "La Primais";
        gn:population    0 .

<https://sws.geonames.org/8287012/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pontchateau Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287012;
        gn:lat           47.43518;
        gn:long          -2.08821;
        gn:name          "Pontchâteau Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3025609/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chemere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3025609;
        gn:lat           47.11667;
        gn:long          -1.91667;
        gn:name          "Chéméré";
        gn:population    1707 .

<https://sws.geonames.org/12310634/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Andoussiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310634;
        gn:lat           46.94359;
        gn:long          -1.40786;
        gn:name          "L'Andoussière";
        gn:population    0 .

<https://sws.geonames.org/8293074/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Orvault Place Jeanne D Arc";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293074;
        gn:lat           47.27069;
        gn:long          -1.62206;
        gn:name          "Bureau de Poste de Orvault Place Jeanne D Arc";
        gn:population    0 .

<https://sws.geonames.org/3003042/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pallet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003042;
        gn:lat           47.13842;
        gn:long          -1.33609;
        gn:name          "Le Pallet";
        gn:population    2574 .

<https://sws.geonames.org/12313208/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Haute Perche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313208;
        gn:lat           47.13136;
        gn:long          -1.97028;
        gn:name          "Haute Perche";
        gn:population    0 .

<https://sws.geonames.org/3019439/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gare de l'Etat";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    3019439;
        gn:lat           47.20283;
        gn:long          -1.56384;
        gn:name          "Gare de l'État";
        gn:population    0 .

<https://sws.geonames.org/10173531/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nantes Sud Bouaye ARoport";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10173531;
        gn:lat           47.143;
        gn:long          -1.662;
        gn:name          "Nantes Sud Bouaye ARoport";
        gn:population    0 .

<https://sws.geonames.org/12310624/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fosse Neuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310624;
        gn:lat           46.95508;
        gn:long          -1.23033;
        gn:name          "Le Fossé Neuf";
        gn:population    0 .

<https://sws.geonames.org/6475376/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Holiday Inn Garden Court Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6475376;
        gn:lat           47.2069;
        gn:long          -1.5481;
        gn:name          "Holiday Inn Garden Court Nantes";
        gn:population    0 .

<https://sws.geonames.org/2995692/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Canal Maritime";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    2995692;
        gn:lat           47.26667;
        gn:long          -1.95;
        gn:name          "Canal Maritime";
        gn:population    0 .

<https://sws.geonames.org/3010907/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bouhonnais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010907;
        gn:lat           47.445;
        gn:long          -1.78405;
        gn:name          "La Bouhonnais";
        gn:population    0 .

<https://sws.geonames.org/8293409/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Pierre Montlimart";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293409;
        gn:lat           47.26982;
        gn:long          -1.02591;
        gn:name          "Bureau de Poste de Saint Pierre Montlimart";
        gn:population    0 .

<https://sws.geonames.org/3002134/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Ardilliers";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002134;
        gn:lat           46.9114;
        gn:long          -1.06041;
        gn:name          "Les Ardilliers";
        gn:population    0 .

<https://sws.geonames.org/10282271/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quality Suites Nantes Atlantique";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10282271;
        gn:lat           47.21944;
        gn:long          -1.56158;
        gn:name          "Quality Suites Nantes Atlantique";
        gn:population    0 .

<https://sws.geonames.org/3000756/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Grees";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000756;
        gn:lat           47.58314;
        gn:long          -1.58486;
        gn:name          "Les Grées";
        gn:population    0 .

<https://sws.geonames.org/3004640/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Chene des Perrieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSEC;
        gn:geonamesID    3004640;
        gn:lat           47.35861;
        gn:long          -1.7637;
        gn:name          "Le Chêne des Perrières";
        gn:population    0 .

<https://sws.geonames.org/6445151/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mortagne-sur-Sevre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6445151;
        gn:lat           46.99167;
        gn:long          -0.95389;
        gn:name          "Mortagne-sur-Sèvre";
        gn:population    5976 .

<https://sws.geonames.org/3018185/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois de la Foi";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    3018185;
        gn:lat           47.58982;
        gn:long          -1.4191;
        gn:name          "Bois de la Foi";
        gn:population    0 .

<https://sws.geonames.org/8293060/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Chauviniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293060;
        gn:lat           47.25373;
        gn:long          -1.57473;
        gn:name          "Bureau de Poste de Nantes Chauviniere";
        gn:population    0 .

<https://sws.geonames.org/3010112/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chaussaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010112;
        gn:lat           47.20048;
        gn:long          -1.1456;
        gn:name          "La Chaussaire";
        gn:population    695 .

<https://sws.geonames.org/8292974/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nort Sur Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292974;
        gn:lat           47.4424;
        gn:long          -1.49625;
        gn:name          "Bureau de Poste de Nort Sur Erdre";
        gn:population    0 .

<https://sws.geonames.org/12313135/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Profondine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313135;
        gn:lat           47.19302;
        gn:long          -1.49041;
        gn:name          "La Profondine";
        gn:population    0 .

<https://sws.geonames.org/3233979/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chabossiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233979;
        gn:lat           47.21557;
        gn:long          -1.68323;
        gn:name          "La Chabossière";
        gn:population    0 .

<https://sws.geonames.org/6435289/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Germain-sur-Moine";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435289;
        gn:lat           47.11778;
        gn:long          -1.12278;
        gn:name          "Saint-Germain-sur-Moine";
        gn:population    2771 .

<https://sws.geonames.org/2985932/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Port-Saint-Pere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2985932;
        gn:lat           47.13354;
        gn:long          -1.74911;
        gn:name          "Port-Saint-Père";
        gn:population    2306 .

<https://sws.geonames.org/12313120/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Trelitiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313120;
        gn:lat           47.08854;
        gn:long          -1.4041;
        gn:name          "La Trélitière";
        gn:population    0 .

<https://sws.geonames.org/6616811/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Moutiers-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616811;
        gn:lat           47.0637;
        gn:long          -2.0008;
        gn:name          "Les Moutiers-en-Retz";
        gn:population    1576 .

<https://sws.geonames.org/2977052/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sauveur-de-Landemont";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977052;
        gn:lat           47.28333;
        gn:long          -1.25;
        gn:name          "Saint-Sauveur-de-Landemont";
        gn:population    0 .

<https://sws.geonames.org/11746353/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arcades du Mesnil";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNLA;
        gn:geonamesID    11746353;
        gn:lat           47.49376;
        gn:long          -1.45849;
        gn:name          "Arcades du Mesnil";
        gn:population    0 .

<https://sws.geonames.org/2977168/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Roch";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977168;
        gn:lat           47.40547;
        gn:long          -2.05345;
        gn:name          "Saint-Roch";
        gn:population    0 .

<https://sws.geonames.org/3002088/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Aulnais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002088;
        gn:lat           47.40821;
        gn:long          -1.89356;
        gn:name          "Les Aulnais";
        gn:population    0 .

<https://sws.geonames.org/11185790/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaye de Pontron";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSTS;
        gn:geonamesID    11185790;
        gn:lat           47.50612;
        gn:long          -0.94671;
        gn:name          "Abbaye de Pontron";
        gn:population    0 .

<https://sws.geonames.org/12324070/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quartier d'Assac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12324070;
        gn:lat           47.32402;
        gn:long          -2.03851;
        gn:name          "Quartier d'Assac";
        gn:population    0 .

<https://sws.geonames.org/12310649/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Menardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310649;
        gn:lat           46.90764;
        gn:long          -1.26758;
        gn:name          "La Ménardière";
        gn:population    0 .

<https://sws.geonames.org/11746343/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arcades du Mesnil";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.ARCH;
        gn:geonamesID    11746343;
        gn:lat           47.4937;
        gn:long          -1.45846;
        gn:name          "Arcades du Mesnil";
        gn:population    0 .

<https://sws.geonames.org/6434516/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vair-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434516;
        gn:lat           47.40833;
        gn:long          -1.09583;
        gn:name          "Vair-sur-Loire";
        gn:population    4624 .

<https://sws.geonames.org/2978520/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Mars-la-Jaille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978520;
        gn:lat           47.52538;
        gn:long          -1.18465;
        gn:name          "Saint-Mars-la-Jaille";
        gn:population    2371 .

<https://sws.geonames.org/3007700/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Anglesort";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007700;
        gn:lat           47.22024;
        gn:long          -1.40071;
        gn:name          "L'Anglesort";
        gn:population    0 .

<https://sws.geonames.org/2973003/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Tharon-Plage";
        <https://schema.org/elevation>  12.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:P;
        gn:featureCode                  gn:P.PPL;
        gn:geonamesID                   2973003;
        gn:lat                          47.165;
        gn:long                         -2.1631;
        gn:name                         "Tharon-Plage";
        gn:population                   0 .

<https://sws.geonames.org/12313079/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Moussaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313079;
        gn:lat           47.04232;
        gn:long          -1.17043;
        gn:name          "La Moussaudière";
        gn:population    0 .

<https://sws.geonames.org/6490226/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "WESTOTEL Nantes-Atlantique";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6490226;
        gn:lat           47.2829;
        gn:long          -1.55085;
        gn:name          "WESTOTEL Nantes-Atlantique";
        gn:population    0 .

<https://sws.geonames.org/12305889/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bas Briace";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305889;
        gn:lat           47.19572;
        gn:long          -1.34565;
        gn:name          "Bas Briacé";
        gn:population    0 .

<https://sws.geonames.org/2983901/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bois de Restin";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2983901;
        gn:lat           47.53286;
        gn:long          -2.06143;
        gn:name          "Bois de Restin";
        gn:population    0 .

<https://sws.geonames.org/8292960/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Bourgeonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292960;
        gn:lat           47.25335;
        gn:long          -1.5594;
        gn:name          "Bureau de Poste de Nantes Bourgeonniere";
        gn:population    0 .

<https://sws.geonames.org/7535063/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Golf Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RECG;
        gn:geonamesID    7535063;
        gn:lat           47.32715;
        gn:long          -1.74748;
        gn:name          "Golf Nantes";
        gn:population    0 .

<https://sws.geonames.org/2989876/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nozay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2989876;
        gn:lat           47.56473;
        gn:long          -1.62559;
        gn:name          "Nozay";
        gn:population    3419 .

<https://sws.geonames.org/3026985/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chanais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3026985;
        gn:lat           47.35941;
        gn:long          -1.66191;
        gn:name          "Chanais";
        gn:population    0 .

<https://sws.geonames.org/3009246/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Furetiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009246;
        gn:lat           47.40703;
        gn:long          -1.45965;
        gn:name          "La Furetière";
        gn:population    0 .

<https://sws.geonames.org/6501022/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "My Suite St Nazaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6501022;
        gn:lat           47.3034;
        gn:long          -2.1843;
        gn:name          "My Suite St Nazaire";
        gn:population    0 .

<https://sws.geonames.org/6456953/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Saint-Florent";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456953;
        gn:lat           47.33361;
        gn:long          -1.05583;
        gn:name          "La Chapelle-Saint-Florent";
        gn:population    1250 .

<https://sws.geonames.org/3009231/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gandiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009231;
        gn:lat           47.30119;
        gn:long          -1.71095;
        gn:name          "La Gandinière";
        gn:population    0 .

<https://sws.geonames.org/8292966/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Mesanger";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292966;
        gn:lat           47.4327;
        gn:long          -1.22875;
        gn:name          "Bureau de Poste de Mesanger";
        gn:population    0 .

<https://sws.geonames.org/12310632/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roche Pepin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310632;
        gn:lat           46.93676;
        gn:long          -1.25889;
        gn:name          "La Roche Pépin";
        gn:population    0 .

<https://sws.geonames.org/12320451/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Burin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12320451;
        gn:lat           47.5005;
        gn:long          -2.17792;
        gn:name          "Burin";
        gn:population    0 .

<https://sws.geonames.org/2985487/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Prefoure";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2985487;
        gn:lat           47.58958;
        gn:long          -1.01097;
        gn:name          "Préfoure";
        gn:population    0 .

<https://sws.geonames.org/9178637/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Radisson Blu Hotel Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178637;
        gn:lat           47.21749;
        gn:long          -1.56283;
        gn:name          "Radisson Blu Hotel Nantes";
        gn:population    0 .

<https://sws.geonames.org/12313008/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Normandais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313008;
        gn:lat           47.55715;
        gn:long          -2.05462;
        gn:name          "La Normandais";
        gn:population    0 .

<https://sws.geonames.org/10111752/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brit Hotel Cholet L'azur";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10111752;
        gn:lat           47.1008;
        gn:long          -0.9943;
        gn:name          "Brit Hotel Cholet L'azur";
        gn:population    0 .

<https://sws.geonames.org/12310637/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Ardoisiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310637;
        gn:lat           46.9262;
        gn:long          -1.8071;
        gn:name          "L'Ardoisière";
        gn:population    0 .

<https://sws.geonames.org/3005031/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Breil";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005031;
        gn:lat           47.41667;
        gn:long          -1.8;
        gn:name          "Le Breil";
        gn:population    0 .

<https://sws.geonames.org/12313112/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rebourgere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313112;
        gn:lat           47.12522;
        gn:long          -1.37518;
        gn:name          "La Rebourgère";
        gn:population    0 .

<https://sws.geonames.org/12312959/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Dervallieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312959;
        gn:lat           47.22542;
        gn:long          -1.5937;
        gn:name          "Les Dervallières";
        gn:population    0 .

<https://sws.geonames.org/3233923/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bras du Migron";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STMA;
        gn:geonamesID    3233923;
        gn:lat           47.28036;
        gn:long          -1.9837;
        gn:name          "Bras du Migron";
        gn:population    0 .

<https://sws.geonames.org/12313020/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Caudry";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313020;
        gn:lat           47.36907;
        gn:long          -2.02299;
        gn:name          "Caudry";
        gn:population    0 .

<https://sws.geonames.org/12305877/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Salle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305877;
        gn:lat           47.55637;
        gn:long          -1.19272;
        gn:name          "La Salle";
        gn:population    0 .

<https://sws.geonames.org/3008072/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mornais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008072;
        gn:lat           47.32988;
        gn:long          -2.02488;
        gn:name          "La Mornais";
        gn:population    0 .

<https://sws.geonames.org/3010838/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bouzenais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010838;
        gn:lat           47.48702;
        gn:long          -1.56215;
        gn:name          "La Bouzenais";
        gn:population    0 .

<https://sws.geonames.org/12312885/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bohiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312885;
        gn:lat           47.55337;
        gn:long          -1.18477;
        gn:name          "La Bohinière";
        gn:population    0 .

<https://sws.geonames.org/3233417/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe de Noeveillard";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    3233417;
        gn:lat           47.10889;
        gn:long          -2.11444;
        gn:name          "Pointe de Noëveillard";
        gn:population    0 .

<https://sws.geonames.org/2967562/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vritz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2967562;
        gn:lat           47.58146;
        gn:long          -1.07024;
        gn:name          "Vritz";
        gn:population    855 .

<https://sws.geonames.org/9178151/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Novotel Nantes Centre Cite Des Congres";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178151;
        gn:lat           47.2139;
        gn:long          -1.54292;
        gn:name          "Novotel Nantes Centre Cité Des Congrès";
        gn:population    0 .

<https://sws.geonames.org/2995507/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Marsac-sur-Don";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2995507;
        gn:lat           47.59481;
        gn:long          -1.68031;
        gn:name          "Marsac-sur-Don";
        gn:population    1305 .

<https://sws.geonames.org/6451597/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouffere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6451597;
        gn:lat           46.96139;
        gn:long          -1.34028;
        gn:name          "Boufféré";
        gn:population    2829 .

<https://sws.geonames.org/12312947/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Linot";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312947;
        gn:lat           47.24809;
        gn:long          -1.47455;
        gn:name          "Le Linot";
        gn:population    0 .

<https://sws.geonames.org/3008671/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Aiguillette";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008671;
        gn:lat           47.12857;
        gn:long          -1.29369;
        gn:name          "L'Aiguillette";
        gn:population    0 .

<https://sws.geonames.org/12312920/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Mazeries";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312920;
        gn:lat           47.38738;
        gn:long          -1.3104;
        gn:name          "Les Mazeries";
        gn:population    0 .

<https://sws.geonames.org/3011329/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Barre-Peinte";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011329;
        gn:lat           47.3425;
        gn:long          -1.34618;
        gn:name          "La Barre-Peinte";
        gn:population    0 .

<https://sws.geonames.org/6456023/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pellerin";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456023;
        gn:lat           47.19833;
        gn:long          -1.75389;
        gn:name          "Le Pellerin";
        gn:population    5050 .

<https://sws.geonames.org/11746357/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gue de la Roche";
        gn:countryCode   "FR";
        gn:featureClass  gn:R;
        gn:featureCode   gn:R.RD;
        gn:geonamesID    11746357;
        gn:lat           47.49089;
        gn:long          -1.46692;
        gn:name          "Gué de la Roche";
        gn:population    0 .

<https://sws.geonames.org/6445198/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Hilaire-de-Loulay";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6445198;
        gn:lat           47.00306;
        gn:long          -1.33083;
        gn:name          "Saint-Hilaire-de-Loulay";
        gn:population    4164 .

<https://sws.geonames.org/12313077/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Anerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313077;
        gn:lat           47.06767;
        gn:long          -1.22574;
        gn:name          "L'Ânerie";
        gn:population    0 .

<https://sws.geonames.org/8293396/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Romagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293396;
        gn:lat           47.0612;
        gn:long          -1.02304;
        gn:name          "Bureau de Poste de La Romagne";
        gn:population    0 .

<https://sws.geonames.org/3233387/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fain";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CHN;
        gn:geonamesID    3233387;
        gn:lat           46.98899;
        gn:long          -2.09677;
        gn:name          "Le Fain";
        gn:population    0 .

<https://sws.geonames.org/3035040/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Barbechat";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3035040;
        gn:lat           47.2775;
        gn:long          -1.28524;
        gn:name          "Barbechat";
        gn:population    1140 .

<https://sws.geonames.org/3233496/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Ermitage";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233496;
        gn:lat           47.2078;
        gn:long          -2.15436;
        gn:name          "L'Ermitage";
        gn:population    0 .

<https://sws.geonames.org/3009041/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gouberte";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009041;
        gn:lat           47.09214;
        gn:long          -1.0225;
        gn:name          "La Gouberte";
        gn:population    0 .

<https://sws.geonames.org/3004813/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Cellier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004813;
        gn:lat           47.31964;
        gn:long          -1.34716;
        gn:name          "Le Cellier";
        gn:population    3596 .

<https://sws.geonames.org/3038716/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Acheneau";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3038716;
        gn:lat           47.19394;
        gn:long          -1.85367;
        gn:name          "Acheneau";
        gn:population    0 .

<https://sws.geonames.org/8293374/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Landemont";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293374;
        gn:lat           47.26592;
        gn:long          -1.24272;
        gn:name          "Bureau de Poste de Landemont";
        gn:population    0 .

<https://sws.geonames.org/3009249/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fromaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009249;
        gn:lat           46.99936;
        gn:long          -1.23746;
        gn:name          "La Fromaudière";
        gn:population    0 .

<https://sws.geonames.org/2977614/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Pere-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977614;
        gn:lat           47.20703;
        gn:long          -2.04497;
        gn:name          "Saint-Père-en-Retz";
        gn:population    3882 .

<https://sws.geonames.org/10111590/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Urbanstyle Graslin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10111590;
        gn:lat           47.21224;
        gn:long          -1.56184;
        gn:name          "Urbanstyle Graslin";
        gn:population    0 .

<https://sws.geonames.org/8293020/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Sebastien Sur Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293020;
        gn:lat           47.20751;
        gn:long          -1.50533;
        gn:name          "Bureau de Poste de Saint Sebastien Sur Loire";
        gn:population    0 .

<https://sws.geonames.org/8292969/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Montagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292969;
        gn:lat           47.19003;
        gn:long          -1.68418;
        gn:name          "Bureau de Poste de La Montagne";
        gn:population    0 .

<https://sws.geonames.org/9174128/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Comfort Hotel Nantes Astoria";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9174128;
        gn:lat           47.21779;
        gn:long          -1.54388;
        gn:name          "Comfort Hotel Nantes Astoria";
        gn:population    0 .

<https://sws.geonames.org/6435312/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Quentin-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435312;
        gn:lat           47.29194;
        gn:long          -0.91306;
        gn:name          "Saint-Quentin-en-Mauges";
        gn:population    1030 .

<https://sws.geonames.org/12313110/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Petiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313110;
        gn:lat           47.15097;
        gn:long          -1.41075;
        gn:name          "La Pétière";
        gn:population    0 .

<https://sws.geonames.org/8292915/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Bouaye";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292915;
        gn:lat           47.1424;
        gn:long          -1.69235;
        gn:name          "Bureau de Poste de Bouaye";
        gn:population    0 .

<https://sws.geonames.org/3008595/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Jauseliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008595;
        gn:lat           47.10514;
        gn:long          -2.07883;
        gn:name          "La Jauselière";
        gn:population    0 .

<https://sws.geonames.org/3010794/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Briantiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010794;
        gn:lat           47.37107;
        gn:long          -1.35226;
        gn:name          "La Briantière";
        gn:population    0 .

<https://sws.geonames.org/12312984/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Guiguenais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312984;
        gn:lat           47.55598;
        gn:long          -1.91533;
        gn:name          "La Guiguenais";
        gn:population    0 .

<https://sws.geonames.org/2978004/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Michel-Chef-Chef";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978004;
        gn:lat           47.18047;
        gn:long          -2.15709;
        gn:name          "Saint-Michel-Chef-Chef";
        gn:population    3435 .

<https://sws.geonames.org/8286986/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bernerie Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286986;
        gn:lat           47.08343;
        gn:long          -2.03429;
        gn:name          "La Bernerie Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12313188/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Tertre du Buchelier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313188;
        gn:lat           47.21564;
        gn:long          -1.73286;
        gn:name          "Le Tertre du Buchelier";
        gn:population    0 .

<https://sws.geonames.org/12313023/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Calvaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313023;
        gn:lat           47.44153;
        gn:long          -2.13893;
        gn:name          "Le Calvaire";
        gn:population    0 .

<https://sws.geonames.org/3007006/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Regeserie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007006;
        gn:lat           47.47059;
        gn:long          -1.17523;
        gn:name          "La Regeserie";
        gn:population    0 .

<https://sws.geonames.org/12312974/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Buchere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312974;
        gn:lat           47.38357;
        gn:long          -1.73306;
        gn:name          "La Buchère";
        gn:population    0 .

<https://sws.geonames.org/7116363/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ecole des mines de Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.SCH;
        gn:geonamesID    7116363;
        gn:lat           47.28223;
        gn:long          -1.52081;
        gn:name          "Ecole des mines de Nantes";
        gn:population    0 .

<https://sws.geonames.org/8293076/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Beaulieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293076;
        gn:lat           47.20622;
        gn:long          -1.53235;
        gn:name          "Bureau de Poste de Nantes Beaulieu";
        gn:population    0 .

<https://sws.geonames.org/3003964/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Patis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003964;
        gn:lat           47.37417;
        gn:long          -1.45107;
        gn:name          "Le Grand Pâtis";
        gn:population    0 .

<https://sws.geonames.org/12313166/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Marboeuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313166;
        gn:lat           47.06553;
        gn:long          -1.52261;
        gn:name          "Marbœuf";
        gn:population    0 .

<https://sws.geonames.org/3000050/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Pelis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000050;
        gn:lat           47.42917;
        gn:long          -1.66928;
        gn:name          "Les Pelis";
        gn:population    0 .

<https://sws.geonames.org/8293057/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Nazaire Penhoet";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293057;
        gn:lat           47.29526;
        gn:long          -2.19027;
        gn:name          "Bureau de Poste de Saint Nazaire Penhoet";
        gn:population    0 .

<https://sws.geonames.org/2977602/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Philbert-de-Grand-Lieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977602;
        gn:lat           47.03573;
        gn:long          -1.64088;
        gn:name          "Saint-Philbert-de-Grand-Lieu";
        gn:population    6757 .

<https://sws.geonames.org/8436209/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Haudaudine";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436209;
        gn:lat           47.20823;
        gn:long          -1.55529;
        gn:name          "Pont Haudaudine";
        gn:population    0 .

<https://sws.geonames.org/3006534/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Salle-et-Chapelle-Aubry";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006534;
        gn:lat           47.25013;
        gn:long          -0.97512;
        gn:name          "La Salle-et-Chapelle-Aubry";
        gn:population    1091 .

<https://sws.geonames.org/9539775/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Citea Nantes Sextant";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539775;
        gn:lat           47.2067;
        gn:long          -1.57929;
        gn:name          "Citea Nantes Sextant";
        gn:population    0 .

<https://sws.geonames.org/12313174/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Bauches du Desert";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313174;
        gn:lat           47.15913;
        gn:long          -1.6479;
        gn:name          "Les Bauches du Désert";
        gn:population    0 .

<https://sws.geonames.org/6449094/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Fay-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449094;
        gn:lat           47.415;
        gn:long          -1.79139;
        gn:name          "Fay-de-Bretagne";
        gn:population    3601 .

<https://sws.geonames.org/2992441/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montigne-sur-Moine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLX;
        gn:geonamesID    2992441;
        gn:lat           47.08333;
        gn:long          -1.13333;
        gn:name          "Montigné-sur-Moine";
        gn:population    0 .

<https://sws.geonames.org/8436221/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ponts de Bellevue";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436221;
        gn:lat           47.23216;
        gn:long          -1.47285;
        gn:name          "Ponts de Bellevue";
        gn:population    0 .

<https://sws.geonames.org/3031153/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Canal de la Boullaie";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    3031153;
        gn:lat           47.37407;
        gn:long          -2.14581;
        gn:name          "Canal de la Boullaie";
        gn:population    0 .

<https://sws.geonames.org/3023191/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe de la Coupelasse";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    3023191;
        gn:lat           47.01667;
        gn:long          -2.01667;
        gn:name          "Pointe de la Coupelasse";
        gn:population    0 .

<https://sws.geonames.org/9178794/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Residence Cerise Nantes Atlantis";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178794;
        gn:lat           47.22709;
        gn:long          -1.65097;
        gn:name          "Residence Cerise Nantes Atlantis";
        gn:population    0 .

<https://sws.geonames.org/6620270/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Stade Marcel-Saupin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.STDM;
        gn:geonamesID    6620270;
        gn:lat           47.21281;
        gn:long          -1.5385;
        gn:name          "Stade Marcel-Saupin";
        gn:population    0 .

<https://sws.geonames.org/12313087/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Menardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313087;
        gn:lat           47.16068;
        gn:long          -1.32002;
        gn:name          "La Ménardière";
        gn:population    0 .

<https://sws.geonames.org/12313157/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sevres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313157;
        gn:lat           47.18583;
        gn:long          -1.52756;
        gn:name          "Sèvres";
        gn:population    0 .

<https://sws.geonames.org/8293010/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Malo De Guersac";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293010;
        gn:lat           47.3429;
        gn:long          -2.17397;
        gn:name          "Bureau de Poste de Saint Malo De Guersac";
        gn:population    0 .

<https://sws.geonames.org/6619610/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mormaison";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    6619610;
        gn:lat           46.90783;
        gn:long          -1.45071;
        gn:name          "Mormaison";
        gn:population    0 .

<https://sws.geonames.org/7304607/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Citea Nantes la Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    7304607;
        gn:lat           47.25842;
        gn:long          -1.49525;
        gn:name          "Citea Nantes la Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/6434476/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Monnieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434476;
        gn:lat           47.13167;
        gn:long          -1.35583;
        gn:name          "Monnières";
        gn:population    2179 .

<https://sws.geonames.org/6499277/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes Sainte Luce";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6499277;
        gn:lat           47.2622;
        gn:long          -1.4936;
        gn:name          "Campanile Nantes Sainte Luce";
        gn:population    0 .

<https://sws.geonames.org/3233499/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Hautiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233499;
        gn:lat           47.23056;
        gn:long          -2.15677;
        gn:name          "La Hautière";
        gn:population    0 .

<https://sws.geonames.org/2994205/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mespras";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2994205;
        gn:lat           47.50297;
        gn:long          -1.76548;
        gn:name          "Mespras";
        gn:population    0 .

<https://sws.geonames.org/12313015/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Champ Blanc";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313015;
        gn:lat           47.45278;
        gn:long          -2.02596;
        gn:name          "Le Champ Blanc";
        gn:population    0 .

<https://sws.geonames.org/3233605/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rocher de Bourg";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233605;
        gn:lat           47.24833;
        gn:long          -2.17139;
        gn:name          "Rocher de Bourg";
        gn:population    0 .

<https://sws.geonames.org/6435250/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montrevault-sur-Evre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6435250;
        gn:lat           47.26139;
        gn:long          -1.04528;
        gn:name          "Montrevault-sur-Èvre";
        gn:population    15971 .

<https://sws.geonames.org/8293019/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Philbert De Grandlieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293019;
        gn:lat           47.03505;
        gn:long          -1.63892;
        gn:name          "Bureau de Poste de Saint Philbert De Grandlieu";
        gn:population    0 .

<https://sws.geonames.org/10174531/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arcantis Hotel Le Jules Verne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10174531;
        gn:lat           47.21409;
        gn:long          -1.55723;
        gn:name          "Arcantis Hotel Le Jules Verne";
        gn:population    0 .

<https://sws.geonames.org/3007660/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Canal de Languitre";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    3007660;
        gn:lat           47.36667;
        gn:long          -2.16667;
        gn:name          "Canal de Languitre";
        gn:population    0 .

<https://sws.geonames.org/3006326/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Tacherie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006326;
        gn:lat           47.43084;
        gn:long          -1.74357;
        gn:name          "La Tacherie";
        gn:population    0 .

<https://sws.geonames.org/6613155/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ancenis-Saint-Gereon";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6613155;
        gn:lat           47.37278;
        gn:long          -1.17833;
        gn:name          "Ancenis-Saint-Géréon";
        gn:population    10595 .

<https://sws.geonames.org/2980488/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Luce-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980488;
        gn:lat           47.25508;
        gn:long          -1.48269;
        gn:name          "Sainte-Luce-sur-Loire";
        gn:population    13056 .

<https://sws.geonames.org/3024412/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Coiffi";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3024412;
        gn:lat           47.47703;
        gn:long          -2.06786;
        gn:name          "Coiffi";
        gn:population    0 .

<https://sws.geonames.org/3025972/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chaudron-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3025972;
        gn:lat           47.28809;
        gn:long          -0.98547;
        gn:name          "Chaudron-en-Mauges";
        gn:population    1497 .

<https://sws.geonames.org/12312892/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Petit Coiscault";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312892;
        gn:lat           47.57015;
        gn:long          -1.2286;
        gn:name          "Le Petit Coiscault";
        gn:population    0 .

<https://sws.geonames.org/12313092/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Forges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313092;
        gn:lat           47.11064;
        gn:long          -1.28263;
        gn:name          "Les Forges";
        gn:population    0 .

<https://sws.geonames.org/2972127/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de Touvois";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2972127;
        gn:lat           46.90069;
        gn:long          -1.6478;
        gn:name          "Forêt de Touvois";
        gn:population    0 .

<https://sws.geonames.org/3007436/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Paquelais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007436;
        gn:lat           47.33238;
        gn:long          -1.69607;
        gn:name          "La Paquelais";
        gn:population    0 .

<https://sws.geonames.org/3015519/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gourmalon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3015519;
        gn:lat           47.11015;
        gn:long          -2.10045;
        gn:name          "Gourmalon";
        gn:population    0 .

<https://sws.geonames.org/2967549/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2967549;
        gn:lat           47.19865;
        gn:long          -1.88108;
        gn:name          "Vue";
        gn:population    1324 .

<https://sws.geonames.org/2986119/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont-Rousseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2986119;
        gn:lat           47.19261;
        gn:long          -1.54691;
        gn:name          "Pont-Rousseau";
        gn:population    0 .

<https://sws.geonames.org/3002981/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pellerin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002981;
        gn:lat           47.19863;
        gn:long          -1.75466;
        gn:name          "Le Pellerin";
        gn:population    4147 .

<https://sws.geonames.org/2989170/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Orvault";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2989170;
        gn:lat           47.27117;
        gn:long          -1.62361;
        gn:name          "Orvault";
        gn:population    25338 .

<https://sws.geonames.org/3016692/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Garambeau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3016692;
        gn:lat           47.31262;
        gn:long          -1.63262;
        gn:name          "Garambeau";
        gn:population    0 .

<https://sws.geonames.org/12310639/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Belon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310639;
        gn:lat           46.93531;
        gn:long          -1.13085;
        gn:name          "Belon";
        gn:population    0 .

<https://sws.geonames.org/2978814/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Leger-les-Vignes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978814;
        gn:lat           47.13576;
        gn:long          -1.73166;
        gn:name          "Saint-Léger-les-Vignes";
        gn:population    1245 .

<https://sws.geonames.org/6434531/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Meme-le-Tenu";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6434531;
        gn:lat           47.02056;
        gn:long          -1.795;
        gn:name          "Saint-Même-le-Tenu";
        gn:population    1138 .

<https://sws.geonames.org/3004560/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Clos";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004560;
        gn:lat           47.49524;
        gn:long          -1.37155;
        gn:name          "Le Clos";
        gn:population    0 .

<https://sws.geonames.org/2979731/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Germain-sur-Moine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979731;
        gn:lat           47.11746;
        gn:long          -1.12223;
        gn:name          "Saint-Germain-sur-Moine";
        gn:population    2611 .

<https://sws.geonames.org/12305806/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hucheloup";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305806;
        gn:lat           47.05911;
        gn:long          -1.22779;
        gn:name          "Hucheloup";
        gn:population    0 .

<https://sws.geonames.org/12305879/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boissay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305879;
        gn:lat           47.59158;
        gn:long          -1.24482;
        gn:name          "Boissay";
        gn:population    0 .

<https://sws.geonames.org/3036182/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Augrain";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3036182;
        gn:lat           47.50369;
        gn:long          -1.59511;
        gn:name          "Augrain";
        gn:population    0 .

<https://sws.geonames.org/6434521/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Julien-de-Concelles";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434521;
        gn:lat           47.25333;
        gn:long          -1.38556;
        gn:name          "Saint-Julien-de-Concelles";
        gn:population    6888 .

<https://sws.geonames.org/12305894/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pe de Sevre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305894;
        gn:lat           47.14156;
        gn:long          -1.36832;
        gn:name          "Le Pé de Sèvre";
        gn:population    0 .

<https://sws.geonames.org/3009858/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Coueronnais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009858;
        gn:lat           47.43571;
        gn:long          -1.85928;
        gn:name          "La Coueronnais";
        gn:population    0 .

<https://sws.geonames.org/11279879/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Park And Suites Nantes Centre";
        <https://schema.org/elevation>  0.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:S;
        gn:featureCode                  gn:S.HTL;
        gn:geonamesID                   11279879;
        gn:lat                          47.21515;
        gn:long                         -1.55221;
        gn:name                         "Park And Suites Nantes Centre";
        gn:population                   0 .

<https://sws.geonames.org/2971680/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trignac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2971680;
        gn:lat           47.31779;
        gn:long          -2.18918;
        gn:name          "Trignac";
        gn:population    7132 .

<https://sws.geonames.org/10297844/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Citotel Pommeraye";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297844;
        gn:lat           47.21406;
        gn:long          -1.56024;
        gn:name          "Citotel Pommeraye";
        gn:population    0 .

<https://sws.geonames.org/2973550/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Canal de la Taillee";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    2973550;
        gn:lat           47.30548;
        gn:long          -2.05724;
        gn:name          "Canal de la Taillée";
        gn:population    0 .

<https://sws.geonames.org/3004119/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Gavre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004119;
        gn:lat           47.52061;
        gn:long          -1.74815;
        gn:name          "Le Gâvre";
        gn:population    1026 .

<https://sws.geonames.org/6451599/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouin";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6451599;
        gn:lat           46.97361;
        gn:long          -2.00167;
        gn:name          "Bouin";
        gn:population    2155 .

<https://sws.geonames.org/12313102/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Patis Vinet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313102;
        gn:lat           47.18067;
        gn:long          -1.42169;
        gn:name          "Le Pâtis Vinet";
        gn:population    0 .

<https://sws.geonames.org/6434512/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Fiacre-sur-Maine";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434512;
        gn:lat           47.14333;
        gn:long          -1.41667;
        gn:name          "Saint-Fiacre-sur-Maine";
        gn:population    1186 .

<https://sws.geonames.org/12313010/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fozo";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313010;
        gn:lat           47.56196;
        gn:long          -2.05829;
        gn:name          "Le Fozo";
        gn:population    0 .

<https://sws.geonames.org/8287009/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "St-Etienne-de-Montluc Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8287009;
        gn:lat           47.27546;
        gn:long          -1.78718;
        gn:name          "St-Étienne-de-Montluc Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8286945/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Severac Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286945;
        gn:lat           47.54975;
        gn:long          -2.07274;
        gn:name          "Sévérac Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12312969/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bergerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312969;
        gn:lat           47.2354;
        gn:long          -1.63225;
        gn:name          "La Bergerie";
        gn:population    0 .

<https://sws.geonames.org/12305885/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gergauderie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305885;
        gn:lat           47.40469;
        gn:long          -1.7965;
        gn:name          "La Gergauderie";
        gn:population    0 .

<https://sws.geonames.org/8286981/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Port Saint-Pere Saint-Mars Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286981;
        gn:lat           47.11608;
        gn:long          -1.74009;
        gn:name          "Port Saint-Père Saint-Mars Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8436197/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Anne-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436197;
        gn:lat           47.20821;
        gn:long          -1.5659;
        gn:name          "Pont Anne-de-Bretagne";
        gn:population    0 .

<https://sws.geonames.org/12312895/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Metairie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312895;
        gn:lat           47.48619;
        gn:long          -1.21077;
        gn:name          "La Métairie";
        gn:population    0 .

<https://sws.geonames.org/2981888/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Aignan-Grandlieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981888;
        gn:lat           47.12374;
        gn:long          -1.6308;
        gn:name          "Saint-Aignan-Grandlieu";
        gn:population    0 .

<https://sws.geonames.org/3006786/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rochelle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006786;
        gn:lat           47.2675;
        gn:long          -1.38631;
        gn:name          "La Rochelle";
        gn:population    0 .

<https://sws.geonames.org/12312955/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Clos";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312955;
        gn:lat           47.24525;
        gn:long          -1.52958;
        gn:name          "Le Grand Clos";
        gn:population    0 .

<https://sws.geonames.org/6614150/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chemere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6614150;
        gn:lat           47.12194;
        gn:long          -1.91472;
        gn:name          "Chéméré";
        gn:population    2171 .

<https://sws.geonames.org/12305905/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boiseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305905;
        gn:lat           47.19393;
        gn:long          -1.69706;
        gn:name          "Boiseau";
        gn:population    0 .

<https://sws.geonames.org/3033968/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beauvoir-sur-Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3033968;
        gn:lat           46.91506;
        gn:long          -2.04085;
        gn:name          "Beauvoir-sur-Mer";
        gn:population    3625 .

<https://sws.geonames.org/3007233/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Poiteviniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007233;
        gn:lat           47.53217;
        gn:long          -1.30716;
        gn:name          "La Poitevinière";
        gn:population    0 .

<https://sws.geonames.org/8292986/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Pont St Martin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292986;
        gn:lat           47.1249;
        gn:long          -1.58614;
        gn:name          "Bureau de Poste de Pont St Martin";
        gn:population    0 .

<https://sws.geonames.org/12313147/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Moulinier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313147;
        gn:lat           47.13831;
        gn:long          -1.43279;
        gn:name          "Le Moulinier";
        gn:population    0 .

<https://sws.geonames.org/12312910/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Coudreciere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312910;
        gn:lat           47.5724;
        gn:long          -1.3446;
        gn:name          "La Coudrecière";
        gn:population    0 .

<https://sws.geonames.org/12313117/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bigotiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313117;
        gn:lat           47.11543;
        gn:long          -1.37678;
        gn:name          "La Bigotière";
        gn:population    0 .

<https://sws.geonames.org/8293000/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Etienne De Mont Luc";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293000;
        gn:lat           47.27782;
        gn:long          -1.78502;
        gn:name          "Bureau de Poste de Saint Etienne De Mont Luc";
        gn:population    0 .

<https://sws.geonames.org/6616808/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fresne-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6616808;
        gn:lat           47.40083;
        gn:long          -0.92833;
        gn:name          "Le Fresne-sur-Loire";
        gn:population    978 .

<https://sws.geonames.org/12313226/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tourte";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313226;
        gn:lat           47.11928;
        gn:long          -2.09831;
        gn:name          "Tourte";
        gn:population    0 .

<https://sws.geonames.org/9172749/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appart City Nantes Quais De Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9172749;
        gn:lat           47.2096;
        gn:long          -1.56742;
        gn:name          "Appart City Nantes Quais De Loire";
        gn:population    0 .

<https://sws.geonames.org/3233413/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nor Plat";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233413;
        gn:lat           47.08033;
        gn:long          -2.09448;
        gn:name          "Nor Plat";
        gn:population    0 .

<https://sws.geonames.org/8293005/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Julien De Concelles";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293005;
        gn:lat           47.25097;
        gn:long          -1.38679;
        gn:name          "Bureau de Poste de Saint Julien De Concelles";
        gn:population    0 .

<https://sws.geonames.org/12308447/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fourneau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308447;
        gn:lat           47.35713;
        gn:long          -1.17384;
        gn:name          "Le Fourneau";
        gn:population    0 .

<https://sws.geonames.org/3001866/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Boeufs";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3001866;
        gn:lat           47.05;
        gn:long          -2.01667;
        gn:name          "Les Boeufs";
        gn:population    0 .

<https://sws.geonames.org/2992100/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montrelais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2992100;
        gn:lat           47.38952;
        gn:long          -0.96664;
        gn:name          "Montrelais";
        gn:population    0 .

<https://sws.geonames.org/6455116/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brains";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6455116;
        gn:lat           47.16917;
        gn:long          -1.72167;
        gn:name          "Brains";
        gn:population    2790 .

<https://sws.geonames.org/10297842/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Coeur de Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297842;
        gn:lat           47.22841;
        gn:long          -1.56344;
        gn:name          "Coeur de Loire";
        gn:population    0 .

<https://sws.geonames.org/6434528/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Malo-de-Guersac";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434528;
        gn:lat           47.35083;
        gn:long          -2.17972;
        gn:name          "Saint-Malo-de-Guersac";
        gn:population    3175 .

<https://sws.geonames.org/2978532/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de Saint-Mars";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2978532;
        gn:lat           47.54636;
        gn:long          -1.24308;
        gn:name          "Forêt de Saint-Mars";
        gn:population    0 .

<https://sws.geonames.org/12312901/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tacon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312901;
        gn:lat           47.41624;
        gn:long          -1.25049;
        gn:name          "Tacon";
        gn:population    0 .

<https://sws.geonames.org/8292905/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Aigrefeuille Sur Maine";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292905;
        gn:lat           47.07689;
        gn:long          -1.40127;
        gn:name          "Bureau de Poste de Aigrefeuille Sur Maine";
        gn:population    0 .

<https://sws.geonames.org/3031875/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boivre";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3031875;
        gn:lat           47.21312;
        gn:long          -2.16078;
        gn:name          "Boivre";
        gn:population    0 .

<https://sws.geonames.org/3025581/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile la Chenaie";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3025581;
        gn:lat           47.25274;
        gn:long          -1.43785;
        gn:name          "Île la Chenaie";
        gn:population    0 .

<https://sws.geonames.org/3011325/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Barriais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011325;
        gn:lat           47.31084;
        gn:long          -1.94822;
        gn:name          "La Barriais";
        gn:population    0 .

<https://sws.geonames.org/3009149/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009149;
        gn:lat           46.95834;
        gn:long          -1.38012;
        gn:name          "La Gaudière";
        gn:population    0 .

<https://sws.geonames.org/8293030/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Le Temple De Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293030;
        gn:lat           47.32855;
        gn:long          -1.79131;
        gn:name          "Bureau de Poste de Le Temple De Bretagne";
        gn:population    0 .

<https://sws.geonames.org/6515115/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ibis Nantes Centre Gare Sud";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6515115;
        gn:lat           47.2152;
        gn:long          -1.547;
        gn:name          "Ibis Nantes Centre Gare Sud";
        gn:population    0 .

<https://sws.geonames.org/3006863/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roberdais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006863;
        gn:lat           47.54057;
        gn:long          -1.75638;
        gn:name          "La Roberdais";
        gn:population    0 .

<https://sws.geonames.org/3009228/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gapaillere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009228;
        gn:lat           47.47202;
        gn:long          -1.28506;
        gn:name          "La Gapaillère";
        gn:population    0 .

<https://sws.geonames.org/12313196/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Joussiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313196;
        gn:lat           47.17145;
        gn:long          -1.74731;
        gn:name          "La Joussinière";
        gn:population    0 .

<https://sws.geonames.org/3010278/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Saint-Florent";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010278;
        gn:lat           47.33393;
        gn:long          -1.05631;
        gn:name          "La Chapelle-Saint-Florent";
        gn:population    1148 .

<https://sws.geonames.org/3006432/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Sensie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006432;
        gn:lat           47.34322;
        gn:long          -2.07881;
        gn:name          "La Sensie";
        gn:population    0 .

<https://sws.geonames.org/2978809/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Leger-sous-Cholet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978809;
        gn:lat           47.09339;
        gn:long          -0.91031;
        gn:name          "Saint-Léger-sous-Cholet";
        gn:population    2797 .

<https://sws.geonames.org/9539819/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Domaine De L'Ocean";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539819;
        gn:lat           47.23324;
        gn:long          -2.17234;
        gn:name          "Le Domaine De L'Océan";
        gn:population    0 .

<https://sws.geonames.org/2981711/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Andre-Treize-Voies";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981711;
        gn:lat           46.93418;
        gn:long          -1.41212;
        gn:name          "Saint-André-Treize-Voies";
        gn:population    1019 .

<https://sws.geonames.org/12308502/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Terreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308502;
        gn:lat           47.23717;
        gn:long          -1.06866;
        gn:name          "Le Terreau";
        gn:population    0 .

<https://sws.geonames.org/6456058/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cornuaille";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456058;
        gn:lat           47.51083;
        gn:long          -0.985;
        gn:name          "La Cornuaille";
        gn:population    951 .

<https://sws.geonames.org/12313109/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gare";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313109;
        gn:lat           47.16213;
        gn:long          -1.39256;
        gn:name          "La Gare";
        gn:population    0 .

<https://sws.geonames.org/8293355/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Cande";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293355;
        gn:lat           47.5598;
        gn:long          -1.03582;
        gn:name          "Bureau de Poste de Cande";
        gn:population    0 .

<https://sws.geonames.org/3008870/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cruaudais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008870;
        gn:lat           47.26417;
        gn:long          -1.94607;
        gn:name          "La Cruaudais";
        gn:population    0 .

<https://sws.geonames.org/6498332/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel de Bourgogne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6498332;
        gn:lat           47.2175;
        gn:long          -1.5443;
        gn:name          "Hotel de Bourgogne";
        gn:population    0 .

<https://sws.geonames.org/3008424/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Lortiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008424;
        gn:lat           47.08858;
        gn:long          -1.17713;
        gn:name          "La Lortière";
        gn:population    0 .

<https://sws.geonames.org/6434519/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Jean-de-Boiseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434519;
        gn:lat           47.19417;
        gn:long          -1.72472;
        gn:name          "Saint-Jean-de-Boiseau";
        gn:population    5692 .

<https://sws.geonames.org/12313017/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montmignac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313017;
        gn:lat           47.41697;
        gn:long          -1.98604;
        gn:name          "Montmignac";
        gn:population    0 .

<https://sws.geonames.org/12305902/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bellevue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305902;
        gn:lat           47.21106;
        gn:long          -1.61782;
        gn:name          "Bellevue";
        gn:population    0 .

<https://sws.geonames.org/12310646/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Couroliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310646;
        gn:lat           46.92814;
        gn:long          -1.39139;
        gn:name          "La Courolière";
        gn:population    0 .

<https://sws.geonames.org/2980372/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Pazanne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980372;
        gn:lat           47.10355;
        gn:long          -1.81045;
        gn:name          "Sainte-Pazanne";
        gn:population    3734 .

<https://sws.geonames.org/12492926/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Archives departementales de la Loire-Atlantique";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.ARCHV;
        gn:geonamesID    12492926;
        gn:lat           47.22486;
        gn:long          -1.55755;
        gn:name          "Archives départementales de la Loire-Atlantique";
        gn:population    0 .

<https://sws.geonames.org/8436211/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Aristide-Briand";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436211;
        gn:lat           47.21008;
        gn:long          -1.54208;
        gn:name          "Pont Aristide-Briand";
        gn:population    0 .

<https://sws.geonames.org/2993820/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mindin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2993820;
        gn:lat           47.2631;
        gn:long          -2.16655;
        gn:name          "Mindin";
        gn:population    0 .

<https://sws.geonames.org/12308497/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Gatines";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308497;
        gn:lat           47.2543;
        gn:long          -1.15053;
        gn:name          "Les Gâtines";
        gn:population    0 .

<https://sws.geonames.org/12253514/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Eglise Saint-Croix";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RLG;
        gn:geonamesID    12253514;
        gn:lat           47.21528;
        gn:long          -1.55417;
        gn:name          "Eglise Saint-Croix";
        gn:population    0 .

<https://sws.geonames.org/8293072/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Bouguenais Les Couets";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293072;
        gn:lat           47.18129;
        gn:long          -1.58748;
        gn:name          "Bureau de Poste de Bouguenais Les Couets";
        gn:population    0 .

<https://sws.geonames.org/3008355/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Maillardais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008355;
        gn:lat           47.52715;
        gn:long          -1.76553;
        gn:name          "La Maillardais";
        gn:population    0 .

<https://sws.geonames.org/2972430/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Torfou";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2972430;
        gn:lat           47.03682;
        gn:long          -1.11635;
        gn:name          "Torfou";
        gn:population    2023 .

<https://sws.geonames.org/3002567/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pont Lege";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002567;
        gn:lat           46.92869;
        gn:long          -1.22584;
        gn:name          "Le Pont Legé";
        gn:population    0 .

<https://sws.geonames.org/6435352/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Villedieu-la-Blouere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435352;
        gn:lat           47.14694;
        gn:long          -1.06417;
        gn:name          "Villedieu-la-Blouère";
        gn:population    2406 .

<https://sws.geonames.org/12313005/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bout des Haies";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313005;
        gn:lat           47.54946;
        gn:long          -2.02787;
        gn:name          "Le Bout des Haies";
        gn:population    0 .

<https://sws.geonames.org/12312917/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle Breton";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312917;
        gn:lat           47.4489;
        gn:long          -1.32598;
        gn:name          "La Chapelle Breton";
        gn:population    0 .

<https://sws.geonames.org/6434538/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Philbert-de-Grand-Lieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434538;
        gn:lat           47.035;
        gn:long          -1.64;
        gn:name          "Saint-Philbert-de-Grand-Lieu";
        gn:population    8851 .

<https://sws.geonames.org/2979605/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Guillaume";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979605;
        gn:lat           47.42202;
        gn:long          -2.1194;
        gn:name          "Saint-Guillaume";
        gn:population    0 .

<https://sws.geonames.org/3017667/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Roches de la Fosse";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3017667;
        gn:lat           46.90385;
        gn:long          -2.19193;
        gn:name          "Roches de la Fosse";
        gn:population    0 .

<https://sws.geonames.org/8297438/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Rocheserviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297438;
        gn:lat           46.9363;
        gn:long          -1.51195;
        gn:name          "Bureau de Poste de Rocheserviere";
        gn:population    0 .

<https://sws.geonames.org/8292922/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Le Cellier";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292922;
        gn:lat           47.31925;
        gn:long          -1.34737;
        gn:name          "Bureau de Poste de Le Cellier";
        gn:population    0 .

<https://sws.geonames.org/6532063/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Residhome Res Ducs De Bretange";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6532063;
        gn:lat           47.2138;
        gn:long          -1.5452;
        gn:name          "Residhome Res Ducs De Bretange";
        gn:population    0 .

<https://sws.geonames.org/10297849/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appartcity Nantes Quais de Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297849;
        gn:lat           47.20962;
        gn:long          -1.56746;
        gn:name          "Appartcity Nantes Quais de Loire";
        gn:population    0 .

<https://sws.geonames.org/6449099/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gorges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449099;
        gn:lat           47.10167;
        gn:long          -1.30389;
        gn:name          "Gorges";
        gn:population    4543 .

<https://sws.geonames.org/8292972/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Les Moutiers En Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292972;
        gn:lat           47.06376;
        gn:long          -1.99325;
        gn:name          "Bureau de Poste de Les Moutiers En Retz";
        gn:population    0 .

<https://sws.geonames.org/2980271/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Corcoue-sur-Logne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980271;
        gn:lat           46.96667;
        gn:long          -1.58333;
        gn:name          "Corcoué-sur-Logne";
        gn:population    2480 .

<https://sws.geonames.org/3004572/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Cleray";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004572;
        gn:lat           47.26863;
        gn:long          -1.32386;
        gn:name          "Le Cleray";
        gn:population    0 .

<https://sws.geonames.org/6492472/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Citea Nantes Aubiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6492472;
        gn:lat           47.2604;
        gn:long          -1.4966;
        gn:name          "Citea Nantes Aubiniere";
        gn:population    0 .

<https://sws.geonames.org/12312908/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Villechoux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312908;
        gn:lat           47.56606;
        gn:long          -1.31461;
        gn:name          "Villechoux";
        gn:population    0 .

<https://sws.geonames.org/12313107/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Germaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313107;
        gn:lat           47.16201;
        gn:long          -1.4272;
        gn:name          "Sainte-Germaine";
        gn:population    0 .

<https://sws.geonames.org/7535056/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Golf Carquefou";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RECG;
        gn:geonamesID    7535056;
        gn:lat           47.2891;
        gn:long          -1.4845;
        gn:name          "Golf Carquefou";
        gn:population    0 .

<https://sws.geonames.org/8297401/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Cugand";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297401;
        gn:lat           47.06296;
        gn:long          -1.25601;
        gn:name          "Bureau de Poste de Cugand";
        gn:population    0 .

<https://sws.geonames.org/6612551/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Hilaire-de-Clisson";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6612551;
        gn:lat           47.06222;
        gn:long          -1.30944;
        gn:name          "Saint-Hilaire-de-Clisson";
        gn:population    2268 .

<https://sws.geonames.org/12312887/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Harie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312887;
        gn:lat           47.51278;
        gn:long          -1.18886;
        gn:name          "La Harie";
        gn:population    0 .

<https://sws.geonames.org/6437402/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Thehillac";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6437402;
        gn:lat           47.56778;
        gn:long          -2.11639;
        gn:name          "Théhillac";
        gn:population    583 .

<https://sws.geonames.org/3037796/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arrondissement d'Ancenis";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM3H;
        gn:geonamesID    3037796;
        gn:lat           47.41667;
        gn:long          -1.25;
        gn:name          "Arrondissement d'Ancenis";
        gn:population    60368 .

<https://sws.geonames.org/12313191/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Metairie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313191;
        gn:lat           47.2165;
        gn:long          -1.69962;
        gn:name          "La Métairie";
        gn:population    0 .

<https://sws.geonames.org/3233987/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Jacques";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLX;
        gn:geonamesID    3233987;
        gn:lat           47.19404;
        gn:long          -1.53619;
        gn:name          "Saint-Jacques";
        gn:population    0 .

<https://sws.geonames.org/8292978/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Oudon";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292978;
        gn:lat           47.3474;
        gn:long          -1.28418;
        gn:name          "Bureau de Poste de Oudon";
        gn:population    0 .

<https://sws.geonames.org/12310644/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapeliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310644;
        gn:lat           46.92264;
        gn:long          -1.31399;
        gn:name          "La Chapelière";
        gn:population    0 .

<https://sws.geonames.org/3008119/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Moere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008119;
        gn:lat           47.36667;
        gn:long          -1.91667;
        gn:name          "La Moëre";
        gn:population    0 .

<https://sws.geonames.org/3036826/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile d'Arouix";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3036826;
        gn:lat           47.27441;
        gn:long          -1.40654;
        gn:name          "Île d'Arouix";
        gn:population    0 .

<https://sws.geonames.org/8286998/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Croix-de-Mean Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286998;
        gn:lat           47.30046;
        gn:long          -2.19293;
        gn:name          "La Croix-de-Méan Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12313124/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bonnaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313124;
        gn:lat           47.21399;
        gn:long          -1.43368;
        gn:name          "La Bonnaudière";
        gn:population    0 .

<https://sws.geonames.org/12305811/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fosse";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305811;
        gn:lat           46.91563;
        gn:long          -2.16191;
        gn:name          "La Fosse";
        gn:population    0 .

<https://sws.geonames.org/3000355/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Masures";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000355;
        gn:lat           47.43357;
        gn:long          -1.41857;
        gn:name          "Les Masures";
        gn:population    0 .

<https://sws.geonames.org/12313233/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Portmain";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313233;
        gn:lat           47.12239;
        gn:long          -2.16268;
        gn:name          "Le Portmain";
        gn:population    0 .

<https://sws.geonames.org/3233454/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pe de Buzay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233454;
        gn:lat           47.20365;
        gn:long          -1.81682;
        gn:name          "Le Pé de Buzay";
        gn:population    0 .

<https://sws.geonames.org/12313032/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile d'Aignac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313032;
        gn:lat           47.3667;
        gn:long          -2.19327;
        gn:name          "Île d'Aignac";
        gn:population    0 .

<https://sws.geonames.org/2999236/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Temple-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999236;
        gn:lat           47.32868;
        gn:long          -1.79143;
        gn:name          "Le Temple-de-Bretagne";
        gn:population    1665 .

<https://sws.geonames.org/12312897/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Coindiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312897;
        gn:lat           47.43266;
        gn:long          -1.25632;
        gn:name          "La Coindière";
        gn:population    0 .

<https://sws.geonames.org/2997869/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Embouchure de la Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STMM;
        gn:geonamesID    2997869;
        gn:lat           47.26956;
        gn:long          -2.18345;
        gn:name          "Embouchure de la Loire";
        gn:population    0 .

<https://sws.geonames.org/2975702/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sautron";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2975702;
        gn:lat           47.26345;
        gn:long          -1.67222;
        gn:name          "Sautron";
        gn:population    7405 .

<https://sws.geonames.org/3233444/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Banc de Bilho";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.SHOL;
        gn:geonamesID    3233444;
        gn:lat           47.29096;
        gn:long          -2.12633;
        gn:name          "Banc de Bilho";
        gn:population    0 .

<https://sws.geonames.org/6523836/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appart City Nantes Viarme";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6523836;
        gn:lat           47.2213;
        gn:long          -1.5615;
        gn:name          "Appart City Nantes Viarme";
        gn:population    0 .

<https://sws.geonames.org/11906053/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Marche de Talensac";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.MKT;
        gn:geonamesID    11906053;
        gn:lat           47.22126;
        gn:long          -1.55783;
        gn:name          "Marché de Talensac";
        gn:population    0 .

<https://sws.geonames.org/8436218/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont de Pirmil";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436218;
        gn:lat           47.1991;
        gn:long          -1.54321;
        gn:name          "Pont de Pirmil";
        gn:population    0 .

<https://sws.geonames.org/3006858/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Robertiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006858;
        gn:lat           47.01048;
        gn:long          -1.43555;
        gn:name          "La Robertière";
        gn:population    0 .

<https://sws.geonames.org/3007704/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Angle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007704;
        gn:lat           47.51917;
        gn:long          -1.9325;
        gn:name          "L'Angle";
        gn:population    0 .

<https://sws.geonames.org/2989016/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ouin";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2989016;
        gn:lat           46.96845;
        gn:long          -0.90381;
        gn:name          "Ouin";
        gn:population    0 .

<https://sws.geonames.org/6434491/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Petit-Mars";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434491;
        gn:lat           47.39417;
        gn:long          -1.455;
        gn:name          "Petit-Mars";
        gn:population    3605 .

<https://sws.geonames.org/3020820/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Dreny";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3020820;
        gn:lat           47.56705;
        gn:long          -1.93628;
        gn:name          "Dreny";
        gn:population    0 .

<https://sws.geonames.org/6449076/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Villeneuve-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449076;
        gn:lat           47.04306;
        gn:long          -1.95278;
        gn:name          "Villeneuve-en-Retz";
        gn:population    4931 .

<https://sws.geonames.org/3012871/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile de Menac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3012871;
        gn:lat           47.37345;
        gn:long          -2.18655;
        gn:name          "Île de Menac";
        gn:population    0 .

<https://sws.geonames.org/8292912/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Bernerie En Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292912;
        gn:lat           47.07893;
        gn:long          -2.03537;
        gn:name          "Bureau de Poste de La Bernerie En Retz";
        gn:population    0 .

<https://sws.geonames.org/2971679/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Canal de Trignac";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    2971679;
        gn:lat           47.32264;
        gn:long          -2.19714;
        gn:name          "Canal de Trignac";
        gn:population    0 .

<https://sws.geonames.org/12313160/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Trocardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313160;
        gn:lat           47.17986;
        gn:long          -1.56957;
        gn:name          "La Trocardière";
        gn:population    0 .

<https://sws.geonames.org/12312977/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Blandinais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312977;
        gn:lat           47.28504;
        gn:long          -1.76172;
        gn:name          "La Blandinais";
        gn:population    0 .

<https://sws.geonames.org/6449402/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Botz-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6449402;
        gn:lat           47.30694;
        gn:long          -1.00167;
        gn:name          "Botz-en-Mauges";
        gn:population    806 .

<https://sws.geonames.org/6613998/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Crespin-sur-Moine";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6613998;
        gn:lat           47.09889;
        gn:long          -1.18611;
        gn:name          "Saint-Crespin-sur-Moine";
        gn:population    1554 .

<https://sws.geonames.org/8293079/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Herblain Hotel De Ville";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293079;
        gn:lat           47.21135;
        gn:long          -1.64939;
        gn:name          "Bureau de Poste de Saint Herblain Hotel De Ville";
        gn:population    0 .

<https://sws.geonames.org/12313099/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Verdonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313099;
        gn:lat           47.19905;
        gn:long          -1.38698;
        gn:name          "La Verdonnière";
        gn:population    0 .

<https://sws.geonames.org/3002063/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Sauzais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002063;
        gn:lat           47.53114;
        gn:long          -1.59724;
        gn:name          "Le Sauzais";
        gn:population    0 .

<https://sws.geonames.org/12310636/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Ronde";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310636;
        gn:lat           46.93416;
        gn:long          -1.43044;
        gn:name          "La Ronde";
        gn:population    0 .

<https://sws.geonames.org/12313169/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bourgonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313169;
        gn:lat           47.20601;
        gn:long          -1.65716;
        gn:name          "La Bourgonnière";
        gn:population    0 .

<https://sws.geonames.org/12312932/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Demenure";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312932;
        gn:lat           47.52075;
        gn:long          -1.43294;
        gn:name          "La Demenure";
        gn:population    0 .

<https://sws.geonames.org/3008816/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008816;
        gn:lat           47.39679;
        gn:long          -1.86869;
        gn:name          "La Haie";
        gn:population    0 .

<https://sws.geonames.org/3013634/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Havre";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3013634;
        gn:lat           47.34238;
        gn:long          -1.28774;
        gn:name          "Hâvre";
        gn:population    0 .

<https://sws.geonames.org/6454153/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Reze";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6454153;
        gn:lat           47.19056;
        gn:long          -1.56917;
        gn:name          "Rezé";
        gn:population    40368 .

<https://sws.geonames.org/8286991/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Haie-Fouassiere Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286991;
        gn:lat           47.16155;
        gn:long          -1.39292;
        gn:name          "La Haie-Fouassière Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12312994/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Noe";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312994;
        gn:lat           47.59889;
        gn:long          -2.06678;
        gn:name          "La Noë";
        gn:population    0 .

<https://sws.geonames.org/12312940/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Verrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312940;
        gn:lat           47.24341;
        gn:long          -1.38688;
        gn:name          "La Verrie";
        gn:population    0 .

<https://sws.geonames.org/6434482/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mouzillon";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434482;
        gn:lat           47.14139;
        gn:long          -1.28222;
        gn:name          "Mouzillon";
        gn:population    2810 .

<https://sws.geonames.org/3007349/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Petite Riviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007349;
        gn:lat           47.38572;
        gn:long          -0.98942;
        gn:name          "La Petite Rivière";
        gn:population    0 .

<https://sws.geonames.org/6449119/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mauves-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449119;
        gn:lat           47.29611;
        gn:long          -1.39333;
        gn:name          "Mauves-sur-Loire";
        gn:population    3208 .

<https://sws.geonames.org/3028966/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campbon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3028966;
        gn:lat           47.41208;
        gn:long          -1.96972;
        gn:name          "Campbon";
        gn:population    3327 .

<https://sws.geonames.org/2974539/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sillon de Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.RGN;
        gn:geonamesID    2974539;
        gn:lat           47.36667;
        gn:long          -1.86667;
        gn:name          "Sillon de Bretagne";
        gn:population    0 .

<https://sws.geonames.org/2991700/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mortagne-sur-Sevre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2991700;
        gn:lat           46.99209;
        gn:long          -0.95291;
        gn:name          "Mortagne-sur-Sèvre";
        gn:population    6428 .

<https://sws.geonames.org/12313132/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Mortiers";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313132;
        gn:lat           47.17961;
        gn:long          -1.44419;
        gn:name          "Les Mortiers";
        gn:population    0 .

<https://sws.geonames.org/2993818/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe de Mindin";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    2993818;
        gn:lat           47.26667;
        gn:long          -2.16667;
        gn:name          "Pointe de Mindin";
        gn:population    0 .

<https://sws.geonames.org/9072702/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Chateau de la Bretonniere";
        <https://schema.org/elevation>  30.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:S;
        gn:featureCode                  gn:S.CSTL;
        gn:geonamesID                   9072702;
        gn:lat                          47.33442;
        gn:long                         -1.7474;
        gn:name                         "Château de la Bretonnière";
        gn:population                   0 .

<https://sws.geonames.org/3007291/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Piniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007291;
        gn:lat           46.94215;
        gn:long          -1.37917;
        gn:name          "La Pinière";
        gn:population    0 .

<https://sws.geonames.org/2999485/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Touches";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999485;
        gn:lat           47.44249;
        gn:long          -1.43097;
        gn:name          "Les Touches";
        gn:population    2111 .

<https://sws.geonames.org/3008549/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Lande";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008549;
        gn:lat           47.40687;
        gn:long          -2.11453;
        gn:name          "La Lande";
        gn:population    0 .

<https://sws.geonames.org/3030675/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouzille";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3030675;
        gn:lat           47.3375;
        gn:long          -1.11143;
        gn:name          "Bouzillé";
        gn:population    1353 .

<https://sws.geonames.org/2982682/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rouans";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2982682;
        gn:lat           47.1854;
        gn:long          -1.86022;
        gn:name          "Rouans";
        gn:population    2283 .

<https://sws.geonames.org/2982318/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rozay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2982318;
        gn:lat           47.53152;
        gn:long          -1.91248;
        gn:name          "Rozay";
        gn:population    0 .

<https://sws.geonames.org/8293032/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Treillieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293032;
        gn:lat           47.3291;
        gn:long          -1.61988;
        gn:name          "Bureau de Poste de Treillieres";
        gn:population    0 .

<https://sws.geonames.org/8292927/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Chapelle Sur Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292927;
        gn:lat           47.29621;
        gn:long          -1.55268;
        gn:name          "Bureau de Poste de La Chapelle Sur Erdre";
        gn:population    0 .

<https://sws.geonames.org/8293013/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Mars La Jaille";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293013;
        gn:lat           47.52422;
        gn:long          -1.18631;
        gn:name          "Bureau de Poste de Saint Mars La Jaille";
        gn:population    0 .

<https://sws.geonames.org/12313122/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Frene";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313122;
        gn:lat           47.07703;
        gn:long          -1.36623;
        gn:name          "Le Frêne";
        gn:population    0 .

<https://sws.geonames.org/6616813/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Anne-sur-Brivet";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616813;
        gn:lat           47.4597;
        gn:long          -2.0026;
        gn:name          "Sainte-Anne-sur-Brivet";
        gn:population    2984 .

<https://sws.geonames.org/6435230/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435230;
        gn:lat           47.34333;
        gn:long          -1.16444;
        gn:name          "Liré";
        gn:population    2393 .

<https://sws.geonames.org/6514270/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L Hotel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6514270;
        gn:lat           47.2173;
        gn:long          -1.5476;
        gn:name          "L Hotel";
        gn:population    0 .

<https://sws.geonames.org/12313231/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bois de Comberge";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313231;
        gn:lat           47.17781;
        gn:long          -2.15974;
        gn:name          "Le Bois de Comberge";
        gn:population    0 .

<https://sws.geonames.org/12313082/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Laures";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313082;
        gn:lat           47.18072;
        gn:long          -1.29961;
        gn:name          "Les Laures";
        gn:population    0 .

<https://sws.geonames.org/2999085/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Etriche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999085;
        gn:lat           47.50202;
        gn:long          -1.72404;
        gn:name          "L'Etriché";
        gn:population    0 .

<https://sws.geonames.org/2996668/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Maine";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2996668;
        gn:lat           47.15217;
        gn:long          -1.44455;
        gn:name          "Maine";
        gn:population    0 .

<https://sws.geonames.org/3233407/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Boeufs Jaunes";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233407;
        gn:lat           47.075;
        gn:long          -2.08056;
        gn:name          "Les Bœufs Jaunes";
        gn:population    0 .

<https://sws.geonames.org/6515341/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ibis Nantes La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6515341;
        gn:lat           47.2566;
        gn:long          -1.5157;
        gn:name          "Ibis Nantes La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/12148894/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau de Beaupreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.CSTL;
        gn:geonamesID    12148894;
        gn:lat           47.19919;
        gn:long          -0.99195;
        gn:name          "Château de Beaupréau";
        gn:population    0 .

<https://sws.geonames.org/12313072/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Chatelier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313072;
        gn:lat           47.03441;
        gn:long          -1.14198;
        gn:name          "Le Châtelier";
        gn:population    0 .

<https://sws.geonames.org/6510142/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Atel Grand Hotel De Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6510142;
        gn:lat           47.2124;
        gn:long          -1.5602;
        gn:name          "Atel Grand Hotel De Nantes";
        gn:population    0 .

<https://sws.geonames.org/3007991/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Moucletiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007991;
        gn:lat           47.16929;
        gn:long          -1.29119;
        gn:name          "La Moucletière";
        gn:population    0 .

<https://sws.geonames.org/12308561/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Censivier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308561;
        gn:lat           47.03373;
        gn:long          -1.09226;
        gn:name          "Le Censivier";
        gn:population    0 .

<https://sws.geonames.org/8293069/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Bellevue";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293069;
        gn:lat           47.20916;
        gn:long          -1.6109;
        gn:name          "Bureau de Poste de Nantes Bellevue";
        gn:population    0 .

<https://sws.geonames.org/3007702/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Langlechais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007702;
        gn:lat           47.51274;
        gn:long          -1.75155;
        gn:name          "Langlechais";
        gn:population    0 .

<https://sws.geonames.org/2970923/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vallet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2970923;
        gn:lat           47.16133;
        gn:long          -1.26715;
        gn:name          "Vallet";
        gn:population    7483 .

<https://sws.geonames.org/11746346/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mare";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.LK;
        gn:geonamesID    11746346;
        gn:lat           47.49777;
        gn:long          -1.46499;
        gn:name          "La Mare";
        gn:population    0 .

<https://sws.geonames.org/3013752/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Canal de Haute-Perche";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    3013752;
        gn:lat           47.1;
        gn:long          -2.11667;
        gn:name          "Canal de Haute-Perche";
        gn:population    0 .

<https://sws.geonames.org/6456913/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Saint-Sauveur";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456913;
        gn:lat           47.44111;
        gn:long          -0.98639;
        gn:name          "La Chapelle-Saint-Sauveur";
        gn:population    770 .

<https://sws.geonames.org/3006982/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Renouliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006982;
        gn:lat           46.96155;
        gn:long          -1.41453;
        gn:name          "La Renoulière";
        gn:population    0 .

<https://sws.geonames.org/6434498/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pouille-les-Coteaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434498;
        gn:lat           47.45528;
        gn:long          -1.16222;
        gn:name          "Pouillé-les-Côteaux";
        gn:population    1025 .

<https://sws.geonames.org/12313114/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Miniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313114;
        gn:lat           47.12067;
        gn:long          -1.35099;
        gn:name          "La Minière";
        gn:population    0 .

<https://sws.geonames.org/8292919/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Brains";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292919;
        gn:lat           47.16909;
        gn:long          -1.72199;
        gn:name          "Bureau de Poste de Brains";
        gn:population    0 .

<https://sws.geonames.org/3016947/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Frossay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3016947;
        gn:lat           47.24451;
        gn:long          -1.93557;
        gn:name          "Frossay";
        gn:population    2463 .

<https://sws.geonames.org/6456919/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Landreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456919;
        gn:lat           47.205;
        gn:long          -1.30556;
        gn:name          "Le Landreau";
        gn:population    2977 .

<https://sws.geonames.org/12313205/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pilon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313205;
        gn:lat           47.17335;
        gn:long          -1.78749;
        gn:name          "Pilon";
        gn:population    0 .

<https://sws.geonames.org/3233501/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pointeau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233501;
        gn:lat           47.235;
        gn:long          -2.175;
        gn:name          "Le Pointeau";
        gn:population    0 .

<https://sws.geonames.org/6434524/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Luce-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434524;
        gn:lat           47.24944;
        gn:long          -1.48667;
        gn:name          "Sainte-Luce-sur-Loire";
        gn:population    15247 .

<https://sws.geonames.org/3233925/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Basse Bignonnais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233925;
        gn:lat           47.2983;
        gn:long          -1.8995;
        gn:name          "La Basse Bignonnais";
        gn:population    0 .

<https://sws.geonames.org/12313022/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Clos";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313022;
        gn:lat           47.43887;
        gn:long          -2.10138;
        gn:name          "Le Clos";
        gn:population    0 .

<https://sws.geonames.org/12313027/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Grands Moulins";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313027;
        gn:lat           47.32361;
        gn:long          -2.08251;
        gn:name          "Les Grands Moulins";
        gn:population    0 .

<https://sws.geonames.org/3233617/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Basse de l'Imperlay";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.RF;
        gn:geonamesID    3233617;
        gn:lat           47.28222;
        gn:long          -2.13861;
        gn:name          "Basse de l'Imperlay";
        gn:population    0 .

<https://sws.geonames.org/2996628/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Maisdon-sur-Sevre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2996628;
        gn:lat           47.09765;
        gn:long          -1.38482;
        gn:name          "Maisdon-sur-Sèvre";
        gn:population    2218 .

<https://sws.geonames.org/2978658/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Macaire-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978658;
        gn:lat           47.12375;
        gn:long          -0.9916;
        gn:name          "Saint-Macaire-en-Mauges";
        gn:population    6033 .

<https://sws.geonames.org/3006372/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lasseron";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006372;
        gn:lat           47.47354;
        gn:long          -0.97077;
        gn:name          "Lasseron";
        gn:population    0 .

<https://sws.geonames.org/6498553/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Escale Oceania Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6498553;
        gn:lat           47.1592;
        gn:long          -1.5971;
        gn:name          "Escale Oceania Nantes";
        gn:population    0 .

<https://sws.geonames.org/6612548/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Remouille";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6612548;
        gn:lat           47.05556;
        gn:long          -1.37694;
        gn:name          "Remouillé";
        gn:population    1899 .

<https://sws.geonames.org/12313172/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Coteaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313172;
        gn:lat           47.18313;
        gn:long          -1.66854;
        gn:name          "Les Coteaux";
        gn:population    0 .

<https://sws.geonames.org/11205233/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaye de Villeneuve";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSTS;
        gn:geonamesID    11205233;
        gn:lat           47.12336;
        gn:long          -1.53392;
        gn:name          "Abbaye de Villeneuve";
        gn:population    0 .

<https://sws.geonames.org/6434489/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Paulx";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434489;
        gn:lat           46.96278;
        gn:long          -1.75472;
        gn:name          "Paulx";
        gn:population    1978 .

<https://sws.geonames.org/8292944/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Fegreac";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292944;
        gn:lat           47.58525;
        gn:long          -2.04405;
        gn:name          "Bureau de Poste de Fegreac";
        gn:population    0 .

<https://sws.geonames.org/2977847/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Omer";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977847;
        gn:lat           47.47381;
        gn:long          -1.85714;
        gn:name          "Saint-Omer";
        gn:population    0 .

<https://sws.geonames.org/7535058/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Golf de la Bretesche";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RECG;
        gn:geonamesID    7535058;
        gn:lat           47.47957;
        gn:long          -2.17426;
        gn:name          "Golf de la Bretesche";
        gn:population    0 .

<https://sws.geonames.org/12313178/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grande Ville";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313178;
        gn:lat           47.08439;
        gn:long          -1.60539;
        gn:name          "La Grande Ville";
        gn:population    0 .

<https://sws.geonames.org/12313150/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mauvillonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313150;
        gn:lat           47.02212;
        gn:long          -1.45573;
        gn:name          "La Mauvillonnière";
        gn:population    0 .

<https://sws.geonames.org/6458641/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sauveur-de-Landemont";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6458641;
        gn:lat           47.2842;
        gn:long          -1.25578;
        gn:name          "Saint-Sauveur-de-Landemont";
        gn:population    854 .

<https://sws.geonames.org/12313013/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hessin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313013;
        gn:lat           47.46685;
        gn:long          -2.00542;
        gn:name          "Hessin";
        gn:population    0 .

<https://sws.geonames.org/8293017/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Sainte Pazanne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293017;
        gn:lat           47.10449;
        gn:long          -1.81191;
        gn:name          "Bureau de Poste de Sainte Pazanne";
        gn:population    0 .

<https://sws.geonames.org/2986785/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plesse";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2986785;
        gn:lat           47.54178;
        gn:long          -1.88725;
        gn:name          "Plessé";
        gn:population    3833 .

<https://sws.geonames.org/12313129/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Portereau des Landes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313129;
        gn:lat           47.19439;
        gn:long          -1.47674;
        gn:name          "Le Portereau des Landes";
        gn:population    0 .

<https://sws.geonames.org/3233608/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Basse Nazaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.SHOL;
        gn:geonamesID    3233608;
        gn:lat           47.27361;
        gn:long          -2.18972;
        gn:name          "Basse Nazaire";
        gn:population    0 .

<https://sws.geonames.org/12313086/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Nouillere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313086;
        gn:lat           47.16082;
        gn:long          -1.28323;
        gn:name          "La Nouillère";
        gn:population    0 .

<https://sws.geonames.org/6694585/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ancenis";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.AIRP;
        gn:geonamesID    6694585;
        gn:lat           47.408;
        gn:long          -1.178;
        gn:name          "Ancenis";
        gn:population    0 .

<https://sws.geonames.org/6456025/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Planche";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456025;
        gn:lat           47.01639;
        gn:long          -1.43528;
        gn:name          "La Planche";
        gn:population    2610 .

<https://sws.geonames.org/3233425/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe de la Pierre";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    3233425;
        gn:lat           47.16;
        gn:long          -2.19639;
        gn:name          "Pointe de la Pierre";
        gn:population    0 .

<https://sws.geonames.org/6434543/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sautron";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434543;
        gn:lat           47.26361;
        gn:long          -1.66833;
        gn:name          "Sautron";
        gn:population    7915 .

<https://sws.geonames.org/2992206/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montoir-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2992206;
        gn:lat           47.32824;
        gn:long          -2.14877;
        gn:name          "Montoir-de-Bretagne";
        gn:population    6762 .

<https://sws.geonames.org/2972989/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Thehillac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2972989;
        gn:lat           47.56799;
        gn:long          -2.11602;
        gn:name          "Théhillac";
        gn:population    551 .

<https://sws.geonames.org/12148844/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau de Tiffauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.CSTL;
        gn:geonamesID    12148844;
        gn:lat           47.01658;
        gn:long          -1.11486;
        gn:name          "Château de Tiffauges";
        gn:population    0 .

<https://sws.geonames.org/2979544/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Hilaire-de-Mortagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979544;
        gn:lat           46.97477;
        gn:long          -0.93845;
        gn:name          "Saint-Hilaire-de-Mortagne";
        gn:population    0 .

<https://sws.geonames.org/2985302/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Prinquiau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2985302;
        gn:lat           47.3628;
        gn:long          -2.01217;
        gn:name          "Prinquiau";
        gn:population    2243 .

<https://sws.geonames.org/2968805/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Villedieu-la-Blouere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2968805;
        gn:lat           47.14738;
        gn:long          -1.06286;
        gn:name          "Villedieu-la-Blouère";
        gn:population    2236 .

<https://sws.geonames.org/2987810/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Peslan";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2987810;
        gn:lat           47.47846;
        gn:long          -1.8694;
        gn:name          "Peslan";
        gn:population    0 .

<https://sws.geonames.org/9179085/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sejours & Affaires Nantes La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9179085;
        gn:lat           47.25798;
        gn:long          -1.51517;
        gn:name          "Sejours & Affaires Nantes La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/3029977/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brive";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3029977;
        gn:lat           47.48857;
        gn:long          -2.00321;
        gn:name          "Brivé";
        gn:population    0 .

<https://sws.geonames.org/8292963/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Malville";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292963;
        gn:lat           47.36008;
        gn:long          -1.86238;
        gn:name          "Bureau de Poste de Malville";
        gn:population    0 .

<https://sws.geonames.org/12312913/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Provostiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312913;
        gn:lat           47.52355;
        gn:long          -1.34567;
        gn:name          "La Provostière";
        gn:population    0 .

<https://sws.geonames.org/8292917/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Bourgneuf En Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292917;
        gn:lat           47.04239;
        gn:long          -1.95433;
        gn:name          "Bureau de Poste de Bourgneuf En Retz";
        gn:population    0 .

<https://sws.geonames.org/2984708/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quilly";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2984708;
        gn:lat           47.46182;
        gn:long          -1.95411;
        gn:name          "Quilly";
        gn:population    1001 .

<https://sws.geonames.org/12312877/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Peignerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312877;
        gn:lat           47.42005;
        gn:long          -0.97402;
        gn:name          "La Peignerie";
        gn:population    0 .

<https://sws.geonames.org/7290081/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grand Patais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    7290081;
        gn:lat           47.37342;
        gn:long          -1.46959;
        gn:name          "La Grand Patais";
        gn:population    0 .

<https://sws.geonames.org/6435311/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Pierre-Montlimart";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435311;
        gn:lat           47.27056;
        gn:long          -1.02667;
        gn:name          "Saint-Pierre-Montlimart";
        gn:population    3258 .

<https://sws.geonames.org/8286983/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "St-Hilaire-de-Chaleons Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286983;
        gn:lat           47.10569;
        gn:long          -1.865;
        gn:name          "St-Hilaire-de-Chaléons Railway Station";
        gn:population    0 .

<https://sws.geonames.org/12312986/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Renais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312986;
        gn:lat           47.46635;
        gn:long          -1.96312;
        gn:name          "La Rénais";
        gn:population    0 .

<https://sws.geonames.org/10117423/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Seven Urban Suites Nantes Cite Des Congres";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10117423;
        gn:lat           47.2077;
        gn:long          -1.53981;
        gn:name          "Seven Urban Suites Nantes Cite Des Congres";
        gn:population    0 .

<https://sws.geonames.org/3004567/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Clion-sur-Mer";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004567;
        gn:lat           47.12064;
        gn:long          -2.0541;
        gn:name          "Le Clion-sur-Mer";
        gn:population    0 .

<https://sws.geonames.org/12313223/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Manoir";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313223;
        gn:lat           47.10846;
        gn:long          -2.09479;
        gn:name          "Le Manoir";
        gn:population    0 .

<https://sws.geonames.org/6612553/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Touvois";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6612553;
        gn:lat           46.90278;
        gn:long          -1.68306;
        gn:name          "Touvois";
        gn:population    1794 .

<https://sws.geonames.org/3010089/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chauvais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010089;
        gn:lat           47.33559;
        gn:long          -1.57095;
        gn:name          "La Chauvais";
        gn:population    0 .

<https://sws.geonames.org/10281590/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Appart City Nantes Quai de La Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10281590;
        gn:lat           47.21944;
        gn:long          -1.56158;
        gn:name          "Appart City Nantes Quai de La Loire";
        gn:population    0 .

<https://sws.geonames.org/2984381/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ruisseau du Rateau";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2984381;
        gn:lat           47.41667;
        gn:long          -1.48655;
        gn:name          "Ruisseau du Rateau";
        gn:population    0 .

<https://sws.geonames.org/3016162/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Getigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3016162;
        gn:lat           47.07584;
        gn:long          -1.24978;
        gn:name          "Gétigné";
        gn:population    3326 .

<https://sws.geonames.org/12305897/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Chene";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305897;
        gn:lat           47.16567;
        gn:long          -1.48501;
        gn:name          "Le Chêne";
        gn:population    0 .

<https://sws.geonames.org/3019087/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Falleron";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3019087;
        gn:lat           47.02913;
        gn:long          -1.98065;
        gn:name          "Falleron";
        gn:population    0 .

<https://sws.geonames.org/8286993/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gorges Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286993;
        gn:lat           47.10779;
        gn:long          -1.31374;
        gn:name          "Gorges Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3004654/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Chemin-Nantais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004654;
        gn:lat           47.28845;
        gn:long          -1.43417;
        gn:name          "Le Chemin-Nantais";
        gn:population    0 .

<https://sws.geonames.org/3031222/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031222;
        gn:lat           46.97417;
        gn:long          -1.99846;
        gn:name          "Bouin";
        gn:population    2385 .

<https://sws.geonames.org/8436208/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Passerelle Victor-Schoelcher";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436208;
        gn:lat           47.20903;
        gn:long          -1.56152;
        gn:name          "Passerelle Victor-Schœlcher";
        gn:population    0 .

<https://sws.geonames.org/8436223/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont de Mauves";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436223;
        gn:lat           47.29258;
        gn:long          -1.38108;
        gn:name          "Pont de Mauves";
        gn:population    0 .

<https://sws.geonames.org/3008079/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Morandais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008079;
        gn:lat           47.38309;
        gn:long          -2.09083;
        gn:name          "La Morandais";
        gn:population    0 .

<https://sws.geonames.org/12312967/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bretonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312967;
        gn:lat           47.26837;
        gn:long          -1.67258;
        gn:name          "La Bretonnière";
        gn:population    0 .

<https://sws.geonames.org/3008188/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Meignelais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008188;
        gn:lat           47.39239;
        gn:long          -1.80869;
        gn:name          "La Meignelais";
        gn:population    0 .

<https://sws.geonames.org/3004138/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fuilet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3004138;
        gn:lat           47.28345;
        gn:long          -1.1131;
        gn:name          "Le Fuilet";
        gn:population    1925 .

<https://sws.geonames.org/12313089/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rouaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313089;
        gn:lat           47.13129;
        gn:long          -1.2957;
        gn:name          "La Rouaudière";
        gn:population    0 .

<https://sws.geonames.org/3233450/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Croix de Mean";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233450;
        gn:lat           47.30267;
        gn:long          -2.19122;
        gn:name          "La Croix de Méan";
        gn:population    0 .

<https://sws.geonames.org/12313159/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Landes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313159;
        gn:lat           47.17331;
        gn:long          -1.58438;
        gn:name          "Les Landes";
        gn:population    0 .

<https://sws.geonames.org/8293012/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Mars Du Desert";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293012;
        gn:lat           47.36426;
        gn:long          -1.40539;
        gn:name          "Bureau de Poste de Saint Mars Du Desert";
        gn:population    0 .

<https://sws.geonames.org/12514797/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Plessis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12514797;
        gn:lat           47.56614;
        gn:long          -2.17795;
        gn:name          "Le Plessis";
        gn:population    0 .

<https://sws.geonames.org/2980761/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Anne-sur-Brivet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980761;
        gn:lat           47.46071;
        gn:long          -2.00415;
        gn:name          "Sainte-Anne-sur-Brivet";
        gn:population    2086 .

<https://sws.geonames.org/12310611/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Lazare";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310611;
        gn:lat           47.01012;
        gn:long          -1.10796;
        gn:name          "Saint-Lazare";
        gn:population    0 .

<https://sws.geonames.org/3233440/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Banc du Pointeau";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.SHOL;
        gn:geonamesID    3233440;
        gn:lat           47.22321;
        gn:long          -2.1869;
        gn:name          "Banc du Pointeau";
        gn:population    0 .

<https://sws.geonames.org/10173546/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nantes Est Sainte Luce Sur Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10173546;
        gn:lat           47.262;
        gn:long          -1.494;
        gn:name          "Nantes Est Sainte Luce Sur Loire";
        gn:population    0 .

<https://sws.geonames.org/8436214/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Eric-Tabarly";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436214;
        gn:lat           47.21253;
        gn:long          -1.52919;
        gn:name          "Pont Éric-Tabarly";
        gn:population    0 .

<https://sws.geonames.org/6449416/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cande";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449416;
        gn:lat           47.56083;
        gn:long          -1.03722;
        gn:name          "Candé";
        gn:population    2845 .

<https://sws.geonames.org/3233932/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gabon de la Marechale";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.DTCHD;
        gn:geonamesID    3233932;
        gn:lat           47.27845;
        gn:long          -1.92103;
        gn:name          "Gabon de la Maréchale";
        gn:population    0 .

<https://sws.geonames.org/6449072/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Blain";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449072;
        gn:lat           47.47611;
        gn:long          -1.76361;
        gn:name          "Blain";
        gn:population    9687 .

<https://sws.geonames.org/12312894/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Chapelettes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312894;
        gn:lat           47.51743;
        gn:long          -1.23767;
        gn:name          "Les Chapelettes";
        gn:population    0 .

<https://sws.geonames.org/13494803/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ancien Grand Hotel de la plage et du golf";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    13494803;
        gn:lat           47.11085;
        gn:long          -2.1162;
        gn:name          "Ancien Grand Hôtel de la plage et du golf";
        gn:population    0 .

<https://sws.geonames.org/3030972/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Baie de Bourgneuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.BAY;
        gn:geonamesID    3030972;
        gn:lat           47.0673;
        gn:long          -2.1792;
        gn:name          "Baie de Bourgneuf";
        gn:population    0 .

<https://sws.geonames.org/3007397/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Pepiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007397;
        gn:lat           47.10492;
        gn:long          -1.41254;
        gn:name          "La Pepière";
        gn:population    0 .

<https://sws.geonames.org/8293003/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Jean De Boiseau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293003;
        gn:lat           47.1945;
        gn:long          -1.6999;
        gn:name          "Bureau de Poste de Saint Jean De Boiseau";
        gn:population    0 .

<https://sws.geonames.org/3011134/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Belle-Ile";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3011134;
        gn:lat           47.2606;
        gn:long          -1.87882;
        gn:name          "Belle-Île";
        gn:population    0 .

<https://sws.geonames.org/2985309/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de Prince";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2985309;
        gn:lat           47.15596;
        gn:long          -1.89191;
        gn:name          "Forêt de Princé";
        gn:population    0 .

<https://sws.geonames.org/3024578/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Clisson";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3024578;
        gn:lat           47.0871;
        gn:long          -1.28297;
        gn:name          "Clisson";
        gn:population    6480 .

<https://sws.geonames.org/3006454/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Seguiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006454;
        gn:lat           47.06343;
        gn:long          -0.93996;
        gn:name          "La Séguinière";
        gn:population    3744 .

<https://sws.geonames.org/9178224/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Park & Suites Confort Carquefou";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9178224;
        gn:lat           47.26892;
        gn:long          -1.48496;
        gn:name          "Park & Suites Confort Carquefou";
        gn:population    0 .

<https://sws.geonames.org/6456031/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Temple-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456031;
        gn:lat           47.3283;
        gn:long          -1.7893;
        gn:name          "Le Temple-de-Bretagne";
        gn:population    2006 .

<https://sws.geonames.org/8292981/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Le Pellerin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292981;
        gn:lat           47.198;
        gn:long          -1.75198;
        gn:name          "Bureau de Poste de Le Pellerin";
        gn:population    0 .

<https://sws.geonames.org/3011029/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Birochere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011029;
        gn:lat           47.10776;
        gn:long          -2.07788;
        gn:name          "La Birochere";
        gn:population    0 .

<https://sws.geonames.org/3033870/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Begrolles-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3033870;
        gn:lat           47.14102;
        gn:long          -0.93991;
        gn:name          "Bégrolles-en-Mauges";
        gn:population    1617 .

<https://sws.geonames.org/12719961/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Artotheque de Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.LIBR;
        gn:geonamesID    12719961;
        gn:lat           47.21121;
        gn:long          -1.5623;
        gn:name          "Artothèque de Nantes";
        gn:population    0 .

<https://sws.geonames.org/3233610/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Croix";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233610;
        gn:lat           47.25268;
        gn:long          -2.14937;
        gn:name          "La Croix";
        gn:population    0 .

<https://sws.geonames.org/6451606/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chambretaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6451606;
        gn:lat           46.92167;
        gn:long          -0.96472;
        gn:name          "Chambretaud";
        gn:population    1460 .

<https://sws.geonames.org/2986498/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Etang de la Poiteviniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.LK;
        gn:geonamesID    2986498;
        gn:lat           47.53716;
        gn:long          -1.29875;
        gn:name          "Étang de la Poitevinière";
        gn:population    0 .

<https://sws.geonames.org/3003890/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Gue";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003890;
        gn:lat           47.38967;
        gn:long          -2.12211;
        gn:name          "Le Gué";
        gn:population    0 .

<https://sws.geonames.org/12308551/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont de Moine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308551;
        gn:lat           47.09638;
        gn:long          -1.126;
        gn:name          "Pont de Moine";
        gn:population    0 .

<https://sws.geonames.org/6614514/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Paimbœuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614514;
        gn:lat           47.2875;
        gn:long          -2.03167;
        gn:name          "Paimbœuf";
        gn:population    3144 .

<https://sws.geonames.org/2988522/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Paribou";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2988522;
        gn:lat           47.4;
        gn:long          -1.81667;
        gn:name          "Paribou";
        gn:population    0 .

<https://sws.geonames.org/2991285/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mouzillon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2991285;
        gn:lat           47.14149;
        gn:long          -1.28388;
        gn:name          "Mouzillon";
        gn:population    2385 .

<https://sws.geonames.org/12313029/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile de Mazin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313029;
        gn:lat           47.39415;
        gn:long          -2.19666;
        gn:name          "Île de Mazin";
        gn:population    0 .

<https://sws.geonames.org/9539757/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nuit De Retz Hotel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539757;
        gn:lat           47.14254;
        gn:long          -1.75214;
        gn:name          "Nuit De Retz Hotel";
        gn:population    0 .

<https://sws.geonames.org/9539809/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Contact Hotel Terminus";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539809;
        gn:lat           47.21775;
        gn:long          -1.54373;
        gn:name          "Contact Hotel Terminus";
        gn:population    0 .

<https://sws.geonames.org/3002697/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Plessis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002697;
        gn:lat           47.55152;
        gn:long          -1.8738;
        gn:name          "Le Plessis";
        gn:population    0 .

<https://sws.geonames.org/8297423/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Montaigu";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297423;
        gn:lat           46.97727;
        gn:long          -1.31078;
        gn:name          "Bureau de Poste de Montaigu";
        gn:population    0 .

<https://sws.geonames.org/8286978/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Oudon Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286978;
        gn:lat           47.34306;
        gn:long          -1.29166;
        gn:name          "Oudon Railway Station";
        gn:population    0 .

<https://sws.geonames.org/2979589/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Herblon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979589;
        gn:lat           47.40818;
        gn:long          -1.09575;
        gn:name          "Saint-Herblon";
        gn:population    1950 .

<https://sws.geonames.org/3233974/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile Pivin";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3233974;
        gn:lat           47.20367;
        gn:long          -1.70969;
        gn:name          "Île Pivin";
        gn:population    0 .

<https://sws.geonames.org/8292953/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Haute Goulaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292953;
        gn:lat           47.19995;
        gn:long          -1.431;
        gn:name          "Bureau de Poste de Haute Goulaine";
        gn:population    0 .

<https://sws.geonames.org/10297831/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Le Cambronne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297831;
        gn:lat           47.21189;
        gn:long          -1.56168;
        gn:name          "Hôtel Le Cambronne";
        gn:population    0 .

<https://sws.geonames.org/8292996/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Aignan Grand Lieu";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292996;
        gn:lat           47.12345;
        gn:long          -1.63115;
        gn:name          "Bureau de Poste de Saint Aignan Grand Lieu";
        gn:population    0 .

<https://sws.geonames.org/3010040/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chevroliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010040;
        gn:lat           47.09105;
        gn:long          -1.61119;
        gn:name          "La Chevrolière";
        gn:population    5220 .

<https://sws.geonames.org/6613890/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Christophe-du-Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6613890;
        gn:lat           47.02861;
        gn:long          -0.94528;
        gn:name          "Saint-Christophe-du-Bois";
        gn:population    2699 .

<https://sws.geonames.org/6434488/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pannece";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434488;
        gn:lat           47.48611;
        gn:long          -1.23944;
        gn:name          "Pannecé";
        gn:population    1342 .

<https://sws.geonames.org/6496933/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brit'Hotel Le Kerann";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6496933;
        gn:lat           47.2336;
        gn:long          -1.6525;
        gn:name          "Brit'Hotel Le Kerann";
        gn:population    0 .

<https://sws.geonames.org/12313210/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Marais Mainguy";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313210;
        gn:lat           47.11712;
        gn:long          -2.00464;
        gn:name          "Le Marais Mainguy";
        gn:population    0 .

<https://sws.geonames.org/12305887/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pe Bardou";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305887;
        gn:lat           47.22724;
        gn:long          -1.31321;
        gn:name          "Le Pé Bardou";
        gn:population    0 .

<https://sws.geonames.org/8286947/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Dreffeac Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286947;
        gn:lat           47.48182;
        gn:long          -2.05032;
        gn:name          "Dreffeac Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3008695/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Huchetiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008695;
        gn:lat           47.56295;
        gn:long          -1.51752;
        gn:name          "La Huchetière";
        gn:population    0 .

<https://sws.geonames.org/12750476/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Observatoire des Sciences de l'Univers Nantes Atlantique";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.OBS;
        gn:geonamesID    12750476;
        gn:lat           47.23881;
        gn:long          -1.55563;
        gn:name          "Observatoire des Sciences de l'Univers Nantes Atlantique";
        gn:population    0 .

<https://sws.geonames.org/2974701/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Severac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2974701;
        gn:lat           47.55029;
        gn:long          -2.0762;
        gn:name          "Sévérac";
        gn:population    1288 .

<https://sws.geonames.org/8293039/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Vigneux De Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293039;
        gn:lat           47.32672;
        gn:long          -1.73606;
        gn:name          "Bureau de Poste de Vigneux De Bretagne";
        gn:population    0 .

<https://sws.geonames.org/12310618/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bretiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310618;
        gn:lat           46.97873;
        gn:long          -1.24144;
        gn:name          "La Bretinière";
        gn:population    0 .

<https://sws.geonames.org/6618280/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Marne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6618280;
        gn:lat           46.99556;
        gn:long          -1.74111;
        gn:name          "La Marne";
        gn:population    1479 .

<https://sws.geonames.org/2972243/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Tournebride";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2972243;
        gn:lat           47.17703;
        gn:long          -1.40989;
        gn:name          "Tournebride";
        gn:population    0 .

<https://sws.geonames.org/13236900/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boulevard Le Corbusier";
        gn:countryCode   "FR";
        gn:featureClass  gn:R;
        gn:featureCode   gn:R.ST;
        gn:geonamesID    13236900;
        gn:lat           47.18889;
        gn:long          -1.5712;
        gn:name          "Boulevard Le Corbusier";
        gn:population    0 .

<https://sws.geonames.org/12308488/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rimonerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308488;
        gn:lat           47.27545;
        gn:long          -1.13385;
        gn:name          "La Rimonerie";
        gn:population    0 .

<https://sws.geonames.org/3005351/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bas Mats";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3005351;
        gn:lat           47.37012;
        gn:long          -1.9506;
        gn:name          "Le Bas Mats";
        gn:population    0 .

<https://sws.geonames.org/3233447/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hautgas";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233447;
        gn:lat           47.31544;
        gn:long          -2.06087;
        gn:name          "Hautgas";
        gn:population    0 .

<https://sws.geonames.org/8292934/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Clisson";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292934;
        gn:lat           47.08889;
        gn:long          -1.27665;
        gn:name          "Bureau de Poste de Clisson";
        gn:population    0 .

<https://sws.geonames.org/3026308/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau-Bougon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3026308;
        gn:lat           47.16667;
        gn:long          -1.58333;
        gn:name          "Château-Bougon";
        gn:population    0 .

<https://sws.geonames.org/2980127/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Fiacre-sur-Maine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980127;
        gn:lat           47.14245;
        gn:long          -1.41675;
        gn:name          "Saint-Fiacre-sur-Maine";
        gn:population    1071 .

<https://sws.geonames.org/6434494/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pontchateau";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434494;
        gn:lat           47.43694;
        gn:long          -2.08778;
        gn:name          "Pontchâteau";
        gn:population    10666 .

<https://sws.geonames.org/3020823/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Dreneuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3020823;
        gn:lat           47.44774;
        gn:long          -1.66393;
        gn:name          "Dreneuf";
        gn:population    0 .

<https://sws.geonames.org/3007288/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Piquelotais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007288;
        gn:lat           47.37821;
        gn:long          -1.74346;
        gn:name          "La Piquelotais";
        gn:population    0 .

<https://sws.geonames.org/12313201/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Launay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313201;
        gn:lat           47.19763;
        gn:long          -1.82823;
        gn:name          "Launay";
        gn:population    0 .

<https://sws.geonames.org/12312915/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Bois Bautier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312915;
        gn:lat           47.45871;
        gn:long          -1.30848;
        gn:name          "Le Bois Bautier";
        gn:population    0 .

<https://sws.geonames.org/2996904/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de Machecoul";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2996904;
        gn:lat           47.01775;
        gn:long          -1.74029;
        gn:name          "Forêt de Machecoul";
        gn:population    0 .

<https://sws.geonames.org/3012217/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bourg de Joue-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3012217;
        gn:lat           47.49596;
        gn:long          -1.42047;
        gn:name          "Bourg de Joué-sur-Erdre";
        gn:population    1834 .

<https://sws.geonames.org/3233410/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nor Garin";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233410;
        gn:lat           47.08079;
        gn:long          -2.07984;
        gn:name          "Nor Garin";
        gn:population    0 .

<https://sws.geonames.org/12313119/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313119;
        gn:lat           47.09725;
        gn:long          -1.36478;
        gn:name          "Le Pay";
        gn:population    0 .

<https://sws.geonames.org/12313141/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bouteillerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313141;
        gn:lat           47.16276;
        gn:long          -1.44166;
        gn:name          "La Bouteillerie";
        gn:population    0 .

<https://sws.geonames.org/2975597/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Savenay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2975597;
        gn:lat           47.36106;
        gn:long          -1.94206;
        gn:name          "Savenay";
        gn:population    6770 .

<https://sws.geonames.org/8293044/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Copernic";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293044;
        gn:lat           47.21485;
        gn:long          -1.56543;
        gn:name          "Bureau de Poste de Nantes Copernic";
        gn:population    0 .

<https://sws.geonames.org/12313228/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Grandes Vallees";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313228;
        gn:lat           47.11324;
        gn:long          -2.11457;
        gn:name          "Les Grandes Vallées";
        gn:population    0 .

<https://sws.geonames.org/6434551/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trans-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434551;
        gn:lat           47.47639;
        gn:long          -1.37361;
        gn:name          "Trans-sur-Erdre";
        gn:population    1065 .

<https://sws.geonames.org/10110274/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Des 3 Marchands";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10110274;
        gn:lat           47.21851;
        gn:long          -1.55624;
        gn:name          "Hotel Des 3 Marchands";
        gn:population    0 .

<https://sws.geonames.org/2988634/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pannece";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2988634;
        gn:lat           47.48549;
        gn:long          -1.24002;
        gn:name          "Pannecé";
        gn:population    1025 .

<https://sws.geonames.org/3002517/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret de Leppo";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    3002517;
        gn:lat           47.23774;
        gn:long          -1.08881;
        gn:name          "Forêt de Leppo";
        gn:population    0 .

<https://sws.geonames.org/8293406/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Leger Sous Cholet";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293406;
        gn:lat           47.092;
        gn:long          -0.91126;
        gn:name          "Bureau de Poste de Saint Leger Sous Cholet";
        gn:population    0 .

<https://sws.geonames.org/6941453/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rue du Bois Praud";
        gn:countryCode   "FR";
        gn:featureClass  gn:R;
        gn:featureCode   gn:R.ST;
        gn:geonamesID    6941453;
        gn:lat           47.19885;
        gn:long          -1.52554;
        gn:name          "Rue du Bois Praud";
        gn:population    0 .

<https://sws.geonames.org/3008294/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile de la Marechale";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3008294;
        gn:lat           47.27262;
        gn:long          -1.92108;
        gn:name          "Île de la Maréchale";
        gn:population    0 .

<https://sws.geonames.org/3233466/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Noe";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233466;
        gn:lat           47.26548;
        gn:long          -1.96786;
        gn:name          "La Noë";
        gn:population    0 .

<https://sws.geonames.org/8297385/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Bouin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8297385;
        gn:lat           46.9737;
        gn:long          -1.9985;
        gn:name          "Bureau de Poste de Bouin";
        gn:population    0 .

<https://sws.geonames.org/12305733/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Recoins";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305733;
        gn:lat           47.26363;
        gn:long          -1.13828;
        gn:name          "Les Recoins";
        gn:population    0 .

<https://sws.geonames.org/3018859/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Fay-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3018859;
        gn:lat           47.41515;
        gn:long          -1.79196;
        gn:name          "Fay-de-Bretagne";
        gn:population    2687 .

<https://sws.geonames.org/8286973/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Basse-Indre Saint-Herblain Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286973;
        gn:lat           47.20428;
        gn:long          -1.66105;
        gn:name          "La Basse-Indre Saint-Herblain Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3006258/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Tiollais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006258;
        gn:lat           47.41346;
        gn:long          -1.93321;
        gn:name          "La Tiollais";
        gn:population    0 .

<https://sws.geonames.org/2984849/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quehillac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2984849;
        gn:lat           47.42428;
        gn:long          -1.89976;
        gn:name          "Quéhillac";
        gn:population    0 .

<https://sws.geonames.org/6616816/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sulpice-des-Landes";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6616816;
        gn:lat           47.5749;
        gn:long          -1.2052;
        gn:name          "Saint-Sulpice-des-Landes";
        gn:population    636 .

<https://sws.geonames.org/10175485/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes Centre St Jac";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10175485;
        gn:lat           47.19617;
        gn:long          -1.53097;
        gn:name          "Campanile Nantes Centre St Jac";
        gn:population    0 .

<https://sws.geonames.org/6498801/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Citea Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6498801;
        gn:lat           47.2067;
        gn:long          -1.5792;
        gn:name          "Citea Nantes";
        gn:population    0 .

<https://sws.geonames.org/6456021/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Montagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456021;
        gn:lat           47.19;
        gn:long          -1.68389;
        gn:name          "La Montagne";
        gn:population    6215 .

<https://sws.geonames.org/11073018/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plage de la Boutinardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.BCH;
        gn:geonamesID    11073018;
        gn:lat           47.094;
        gn:long          -2.05273;
        gn:name          "Plage de la Boutinardière";
        gn:population    0 .

<https://sws.geonames.org/6613024/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Clisson";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6613024;
        gn:lat           47.08694;
        gn:long          -1.28361;
        gn:name          "Clisson";
        gn:population    7035 .

<https://sws.geonames.org/12313198/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Soherie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313198;
        gn:lat           47.02959;
        gn:long          -1.6989;
        gn:name          "La Sohérie";
        gn:population    0 .

<https://sws.geonames.org/6449088/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Couffe";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449088;
        gn:lat           47.39139;
        gn:long          -1.29278;
        gn:name          "Couffé";
        gn:population    2543 .

<https://sws.geonames.org/2977598/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Philbert-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2977598;
        gn:lat           47.15107;
        gn:long          -1.01595;
        gn:name          "Saint-Philbert-en-Mauges";
        gn:population    346 .

<https://sws.geonames.org/9179105/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Seven Urban Suites";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9179105;
        gn:lat           47.20829;
        gn:long          -1.53833;
        gn:name          "Seven Urban Suites";
        gn:population    0 .

<https://sws.geonames.org/3021084/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Donneau";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3021084;
        gn:lat           47.37107;
        gn:long          -1.29488;
        gn:name          "Donneau";
        gn:population    0 .

<https://sws.geonames.org/3233452/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Martiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233452;
        gn:lat           47.20486;
        gn:long          -1.77737;
        gn:name          "La Martinière";
        gn:population    0 .

<https://sws.geonames.org/3233986/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bras de la Madeleine";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STMA;
        gn:geonamesID    3233986;
        gn:lat           47.2;
        gn:long          -1.56667;
        gn:name          "Bras de la Madeleine";
        gn:population    0 .

<https://sws.geonames.org/3233491/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rochers de la Roussellarie";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233491;
        gn:lat           47.19413;
        gn:long          -2.16636;
        gn:name          "Rochers de la Roussellarie";
        gn:population    0 .

<https://sws.geonames.org/9177353/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Kyriad  Nantes Ouest - Saint Herblain";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177353;
        gn:lat           47.22778;
        gn:long          -1.62445;
        gn:name          "Kyriad  Nantes Ouest - Saint Herblain";
        gn:population    0 .

<https://sws.geonames.org/12313217/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Olivettes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313217;
        gn:lat           47.12209;
        gn:long          -2.10537;
        gn:name          "Les Olivettes";
        gn:population    0 .

<https://sws.geonames.org/3233944/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Chemin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233944;
        gn:lat           47.19659;
        gn:long          -1.78258;
        gn:name          "Le Grand Chemin";
        gn:population    0 .

<https://sws.geonames.org/3024773/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Clanet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3024773;
        gn:lat           47.45179;
        gn:long          -1.63369;
        gn:name          "Clanet";
        gn:population    0 .

<https://sws.geonames.org/3233404/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pierre du Chenal";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RK;
        gn:geonamesID    3233404;
        gn:lat           47.07404;
        gn:long          -2.12551;
        gn:name          "Pierre du Chenal";
        gn:population    0 .

<https://sws.geonames.org/12310648/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chataigneraie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310648;
        gn:lat           46.92625;
        gn:long          -1.03773;
        gn:name          "La Châtaigneraie";
        gn:population    0 .

<https://sws.geonames.org/12313030/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile d'Errand";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313030;
        gn:lat           47.37264;
        gn:long          -2.15921;
        gn:name          "Île d'Errand";
        gn:population    0 .

<https://sws.geonames.org/7535060/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Golf Pornic";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RECG;
        gn:geonamesID    7535060;
        gn:lat           47.1191;
        gn:long          -2.1173;
        gn:name          "Golf Pornic";
        gn:population    0 .

<https://sws.geonames.org/3003672/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Longeron";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003672;
        gn:lat           47.01845;
        gn:long          -1.05763;
        gn:name          "Le Longeron";
        gn:population    2004 .

<https://sws.geonames.org/6449074/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouee";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449074;
        gn:lat           47.32083;
        gn:long          -1.91;
        gn:name          "Bouée";
        gn:population    956 .

<https://sws.geonames.org/8293348/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Beaupreau";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293348;
        gn:lat           47.20386;
        gn:long          -0.98986;
        gn:name          "Bureau de Poste de Beaupreau";
        gn:population    0 .

<https://sws.geonames.org/12312952/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Chenaies";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312952;
        gn:lat           47.36891;
        gn:long          -1.5843;
        gn:name          "Les Chênaies";
        gn:population    0 .

<https://sws.geonames.org/6473356/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Kyriad";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6473356;
        gn:lat           47.2177;
        gn:long          -1.5444;
        gn:name          "Kyriad";
        gn:population    0 .

<https://sws.geonames.org/8293054/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Republique";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293054;
        gn:lat           47.20475;
        gn:long          -1.55341;
        gn:name          "Bureau de Poste de Nantes Republique";
        gn:population    0 .

<https://sws.geonames.org/3015298/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Grandchamps-des-Fontaines";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3015298;
        gn:lat           47.36512;
        gn:long          -1.60589;
        gn:name          "Grandchamps-des-Fontaines";
        gn:population    0 .

<https://sws.geonames.org/3013246/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ruisseau Hocmard";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3013246;
        gn:lat           47.31215;
        gn:long          -1.53345;
        gn:name          "Ruisseau Hocmard";
        gn:population    0 .

<https://sws.geonames.org/12313144/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Mortaliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313144;
        gn:lat           47.17058;
        gn:long          -1.46378;
        gn:name          "La Mortalière";
        gn:population    0 .

<https://sws.geonames.org/12313181/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Barbatiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313181;
        gn:lat           47.02535;
        gn:long          -1.59382;
        gn:name          "La Barbatière";
        gn:population    0 .

<https://sws.geonames.org/6455415/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Romagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6455415;
        gn:lat           47.06111;
        gn:long          -1.02194;
        gn:name          "La Romagne";
        gn:population    1835 .

<https://sws.geonames.org/12312930/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gannerais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312930;
        gn:lat           47.57369;
        gn:long          -1.38604;
        gn:name          "La Gannerais";
        gn:population    0 .

<https://sws.geonames.org/8293025/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Severac";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293025;
        gn:lat           47.55067;
        gn:long          -2.07365;
        gn:name          "Bureau de Poste de Severac";
        gn:population    0 .

<https://sws.geonames.org/7284016/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Haute Goulaine TV Mast";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.TOWR;
        gn:geonamesID    7284016;
        gn:lat           47.18691;
        gn:long          -1.43578;
        gn:name          "Haute Goulaine TV Mast";
        gn:population    0 .

<https://sws.geonames.org/3031022/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bourg de Nozay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031022;
        gn:lat           47.56667;
        gn:long          -1.61667;
        gn:name          "Bourg de Nozay";
        gn:population    0 .

<https://sws.geonames.org/10110277/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Belfort";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10110277;
        gn:lat           47.21112;
        gn:long          -1.54463;
        gn:name          "Hotel Belfort";
        gn:population    0 .

<https://sws.geonames.org/12156387/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "chateau de Clermont-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.CSTL;
        gn:geonamesID    12156387;
        gn:lat           47.32515;
        gn:long          -1.33368;
        gn:name          "château de Clermont-sur-Loire";
        gn:population    0 .

<https://sws.geonames.org/12313094/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Brie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313094;
        gn:lat           47.10782;
        gn:long          -1.33341;
        gn:name          "La Brie";
        gn:population    0 .

<https://sws.geonames.org/3034283/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau de Beaujour";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HSEC;
        gn:geonamesID    3034283;
        gn:lat           47.53333;
        gn:long          -1.21667;
        gn:name          "Château de Beaujour";
        gn:population    0 .

<https://sws.geonames.org/6299464/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Saint-Nazaire - Montoir";
        <https://schema.org/elevation>  3.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:S;
        gn:featureCode                  gn:S.AIRP;
        gn:geonamesID                   6299464;
        gn:lat                          47.31219;
        gn:long                         -2.14918;
        gn:name                         "Saint-Nazaire - Montoir";
        gn:population                   0 .

<https://sws.geonames.org/2984674/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quinhu";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2984674;
        gn:lat           47.48571;
        gn:long          -1.895;
        gn:name          "Quinhu";
        gn:population    0 .

<https://sws.geonames.org/3026250/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateauneuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3026250;
        gn:lat           46.91762;
        gn:long          -1.91219;
        gn:name          "Châteauneuf";
        gn:population    683 .

<https://sws.geonames.org/8286990/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vertou Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286990;
        gn:lat           47.18597;
        gn:long          -1.47793;
        gn:name          "Vertou Railway Station";
        gn:population    0 .

<https://sws.geonames.org/8293401/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Florent Le Vieil";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293401;
        gn:lat           47.361;
        gn:long          -1.01623;
        gn:name          "Bureau de Poste de Saint Florent Le Vieil";
        gn:population    0 .

<https://sws.geonames.org/3034228/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beaumard";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3034228;
        gn:lat           47.4566;
        gn:long          -2.11399;
        gn:name          "Beaumard";
        gn:population    0 .

<https://sws.geonames.org/3007934/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lance";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007934;
        gn:lat           47.53771;
        gn:long          -1.92677;
        gn:name          "Lancé";
        gn:population    0 .

<https://sws.geonames.org/3031659/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bonnœuvre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031659;
        gn:lat           47.53333;
        gn:long          -1.23333;
        gn:name          "Bonnœuvre";
        gn:population    548 .

<https://sws.geonames.org/2981296/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Brevin-les-Pins";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981296;
        gn:lat           47.24693;
        gn:long          -2.16647;
        gn:name          "Saint-Brevin-les-Pins";
        gn:population    10396 .

<https://sws.geonames.org/3009255/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Freusiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009255;
        gn:lat           47.32047;
        gn:long          -1.76702;
        gn:name          "La Freusière";
        gn:population    0 .

<https://sws.geonames.org/12312944/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Monceaux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312944;
        gn:lat           47.31108;
        gn:long          -1.50832;
        gn:name          "Les Monceaux";
        gn:population    0 .

<https://sws.geonames.org/2988583/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Foret du Parc";
        gn:countryCode   "FR";
        gn:featureClass  gn:V;
        gn:featureCode   gn:V.FRST;
        gn:geonamesID    2988583;
        gn:lat           47.30286;
        gn:long          -1.22214;
        gn:name          "Forêt du Parc";
        gn:population    0 .

<https://sws.geonames.org/12313136/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beautour";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313136;
        gn:lat           47.17763;
        gn:long          -1.50496;
        gn:name          "Beautour";
        gn:population    0 .

<https://sws.geonames.org/2997692/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Longrais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2997692;
        gn:lat           47.34215;
        gn:long          -1.43595;
        gn:name          "Longrais";
        gn:population    0 .

<https://sws.geonames.org/8292975/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Notre Dame Des Landes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292975;
        gn:lat           47.38041;
        gn:long          -1.71141;
        gn:name          "Bureau de Poste de Notre Dame Des Landes";
        gn:population    0 .

<https://sws.geonames.org/3011203/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Baudonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011203;
        gn:lat           47.59857;
        gn:long          -1.0639;
        gn:name          "La Baudonnière";
        gn:population    0 .

<https://sws.geonames.org/11280028/>
        rdf:type                        gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel                   "Residhome Nantes Les Berges De La Loire";
        <https://schema.org/elevation>  0.0;
        gn:countryCode                  "FR";
        gn:featureClass                 gn:S;
        gn:featureCode                  gn:S.HTL;
        gn:geonamesID                   11280028;
        gn:lat                          47.21214;
        gn:long                         -1.53824;
        gn:name                         "Residhome Nantes Les Berges De La Loire";
        gn:population                   0 .

<https://sws.geonames.org/9177317/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inter-Hotel Saint James";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177317;
        gn:lat           46.95699;
        gn:long          -1.35095;
        gn:name          "Inter-Hotel Saint James";
        gn:population    0 .

<https://sws.geonames.org/10234497/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Univea Suites Nantes La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10234497;
        gn:lat           47.25995;
        gn:long          -1.49819;
        gn:name          "Univea Suites Nantes La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/8292926/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Chapelle Heulin";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292926;
        gn:lat           47.17641;
        gn:long          -1.34028;
        gn:name          "Bureau de Poste de La Chapelle Heulin";
        gn:population    0 .

<https://sws.geonames.org/12312922/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Branchere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312922;
        gn:lat           47.34702;
        gn:long          -1.32768;
        gn:name          "La Branchère";
        gn:population    0 .

<https://sws.geonames.org/3003466/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Menil";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003466;
        gn:lat           47.56088;
        gn:long          -1.66588;
        gn:name          "Le Ménil";
        gn:population    0 .

<https://sws.geonames.org/2999572/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Sorinieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999572;
        gn:lat           47.14744;
        gn:long          -1.53004;
        gn:name          "Les Sorinières";
        gn:population    6698 .

<https://sws.geonames.org/2987036/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pirudel";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2987036;
        gn:lat           47.52184;
        gn:long          -1.6747;
        gn:name          "Pirudel";
        gn:population    0 .

<https://sws.geonames.org/3007320/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Piardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007320;
        gn:lat           47.53471;
        gn:long          -1.86018;
        gn:name          "La Piardière";
        gn:population    0 .

<https://sws.geonames.org/6452331/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Barbechat";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6452331;
        gn:lat           47.2775;
        gn:long          -1.28639;
        gn:name          "Barbechat";
        gn:population    1275 .

<https://sws.geonames.org/12313126/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fontaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313126;
        gn:lat           47.20286;
        gn:long          -1.49408;
        gn:name          "La Fontaine";
        gn:population    0 .

<https://sws.geonames.org/8293398/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Andre De La Marche";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293398;
        gn:lat           47.1011;
        gn:long          -0.99439;
        gn:name          "Bureau de Poste de Saint Andre De La Marche";
        gn:population    0 .

<https://sws.geonames.org/12313235/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Coeures";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313235;
        gn:lat           47.12014;
        gn:long          -2.12576;
        gn:name          "Les Cœurés";
        gn:population    0 .

<https://sws.geonames.org/11746344/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arcades du Gue de la Roche";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.ARCH;
        gn:geonamesID    11746344;
        gn:lat           47.49087;
        gn:long          -1.4682;
        gn:name          "Arcades du Gué de la Roche";
        gn:population    0 .

<https://sws.geonames.org/6455303/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateauneuf";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6455303;
        gn:lat           46.9175;
        gn:long          -1.91056;
        gn:name          "Châteauneuf";
        gn:population    1027 .

<https://sws.geonames.org/3009280/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fraudais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009280;
        gn:lat           47.49798;
        gn:long          -1.73678;
        gn:name          "La Fraudais";
        gn:population    0 .

<https://sws.geonames.org/12313034/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Caves";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313034;
        gn:lat           47.33103;
        gn:long          -2.1392;
        gn:name          "Les Caves";
        gn:population    0 .

<https://sws.geonames.org/9173332/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Best Western Villa Saint Antoine";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9173332;
        gn:lat           47.08687;
        gn:long          -1.27839;
        gn:name          "Best Western Villa Saint Antoine";
        gn:population    0 .

<https://sws.geonames.org/3233449/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Menee Lambourg";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233449;
        gn:lat           47.30667;
        gn:long          -2.1875;
        gn:name          "La Menée Lambourg";
        gn:population    0 .

<https://sws.geonames.org/11906050/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Machines de l'ile";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.MUS;
        gn:geonamesID    11906050;
        gn:lat           47.20557;
        gn:long          -1.56451;
        gn:name          "Machines de l'île";
        gn:population    0 .

<https://sws.geonames.org/2998404/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ligne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998404;
        gn:lat           47.41148;
        gn:long          -1.37796;
        gn:name          "Ligné";
        gn:population    3222 .

<https://sws.geonames.org/3233919/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile de Pierre Rouge";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISLX;
        gn:geonamesID    3233919;
        gn:lat           47.295;
        gn:long          -1.975;
        gn:name          "Île de Pierre Rouge";
        gn:population    0 .

<https://sws.geonames.org/2987658/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Petit-Mars";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2987658;
        gn:lat           47.39439;
        gn:long          -1.45492;
        gn:name          "Petit-Mars";
        gn:population    2629 .

<https://sws.geonames.org/12313184/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Riviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313184;
        gn:lat           46.9233;
        gn:long          -1.6579;
        gn:name          "La Rivière";
        gn:population    0 .

<https://sws.geonames.org/6434496/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pornic";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434496;
        gn:lat           47.11556;
        gn:long          -2.10333;
        gn:name          "Pornic";
        gn:population    14703 .

<https://sws.geonames.org/6435314/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Remy-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435314;
        gn:lat           47.27083;
        gn:long          -1.07556;
        gn:name          "Saint-Rémy-en-Mauges";
        gn:population    1406 .

<https://sws.geonames.org/3005703/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Vendette";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3005703;
        gn:lat           46.98477;
        gn:long          -2.15197;
        gn:name          "La Vendette";
        gn:population    0 .

<https://sws.geonames.org/3007706/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Angle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007706;
        gn:lat           47.27154;
        gn:long          -1.83964;
        gn:name          "L'Angle";
        gn:population    0 .

<https://sws.geonames.org/8286532/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sebastien-Frene-Rond Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286532;
        gn:lat           47.19057;
        gn:long          -1.49604;
        gn:name          "Saint-Sébastien-Frêne-Rond Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3008597/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Jaunais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008597;
        gn:lat           47.38333;
        gn:long          -1.66667;
        gn:name          "La Jaunais";
        gn:population    0 .

<https://sws.geonames.org/2976814/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Symphorien";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2976814;
        gn:lat           46.98048;
        gn:long          -1.17333;
        gn:name          "Saint-Symphorien";
        gn:population    0 .

<https://sws.geonames.org/8292914/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Blain";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292914;
        gn:lat           47.47397;
        gn:long          -1.76215;
        gn:name          "Bureau de Poste de Blain";
        gn:population    0 .

<https://sws.geonames.org/3014396/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Gueny";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3014396;
        gn:lat           47.44429;
        gn:long          -1.7087;
        gn:name          "Gueny";
        gn:population    0 .

<https://sws.geonames.org/11073020/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Plage de la Source";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.BCH;
        gn:geonamesID    11073020;
        gn:lat           47.10647;
        gn:long          -2.09659;
        gn:name          "Plage de la Source";
        gn:population    0 .

<https://sws.geonames.org/12312979/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Etang Bernard";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312979;
        gn:lat           47.24036;
        gn:long          -1.74982;
        gn:name          "L'Étang Bernard";
        gn:population    0 .

<https://sws.geonames.org/12313162/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bauche Tue-Loup";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313162;
        gn:lat           47.13909;
        gn:long          -1.55071;
        gn:name          "La Bauche Tue-Loup";
        gn:population    0 .

<https://sws.geonames.org/3006640/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rouxiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006640;
        gn:lat           47.44242;
        gn:long          -1.06667;
        gn:name          "La Rouxière";
        gn:population    893 .

<https://sws.geonames.org/3233615/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Grande Ville";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233615;
        gn:lat           47.26405;
        gn:long          -2.13722;
        gn:name          "La Grande Ville";
        gn:population    0 .

<https://sws.geonames.org/12312937/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Pierre Percee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312937;
        gn:lat           47.28153;
        gn:long          -1.38531;
        gn:name          "La Pierre Percée";
        gn:population    0 .

<https://sws.geonames.org/2976928/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Sigismond";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2976928;
        gn:lat           47.45416;
        gn:long          -0.94223;
        gn:name          "Saint-Sigismond";
        gn:population    328 .

<https://sws.geonames.org/6456917/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Gavre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456917;
        gn:lat           47.52056;
        gn:long          -1.74861;
        gn:name          "Le Gâvre";
        gn:population    1781 .

<https://sws.geonames.org/12313025/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cordionnais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313025;
        gn:lat           47.3288;
        gn:long          -2.12215;
        gn:name          "La Cordionnais";
        gn:population    0 .

<https://sws.geonames.org/8293029/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Suce Sur Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293029;
        gn:lat           47.3398;
        gn:long          -1.52708;
        gn:name          "Bureau de Poste de Suce Sur Erdre";
        gn:population    0 .

<https://sws.geonames.org/3031411/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Botz-en-Mauges";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3031411;
        gn:lat           47.3069;
        gn:long          -1.00119;
        gn:name          "Botz-en-Mauges";
        gn:population    712 .

<https://sws.geonames.org/6615072/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bernardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6615072;
        gn:lat           47.05;
        gn:long          -1.26667;
        gn:name          "La Bernardière";
        gn:population    1796 .

<https://sws.geonames.org/12310608/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Retoubliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310608;
        gn:lat           47.02576;
        gn:long          -1.32074;
        gn:name          "La Rétoublière";
        gn:population    0 .

<https://sws.geonames.org/12313098/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Embreil";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313098;
        gn:lat           47.22104;
        gn:long          -1.43276;
        gn:name          "Embreil";
        gn:population    0 .

<https://sws.geonames.org/6612546/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montrelais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6612546;
        gn:lat           47.38889;
        gn:long          -0.96639;
        gn:name          "Montrelais";
        gn:population    859 .

<https://sws.geonames.org/12312942/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Durandiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312942;
        gn:lat           47.23516;
        gn:long          -1.36248;
        gn:name          "La Durandière";
        gn:population    0 .

<https://sws.geonames.org/6434484/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Nort-sur-Erdre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434484;
        gn:lat           47.43944;
        gn:long          -1.49833;
        gn:name          "Nort-sur-Erdre";
        gn:population    8651 .

<https://sws.geonames.org/6435284/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Florent-le-Vieil";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435284;
        gn:lat           47.36139;
        gn:long          -1.01639;
        gn:name          "Saint-Florent-le-Vieil";
        gn:population    2676 .

<https://sws.geonames.org/6434541/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Viaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434541;
        gn:lat           47.25583;
        gn:long          -2.01944;
        gn:name          "Saint-Viaud";
        gn:population    2457 .

<https://sws.geonames.org/3000394/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Mares";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3000394;
        gn:lat           47.32667;
        gn:long          -1.20761;
        gn:name          "Les Mares";
        gn:population    0 .

<https://sws.geonames.org/6456072/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Marillais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456072;
        gn:lat           47.35861;
        gn:long          -1.07333;
        gn:name          "Le Marillais";
        gn:population    1040 .

<https://sws.geonames.org/6614972/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pin";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614972;
        gn:lat           47.58909;
        gn:long          -1.15356;
        gn:name          "Le Pin";
        gn:population    770 .

<https://sws.geonames.org/12313131/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Fremondiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313131;
        gn:lat           47.1975;
        gn:long          -1.43984;
        gn:name          "La Frémondière";
        gn:population    0 .

<https://sws.geonames.org/12308558/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Girardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308558;
        gn:lat           47.04465;
        gn:long          -0.90489;
        gn:name          "La Girardière";
        gn:population    0 .

<https://sws.geonames.org/2990039/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Notre-Dame-des-Landes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2990039;
        gn:lat           47.38113;
        gn:long          -1.70949;
        gn:name          "Notre-Dame-des-Landes";
        gn:population    1773 .

<https://sws.geonames.org/8292929/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Chateauthebaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292929;
        gn:lat           47.1238;
        gn:long          -1.4202;
        gn:name          "Bureau de Poste de Chateauthebaud";
        gn:population    0 .

<https://sws.geonames.org/6616818/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Teille";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616818;
        gn:lat           47.4615;
        gn:long          -1.279;
        gn:name          "Teillé";
        gn:population    1785 .

<https://sws.geonames.org/8286995/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Cugand la Bernardiere Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286995;
        gn:lat           47.05769;
        gn:long          -1.2517;
        gn:name          "Cugand la Bernardière Railway Station";
        gn:population    0 .

<https://sws.geonames.org/2995558/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Marongle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2995558;
        gn:lat           47.55171;
        gn:long          -1.97962;
        gn:name          "Marongle";
        gn:population    0 .

<https://sws.geonames.org/3034764/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bas Baudet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3034764;
        gn:lat           47.41667;
        gn:long          -0.91667;
        gn:name          "Bas Baudet";
        gn:population    0 .

<https://sws.geonames.org/12308355/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Pugle";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12308355;
        gn:lat           47.5314;
        gn:long          -1.0893;
        gn:name          "La Pugle";
        gn:population    0 .

<https://sws.geonames.org/8293061/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Contrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293061;
        gn:lat           47.2214;
        gn:long          -1.59243;
        gn:name          "Bureau de Poste de Nantes Contrie";
        gn:population    0 .

<https://sws.geonames.org/3010357/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-du-Genet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010357;
        gn:lat           47.18203;
        gn:long          -1.01857;
        gn:name          "La Chapelle-du-Genêt";
        gn:population    1165 .

<https://sws.geonames.org/10174391/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mercure Nantes Centre Gd Hotel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10174391;
        gn:lat           47.21445;
        gn:long          -1.55706;
        gn:name          "Mercure Nantes Centre Gd Hotel";
        gn:population    0 .

<https://sws.geonames.org/6614196/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Torfou";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6614196;
        gn:lat           47.0375;
        gn:long          -1.11583;
        gn:name          "Torfou";
        gn:population    2077 .

<https://sws.geonames.org/3002811/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002811;
        gn:lat           47.5893;
        gn:long          -1.153;
        gn:name          "Le Pin";
        gn:population    0 .

<https://sws.geonames.org/3010466/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chambaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010466;
        gn:lat           47.08635;
        gn:long          -1.39651;
        gn:name          "La Chambaudière";
        gn:population    0 .

<https://sws.geonames.org/3008185/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Meilleraye-de-Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008185;
        gn:lat           47.55965;
        gn:long          -1.40187;
        gn:name          "La Meilleraye-de-Bretagne";
        gn:population    1113 .

<https://sws.geonames.org/6456028/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Remaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456028;
        gn:lat           47.2375;
        gn:long          -1.24333;
        gn:name          "La Remaudière";
        gn:population    1284 .

<https://sws.geonames.org/12313084/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bretonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313084;
        gn:lat           47.20101;
        gn:long          -1.31388;
        gn:name          "La Bretonnière";
        gn:population    0 .

<https://sws.geonames.org/12312998/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Catee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312998;
        gn:lat           47.56767;
        gn:long          -2.02268;
        gn:name          "La Catée";
        gn:population    0 .

<https://sws.geonames.org/3011143/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Belerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011143;
        gn:lat           47.42428;
        gn:long          -1.53833;
        gn:name          "La Belerie";
        gn:population    0 .

<https://sws.geonames.org/2971900/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Trelagot";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2971900;
        gn:lat           47.32869;
        gn:long          -2.08012;
        gn:name          "Trelagot";
        gn:population    0 .

<https://sws.geonames.org/6614871/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chanverrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614871;
        gn:lat           46.96111;
        gn:long          -0.995;
        gn:name          "Chanverrie";
        gn:population    5545 .

<https://sws.geonames.org/3002655/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Plessis-Pas Brunet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3002655;
        gn:lat           47.42667;
        gn:long          -1.52452;
        gn:name          "Le Plessis-Pas Brunet";
        gn:population    0 .

<https://sws.geonames.org/6454810/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Gervais";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6454810;
        gn:lat           46.90194;
        gn:long          -1.99833;
        gn:name          "Saint-Gervais";
        gn:population    2621 .

<https://sws.geonames.org/6616806/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boissiere-du-Dore";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6616806;
        gn:lat           47.232;
        gn:long          -1.2196;
        gn:name          "La Boissière-du-Doré";
        gn:population    1106 .

<https://sws.geonames.org/3006657/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rousseliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006657;
        gn:lat           47.41358;
        gn:long          -1.20547;
        gn:name          "La Rousselière";
        gn:population    0 .

<https://sws.geonames.org/2980260/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Etienne-de-Mer-Morte";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980260;
        gn:lat           46.92886;
        gn:long          -1.74272;
        gn:name          "Saint-Étienne-de-Mer-Morte";
        gn:population    1084 .

<https://sws.geonames.org/12312989/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Touche Basse";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312989;
        gn:lat           47.35958;
        gn:long          -1.96191;
        gn:name          "La Touche Basse";
        gn:population    0 .

<https://sws.geonames.org/6449114/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Maisdon-sur-Sevre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449114;
        gn:lat           47.09722;
        gn:long          -1.385;
        gn:name          "Maisdon-sur-Sèvre";
        gn:population    2908 .

<https://sws.geonames.org/12310633/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Hallay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310633;
        gn:lat           46.93952;
        gn:long          -1.35113;
        gn:name          "Le Hallay";
        gn:population    0 .

<https://sws.geonames.org/3026195/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chateau-Thebaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3026195;
        gn:lat           47.12511;
        gn:long          -1.42153;
        gn:name          "Château-Thébaud";
        gn:population    0 .

<https://sws.geonames.org/12313207/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Cyr En Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313207;
        gn:lat           47.03216;
        gn:long          -1.90095;
        gn:name          "Saint-Cyr En Retz";
        gn:population    0 .

<https://sws.geonames.org/12305890/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Cognardiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305890;
        gn:lat           47.1552;
        gn:long          -1.36426;
        gn:name          "La Cognardière";
        gn:population    0 .

<https://sws.geonames.org/12310656/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Cormier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310656;
        gn:lat           46.90608;
        gn:long          -1.24806;
        gn:name          "Le Cormier";
        gn:population    0 .

<https://sws.geonames.org/3233462/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roche";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233462;
        gn:lat           47.25957;
        gn:long          -1.91829;
        gn:name          "La Roche";
        gn:population    0 .

<https://sws.geonames.org/3006895/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Riviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006895;
        gn:lat           47.35763;
        gn:long          -1.45976;
        gn:name          "La Rivière";
        gn:population    0 .

<https://sws.geonames.org/3010257/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Saint-Sauveur";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010257;
        gn:lat           47.44111;
        gn:long          -0.9846;
        gn:name          "La Chapelle-Saint-Sauveur";
        gn:population    677 .

<https://sws.geonames.org/6613858/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Landemont";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6613858;
        gn:lat           47.265;
        gn:long          -1.24222;
        gn:name          "Landemont";
        gn:population    1619 .

<https://sws.geonames.org/3009548/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Favriere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009548;
        gn:lat           47.35547;
        gn:long          -1.57476;
        gn:name          "La Favrière";
        gn:population    0 .

<https://sws.geonames.org/8436226/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont de Saint-Florent-le-Vieil";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436226;
        gn:lat           47.36992;
        gn:long          -1.01584;
        gn:name          "Pont de Saint-Florent-le-Vieil";
        gn:population    0 .

<https://sws.geonames.org/6449428/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Oree d'Anjou";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449428;
        gn:lat           47.33694;
        gn:long          -1.26667;
        gn:name          "Orée d'Anjou";
        gn:population    16324 .

<https://sws.geonames.org/8292946/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Le Gavre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292946;
        gn:lat           47.52109;
        gn:long          -1.75021;
        gn:name          "Bureau de Poste de Le Gavre";
        gn:population    0 .

<https://sws.geonames.org/2997586/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lorganais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2997586;
        gn:lat           47.45333;
        gn:long          -2.19071;
        gn:name          "Lorganais";
        gn:population    0 .

<https://sws.geonames.org/2980808/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Dolay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980808;
        gn:lat           47.54482;
        gn:long          -2.15487;
        gn:name          "Saint-Dolay";
        gn:population    2116 .

<https://sws.geonames.org/3034062/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beaurepaire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3034062;
        gn:lat           46.91047;
        gn:long          -1.08936;
        gn:name          "Beaurepaire";
        gn:population    1676 .

<https://sws.geonames.org/12313213/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Rivieres Aux Guerins";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313213;
        gn:lat           47.03446;
        gn:long          -1.94022;
        gn:name          "Les Rivières Aux Guérins";
        gn:population    0 .

<https://sws.geonames.org/8292991/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Reze Principal";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292991;
        gn:lat           47.17939;
        gn:long          -1.54571;
        gn:name          "Bureau de Poste de Reze Principal";
        gn:population    0 .

<https://sws.geonames.org/3029128/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Callac";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3029128;
        gn:lat           47.42404;
        gn:long          -2.14178;
        gn:name          "Callac";
        gn:population    0 .

<https://sws.geonames.org/12313138/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Massonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313138;
        gn:lat           47.17002;
        gn:long          -1.44426;
        gn:name          "La Massonnière";
        gn:population    0 .

<https://sws.geonames.org/2996861/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bras de la Madeleine";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STMA;
        gn:geonamesID    2996861;
        gn:lat           47.20069;
        gn:long          -1.57476;
        gn:name          "Bras de la Madeleine";
        gn:population    0 .

<https://sws.geonames.org/3233930/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile Sardine";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISLX;
        gn:geonamesID    3233930;
        gn:lat           47.23333;
        gn:long          -1.58333;
        gn:name          "Île Sardine";
        gn:population    0 .

<https://sws.geonames.org/7506773/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Novotel Nantes Centre Bord de Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    7506773;
        gn:lat           47.20647;
        gn:long          -1.54808;
        gn:name          "Hôtel Novotel Nantes Centre Bord de Loire";
        gn:population    0 .

<https://sws.geonames.org/11746358/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Vieil Essart";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    11746358;
        gn:lat           47.49581;
        gn:long          -1.46116;
        gn:name          "Le Vieil Essart";
        gn:population    0 .

<https://sws.geonames.org/6505258/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Akena Sainte Luce";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6505258;
        gn:lat           47.2538;
        gn:long          -1.4758;
        gn:name          "Hotel Akena Sainte Luce";
        gn:population    0 .

<https://sws.geonames.org/2996306/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Malville";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2996306;
        gn:lat           47.35996;
        gn:long          -1.86321;
        gn:name          "Malville";
        gn:population    3271 .

<https://sws.geonames.org/3009930/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Contrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLX;
        gn:geonamesID    3009930;
        gn:lat           47.21667;
        gn:long          -1.6;
        gn:name          "La Contrie";
        gn:population    0 .

<https://sws.geonames.org/2999721/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Rotis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2999721;
        gn:lat           47.54133;
        gn:long          -1.74638;
        gn:name          "Les Rotis";
        gn:population    0 .

<https://sws.geonames.org/8292965/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Meilleraye De Bretagne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292965;
        gn:lat           47.5602;
        gn:long          -1.40145;
        gn:name          "Bureau de Poste de La Meilleraye De Bretagne";
        gn:population    0 .

<https://sws.geonames.org/8293051/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Longchamp";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293051;
        gn:lat           47.23585;
        gn:long          -1.56784;
        gn:name          "Bureau de Poste de Nantes Longchamp";
        gn:population    0 .

<https://sws.geonames.org/2980109/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Florent-le-Vieil";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2980109;
        gn:lat           47.36069;
        gn:long          -1.01515;
        gn:name          "Saint-Florent-le-Vieil";
        gn:population    2793 .

<https://sws.geonames.org/3014398/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Guenrouet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3014398;
        gn:lat           47.51939;
        gn:long          -1.95679;
        gn:name          "Guenrouet";
        gn:population    2601 .

<https://sws.geonames.org/6434536/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Sainte-Pazanne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434536;
        gn:lat           47.10306;
        gn:long          -1.81083;
        gn:name          "Sainte-Pazanne";
        gn:population    6659 .

<https://sws.geonames.org/6614498/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Touches";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614498;
        gn:lat           47.44132;
        gn:long          -1.4296;
        gn:name          "Les Touches";
        gn:population    2488 .

<https://sws.geonames.org/6508918/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Relais Mercure Nantes Ouest";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6508918;
        gn:lat           47.2617;
        gn:long          -1.6717;
        gn:name          "Relais Mercure Nantes Ouest";
        gn:population    0 .

<https://sws.geonames.org/6456030/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Les Sorinieres";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456030;
        gn:lat           47.14639;
        gn:long          -1.53;
        gn:name          "Les Sorinières";
        gn:population    8216 .

<https://sws.geonames.org/6497899/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Alliance Pornic Thalassotherapie";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6497899;
        gn:lat           47.1075;
        gn:long          -2.0981;
        gn:name          "Alliance Pornic Thalassotherapie";
        gn:population    0 .

<https://sws.geonames.org/8292936/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Coueron Principal";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292936;
        gn:lat           47.21289;
        gn:long          -1.72977;
        gn:name          "Bureau de Poste de Coueron Principal";
        gn:population    0 .

<https://sws.geonames.org/2987358/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pichon";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2987358;
        gn:lat           47.51072;
        gn:long          -1.55773;
        gn:name          "Pichon";
        gn:population    0 .

<https://sws.geonames.org/6491374/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Campanile Nantes St Sebastien";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6491374;
        gn:lat           47.2107;
        gn:long          -1.4866;
        gn:name          "Campanile Nantes St Sebastien";
        gn:population    0 .

<https://sws.geonames.org/6474158/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mascotte Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6474158;
        gn:lat           47.1584;
        gn:long          -1.60035;
        gn:name          "Mascotte Nantes";
        gn:population    0 .

<https://sws.geonames.org/12305899/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Champ Siome";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305899;
        gn:lat           47.1487;
        gn:long          -1.55435;
        gn:name          "Le Champ Siôme";
        gn:population    0 .

<https://sws.geonames.org/2983807/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Revin";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2983807;
        gn:lat           47.37143;
        gn:long          -2.12905;
        gn:name          "Revin";
        gn:population    0 .

<https://sws.geonames.org/2981137/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Christophe-la-Couperie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2981137;
        gn:lat           47.25309;
        gn:long          -1.18108;
        gn:name          "Saint-Christophe-la-Couperie";
        gn:population    482 .

<https://sws.geonames.org/6614104/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Basse-Goulaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6614104;
        gn:lat           47.21528;
        gn:long          -1.46556;
        gn:name          "Basse-Goulaine";
        gn:population    8867 .

<https://sws.geonames.org/6620269/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Stade de La Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.STDM;
        gn:geonamesID    6620269;
        gn:lat           47.25605;
        gn:long          -1.52472;
        gn:name          "Stade de La Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/6617849/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Mormaison";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6617849;
        gn:lat           46.9071;
        gn:long          -1.4491;
        gn:name          "Mormaison";
        gn:population    1049 .

<https://sws.geonames.org/2979336/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Jean";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLX;
        gn:geonamesID    2979336;
        gn:lat           46.96473;
        gn:long          -1.58326;
        gn:name          "Saint-Jean";
        gn:population    0 .

<https://sws.geonames.org/8292956/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Indre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292956;
        gn:lat           47.19891;
        gn:long          -1.67181;
        gn:name          "Bureau de Poste de Indre";
        gn:population    0 .

<https://sws.geonames.org/2983770/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Reze";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2983770;
        gn:lat           47.19058;
        gn:long          -1.56885;
        gn:name          "Rezé";
        gn:population    39248 .

<https://sws.geonames.org/3009672/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Dechausserie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009672;
        gn:lat           47.38285;
        gn:long          -1.45274;
        gn:name          "La Dechausserie";
        gn:population    0 .

<https://sws.geonames.org/8286976/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Cellier Railway Station";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.RSTN;
        gn:geonamesID    8286976;
        gn:lat           47.3131;
        gn:long          -1.35116;
        gn:name          "Le Cellier Railway Station";
        gn:population    0 .

<https://sws.geonames.org/3007136/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Prinais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007136;
        gn:lat           47.26524;
        gn:long          -2.14667;
        gn:name          "La Prinais";
        gn:population    0 .

<https://sws.geonames.org/12312949/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Grand Blottereau";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312949;
        gn:lat           47.22732;
        gn:long          -1.50818;
        gn:name          "Le Grand Blottereau";
        gn:population    0 .

<https://sws.geonames.org/10345124/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Seven Urban Nantes Centre";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10345124;
        gn:lat           47.20775;
        gn:long          -1.53972;
        gn:name          "Hotel Seven Urban Nantes Centre";
        gn:population    0 .

<https://sws.geonames.org/6531363/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Arcantis Hotel Jules Verne";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6531363;
        gn:lat           47.21383;
        gn:long          -1.5569;
        gn:name          "Arcantis Hotel Jules Verne";
        gn:population    0 .

<https://sws.geonames.org/12312964/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bugalliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312964;
        gn:lat           47.26097;
        gn:long          -1.63377;
        gn:name          "La Bugallière";
        gn:population    0 .

<https://sws.geonames.org/3013764/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Haute Indre";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3013764;
        gn:lat           47.19652;
        gn:long          -1.65078;
        gn:name          "Haute Indre";
        gn:population    0 .

<https://sws.geonames.org/8293066/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Herblain Sillon";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293066;
        gn:lat           47.2436;
        gn:long          -1.6065;
        gn:name          "Bureau de Poste de Saint Herblain Sillon";
        gn:population    0 .

<https://sws.geonames.org/3019258/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Evrunes";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3019258;
        gn:lat           47.00012;
        gn:long          -0.97381;
        gn:name          "Évrunes";
        gn:population    0 .

<https://sws.geonames.org/6456907/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bernerie-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456907;
        gn:lat           47.08139;
        gn:long          -2.0375;
        gn:name          "La Bernerie-en-Retz";
        gn:population    2944 .

<https://sws.geonames.org/6614565/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Longeron";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6614565;
        gn:lat           47.01806;
        gn:long          -1.05917;
        gn:name          "Le Longeron";
        gn:population    2080 .

<https://sws.geonames.org/12313153/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chancele";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313153;
        gn:lat           46.93825;
        gn:long          -1.44182;
        gn:name          "Chancelé";
        gn:population    0 .

<https://sws.geonames.org/12310616/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Landefrere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310616;
        gn:lat           46.97992;
        gn:long          -1.49902;
        gn:name          "Landefrère";
        gn:population    0 .

<https://sws.geonames.org/3008339/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Maison-Rouge";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008339;
        gn:lat           46.95252;
        gn:long          -2.18671;
        gn:name          "La Maison-Rouge";
        gn:population    0 .

<https://sws.geonames.org/12305904/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beauvoir";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305904;
        gn:lat           47.18023;
        gn:long          -1.62841;
        gn:name          "Beauvoir";
        gn:population    0 .

<https://sws.geonames.org/6435296/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Laurent-des-Autels";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435296;
        gn:lat           47.28694;
        gn:long          -1.19083;
        gn:name          "Saint-Laurent-des-Autels";
        gn:population    2111 .

<https://sws.geonames.org/8293037/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Vertou";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293037;
        gn:lat           47.16806;
        gn:long          -1.47133;
        gn:name          "Bureau de Poste de Vertou";
        gn:population    0 .

<https://sws.geonames.org/3033618/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Belligne";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3033618;
        gn:lat           47.46774;
        gn:long          -1.0278;
        gn:name          "Belligné";
        gn:population    1690 .

<https://sws.geonames.org/6434563/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vue";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434563;
        gn:lat           47.19861;
        gn:long          -1.88111;
        gn:name          "Vue";
        gn:population    1648 .

<https://sws.geonames.org/2998400/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lignee";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    2998400;
        gn:lat           46.92646;
        gn:long          -1.2228;
        gn:name          "Lignée";
        gn:population    0 .

<https://sws.geonames.org/6449396/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Beausse";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6449396;
        gn:lat           47.32111;
        gn:long          -0.92694;
        gn:name          "Beausse";
        gn:population    389 .

<https://sws.geonames.org/3010915/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Boucherie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010915;
        gn:lat           47.41869;
        gn:long          -1.56203;
        gn:name          "La Boucherie";
        gn:population    0 .

<https://sws.geonames.org/2988323/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Paulx";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2988323;
        gn:lat           46.96341;
        gn:long          -1.75511;
        gn:name          "Paulx";
        gn:population    1473 .

<https://sws.geonames.org/3233937/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ile de Bois";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.ISL;
        gn:geonamesID    3233937;
        gn:lat           47.21036;
        gn:long          -1.80532;
        gn:name          "Île de Bois";
        gn:population    0 .

<https://sws.geonames.org/2997789/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Lonce";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2997789;
        gn:lat           47.3286;
        gn:long          -2.18387;
        gn:name          "Lonce";
        gn:population    0 .

<https://sws.geonames.org/8436216/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pont Leopold-Sedar-Senghor";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.BDG;
        gn:geonamesID    8436216;
        gn:lat           47.20588;
        gn:long          -1.5253;
        gn:name          "Pont Léopold-Sédar-Senghor";
        gn:population    0 .

<https://sws.geonames.org/3006744/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rogere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006744;
        gn:lat           47.09662;
        gn:long          -2.04512;
        gn:name          "La Rogère";
        gn:population    0 .

<https://sws.geonames.org/3037691/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Andreze";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3037691;
        gn:lat           47.17155;
        gn:long          -0.95239;
        gn:name          "Andrezé";
        gn:population    1905 .

<https://sws.geonames.org/8293413/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de La Seguiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293413;
        gn:lat           47.06197;
        gn:long          -0.93986;
        gn:name          "Bureau de Poste de La Seguiniere";
        gn:population    0 .

<https://sws.geonames.org/3031140/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boulogne";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STM;
        gn:geonamesID    3031140;
        gn:lat           47.06795;
        gn:long          -1.67511;
        gn:name          "Boulogne";
        gn:population    0 .

<https://sws.geonames.org/3233629/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Port de Donges";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.PRT;
        gn:geonamesID    3233629;
        gn:lat           47.30559;
        gn:long          -2.06655;
        gn:name          "Port de Donges";
        gn:population    0 .

<https://sws.geonames.org/3010109/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chaussee";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010109;
        gn:lat           47.0927;
        gn:long          -1.41508;
        gn:name          "La Chaussée";
        gn:population    0 .

<https://sws.geonames.org/6435274/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Andre-de-la-Marche";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6435274;
        gn:lat           47.1;
        gn:long          -0.995;
        gn:name          "Saint-André-de-la-Marche";
        gn:population    2754 .

<https://sws.geonames.org/3037672/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Anetz";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3037672;
        gn:lat           47.38059;
        gn:long          -1.10583;
        gn:name          "Anetz";
        gn:population    1468 .

<https://sws.geonames.org/6456062/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Fief-Sauvin";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6456062;
        gn:lat           47.22111;
        gn:long          -1.04167;
        gn:name          "Le Fief-Sauvin";
        gn:population    1642 .

<https://sws.geonames.org/3003022/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Pas Chevalier";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003022;
        gn:lat           47.40179;
        gn:long          -1.53619;
        gn:name          "Le Pas Chevalier";
        gn:population    0 .

<https://sws.geonames.org/6449071/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Besne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449071;
        gn:lat           47.3975;
        gn:long          -2.09139;
        gn:name          "Besné";
        gn:population    2999 .

<https://sws.geonames.org/13494805/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Eglise Saint-Gilles";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.CH;
        gn:geonamesID    13494805;
        gn:lat           47.11585;
        gn:long          -2.1037;
        gn:name          "Église Saint-Gilles";
        gn:population    0 .

<https://sws.geonames.org/2970747/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Varades";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2970747;
        gn:lat           47.385;
        gn:long          -1.03039;
        gn:name          "Varades";
        gn:population    3452 .

<https://sws.geonames.org/6492231/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Oceania Nantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6492231;
        gn:lat           47.1789;
        gn:long          -1.6189;
        gn:name          "Oceania Nantes";
        gn:population    0 .

<https://sws.geonames.org/3010793/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bricaudiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010793;
        gn:lat           47.43821;
        gn:long          -1.52881;
        gn:name          "La Bricaudière";
        gn:population    0 .

<https://sws.geonames.org/9174041/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "City Residence Nantes Beaujoire";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9174041;
        gn:lat           47.2508;
        gn:long          -1.50899;
        gn:name          "City Residence Nantes Beaujoire";
        gn:population    0 .

<https://sws.geonames.org/2972128/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Touvois";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2972128;
        gn:lat           46.90263;
        gn:long          -1.68387;
        gn:name          "Touvois";
        gn:population    1407 .

<https://sws.geonames.org/6445247/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Treize-Septiers";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6445247;
        gn:lat           46.98444;
        gn:long          -1.23028;
        gn:name          "Treize-Septiers";
        gn:population    3177 .

<https://sws.geonames.org/6449116/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Marsac-sur-Don";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449116;
        gn:lat           47.59556;
        gn:long          -1.68028;
        gn:name          "Marsac-sur-Don";
        gn:population    1499 .

<https://sws.geonames.org/3006913/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Riotiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006913;
        gn:lat           47.41667;
        gn:long          -0.93333;
        gn:name          "La Riotière";
        gn:population    0 .

<https://sws.geonames.org/3003012/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Patis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3003012;
        gn:lat           46.99857;
        gn:long          -1.37445;
        gn:name          "Le Pâtis";
        gn:population    0 .

<https://sws.geonames.org/6456033/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Roche-Blanche";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456033;
        gn:lat           47.44083;
        gn:long          -1.14056;
        gn:name          "La Roche-Blanche";
        gn:population    1187 .

<https://sws.geonames.org/2978524/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Mars-du-Desert";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2978524;
        gn:lat           47.3645;
        gn:long          -1.4101;
        gn:name          "Saint-Mars-du-Désert";
        gn:population    4002 .

<https://sws.geonames.org/6458635/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montfaucon-Montigne";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6458635;
        gn:lat           47.1;
        gn:long          -1.125;
        gn:name          "Montfaucon-Montigné";
        gn:population    1920 .

<https://sws.geonames.org/12312919/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Bourgonniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312919;
        gn:lat           47.43714;
        gn:long          -1.32667;
        gn:name          "La Bourgonnière";
        gn:population    0 .

<https://sws.geonames.org/3233414/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Caillou";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.RKS;
        gn:geonamesID    3233414;
        gn:lat           47.07966;
        gn:long          -2.10676;
        gn:name          "Le Caillou";
        gn:population    0 .

<https://sws.geonames.org/3233464/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Merlet";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3233464;
        gn:lat           47.31258;
        gn:long          -1.86563;
        gn:name          "Merlet";
        gn:population    0 .

<https://sws.geonames.org/3026845/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Chantenay-sur-Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3026845;
        gn:lat           47.20464;
        gn:long          -1.60226;
        gn:name          "Chantenay-sur-Loire";
        gn:population    0 .

<https://sws.geonames.org/6437361/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rieux";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6437361;
        gn:lat           47.59778;
        gn:long          -2.1075;
        gn:name          "Rieux";
        gn:population    2831 .

<https://sws.geonames.org/6434555/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Vallet";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6434555;
        gn:lat           47.16167;
        gn:long          -1.26694;
        gn:name          "Vallet";
        gn:population    8953 .

<https://sws.geonames.org/2979552/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Saint-Hilaire-de-Chaleons";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2979552;
        gn:lat           47.10328;
        gn:long          -1.86577;
        gn:name          "Saint-Hilaire-de-Chaléons";
        gn:population    1760 .

<https://sws.geonames.org/6449096/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Fresnay-en-Retz";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4H;
        gn:geonamesID    6449096;
        gn:lat           47.02444;
        gn:long          -1.87639;
        gn:name          "Fresnay-en-Retz";
        gn:population    1202 .

<https://sws.geonames.org/3006303/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Telindiere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3006303;
        gn:lat           47.19853;
        gn:long          -1.7359;
        gn:name          "La Télindière";
        gn:population    0 .

<https://sws.geonames.org/3233971/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Petite Riviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.STMA;
        gn:geonamesID    3233971;
        gn:lat           47.20291;
        gn:long          -1.74427;
        gn:name          "La Petite Rivière";
        gn:population    0 .

<https://sws.geonames.org/11906047/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Jardin des Plantes";
        gn:countryCode   "FR";
        gn:featureClass  gn:L;
        gn:featureCode   gn:L.PRK;
        gn:geonamesID    11906047;
        gn:lat           47.21958;
        gn:long          -1.54277;
        gn:name          "Jardin des Plantes";
        gn:population    0 .

<https://sws.geonames.org/10297836/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Hotel Saint Daniel";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10297836;
        gn:lat           47.2149;
        gn:long          -1.55404;
        gn:name          "Hotel Saint Daniel";
        gn:population    0 .

<https://sws.geonames.org/6449086/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Corsept";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449086;
        gn:lat           47.2775;
        gn:long          -2.05917;
        gn:name          "Corsept";
        gn:population    2684 .

<https://sws.geonames.org/6445175/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Montreverd";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6445175;
        gn:lat           46.93444;
        gn:long          -1.41222;
        gn:name          "Montréverd";
        gn:population    3638 .

<https://sws.geonames.org/6502875/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Brit'Hotel Amandine";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    6502875;
        gn:lat           47.2546;
        gn:long          -1.5296;
        gn:name          "Brit'Hotel Amandine";
        gn:population    0 .

<https://sws.geonames.org/3233927/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Canal du Marais de la Roche";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    3233927;
        gn:lat           47.2952;
        gn:long          -1.88012;
        gn:name          "Canal du Marais de la Roche";
        gn:population    0 .

<https://sws.geonames.org/6456920/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Loroux-Bottereau";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6456920;
        gn:lat           47.2383;
        gn:long          -1.3483;
        gn:name          "Le Loroux-Bottereau";
        gn:population    8126 .

<https://sws.geonames.org/8292998/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Saint Brevin Les Pins";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292998;
        gn:lat           47.24815;
        gn:long          -2.16516;
        gn:name          "Bureau de Poste de Saint Brevin Les Pins";
        gn:population    0 .

<https://sws.geonames.org/10943617/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Abbaye de Bellefontaine";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.MSTY;
        gn:geonamesID    10943617;
        gn:lat           47.15185;
        gn:long          -0.93833;
        gn:name          "Abbaye de Bellefontaine";
        gn:population    0 .

<https://sws.geonames.org/12312889/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Loiriere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312889;
        gn:lat           47.44742;
        gn:long          -1.18152;
        gn:name          "La Loirière";
        gn:population    0 .

<https://sws.geonames.org/12313215/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Hourserie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313215;
        gn:lat           47.13098;
        gn:long          -2.04876;
        gn:name          "La Hourserie";
        gn:population    0 .

<https://sws.geonames.org/12310641/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Rangiziere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12310641;
        gn:lat           46.92907;
        gn:long          -1.26469;
        gn:name          "La Rangizière";
        gn:population    0 .

<https://sws.geonames.org/3008708/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Houssaie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3008708;
        gn:lat           47.50678;
        gn:long          -1.26928;
        gn:name          "La Houssaie";
        gn:population    0 .

<https://sws.geonames.org/8293081/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes St Joseph De Porterie";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8293081;
        gn:lat           47.26937;
        gn:long          -1.5178;
        gn:name          "Bureau de Poste de Nantes St Joseph De Porterie";
        gn:population    0 .

<https://sws.geonames.org/2983590/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rieux";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2983590;
        gn:lat           47.59809;
        gn:long          -2.10857;
        gn:name          "Rieux";
        gn:population    2736 .

<https://sws.geonames.org/3011364/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Barbiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3011364;
        gn:lat           47.38583;
        gn:long          -1.10404;
        gn:name          "La Barbinière";
        gn:population    0 .

<https://sws.geonames.org/12313193/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gautronniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313193;
        gn:lat           47.17065;
        gn:long          -1.73681;
        gn:name          "La Gautronnière";
        gn:population    0 .

<https://sws.geonames.org/11073017/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Pointe du Parracaud";
        gn:countryCode   "FR";
        gn:featureClass  gn:T;
        gn:featureCode   gn:T.PT;
        gn:geonamesID    11073017;
        gn:lat           47.01722;
        gn:long          -2.01118;
        gn:name          "Pointe du Parracaud";
        gn:population    0 .

<https://sws.geonames.org/3010312/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Chapelle-Launay";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3010312;
        gn:lat           47.37195;
        gn:long          -1.9715;
        gn:name          "La Chapelle-Launay";
        gn:population    2467 .

<https://sws.geonames.org/3009102/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gicqueliere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3009102;
        gn:lat           47.50607;
        gn:long          -1.40892;
        gn:name          "La Gicquelière";
        gn:population    0 .

<https://sws.geonames.org/12305881/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Boire Courant";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12305881;
        gn:lat           47.24551;
        gn:long          -1.43482;
        gn:name          "Boire Courant";
        gn:population    0 .

<https://sws.geonames.org/9177296/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Inter-Hotel Novella Nantes Carquefou";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9177296;
        gn:lat           47.26872;
        gn:long          -1.48479;
        gn:name          "Inter-Hotel Novella Nantes Carquefou";
        gn:population    0 .

<https://sws.geonames.org/3233627/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Potangis";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPLL;
        gn:geonamesID    3233627;
        gn:lat           47.27024;
        gn:long          -2.06012;
        gn:name          "Le Potangis";
        gn:population    0 .

<https://sws.geonames.org/12313037/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Gagnerie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313037;
        gn:lat           47.31678;
        gn:long          -2.19328;
        gn:name          "La Gagnerie";
        gn:population    0 .

<https://sws.geonames.org/9539821/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Premiere Classe Nantes Ouest";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    9539821;
        gn:lat           47.23409;
        gn:long          -1.64879;
        gn:name          "Premiere Classe Nantes Ouest";
        gn:population    0 .

<https://sws.geonames.org/6452362/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Angrie";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6452362;
        gn:lat           47.57;
        gn:long          -0.97333;
        gn:name          "Angrie";
        gn:population    947 .

<https://sws.geonames.org/6451589/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Barbatre";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6451589;
        gn:lat           46.94389;
        gn:long          -2.18056;
        gn:name          "Barbâtre";
        gn:population    1752 .

<https://sws.geonames.org/3233456/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Ancien Canal Maritime de Basse Loire";
        gn:countryCode   "FR";
        gn:featureClass  gn:H;
        gn:featureCode   gn:H.CNL;
        gn:geonamesID    3233456;
        gn:lat           47.2805;
        gn:long          -1.94859;
        gn:name          "Ancien Canal Maritime de Basse Loire";
        gn:population    0 .

<https://sws.geonames.org/10283545/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Quality and Suites Nantes Atlantique";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.HTL;
        gn:geonamesID    10283545;
        gn:lat           47.25133;
        gn:long          -1.51004;
        gn:name          "Quality and Suites Nantes Atlantique";
        gn:population    0 .

<https://sws.geonames.org/8292931/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bureau de Poste de Nantes Saint Donatien";
        gn:countryCode   "FR";
        gn:featureClass  gn:S;
        gn:featureCode   gn:S.PO;
        gn:geonamesID    8292931;
        gn:lat           47.22808;
        gn:long          -1.54174;
        gn:name          "Bureau de Poste de Nantes Saint Donatien";
        gn:population    0 .

<https://sws.geonames.org/2998625/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "L'Herbraire";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2998625;
        gn:lat           47.44203;
        gn:long          -1.10666;
        gn:name          "L'Herbraire";
        gn:population    0 .

<https://sws.geonames.org/3007217/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Pommeraie";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    3007217;
        gn:lat           47.18583;
        gn:long          -1.26953;
        gn:name          "La Pommeraie";
        gn:population    0 .

<https://sws.geonames.org/2983221/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Rocheserviere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    2983221;
        gn:lat           46.93851;
        gn:long          -1.5098;
        gn:name          "Rocheservière";
        gn:population    2404 .

<https://sws.geonames.org/12313000/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Barrisset";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313000;
        gn:lat           47.56917;
        gn:long          -2.02827;
        gn:name          "Barrisset";
        gn:population    0 .

<https://sws.geonames.org/12312951/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Le Brossais";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12312951;
        gn:lat           47.37423;
        gn:long          -1.61487;
        gn:name          "Le Brossais";
        gn:population    0 .

<https://sws.geonames.org/12313203/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "La Raffiniere";
        gn:countryCode   "FR";
        gn:featureClass  gn:P;
        gn:featureCode   gn:P.PPL;
        gn:geonamesID    12313203;
        gn:lat           47.1933;
        gn:long          -1.84135;
        gn:name          "La Raffinière";
        gn:population    0 .

<https://sws.geonames.org/6449078/>
        rdf:type         gn:GeonamesFeature;
        <http://dbpedia.org/ontology/timeZone>
                "Europe/Paris";
        skos:altLabel    "Bouvron";
        gn:countryCode   "FR";
        gn:featureClass  gn:A;
        gn:featureCode   gn:A.ADM4;
        gn:geonamesID    6449078;
        gn:lat           47.41778;
        gn:long          -1.84778;
        gn:name          "Bouvron";
        gn:population    3141 .
```
