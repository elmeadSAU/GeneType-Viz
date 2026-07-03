# 🧬 GeneType-Viz: Genomic Blood Type Predictor & Compatibility Matrix

An open-source personal bioinformatics pipeline that parses raw genomic microarray data (e.g., 23andMe, AncestryDNA formats), isolates specific Single Nucleotide Polymorphisms (SNPs) associated with blood antigens, and renders a custom dual-panel vector data visualization.

## 📊 Sample Visualization Output

The pipeline generates a clean, dual-panel presentation-ready layout:
- **Genomic Discovery Card (Left):** Maps verified raw genetic marker data directly to predictive phenotypical outcomes.
- **Compatibility Matrix (Right):** Generates a vector chart calculating donor/recipient parameters across all major blood phenotypes based on the extracted genetic markers.

## 🧬 Biological Mechanism & Target SNPs

This tool isolates and reads three key genetic markers to determine the ABO group and Rh factor:

| Genetic Marker (rsID) | Target Gene | Biological Role / Detected Allele Variants |
| :--- | :--- | :--- |
| **rs8176719** | *ABO* | Determines Type O status via a critical single-nucleotide deletion. |
| **rs8176746** | *ABO* | Distinguishes between standard blood type base states. |
| **rs2075554** | *RHD* | Tracks Rh blood group system markers to predict (+) or (-) antigen status. |

## 🚀 Quickstart Guide

### 1. Installation & Environment Setup
Clone this repository to your local machine, navigate into the directory, and ensure your virtual environment is active:
```bash
# Install dependencies
pip install -r requirements.txt
python main.py
eof
