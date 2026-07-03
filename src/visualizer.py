import matplotlib.pyplot as plt

class BloodTypeVisualizer:
    """Generates a premium visual profile for blood compatibility using standard vector shapes."""
    
    def __init__(self, blood_type: str, trait: str, markers: dict):
        self.blood_type = blood_type
        self.trait = trait
        self.markers = markers
        self.blood_groups = ['O-', 'O+', 'A-', 'A+', 'B-', 'B+', 'AB-', 'AB+']

    def generate_dashboard(self, output_path: str = "blood_type_profile.png"):
        """Plots and saves the dual-panel genomic visualization."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        fig.suptitle("Personal Genomic Profile Analysis", fontsize=16, fontweight='bold', color='#2c3e50')
        fig.patch.set_facecolor('#f8f9fa')

        # --- Left Panel: Discovery Card ---
        ax1.set_facecolor('#ffffff')
        ax1.set_xlim(0, 1)
        ax1.set_ylim(0, 1)

        ax1.text(0.1, 0.85, "PREDICTED BLOOD TYPE", fontsize=10, color='#7f8c8d', fontweight='bold')
        ax1.text(0.1, 0.72, self.blood_type, fontsize=28, color='#c0392b', fontweight='bold')
        ax1.text(0.1, 0.64, f"✦  {self.trait} Status", fontsize=12, color='#27ae60', style='italic', fontweight='bold')
        ax1.plot([0.1, 0.9], [0.55, 0.55], color='#bdc3c7', lw=1)

        ax1.text(0.1, 0.45, "GENETIC EVIDENCE (RAW DATA)", fontsize=10, color='#7f8c8d', fontweight='bold')
        y_pos = 0.35
        for marker, genotype in self.markers.items():
            ax1.text(0.1, y_pos, f"◆  {marker}:", fontsize=11, fontweight='bold', color='#34495e')
            ax1.text(0.55, y_pos, genotype, fontsize=11, color='#2980b9', fontweight='bold')
            y_pos -= 0.08

        ax1.axis('off')

        # --- Right Panel: Compatibility Grid ---
        ax2.set_facecolor('#ffffff')
        can_give = [1] * 8
        can_receive = [1] + [0] * 7

        ax2.scatter(self.blood_groups, [1]*8, s=[400 if x else 100 for x in can_give], 
                    c=['#e74c3c' if x else '#bdc3c7' for x in can_give], alpha=0.8, edgecolors='black')
        ax2.scatter(self.blood_groups, [0]*8, s=[400 if x else 100 for x in can_receive], 
                    c=['#27ae60' if x else '#f1f2f6' for x in can_receive], alpha=0.8, edgecolors='black')

        ax2.set_ylim(-0.5, 1.5)
        ax2.set_yticks([0, 1])
        ax2.set_yticklabels(['Can Receive From', 'Can Transfuse To'], fontsize=11, fontweight='bold', color='#34495e')
        ax2.set_xticks(range(len(self.blood_groups)))
        ax2.set_xticklabels(self.blood_groups, fontsize=11, fontweight='bold')
        
        for spine in ax2.spines.values():
            spine.set_visible(False)
        ax2.tick_params(axis='both', which='both', length=0)
        ax2.grid(axis='x', linestyle='--', alpha=0.5)

        plt.tight_layout()
        plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor())
        plt.close()
