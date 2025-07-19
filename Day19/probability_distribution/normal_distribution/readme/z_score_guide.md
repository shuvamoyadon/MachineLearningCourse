# 📊 Understanding Z-Scores: A Complete Guide

## 🎯 What is a Z-Score?

A Z-score (or standard score) measures how many standard deviations a data point is from the mean. It's a way to standardize values from different normal distributions.

```
z = (x - μ) / σ
```

## 📋 Key Concepts

### 1. Z-Score Formula

$$
z = \frac{x - \mu}{\sigma}
$$

| Symbol | Meaning |
|--------|---------|
| x      | Individual data point |
| μ (mu) | Mean of the data |
| σ (sigma) | Standard deviation |
| z      | Z-score |

### 2. Interpretation
- **z = 0**: Value is exactly at the mean
- **z = +1**: 1 standard deviation above the mean
- **z = -1**: 1 standard deviation below the mean
- **|z| > 2**: Typically considered unusual (potential outlier)

## 📈 The Standard Normal Distribution

- Mean (μ) = 0
- Standard Deviation (σ) = 1
- Total area under the curve = 1 (100% probability)

## 📊 Empirical Rule (68-95-99.7 Rule)

| Range | % of Data | Z-Score Range |
|-------|-----------|---------------|
| μ ± 1σ | ~68% | -1 to 1 |
| μ ± 2σ | ~95% | -2 to 2 |
| μ ± 3σ | ~99.7% | -3 to 3 |

## 📚 Z-Table Reference

| Z-Score | Area to Left | % Below |
|---------|--------------|---------|
| -3.0 | 0.0013 | 0.13% |
| -2.0 | 0.0228 | 2.28% |
| -1.0 | 0.1587 | 15.87% |
| 0.0 | 0.5000 | 50.00% |
| 1.0 | 0.8413 | 84.13% |
| 2.0 | 0.9772 | 97.72% |
| 3.0 | 0.9987 | 99.87% |

## 🧮 Practical Example

You scored 85 on a test where:
- Mean (μ) = 70
- Standard Deviation (σ) = 10

**Calculation:**
```
z = (85 - 70) / 10 = 1.5
```

**Interpretation:**
- Your score is 1.5 standard deviations above the mean
- From Z-table: 0.9332 or 93.32% of scores are below yours
- You scored better than ~93% of test takers! 🎉

## 💻 Python Implementation

```python
import numpy as np
from scipy import stats

# Calculate z-score
def calculate_z_score(value, mean, std_dev):
    return (value - mean) / std_dev

# Example usage
score = 85
mean = 70
std_dev = 10

z = calculate_z_score(score, mean, std_dev)
percentile = stats.norm.cdf(z) * 100

print(f"Z-score: {z:.2f}")
print(f"Percentile: {percentile:.2f}%")
```

## 🚨 Common Use Cases

1. **Outlier Detection**
   - Values with |z| > 3 are often considered outliers

2. **Test Scoring**
   - Compare performance across different tests
   - Standardize scores from different distributions

3. **Quality Control**
   - Monitor process variations
   - Identify defects in manufacturing

4. **Machine Learning**
   - Feature scaling
   - Data normalization

## 📝 When to Use Z-Scores

- Your data is normally distributed
- You know the population mean and standard deviation
- You need to compare data from different scales

## ⚠️ Limitations

- Not suitable for non-normal distributions
- Sensitive to outliers when calculating mean and SD
- Requires knowledge of population parameters

## 📚 Additional Resources

1. [Khan Academy: Z-scores](https://www.khanacademy.org/math/statistics-probability/modeling-distributions-of-data/z-scores/a/z-scores-review)
2. [Stat Trek: Z-Score Table](https://stattrek.com/statistics/tables/z-table.aspx)
3. [Towards Data Science: Understanding Z-scores](https://towardsdatascience.com/understanding-z-scores-26f5bc9f06d0)
