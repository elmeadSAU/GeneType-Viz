import pandas as pd
import os

def check_tetrachromacy(dna_file_path):
    print("=" * 60)
    print("🧬 DNA-Visualization: Tetrachromacy Genetic Scanner 🧬")
    print("=" * 60)
    
    if not os.path.exists(dna_file_path):
        print(f"❌ Error: File not found at '{dna_file_path}'")
        return

    # Target SNPs associated with the OPN1LW gene variants
    target_snps = {
        'rs5928666': 'OPN1LW (Red Cone Variant 1)',
        'rs5928643': 'OPN1LW (Red Cone Variant 2)'
    }

    print(f"Parsing raw sequence data from: {dna_file_path}...\n")
    
    try:
        df = pd.read_csv(
            dna_file_path, 
            sep=None, 
            comment='#', 
            names=['rsid', 'chromosome', 'position', 'genotype'],
            dtype={'rsid': str, 'chromosome': str, 'genotype': str},
            engine='python'
        )
    except Exception as e:
        print(f"❌ Error parsing file structure: {e}")
        return

    found_markers = df[df['rsid'].isin(target_snps.keys())]

    if found_markers.empty:
        print("🔍 Status: Target SNPs not found in this dataset.")
        return

    print("📊 Found Genetic Markers:")
    print("-" * 50)
    
    has_variation = False
    for _, row in found_markers.iterrows():
        rsid = row['rsid']
        genotype = str(row['genotype']).strip()
        gene_name = target_snps[rsid]
        
        print(f"• SNP ID: {rsid} -> {gene_name}")
        print(f"  Your Genotype: {genotype}")
        
        cleaned_genotype = genotype.replace('-', '').replace(' ', '')
        if len(set(cleaned_genotype)) > 1:
            has_variation = True
            print("  ✨ Result: Heterozygous variant detected!")
        else:
            print("  🔹 Result: Homozygous.")
        print("-" * 50)

    print("\n💡 Final Analysis:")
    if has_variation:
        print("🎉 [POSSIBLE TETRACHROMAT] Dual-variant setup detected.")
        print("   You possess the framework to express a 4th cone!")
    else:
        print("   Standard Trichromat Profile. No dual-variant shift.")
    print("=" * 60)

check_tetrachromacy('data/sample_genome.txt')
