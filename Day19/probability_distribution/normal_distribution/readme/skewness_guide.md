# 📊 Understanding Skewness in Data Distributions

## 📘 What is Skewness?

Skewness measures how asymmetric a distribution is around its mean.
- If data is perfectly symmetric, skewness = 0
- If data is tilted left or right, skewness ≠ 0

## 📈 Types of Skewness

| Type | Description | Shape | Real Example |
|------|-------------|-------|--------------|
| **Zero Skew (Symmetric)** | Mean ≈ Median ≈ Mode | Bell-shaped | Heights of people |
| **Positive Skew (Right-skewed)** | Tail is long on the right | Mean > Median | Income (a few earn a lot) |
| **Negative Skew (Left-skewed)** | Tail is long on the left | Mean < Median | Age at retirement (most retire around 60, few retire early) |

## 📊 Visual Representation

```
Negative Skew:     Symmetric:        Positive Skew:
    ▃▆███▇▃             ▃▅██▅▃              ▃▂▃▅██▇▇
       ◀︎                 │                   ▶︎
     Left tail          Center            Right tail
```

## 🧮 Measuring Skewness

### Formula (Pearson's Moment Coefficient of Skewness)

$$
\text{Skewness} = \frac{n}{(n-1)(n-2)} \sum \left(\frac{x_i - \bar{x}}{s}\right)^3
$$

Where:
- $n$ = number of observations
- $x_i$ = each value
- $\bar{x}$ = sample mean
- $s$ = sample standard deviation

### Python Implementation

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = [10, 20, 25, 30, 60, 90, 300]  # Right-skewed data

# Calculate skewness
skewness = pd.Series(data).skew()
print(f"Skewness: {skewness:.4f}")

# Visualize distribution
plt.figure(figsize=(10, 5))
sns.histplot(data, kde=True)
plt.title(f'Distribution (Skewness = {skewness:.2f})')
plt.axvline(np.mean(data), color='r', linestyle='--', label=f'Mean: {np.mean(data):.1f}')
plt.axvline(np.median(data), color='g', linestyle='-', label=f'Median: {np.median(data):.1f}')
plt.legend()
plt.show()
```

## 🌟 Why Skewness Matters in Data Science

| Use Case | Importance |
|----------|------------|
| **🔍 EDA (Exploratory Data Analysis)** | Identifies non-normal distributions |
| **⚠️ Outlier Detection** | High skewness may indicate outliers |
| **🧠 Machine Learning** | Many models assume normal distribution |
| **📊 Statistical Testing** | Affects test validity (e.g., t-tests, ANOVA) |
| **📈 Data Transformation** | Guides choice of normalization techniques |

## 🔧 Fixing Skewness

### Common Transformations

| Transformation | Formula | Best For |
|----------------|---------|-----------|
| **Logarithmic** | log(x) | Right-skewed data (x > 0) |
| **Square Root** | √x | Mild right skew (x ≥ 0) |
| **Reciprocal** | 1/x | Strong right skew (x ≠ 0) |
| **Square** | x² | Left-skewed data |
| **Box-Cox** | Special formula | Various skewness types |

### Example: Log Transformation

```python
# Apply log transformation to right-skewed data
transformed_data = np.log1p(data)  # log(1+x) to handle zeros
print(f"Original Skewness: {pd.Series(data).skew():.4f}")
print(f"Transformed Skewness: {pd.Series(transformed_data).skew():.4f}")
```

## 📊 Real-World Examples

### 1. Income Distribution (Right-Skewed)
- Most people earn around average, few earn significantly more
- Mean > Median
- Common transformation: log(income)

### 2. Age at Retirement (Left-Skewed)
- Most people retire around 60-65
- Few retire very early
- Mean < Median

### 3. Test Scores (Symmetric)
- Most scores around average
- Equal number of high and low scores
- Mean ≈ Median

## 💡 Key Takeaways

1. **Skewness Value**
   - 0: Symmetric distribution
   - > 0: Right-skewed (tail on right)
   - < 0: Left-skewed (tail on left)

2. **Impact on Analysis**
   - Affects statistical tests
   - Influences model performance
   - May require data transformation

3. **When to Transform**
   - When |skewness| > 1 indicates substantial skew
   - When using models that assume normality
   - When outliers are affecting analysis

## 🛠️ Practical Tips

1. Always visualize your data before and after transformation
2. Consider the nature of your data before applying transformations
3. Document all transformations for reproducibility
4. Check for outliers that might be causing skewness
5. Consider using robust statistical methods for highly skewed data

## 📚 Further Reading
- [Understanding Skewness in Data Science](https://towardsdatascience.com/skewed-data-a-problem-to-your-statistical-model-9a6b4bb2477d)
- [Data Transformation Techniques](https://www.analyticsvidhya.com/blog/2020/07/types-of-skewness-distribution-of-data/)
- [Handling Skewed Data in Machine Learning](https://medium.com/analytics-vidhya/transforming-skewed-data-73da4c2d0d16)
