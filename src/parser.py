import os

class DNAParser:
    """Handles parsing raw genetic microarray text files for target SNPs."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Target genome file not found at: {filepath}")

    def extract_genotypes(self, target_snps: list) -> dict:
        """Parses the file and extracts matching rsID genotypes."""
        results = {}
        with open(self.filepath, 'r') as f:
            for line in f:
                if line.startswith('#') or not line.strip():
                    continue
                
                parts = line.strip().split()
                if len(parts) >= 4:
                    rsid, genotype = parts[0], parts[3]
                    if rsid in target_snps:
                        results[rsid] = genotype
        return results
