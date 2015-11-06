__author__ = 'Jyan Roynson'
from Bio import SeqIO
import argparse
parser = argparse.ArgumentParser(description="Script to determine pseudo chromosome length in bp")
parser.add_argument("-ref", action="store")
args = parser.parse_args()
f1 = open("chromosome_sizes.txt", "w")
chr_num = 1
for s in SeqIO.parse(args.ref, "fasta"):
    f1.write("%d\t%s\n" %(chr_num, len(s)))
    chr_num += 1
f1.close()