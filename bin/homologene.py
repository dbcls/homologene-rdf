#!/usr/bin/env python3
import sys
import argparse

parser = argparse.ArgumentParser(description='RDFize HomoloGene')
parser.add_argument('homologene', help='HomoloGene data file')
args = parser.parse_args()

print("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
print("@prefix dct: <http://purl.org/dc/terms/> .")
print("@prefix obo: <http://purl.obolibrary.org/obo/> .")
print("@prefix sio: <http://semanticscience.org/resource/> .")
print("@prefix orth: <http://purl.org/net/orth#> .")
print("@prefix homologene: <https://identifiers.org/homologene/> .")
print("@prefix taxonomy: <http://identifiers.org/taxonomy/> .")
print("@prefix ncbigene: <http://identifiers.org/ncbigene/> .")
print("@prefix ncbiprotein: <http://identifiers.org/ncbiprotein/> .")
print()
print('<https://ncbi.nlm.nih.gov/homologene/>')
print('    a orth:OrthologyDataset ;')
print('    dct:title "HomoloGene Release 68" ;')
print('    dct:license <https://www.ncbi.nlm.nih.gov/home/about/policies/> .')
print()

gene_info = {}

def print_gene_info(gene_id):
    symbol, taxid, refseq = gene_info[gene_id]
    
    print(f'ncbigene:{gene_id} a orth:Gene ;')
    print(f'    rdfs:label "{symbol}" ;')
    print(f'    obo:RO_0002162 taxonomy:{taxid} ; # in taxon')
    print(f'    sio:SIO_010078 ncbiprotein:{refseq} . # encodes')
    print()

def print_group(grp_id, genes):
    if grp_id == "" or len(genes) == 0:
        return
    
    print(f'homologene:{grp_id} a orth:OrthologsCluster ;')
    print(f'    orth:inDataset <https://ncbi.nlm.nih.gov/homologene/> ;')
    n = len(genes)
    for i in range(n-1):
        print(f'    orth:hasHomologousMember ncbigene:{genes[i]} ;')
    print(f'    orth:hasHomologousMember ncbigene:{genes[n-1]} .')
    print()
    for gene in genes:
        print_gene_info(gene)

fp = open(args.homologene, 'r')
prev_grp_id = ""
genes = []
for line in fp:
    fields = line.strip().split('\t')
    if len(fields) != 6:
        print("err", file=sys.stderr, flush=True)
        continue
    grp_id, tax_id, gene_id, symbol, gi, refseq = fields
    gene_info[gene_id] = (symbol, tax_id, refseq);
    if prev_grp_id != grp_id:
        print_group(prev_grp_id, genes)
        prev_grp_id = grp_id
        genes = []
    genes.append(gene_id)
    
print_group(prev_grp_id, genes)
