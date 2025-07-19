"""
Categorical vs Categorical Analysis

This script generates a stacked bar chart for categorical vs categorical analysis.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Sample data: Study Method vs Exam Result (Pass/Fail)
    data = {
        'Study_Method': ['Self-Study']*20 + ['Group']*20 + ['Tutoring']*20,
        'Result': (['Pass']*8 + ['Fail']*12 +  # Self-Study
                  ['Pass']*15 + ['Fail']*5 +   # Group
                  ['Pass']*18 + ['Fail']*2)    # Tutoring
    }
    
    df = pd.DataFrame(data)
    
    # Create cross-tabulation
    cross_tab = pd.crosstab(df['Study_Method'], df['Result'])
    
    # Create visualization
    plt.figure(figsize=(10, 6))
    cross_tab.plot(kind='bar', stacked=True, color=['#ff6b6b', '#51cf66'])
    
    plt.title('Exam Results by Study Method', pad=20, fontsize=14, fontweight='bold')
    plt.xlabel('Study Method', fontsize=12)
    plt.ylabel('Number of Students', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Result', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    # Add percentage labels
    ax = plt.gca()
    for p in ax.patches:
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy()
        if height > 0:  # Only add label if height is greater than 0
            ax.text(x + width/2, 
                   y + height/2, 
                   f'{int(height)}',
                   ha='center',
                   va='center',
                   color='white',
                   fontweight='bold')
    
    # Save the plot
    plt.savefig('/Users/shuvamoy/Documents/MLearn/Day1/descriptive_statistics/graph/study_method_vs_result.png', 
                dpi=300, bbox_inches='tight')
    print("Stacked bar chart saved as 'graph/study_method_vs_result.png'")

if __name__ == "__main__":
    main()
