"""
Categorical vs Numerical Analysis

This script generates a box plot for categorical vs numerical analysis.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Sample data: Product Category vs Sales
    np.random.seed(42)
    
    # Generate sample data for three product categories
    data = {
        'Category': (['Electronics'] * 30 + 
                    ['Clothing'] * 30 + 
                    ['Furniture'] * 30),
        'Sales': (
            # Electronics: higher variance, higher average
            list(np.random.normal(1200, 300, 30)) +
            # Clothing: moderate average, less variance
            list(np.random.normal(800, 150, 30)) +
            # Furniture: lower average, some high-value sales
            list(np.random.normal(500, 200, 25)) + list(np.random.normal(1500, 100, 5))
        )
    }
    
    df = pd.DataFrame(data)
    
    # Create visualization
    plt.figure(figsize=(12, 6))
    
    # Create boxplot
    ax = sns.boxplot(x='Category', y='Sales', data=df, 
                    order=['Electronics', 'Clothing', 'Furniture'],
                    palette='viridis')
    
    # Add stripplot to show individual data points
    sns.stripplot(x='Category', y='Sales', data=df, 
                 order=['Electronics', 'Clothing', 'Furniture'],
                 color='black', alpha=0.5, size=5, jitter=True)
    
    # Add mean line
    means = df.groupby('Category')['Sales'].mean()
    for i, category in enumerate(['Electronics', 'Clothing', 'Furniture']):
        plt.hlines(means[category], i-0.4, i+0.4, colors='red', linestyles='dashed', linewidth=2)
    
    # Customize the plot
    plt.title('Sales Distribution by Product Category', fontsize=16, pad=20, fontweight='bold')
    plt.xlabel('Product Category', fontsize=12)
    plt.ylabel('Sales ($)', fontsize=12)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add mean values as text
    for i, category in enumerate(['Electronics', 'Clothing', 'Furniture']):
        plt.text(i, means[category] + 50, f'Mean: ${means[category]:.0f}',
                ha='center', va='bottom', fontweight='bold', color='red')
    
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('/Users/shuvamoy/Documents/MLearn/Day1/descriptive_statistics/graph/category_vs_sales.png', 
                dpi=300, bbox_inches='tight')
    print("Box plot saved as 'graph/category_vs_sales.png'")

if __name__ == "__main__":
    main()
