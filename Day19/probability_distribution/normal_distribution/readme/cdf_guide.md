# 📊 Understanding CDF: The Complete Guide

## 📘 What is CDF?

The Cumulative Distribution Function (CDF) tells you the probability that a random variable takes a value less than or equal to a specific number in a distribution.

### 🔍 In Simple Terms
- **PDF** tells you "How dense is the value at x?"
- **CDF** tells you "How much of the data is less than or equal to x?"

### ✅ Example
If your CDF at x = 85 is 0.93, it means:
- 93% of values are below 85
- You're in the 93rd percentile

## 🧮 CDF Formula for Normal Distribution

$$
F(x) = P(X \leq x) = \frac{1}{2} \left[1 + \text{erf}\left(\frac{x-\mu}{\sigma\sqrt{2}}\right)\right]
$$

### Where:
| Symbol | Meaning |
|--------|---------|
| x | The value you're checking |
| μ (mu) | Mean of the distribution |
| σ (sigma) | Standard deviation |
| erf() | Error function (built into most math libraries) |

## 🐍 Python Implementation

```python
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

# Parameters
mu = 70      # mean
sigma = 10   # standard deviation

# Calculate CDF at a specific point
x = 85
cdf_value = norm.cdf(x, loc=mu, scale=sigma)
print(f"CDF at x = {x}: {cdf_value:.4f} (or {cdf_value*100:.1f}%)")

# Generate data for plotting
x_values = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
cdf_values = norm.cdf(x_values, loc=mu, scale=sigma)

# Plot CDF
plt.figure(figsize=(10, 5))
plt.plot(x_values, cdf_values, 'b-', label='CDF')
plt.axvline(x, color='r', linestyle='--', label=f'x = {x}')
plt.axhline(cdf_value, color='g', linestyle=':', label=f'CDF = {cdf_value:.2f}')
plt.title('Cumulative Distribution Function (CDF)')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.legend()
plt.grid(True)
plt.show()
```

## 📈 Visual Explanation
- CDF is an S-shaped curve that starts at 0 and approaches 1
- The curve is steepest around the mean
- The total area under the PDF curve to the left of x equals the CDF at x

## ✅ CDF Properties

| Property | Meaning |
|----------|---------|
| Always increases | Never decreases as x increases |
| Range | Always between 0 and 1 |
| At x → -∞ | CDF(x) = 0 |
| At x → +∞ | CDF(x) = 1 |
| At x = μ | CDF(μ) = 0.5 (for symmetric distributions) |

## 🔄 CDF vs PDF: Key Differences

| Feature | PDF | CDF |
|---------|-----|-----|
| Shape | Bell curve | S-curve |
| Value at x | Density | Cumulative probability |
| Area under curve | 1 | Not applicable |
| Use cases | Finding most likely values | Finding percentiles, probabilities |
| Relationship | PDF is the derivative of CDF | CDF is the integral of PDF |

## 🎯 Practical Applications

### 1. Percentile Calculation
```python
# Find the 90th percentile
percentile_90 = norm.ppf(0.90, loc=mu, scale=sigma)
print(f"90th percentile: {percentile_90:.2f}")
```

### 2. Probability Between Two Values
```python
# Probability between 60 and 80
prob = norm.cdf(80, mu, sigma) - norm.cdf(60, mu, sigma)
print(f"Probability between 60 and 80: {prob*100:.1f}%")
```

### 3. Finding Thresholds
```python
# Find the value below which 95% of data falls
threshold = norm.ppf(0.95, loc=mu, scale=sigma)
print(f"95% of values are below: {threshold:.2f}")
```

## 📊 Real-World Use Cases

| Industry | Application | Example |
|----------|-------------|---------|
| 🎓 Education | Test scoring | What percentage of students scored below 85? |
| 💼 Finance | Risk assessment | What's the probability of stock price falling below $50? |
| 🏭 Manufacturing | Quality control | What percentage of products meet specifications? |
| 🏥 Healthcare | Medical tests | What's the normal range for blood pressure? |
| 📈 Data Science | Anomaly detection | Is this data point in the top 1%? |

## 💡 Pro Tips
1. Use `scipy.stats.norm.cdf()` for normal distributions
2. For the inverse (percentile to value), use `scipy.stats.norm.ppf()`
3. Remember: CDF gives P(X ≤ x), so for P(X > x) use 1 - CDF(x)
4. The median is the 50th percentile: `median = norm.ppf(0.5, mu, sigma)`

## ⚠️ Common Pitfalls
1. Don't confuse CDF with PDF - they provide different information
2. Ensure your data is normally distributed before using normal CDF
3. Be careful with discrete vs continuous distributions
4. Remember that CDF is always non-decreasing
