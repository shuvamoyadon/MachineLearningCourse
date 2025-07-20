# 📊 Normal Distribution: The Complete Guide

## 📘 What is Normal Distribution?

It's a bell-shaped curve that shows how values are spread around the average. Most values are close to the center, and fewer are far away.

## 🧠 Key Properties of Normal Distribution

| No. | Property | Simple Explanation | Example |
|-----|----------|-------------------|----------|
| 1️⃣ | Symmetrical | Left side = Right side | Scores of students: same shape above and below average |
| 2️⃣ | Mean = Median = Mode | All three are at the center of the curve | If average height is 170 cm, that's also the most common and middle value |
| 3️⃣ | Bell-shaped | High in the middle, low on the sides | Like a hill — most people score near 70, fewer at 90 or 40 |
| 4️⃣ | Total area = 1 | The entire curve represents 100% probability | All possible outcomes are inside the curve |
| 5️⃣ | Empirical Rule | 68%-95%-99.7% rule — shows how data is spread | See below 🔽 |
| 6️⃣ | Defined by μ and σ | Just 2 values: mean (μ) and std deviation (σ) control everything | μ = center, σ = spread |
| 7️⃣ | Tails extend to infinity | Curve never really touches the x-axis | No hard limit, but values far from the mean are rare |
| 8️⃣ | Unimodal | Only one peak (one most common value) | One main score students usually get |

## 📐 Empirical Rule (68-95-99.7 Rule)

| Range | What it means |
|-------|---------------|
| μ ± 1σ | ~68% of values are here |
| μ ± 2σ | ~95% of values are here |
| μ ± 3σ | ~99.7% of values are here |

📌 This helps quickly check how rare or common a value is.

## 🧮 Normal Distribution Formula (PDF)

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \cdot e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

### Where:
- **x**: Data point
- **μ (mu)**: Mean (average)
- **σ (sigma)**: Standard deviation
- **π (pi)**: 3.14159...
- **e**: 2.71828... (Euler's number)

## 📊 Real-World Example

**Heights of Adults (in cm):**
- Mean (μ) = 170 cm
- Standard Deviation (σ) = 10 cm

**What does this tell us?**
- 68% of people are between 160cm and 180cm
- 95% are between 150cm and 190cm
- 99.7% are between 140cm and 200cm

## 🖥️ Python Visualization

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Generate data
x = np.linspace(140, 200, 1000)
y = norm.pdf(x, 170, 10)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, 'b-')
plt.title('Normal Distribution (μ=170, σ=10)')
plt.xlabel('Height (cm)')
plt.ylabel('Probability Density')
plt.grid(True)
plt.show()
```

## 🎯 Summary

A normal distribution is a symmetric, bell-shaped curve centered around the mean, with data spreading based on standard deviation.

### Key Points:
- Described by just two parameters: mean (μ) and standard deviation (σ)
- Perfectly symmetrical around the mean
- Follows the 68-95-99.7 empirical rule
- Widely used in statistics, science, and machine learning

## 📚 When to Use Normal Distribution
- When data clusters around a central value
- For hypothesis testing
- In quality control processes
- When working with sample means (Central Limit Theorem)

## ⚠️ Limitations
- Not all data follows a normal distribution
- Can be misleading for skewed data
- Sensitive to outliers
