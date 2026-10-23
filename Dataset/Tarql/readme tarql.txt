tarql_v1 : tout les attributs sauf admin1
tarql_v2 : juste attributs gn 

requete tarql : 
	tarql --ntriples tarql_v1.rq clean_france_all_features.csv > france_triples.nt 2> avertissements.log
	tarql --ntriples tarql_v2.rq clean_france_all_features.csv > france_triples_gn.nt 2> avertissements.log

convertion en ttl : 
	rapper -i ntriples -o turtle france_triples.nt > france_triples.ttl
	rapper -i ntriples -o turtle france_triples_gn.nt > france_triples_gn.ttl

