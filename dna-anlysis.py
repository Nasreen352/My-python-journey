# DNA Analysis Program
# Created by Nasreen - Biology to IT Journey

# Variables
dna = "ATGCGTAGCTAGCTAG"
genes = ["BRCA1", "TP53", "EGFR", "KRAS"]

# Count nucleotides using count()
a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

# Calculate GC content
total = len(dna)
gc_content = ((g_count + c_count) / total) * 100

# Decision making with if/else
if "ATG" in dna:
    start_codon = "Found ATG (start codon)"
else:
    start_codon = "No start codon"

# for loop - print each nucleotide
print("=" * 40)
print("DNA SEQUENCE ANALYSIS")
print("=" * 40)
print(f"DNA Sequence: {dna}")
print(f"Length: {len(dna)} nucleotides")
print("-" * 40)
print("Nucleotide Count:")
print(f"  A (Adenine): {a_count}")
print(f"  T (Thymine): {t_count}")
print(f"  G (Guanine): {g_count}")
print(f"  C (Cytosine): {c_count}")
print("-" * 40)
print(f"GC Content: {gc_content:.2f}%")
print(f"Start Codon Check: {start_codon}")
print("-" * 40)
print("Genes in Database:")
for gene in genes:
    print(f"  - {gene}")
print("=" * 40)
