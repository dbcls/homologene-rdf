#!/usr/bin/perl -w
use strict;
use File::Basename;
use Getopt::Std;
my $PROGRAM = basename $0;
my $USAGE=
"Usage: $PROGRAM ORGANISM_LIST HOMOLOGENE_TABLE
";

my %OPT;
getopts('', \%OPT);

if (@ARGV != 2) {
    print STDERR $USAGE;
    exit 1;
}
my ($LIST_FILE, $DATA_FILE) = @ARGV;

my @ID = ();
my %ID = ();
my %TAXID = ();
open(LIST, "$LIST_FILE") || die "$!";
print "geneid";
while (<LIST>) {
    chomp;
    my @f = split("\t", $_);
    if ($f[0] =~ /^\d+$/) {
        my $id = $f[0];
        my $taxid = $f[1];
        my $common_name = $f[3];
        $ID{$taxid} = $id;
        $TAXID{$id} = $taxid;
        push @ID, $id;
        print "\t$id $common_name";
    }
}
print "\n";
close(LIST);

my %MEMBER = ();
my %HUMAN_GENE = ();
open(DATA, "$DATA_FILE") || die "$!";
while (<DATA>) {
    chomp;
    my @f = split("\t", $_);
    if (@f != 6) {
        die;
    }
    my $group = $f[0];
    my $taxid = $f[1];
    my $geneid = $f[2];
    my $id = $ID{$taxid};
    if ($MEMBER{$group}{$id}) {
        push @{$MEMBER{$group}{$id}}, $geneid;
    } else {
        $MEMBER{$group}{$id} = [$geneid];
    }
    if ($taxid eq "9606") {
        $HUMAN_GENE{$group}{$geneid} = 1;
    }
}
close(DATA);

### Print matrix
open(PIPE, "|sort -n") || die "$!";
for my $group (sort {$a<=>$b} keys(%MEMBER)) {
    my $line = "$group";
    my @human_gene = keys(%{$HUMAN_GENE{$group}});
    for my $geneid (@human_gene) {
        my $line = get_profile($geneid, $group);
        print PIPE $line;
    }
}
close(PIPE);

################################################################################
### Function ###################################################################
################################################################################

sub get_profile {
    my ($geneid, $group) = @_;
    
    my $line  = $geneid;
    for my $id (@ID) {
        my $elem = 0;
        if ($MEMBER{$group}{$id}) {
            # $elem = scalar(@{$MEMBER{$group}{$id}});
            # $elem = join(",", @{$MEMBER{$group}{$id}});
            $line  .= "\t1";
        } else {
            $line  .= "\t0";
        }
        # $line  .= "\t$elem";
    }
    $line  .= "\n";

    return $line;
}
