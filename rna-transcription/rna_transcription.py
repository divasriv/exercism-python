DNA=['A','T','C','G']
RNA=['U','A','G','C']
def to_rna(dna_strand):
    str=''
    for val in dna_strand:
        str+=RNA[DNA.index(val)]
    return str

a=to_rna("ACGTGGTCTTAA") #"UGCACCAGAAUU"
print(a)


