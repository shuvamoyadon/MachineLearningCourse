"""
Numerical vs Numerical Analysis

This script generates a scatter plot with regression line for numerical vs numerical analysis.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

def main():
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate sample data: Years of Experience vs Salary
    np.random.seed(42)
    
    # Generate base values
    years_exp = np.random.uniform(0, 20, 100)
    
    # Create salary with positive correlation to experience
    salary = 40000 + (years_exp * 2500) + np.random.normal(0, 10000, 100)
    
    # Ensure no negative salaries
    salary = np.maximum(salary, 30000)
    
    # Create DataFrame
    data = pd.DataFrame({
        'Years_Experience': np.round(years_exp, 1),
        'Salary': np.round(salary, -2)  # Round to nearest $100
    })
    
    # Create visualization
    plt.figure(figsize=(12, 7))
    
    # Create scatter plot with regression line
    ax = sns.regplot(x='Years_Experience', y='Salary', data=data, 
                    scatter_kws={'alpha':0.6, 's':80},
                    line_kws={'color':'red', 'linewidth':2.5})
    
    # Calculate correlation
    corr_coef = np.corrcoef(data['Years_Experience'], data['Salary'])[0, 1]
    
    # Customize the plot
    plt.title('Years of Experience vs Salary', fontsize=16, pad=20, fontweight='bold')
    plt.xlabel('Years of Experience', fontsize=12)
    plt.ylabel('Annual Salary ($)', fontsize=12)
    plt.xticks(fontsize=11)
    plt.yticks(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.3)
    
    # Add correlation coefficient
    plt.text(0.02, 0.95, f'Correlation: {corr_coef:.2f}', 
             transform=ax.transAxes, fontsize=12,
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
    
    # Add mean lines
    mean_exp = data['Years_Experience'].mean()
    mean_salary = data['Salary'].mean()
    plt.axvline(mean_exp, color='green', linestyle='--', alpha=0.7, label=f'Mean Exp: {mean_exp:.1f} yrs')
    plt.axhline(mean_salary, color='purple', linestyle='--', alpha=0.7, label=f'Mean Salary: ${mean_salary:,.0f}')
    
    plt.legend()
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('/Users/shuvamoy/Documents/MLearn/Day1/descriptive_statistics/graph/exp_vs_salary.png', 
                dpi=300, bbox_inches='tight')
    print("Scatter plot saved as 'graph/exp_vs_salary.png'")
    
    # Print correlation for reference
    print(f"Correlation coefficient: {corr_coef:.3f}")

if __name__ == "__main__":
    main()
