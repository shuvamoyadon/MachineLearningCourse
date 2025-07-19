"""
Study Method Analysis Script

This script generates a box plot comparing exam scores across different study methods.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate sample data matching the table in the markdown
    data = {
        'Student_ID': range(1, 11),
        'Study_Method': ['Self-Study', 'Group', 'Tutoring', 'Self-Study', 'Group', 
                        'Tutoring', 'Self-Study', 'Group', 'Tutoring', 'Self-Study'],
        'Score': [72, 88, 95, 68, 82, 91, 75, 85, 89, 70]
    }
    df = pd.DataFrame(data)

    # Create visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Study_Method', y='Score', data=df, 
                order=['Self-Study', 'Group', 'Tutoring'])
    
    # Add mean line
    means = df.groupby('Study_Method')['Score'].mean()
    for i, method in enumerate(['Self-Study', 'Group', 'Tutoring']):
        plt.hlines(means[method], i-0.4, i+0.4, colors='red', linestyles='dashed', linewidth=2)
    
    plt.title('Exam Performance by Study Method', pad=20)
    plt.xlabel('Study Method')
    plt.ylabel('Exam Score')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('/Users/shuvamoy/Documents/MLearn/Day1/descriptive_statistics/graph/study_method_vs_scores.png', dpi=300, bbox_inches='tight')
    print("Box plot saved as 'graph/study_method_vs_scores.png'")

if __name__ == "__main__":
    main()
