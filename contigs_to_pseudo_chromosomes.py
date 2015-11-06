__author__ = 'Jyan Roynson'
# takes reference and anchor positions - concatenates contigs into chromosomes based on cM position from anchor list (made for barley reference genome)
import argparse
from Bio import SeqIO

parser = argparse.ArgumentParser(description="Using reference sequence contigs and anchor positions to create pseaudo chromosomes (chromosomes as single fasta entries")
parser.add_argument("-ref", action="store")
parser.add_argument("-anchors", action="store")
args = parser.parse_args()


# parse reference fasta
id_seq = {}
for seq_record in SeqIO.parse(args.ref, "fasta"):
    id_seq[seq_record.id] = str(seq_record.seq)
print("parsing done")
chrom1 = []
chrom2 = []
chrom3 = []
chrom4 = []
chrom5 = []
chrom6 = []
chrom7 = []

with open (args.anchors) as anchors:
    for line in anchors:
        if line.split()[1] == "1":
            if line.split()[0] in id_seq:
                chrom1.append(str(id_seq[line.split()[0]]))
        if line.split()[1] == "2":
            if line.split()[0] in id_seq:
                chrom2.append(str(id_seq[line.split()[0]]))
        if line.split()[1] == "3":
            if line.split()[0] in id_seq:
                chrom3.append(str(id_seq[line.split()[0]]))
        if line.split()[1] == "4":
            if line.split()[0] in id_seq:
                chrom4.append(str(id_seq[line.split()[0]]))
        if line.split()[1] == "5":
            if line.split()[0] in id_seq:
                chrom5.append(str(id_seq[line.split()[0]]))
        if line.split()[1] == "6":
            if line.split()[0] in id_seq:
                chrom6.append(str(id_seq[line.split()[0]]))
        if line.split()[1] == "7":
            if line.split()[0] in id_seq:
                chrom7.append(str(id_seq[line.split()[0]]))
f1 = open("barley_pseudo_chromosomes.fa", "w")
f1.write(">chromosome1\n%s\n>chromosome2\n%s\n>chromosome3\n%s\n>chromosome4\n%s\n>chromosome5\n%s\n>chromosome6\n%s\n>chromosome7\n%s" \
         % ("".join(chrom1),"".join(chrom2),"".join(chrom3),"".join(chrom4),"".join(chrom5),"".join(chrom6),"".join(chrom7)))
f1.close()

