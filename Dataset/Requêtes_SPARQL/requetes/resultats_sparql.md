# Requêtes SPARQL et résultats

## Rq_altitude

```sparql
#Sommets de plus de 3 000 m

PREFIX gn:     <https://www.geonames.org/ontology#>
PREFIX schema: <https://schema.org/>

SELECT ?f ?nom ?alt
WHERE {
  ?f gn:featureCode gn:T.PK ;
     gn:name ?nom ;
     schema:elevation ?alt .
  FILTER(?alt > 3000)
}
ORDER BY DESC(?alt)
LIMIT 20
```

Résultat :

```
f,nom,alt
https://sws.geonames.org/2969640/,Aiguille Verte,4122.0
https://sws.geonames.org/3032586/,Aiguille de Bionnassay,4052.0
https://sws.geonames.org/7576652/,La Meije Pic Central,3973.0
https://sws.geonames.org/3038455/,Sommet de l'Ailefroide,3954.0
https://sws.geonames.org/7576642/,Pointe Durand,3932.0
https://sws.geonames.org/6295658/,Pic Sans Nom,3913.0
https://sws.geonames.org/3037040/,Aiguille d'Argentière,3896.0
https://sws.geonames.org/7576653/,La Meije Pic Oriental,3891.0
https://sws.geonames.org/7576651/,Pic Gaspard,3881.0
https://sws.geonames.org/2971664/,Aiguille de Triolet,3870.0
https://sws.geonames.org/12640316/,Aiguille du Goûter,3863.0
https://sws.geonames.org/2993964/,Aiguille du Midi,3842.0
https://sws.geonames.org/3026670/,Aiguille du Chardonnet,3824.0
https://sws.geonames.org/7576654/,le Pave,3823.0
https://sws.geonames.org/3015873/,Aiguille du Glacier,3817.0
https://sws.geonames.org/3002390/,Le Rateau,3809.0
https://sws.geonames.org/3006190/,La Tour Ronde,3792.0
https://sws.geonames.org/2985752/,Mont Pourri,3779.0
https://sws.geonames.org/7576646/,Pic Coolidge,3775.0
https://sws.geonames.org/3008968/,La Grande Ruine,3765.0
```

## Rq_Construct

```sparql
#les villes de plus de 100 000 habitants

PREFIX gn: <https://www.geonames.org/ontology#>

CONSTRUCT { ?f gn:name ?nom ; gn:population ?pop }
WHERE {
  ?f gn:featureCode gn:P.PPL ; gn:name ?nom ; gn:population ?pop .
  FILTER(?pop > 100000)
}
```

Résultat :

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

<https://sws.geonames.org/12278193/>
        gn:name        "Marne La Vallée";
        gn:population  318325 .

<https://sws.geonames.org/8533870/>
        gn:name        "Saint-Quentin-en-Yvelines";
        gn:population  146598 .

<https://sws.geonames.org/3034610/>
        gn:name        "Paris 17 Batignolles-Monceau";
        gn:population  159212 .

<https://sws.geonames.org/3029374/>
        gn:name        "Paris 18 Buttes-Montmartre";
        gn:population  183127 .

<https://sws.geonames.org/3029372/>
        gn:name        "Paris 19 Buttes-Chaumont";
        gn:population  178691 .

<https://sws.geonames.org/3015772/>
        gn:name        "Paris 13 Gobelins";
        gn:population  181271 .

<https://sws.geonames.org/2994540/>
        gn:name        "Paris 20 Ménilmontant";
        gn:population  185140 .

<https://sws.geonames.org/2992090/>
        gn:name        "Montreuil";
        gn:population  111240 .

<https://sws.geonames.org/2989781/>
        gn:name        "Paris 14 Observatoire";
        gn:population  136455 .

<https://sws.geonames.org/2988394/>
        gn:name        "Paris 16 Passy";
        gn:population  159386 .

