# 🧬 GeneType-Viz: Genomic Antigen Predictor & Tetrachromacy Scanner

An open-source personal bioinformatics pipeline that parses raw genomic microarray 
data (e.g., 23andMe, AncestryDNA formats), isolates specific Single Nucleotide 
Polymorphisms (SNPs) associated with blood antigens and color vision variations, and 
renders data insights directly to your terminal or custom visualization panels.

## 📊 Sample Visualization & Output Layout

The pipeline generates clean, presentation-ready console logs and structured 
layouts:
* **Genomic Discovery Card:** Maps verified raw genetic marker data directly to 
predictive phenotypical blood outcomes and compatibility parameters.
* **Vision Variance Profile:** Evaluates specific coordinates within the 
X-chromosome color-vision pocket to distinguish between standard trichromacy 
profiles and possible heterozygous tetrachromat variants.

## 🧬 Biological Mechanisms & Target SNPs

This tool isolates and analyzes key genetic markers to determine both hematological 
profiles and advanced color-vision capabilities:

### 🩸 Blood Type & Rh Factor Markers

| Genetic Marker (rsID) | Target Gene | Biological Role / Detected Allele Variants |
| :--- | :--- | :--- |
| **rs8176719** | *ABO* | Determines Type O status via a critical single-nucleotide 
deletion. |
| **rs8176746** | *ABO* | Distinguishes between standard blood type base states. |
| **rs2075554** | *RHD* | Tracks Rh blood group system markers to predict (+) or (-) 
antigen status. |

### 👁️ Tetrachromacy & Color Vision Pocket

| Genetic Marker / Position | Target Gene | Biological Role / Insight |
| :--- | :--- | :--- |
| **X-Chr: 153.4 Megabase Corridor** | *OPN1LW* | Targets red cone opsin sequences 
to scan for heterozygous variants required to express a 4th cone matrix. |

## 🚀 Quickstart Guide

### 1. Installation & Environment Setup
Clone this repository to your local machine, navigate into the project directory, 
and ensure your virtual environment is active:

```bash
# Install dependencies
pip install -r requirements.txt

### 2. Running the Analyzers
To run the primary blood compatibility and antigen pipeline:
python main.py

To run the newly integrated color-vision variance profile scanner:
python tetrachromacy_check.py
