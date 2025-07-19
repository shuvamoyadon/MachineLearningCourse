import numpy as np
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample student scores (math marks)
students = {
    'Alice': 78,
    'Bob': 95,
    'Charlie': 50,
    'David': 65,
    'Eva': 88,
    'Frank': 30,
    'Grace': 99,
    'Hank': 45,
    'Ivy': 72,
    'Jack': 60
}

# Convert to DataFrame
df = pd.DataFrame(list(students.items()), columns=['Name', 'Score'])

# Calculate mean and std
mean = df['Score'].mean()
std = df['Score'].std()

# Z-score calculation
df['Z-score'] = (df['Score'] - mean) / std

# Add percentile using CDF from Z-score
df['Percentile'] = df['Z-score'].apply(lambda z: round(norm.cdf(z) * 100, 2))

# Label outliers
df['Remark'] = df['Z-score'].apply(lambda z: 'Outlier' if abs(z) > 2 else 'Normal')

# Display the result with better formatting
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.precision', 2)

print("\n📊 Student Z-Score Report")
print("-" * 50)
print(df)
print("\n📝 Summary Statistics:")
print(f"Mean Score: {mean:.2f}")
print(f"Standard Deviation: {std:.2f}")
print("\nℹ️ Note: Outliers are marked where |Z-score| > 2")

# Optional: Plot the distribution
plt.figure(figsize=(10, 5))
sns.histplot(df['Score'], kde=True, bins=5)
plt.axvline(mean, color='r', linestyle='--', label=f'Mean: {mean:.1f}')
plt.title('Distribution of Student Scores')
plt.xlabel('Score')
plt.ylabel('Count')
plt.legend()
plt.grid(True)
plt.show()