<https://sws.geonames.org/2986082/>
        gn:name        "Paris 11 Popincourt";
        gn:population  138170 .

<https://sws.geonames.org/2983854/>
        gn:name        "Paris 12 Reuilly";
        gn:population  138024 .

<https://sws.geonames.org/2970479/>
        gn:name        "Paris 15 Vaugirard";
        gn:population  229713 .

<https://sws.geonames.org/2968254/>
        gn:name        "Villeurbanne";
        gn:population  131445 .
```

## Rq_hotel

```sparql
#Hôtels autour de Nantes

PREFIX gn: <https://www.geonames.org/ontology#>

SELECT ?f ?nom ?lat ?long
WHERE {
  ?f gn:featureCode gn:S.HTL ;
     gn:name ?nom ;
     gn:lat ?lat ;
     gn:long ?long .
  FILTER(?lat > 47.15 && ?lat < 47.30 && ?long > -1.70 && ?long < -1.45)
}
ORDER BY ?nom
```

Résultat :

```
f,nom,lat,long
https://sws.geonames.org/10297850/,Abat Jour,47.22179,-1.54854
https://sws.geonames.org/9259163/,Adagio Acces Nantes Viarme,47.22308,-1.56266
https://sws.geonames.org/10281142/,Adagio Access Nantes La Beaujoire,47.21944,-1.56158
https://sws.geonames.org/9539815/,Adagio Access Nantes Viarme,47.22294,-1.56288
https://sws.geonames.org/9172611/,Adagio Nantes Centre,47.21691,-1.54621
https://sws.geonames.org/6474236/,Amiral,47.21404,-1.56259
https://sws.geonames.org/6519216/,Appart City Nantes Chateau Des,47.2102,-1.5471
https://sws.geonames.org/10281591/,Appart City Nantes Cite Des Congres,47.21944,-1.56158
https://sws.geonames.org/10281143/,Appart City Nantes Le Viarme,47.21944,-1.56158
https://sws.geonames.org/10281590/,Appart City Nantes Quai de La Loire,47.21944,-1.56158
https://sws.geonames.org/9172749/,Appart City Nantes Quais De Loire,47.2096,-1.56742
https://sws.geonames.org/6523836/,Appart City Nantes Viarme,47.2213,-1.5615
https://sws.geonames.org/6498280/,Appart'City Sanitat,47.2097,-1.5672
https://sws.geonames.org/6493474/,Appart'city Nantes Château des Ducs,47.2144,-1.546
https://sws.geonames.org/10344045/,Appartcity Nantes Quai de Loir,47.20939,-1.56803
https://sws.geonames.org/10297849/,Appartcity Nantes Quais de Loire,47.20962,-1.56746
https://sws.geonames.org/10297848/,Apts Adagio Access Nantes La Beaujoire,47.2514,-1.53154
https://sws.geonames.org/10297847/,Apts Adagio Access Nantes Sextant,47.20669,-1.57929
https://sws.geonames.org/6531363/,Arcantis Hotel Jules Verne,47.21383,-1.5569
https://sws.geonames.org/10174531/,Arcantis Hotel Le Jules Verne,47.21409,-1.55723
https://sws.geonames.org/6510142/,Atel Grand Hotel De Nantes,47.2124,-1.5602
https://sws.geonames.org/10246254/,Atlantys Hatel,47.22797,-1.63271
https://sws.geonames.org/9172997/,Balladins Nantes Saint Herblain,47.22954,-1.6337
https://sws.geonames.org/9173038/,Best Hotel Nantes   Graslin,47.2122,-1.56244
https://sws.geonames.org/9173051/,Best Western  Plus Le Colisee Hotel & Spa,47.23412,-1.65368
https://sws.geonames.org/9173239/,Best Western Plus Hotel De La Regate,47.29344,-1.52665
https://sws.geonames.org/10297845/,Brit Hotel Belfort,47.21123,-1.54459
https://sws.geonames.org/6502875/,Brit'Hotel Amandine,47.2546,-1.5296
https://sws.geonames.org/6496933/,Brit'Hotel Le Kerann,47.2336,-1.6525
https://sws.geonames.org/9173736/,Campanile Nantes Centre,47.19439,-1.52971
https://sws.geonames.org/10175485/,Campanile Nantes Centre St Jac,47.19617,-1.53097
https://sws.geonames.org/10112829/,Campanile Nantes Est Saint Sebastien Sur Loire,47.21197,-1.4865
https://sws.geonames.org/9173744/,Campanile Nantes Ouest - Saint Herblain,47.22656,-1.6301
https://sws.geonames.org/10277071/,Campanile Nantes Ouest Rl,47.22656,-1.6301
https://sws.geonames.org/9173745/,Campanile Nantes Reze,47.19391,-1.57447
https://sws.geonames.org/6499277/,Campanile Nantes Sainte Luce,47.2622,-1.4936
https://sws.geonames.org/6491386/,Campanile Nantes St Herblain,47.2274,-1.6349
https://sws.geonames.org/6491374/,Campanile Nantes St Sebastien,47.2107,-1.4866
https://sws.geonames.org/9539830/,Cerise Nantes La Beaujoire (Residence Studinn),47.25348,-1.52881
https://sws.geonames.org/6498801/,Citea Nantes,47.2067,-1.5792
https://sws.geonames.org/6492472/,Citea Nantes Aubiniere,47.2604,-1.4966
https://sws.geonames.org/9539775/,Citea Nantes Sextant,47.2067,-1.57929
https://sws.geonames.org/7304607/,Citea Nantes la Beaujoire,47.25842,-1.49525
https://sws.geonames.org/6520562/,Citea Residentiel Nantes Aubini,47.2456,-1.5693
https://sws.geonames.org/10154841/,Citea Residentiel Nantes La Beaujoire,47.26034,-1.49657
https://sws.geonames.org/10297844/,Citotel Pommeraye,47.21406,-1.56024
https://sws.geonames.org/9174041/,City Residence Nantes Beaujoire,47.2508,-1.50899
https://sws.geonames.org/10297842/,Coeur de Loire,47.22841,-1.56344
https://sws.geonames.org/9174128/,Comfort Hotel Nantes Astoria,47.21779,-1.54388
https://sws.geonames.org/9539809/,Contact Hotel Terminus,47.21775,-1.54373
https://sws.geonames.org/10297841/,Des Trois Marchands,47.21839,-1.55605
https://sws.geonames.org/6498553/,Escale Oceania Nantes,47.1592,-1.5971
https://sws.geonames.org/10281170/,Escale Oceania Nantes Bouguenais Hotel,47.1729,-1.6189
https://sws.geonames.org/6473718/,Grand Hotel Mercure Nantes Central,47.2139,-1.5568
https://sws.geonames.org/6490216/,Grand Hotel de Nantes,47.21288,-1.56002
https://sws.geonames.org/6475376/,Holiday Inn Garden Court Nantes,47.2069,-1.5481
https://sws.geonames.org/6505258/,Hotel Akena Sainte Luce,47.2538,-1.4758
https://sws.geonames.org/6489822/,Hotel Beautour,47.18202,-1.51408
https://sws.geonames.org/10110277/,Hotel Belfort,47.21112,-1.54463
https://sws.geonames.org/10297840/,Hotel Chateaubriand,47.22199,-1.55469
https://sws.geonames.org/6501003/,Hotel De France Nantes,47.2133,-1.5615
https://sws.geonames.org/10110274/,Hotel Des 3 Marchands,47.21851,-1.55624
https://sws.geonames.org/10297838/,Hotel Du Tourisme,47.21736,-1.55673
https://sws.geonames.org/10110273/,Hotel Duquesne,47.21867,-1.55673
https://sws.geonames.org/9224798/,Hotel Graslin,47.21227,-1.56176
https://sws.geonames.org/10117424/,Hotel Jules Verne Nantes Prochainement All Seasons,47.21455,-1.5576
https://sws.geonames.org/10297836/,Hotel Saint Daniel,47.2149,-1.55404
https://sws.geonames.org/10297835/,Hotel Saint Yves,47.22628,-1.54329
https://sws.geonames.org/10345124/,Hotel Seven Urban Nantes Centre,47.20775,-1.53972
https://sws.geonames.org/6464553/,Hotel Stars Nantes,47.2473,-1.5039
https://sws.geonames.org/6498332/,Hotel de Bourgogne,47.2175,-1.5443
https://sws.geonames.org/10297839/,Hotel de La Gare de Nantes Citotel,47.21771,-1.54395
https://sws.geonames.org/6497876/,Hotel des Colonies,47.215,-1.5603
https://sws.geonames.org/10297833/,Hôtel La Pérouse,47.21668,-1.55648
https://sws.geonames.org/10297831/,Hôtel Le Cambronne,47.21189,-1.56168
https://sws.geonames.org/7506773/,Hôtel Novotel Nantes Centre Bord de Loire,47.20647,-1.54808
https://sws.geonames.org/10297829/,Hôtel Renova,47.21488,-1.5553
https://sws.geonames.org/10297827/,Hôtel Saint Patrick,47.21496,-1.55748
https://sws.geonames.org/6513382/,Ibis Nantes Centre,47.2189,-1.5609
https://sws.geonames.org/6515115/,Ibis Nantes Centre Gare Sud,47.2152,-1.547
https://sws.geonames.org/6515341/,Ibis Nantes La Beaujoire,47.2566,-1.5157
https://sws.geonames.org/9177031/,Ibis Styles Nantes Centre Place Royale,47.21423,-1.55742
https://sws.geonames.org/10297826/,Inn Nantes Centre,47.20701,-1.54845
https://sws.geonames.org/9177085/,Inter-Hotel Agora,47.25211,-1.6189
https://sws.geonames.org/9177178/,Inter-Hotel Du Grand Monarque,47.22161,-1.54744
https://sws.geonames.org/9224792/,Inter-Hotel Grand Hotel De Nantes,47.21262,-1.56024
https://sws.geonames.org/9177258/,Inter-Hotel Le Surcouf,47.2173,-1.54652
https://sws.geonames.org/9177296/,Inter-Hotel Novella Nantes Carquefou,47.26872,-1.48479
https://sws.geonames.org/6473356/,Kyriad,47.2177,-1.5444
https://sws.geonames.org/9177352/,Kyriad  Nantes Est - Carquefou,47.26916,-1.48523
https://sws.geonames.org/9177353/,Kyriad  Nantes Ouest - Saint Herblain,47.22778,-1.62445
https://sws.geonames.org/6499327/,Kyriad - Nantes Centre,47.2175,-1.5443
https://sws.geonames.org/6514270/,L Hotel,47.2173,-1.5476
https://sws.geonames.org/6520008/,Le Domaine D Orvault,47.265,-1.6288
https://sws.geonames.org/10125023/,Le Grand Hotel De Nantes,47.21266,-1.56021
https://sws.geonames.org/10297825/,Logis Beaujoire Hôtel,47.25773,-1.52928
https://sws.geonames.org/6474158/,Mascotte Nantes,47.1584,-1.60035
https://sws.geonames.org/6476171/,Mercure Gd Htl Nantes Ctre 4,47.214,-1.557
https://sws.geonames.org/6473350/,Mercure Ile de Nantes,47.2062,-1.5285
https://sws.geonames.org/9177962/,Mercure Nantes Centre Gare,47.21614,-1.54398
https://sws.geonames.org/10174391/,Mercure Nantes Centre Gd Hotel,47.21445,-1.55706
https://sws.geonames.org/6506044/,Mercure Nantes Gare Sud 3,47.21572,-1.54284
https://sws.geonames.org/10173584/,Nantes Centre Saint Jacques,47.196,-1.531
https://sws.geonames.org/10173560/,Nantes Est Saint SBastien Sur Loire,47.212,-1.487
https://sws.geonames.org/10173546/,Nantes Est Sainte Luce Sur Loire,47.262,-1.494
https://sws.geonames.org/6509061/,Novotel Nantes Carquefou,47.2829,-1.4539
https://sws.geonames.org/9178151/,Novotel Nantes Centre Cité Des Congrès,47.2139,-1.54292
https://sws.geonames.org/6516654/,Novotel Nantes Cite Congres,47.21353,-1.54402
https://sws.geonames.org/10342677/,Novotel Nantes Cite Des Congre,47.214,-1.543
https://sws.geonames.org/6492231/,Oceania Nantes,47.1789,-1.6189
https://sws.geonames.org/9178224/,Park & Suites Confort Carquefou,47.26892,-1.48496
https://sws.geonames.org/9178388/,Park & Suites Elegance Nantes Atlantis,47.22257,-1.62613
https://sws.geonames.org/9178389/,Park & Suites Elegance Nantes Hotel,47.21516,-1.55221
https://sws.geonames.org/9178229/,Park And Suites Confort Nantes Saint Herblain,47.22711,-1.65028
https://sws.geonames.org/11279879/,Park And Suites Nantes Centre,47.21515,-1.55221
https://sws.geonames.org/11279881/,Park And Suites Nantes Ouest Saint Herblain,47.22086,-1.62767
https://sws.geonames.org/9539821/,Premiere Classe Nantes Ouest,47.23409,-1.64879
https://sws.geonames.org/9178513/,Premiere Classe Nantes Reze,47.21837,-1.55362
https://sws.geonames.org/10281898/,Premiere Classe Nantes St Herblain,47.21179,-1.65403
https://sws.geonames.org/6490782/,Premiere Classe Nantes est - Saint Sebastien sur Loire,47.2116,-1.4871
https://sws.geonames.org/9178557/,Quality Hotel & Suites Nantes,47.25225,-1.51182
https://sws.geonames.org/10125021/,Quality Hotel Et Suites Nantes,47.25369,-1.51355
https://sws.geonames.org/10282271/,Quality Suites Nantes Atlantique,47.21944,-1.56158
https://sws.geonames.org/10283545/,Quality and Suites Nantes Atlantique,47.25133,-1.51004
https://sws.geonames.org/10297823/,Quick Palace Nantes,47.25305,-1.51285
https://sws.geonames.org/9178623/,Quintessia & Spa (Ex Domaine D'Orvault),47.25992,-1.58913
https://sws.geonames.org/9178637/,Radisson Blu Hotel Nantes,47.21749,-1.56283
https://sws.geonames.org/6508918/,Relais Mercure Nantes Ouest,47.2617,-1.6717
https://sws.geonames.org/9178794/,Residence Cerise Nantes Atlantis,47.22709,-1.65097
https://sws.geonames.org/9178795/,Residence Cerise Nantes La Beaujoire,47.25341,-1.52835
https://sws.geonames.org/10118622/,Residence De L'ocean La Tranche Sur Mer,47.20252,-1.54299
https://sws.geonames.org/10127364/,Residhome Nantes Berges De La Loire,47.21223,-1.53816
https://sws.geonames.org/11280028/,Residhome Nantes Les Berges De La Loire,47.21214,-1.53824
https://sws.geonames.org/6532063/,Residhome Res Ducs De Bretange,47.2138,-1.5452
https://sws.geonames.org/10278540/,Sajours and Affaires Nantes Ducs de Bretagne,47.21382,-1.54551
https://sws.geonames.org/9179085/,Sejours & Affaires Nantes La Beaujoire,47.25798,-1.51517
https://sws.geonames.org/9179105/,Seven Urban Suites,47.20829,-1.53833
https://sws.geonames.org/10117423/,Seven Urban Suites Nantes Cite Des Congres,47.2077,-1.53981
https://sws.geonames.org/9179084/,Séjours & Affaires Nantes Ducs De Bretagne,47.21382,-1.54551
https://sws.geonames.org/10234497/,Univea Suites Nantes La Beaujoire,47.25995,-1.49819
https://sws.geonames.org/10111590/,Urbanstyle Graslin,47.21224,-1.56184
https://sws.geonames.org/6490226/,WESTOTEL Nantes-Atlantique,47.2829,-1.55085
```

## Rq_population

```sparql
#Les 10 localités les plus peuplées

