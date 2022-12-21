# HomoloGene RDF

## Original data

[NCBI HomoloGene](https://www.ncbi.nlm.nih.gov/homologene)
* Data provider
  * National Center for Biotechnology Information
* License
  * https://www.ncbi.nlm.nih.gov/home/about/policies/
* Download
  * https://ftp.ncbi.nlm.nih.gov/pub/HomoloGene/build68/

## Created RDF

```
./bin/homologene.py original/homologene.data > rdf/homologene.ttl
```

* Creator
  * Hirokazu Chiba
* Turtle file
  * https://github.com/dbcls/homologene-rdf/blob/main/rdf/homologene.ttl
* Schema
  * https://github.com/dbcls/homologene-rdf/blob/main/rdf-config/schema.svg

## SPARQL examples

* [orthologs.rq](https://github.com/dbcls/homologene-rdf/blob/main/sparql/ortholog.rq)
* [paralogs.rq](https://github.com/dbcls/homologene-rdf/blob/main/sparql/paralog.rq)
