#!/usr/bin/perl -w
use strict;
use File::Basename;
use Getopt::Std;
my $PROGRAM = basename $0;
my $USAGE=
"Usage: $PROGRAM
";

my $DATA_FILE = "/home/chiba/github/dbcls/homologene-rdf/original/homologene.data";

my %OPT;
getopts('', \%OPT);

my %GROUP;
open(DATA, $DATA_FILE) || die "$!";
while (<DATA>) {
    chomp;
    my @f = split(/\t/, $_, -1);
    if (@f != 6) {
        die;
    }
    my $group_id = $f[0];
    my $taxid = $f[1];
    my $gene_id = $f[2];
    if ($GROUP{$group_id}{$taxid}) {
        $GROUP{$group_id}{$taxid} .= ",${gene_id}";
    } else {
        $GROUP{$group_id}{$taxid} = "$gene_id";
    }
}
close(DATA);

foreach my $group_id (sort {$a <=> $b} keys %GROUP) {
    if ($GROUP{$group_id}{"9606"} && $GROUP{$group_id}{"10090"}) {
        print join("\t",
                   $GROUP{$group_id}{"9606"},
                   $GROUP{$group_id}{"10090"},
                   $group_id,
            ), "\n";
    }
}