PREFIX gn: <https://www.geonames.org/ontology#>

SELECT ?f ?nom ?pop
WHERE {
  ?f a gn:GeonamesFeature ;
     gn:name ?nom ;
     gn:featureCode gn:P.PPL ;
     gn:population ?pop .
  FILTER(?pop > 0)
}
ORDER BY DESC(?pop)
LIMIT 10
```

Résultat :

```
f,nom,pop
https://sws.geonames.org/12278193/,Marne La Vallée,318325
https://sws.geonames.org/2970479/,Paris 15 Vaugirard,229713
https://sws.geonames.org/2994540/,Paris 20 Ménilmontant,185140
https://sws.geonames.org/3029374/,Paris 18 Buttes-Montmartre,183127
https://sws.geonames.org/3015772/,Paris 13 Gobelins,181271
https://sws.geonames.org/3029372/,Paris 19 Buttes-Chaumont,178691
https://sws.geonames.org/2988394/,Paris 16 Passy,159386
https://sws.geonames.org/3034610/,Paris 17 Batignolles-Monceau,159212
https://sws.geonames.org/8533870/,Saint-Quentin-en-Yvelines,146598
https://sws.geonames.org/2986082/,Paris 11 Popincourt,138170
```

## Rq_type

```sparql
#Types d’entités les plus fréquents

