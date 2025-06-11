import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set style for better visualization
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Create sample data
np.random.seed(42)
study_hours = np.random.normal(5, 1.5, 100)
# Add some correlation with noise
exam_scores = 30 + 5 * study_hours + np.random.normal(0, 3, 100)

data = pd.DataFrame({
    'Study_Hours': study_hours,
    'Exam_Score': exam_scores
})

# Calculate correlation
correlation = data.corr().iloc[0, 1]

# Create visualization with smaller figure size
plt.figure(figsize=(10, 4.5))  # Adjusted size for better proportions

# Scatter plot
plt.subplot(1, 2, 1)
sns.scatterplot(x='Study_Hours', y='Exam_Score', data=data, alpha=0.7)
plt.title('Scatter Plot: Study Hours vs Exam Score', pad=15)
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')

# Add regression line
sns.regplot(x='Study_Hours', y='Exam_Score', data=data, scatter=False, color='red')

# Add correlation text
plt.text(1, 90, f'Correlation: {correlation:.2f}', 
         bbox=dict(facecolor='white', alpha=0.8), 
         transform=plt.gca().transAxes)

# Box plot for bivariate analysis
plt.subplot(1, 2, 2)
# Create categories for study hours
data['Study_Group'] = pd.cut(data['Study_Hours'], 
                           bins=[0, 3, 5, 7, 10], 
                           labels=['0-3h', '3-5h', '5-7h', '7-10h'])
sns.boxplot(x='Study_Group', y='Exam_Score', data=data)
plt.title('Box Plot: Exam Score by Study Group', pad=15)
plt.xlabel('Study Hours Group')
plt.ylabel('Exam Score')

plt.tight_layout()
plt.savefig('bivariate_analysis_plot.png', dpi=150, bbox_inches='tight')  # Reduced DPI for smaller file size
plt.close()

# Print some statistics
print("Bivariate Analysis Summary:")
print(f"Correlation coefficient: {correlation:.2f}")
print("\nSummary statistics by study group:")
print(data.groupby('Study_Group')['Exam_Score'].describe())
