#!/usr/bin/env python3
import argparse
import xml.etree.ElementTree as ET

parser = argparse.ArgumentParser(description='')
parser.add_argument('xml', help='HomoloGene XML file')
args = parser.parse_args()

tree = ET.parse(args.xml)
root = tree.getroot()
    
def main():
    print_header()
    for entries in root:
        for entry in entries:
            hg_id =  entry.find('HG-Entry_hg-id').text
            caption = entry.find('HG-Entry_caption').text
            print(f"homologene:{hg_id} a orth:OrthologsCluster ;")
            print('    orth:inDataset <https://ncbi.nlm.nih.gov/homologene/> ;')
            print(f'    dct:identifier {hg_id} ;')
            print(f'    rdfs:label "{caption}" ;')
            # print(entry.find('HG-Entry_version').text)
            # print(entry.find('HG-Entry_taxid').text)
            gene_ids = get_genes(entry.find('HG-Entry_genes'))
            print(" ;\n".join(gene_ids) + " .\n")
            print_genes(entry.find('HG-Entry_genes'))

def get_genes(genes):
    gene_ids = []
    for gene in genes:
        geneid = gene.find('HG-Gene_geneid').text
        gene_ids.append(f"    orth:hasHomologousMember ncbigene:{geneid}")
    return gene_ids

def print_genes(genes):
    for gene in genes:
        geneid = gene.find('HG-Gene_geneid').text
        symbol = gene.find('HG-Gene_symbol').text
        taxid = gene.find('HG-Gene_taxid').text
        prot = gene.find('HG-Gene_prot-acc').text
        print(f"ncbigene:{geneid} a orth:Gene ;")
        print(f'    rdfs:label "{symbol}" ;')
        print(f'    obo:RO_0002162 taxonomy:{taxid} ; # in taxon')
        print(f'    sio:SIO_010078 ncbiprotein:{prot} . # encodes')
        print()

def print_header():
    print('@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .')
    print('@prefix dct: <http://purl.org/dc/terms/> .')
    print('@prefix obo: <http://purl.obolibrary.org/obo/> .')
    print('@prefix sio: <http://semanticscience.org/resource/> .')
    print('@prefix orth: <http://purl.org/net/orth#> .')
    print('@prefix homologene: <https://identifiers.org/homologene/> .')
    print('@prefix taxonomy: <http://identifiers.org/taxonomy/> .')
    print('@prefix ncbigene: <http://identifiers.org/ncbigene/> .')
    print('@prefix ncbiprotein: <http://identifiers.org/ncbiprotein/> .')
    print()
    print('<https://ncbi.nlm.nih.gov/homologene/>')
    print('    a orth:OrthologyDataset ;')
    print('    dct:title "HomoloGene Release 68" ;')
    print('    dct:license <https://www.ncbi.nlm.nih.gov/home/about/policies/> .')
    print()

if __name__ == '__main__':
    main()