PREFIX gn:   <https://www.geonames.org/ontology#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?code ?definition (COUNT(?f) AS ?nb)
WHERE {
  ?f gn:featureCode ?code .
  ?code skos:definition ?definition .
  FILTER(LANG(?definition) = "en")
}
GROUP BY ?code ?definition
ORDER BY DESC(?nb)
LIMIT 15
```

Résultat :

```
code,definition,nb
https://www.geonames.org/ontology#P.PPL,"a city, town, village, or other agglomeration of buildings where people live and work",79556
https://www.geonames.org/ontology#A.ADM4,a subdivision of a third-order administrative division,34742
https://www.geonames.org/ontology#S.HTL,a building providing lodging and/or meals for the public,12305
https://www.geonames.org/ontology#S.PO,"a public building in which mail is received, sorted and distributed",9838
https://www.geonames.org/ontology#T.PK,"a pointed elevation atop a mountain, ridge, or other hypsographic feature",3325
https://www.geonames.org/ontology#H.STM,a body of running water moving to a lower level in a channel on land,3243
https://www.geonames.org/ontology#S.RSTN,"a facility comprising ticket office, platforms, etc. for loading and unloading train passengers and freight",3085
https://www.geonames.org/ontology#V.FRST,an area dominated by tree vegetation,2642
https://www.geonames.org/ontology#R.ST,a paved urban thoroughfare,2394
https://www.geonames.org/ontology#T.MT,"an elevation standing high above the surrounding area with small summit area, steep slopes and local relief of 300m or more",2023
https://www.geonames.org/ontology#T.PT,"a tapering piece of land projecting into a body of water, less prominent than a cape",979
https://www.geonames.org/ontology#S.CH,a building for public Christian worship,893
https://www.geonames.org/ontology#S.HSEC,"a large house, mansion, or chateau, on a large estate",879
https://www.geonames.org/ontology#S.FRM,a tract of land with associated buildings devoted to agriculture,850
https://www.geonames.org/ontology#S.HSTS,a place of historical importance,848
```
