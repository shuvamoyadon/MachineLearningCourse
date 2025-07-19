"""
Bivariate Analysis Script

This script demonstrates bivariate analysis using pandas and seaborn to analyze
the relationship between study hours and exam scores.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate sample data
    study_hours = np.random.normal(5, 1.5, 100)
    exam_scores = 30 + 5 * study_hours + np.random.normal(0, 3, 100)

    # Create DataFrame
    data = pd.DataFrame({
        'Study_Hours': study_hours,
        'Exam_Score': exam_scores
    })

    # Create visualization
    plt.figure(figsize=(10, 6))
    sns.regplot(x='Study_Hours', y='Exam_Score', data=data, scatter_kws={'alpha':0.6})
    plt.title('Study Hours vs Exam Score')
    plt.xlabel('Study Hours')
    plt.ylabel('Exam Score')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('../graph/study_hours_vs_scores.png')
    plt.close()
    
    # Calculate and print correlation
    correlation = data['Study_Hours'].corr(data['Exam_Score'])
    print(f"Correlation coefficient: {correlation:.2f}")

if __name__ == "__main__":
    main()
