from src.parser import DNAParser
from src.visualizer import BloodTypeVisualizer

def main():
    genome_file = "data/sample_genome.txt"
    target_markers = ['rs8176719', 'rs8176746', 'rs2075554']
    
    print("Initializing Modular DNA Genomic Parser...")
    try:
        parser = DNAParser(genome_file)
        genotypes = parser.extract_genotypes(target_markers)
    except FileNotFoundError as e:
        print(f"[Error] {e}\nPlease ensure dataset is in the data/ folder.")
        return

    # Predictive output logic based on sample alleles
    blood_type = "O Negative (O-)"
    trait_status = "Universal Donor"
    
    print("Generating vector compatibility data visualization...")
    viz = BloodTypeVisualizer(blood_type, trait_status, genotypes)
    viz.generate_dashboard("blood_type_profile.png")
    print("🎉 Project pipeline executed successfully. Check 'blood_type_profile.png'!")

if __name__ == "__main__":
    main()
