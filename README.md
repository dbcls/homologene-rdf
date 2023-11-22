# HomoloGene RDF

## Original data

[NCBI HomoloGene](https://www.ncbi.nlm.nih.gov/homologene)
* Data provider
  * National Center for Biotechnology Information
* License
  * https://www.ncbi.nlm.nih.gov/home/about/policies/
* Statistics
  * https://www.ncbi.nlm.nih.gov/homologene/statistics/
* Download
  * https://ftp.ncbi.nlm.nih.gov/pub/HomoloGene/build68/

## Created RDF

### 2023-05-17

```
$ curl -OR https://ftp.ncbi.nlm.nih.gov/pub/HomoloGene/build68/homologene.xml.gz
$ gunzip homologene.xml.gz
$ ./bin/homologene.xml2ttl.py homologene.xml > rdf/homologene_2023-05-17.ttl
```

* Version
  * release_20230517
* Issued
  * 2023-05-17
* Turtle file
  * https://github.com/dbcls/homologene-rdf/blob/main/rdf/homologene_2023-05-17.ttl
* Schema
  * https://raw.githubusercontent.com/dbcls/rdf-config/master/config/homologene/schema.svg

### Previous version

```
$ ./bin/homologene.data2ttl.py original/homologene.data > rdf/homologene_2023-03-01.ttl
```

* Creator
  * Hirokazu Chiba
* Version
  * release_20230301
* Issued
  * 2023-03-01	
* Turtle file
  * https://github.com/dbcls/homologene-rdf/blob/main/rdf/homologene_2023-03-01.ttl

## SPARQL examples

* [orthologs.rq](https://github.com/dbcls/homologene-rdf/blob/main/sparql/ortholog.rq)
* [paralogs.rq](https://github.com/dbcls/homologene-rdf/blob/main/sparql/paralog.rq)
