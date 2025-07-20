# 📊 Understanding Bernoulli Distribution

## 📘 What is Bernoulli Distribution?

A Bernoulli distribution models a single trial that has only two possible outcomes:
- ✅ Success (1) or 
- ❌ Failure (0)

### 🔹 Real-World Examples
- Toss a coin → Heads (1) or Tails (0)
- Email → Spam (1) or Not Spam (0)
- Pass exam → Yes (1) or No (0)

## 🧠 Key Properties

| Feature | Value |
|---------|-------|
| **Possible Outcomes** | 0 or 1 |
| **Parameter** | p = probability of success (1) |
| **Mean (μ)** | p |
| **Variance (σ²)** | p(1-p) |
| **Support** | x ∈ {0, 1} |

## 🧮 Probability Mass Function (PMF)

$$
P(X=x) = 
\begin{cases} 
p & \text{if } x = 1 \\
1-p & \text{if } x = 0
\end{cases}
$$

## 🧪 Practical Example

**Scenario:** Customer Purchase Probability
- Probability of customer buying: p = 0.3
- Therefore:
  - P(X=1) = 0.3 (customer buys)
  - P(X=0) = 0.7 (customer doesn't buy)

## 🐍 Python Implementation

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

# Parameters
p = 0.3  # probability of success

# Create Bernoulli distribution
dist = bernoulli(p)

# Calculate probabilities
print(f"P(X=1): {dist.pmf(1):.2f}")
print(f"P(X=0): {dist.pmf(0):.2f}")

# Generate samples
samples = dist.rvs(size=1000)

# Plot distribution
plt.figure(figsize=(8, 5))
plt.hist(samples, bins=[-0.5, 0.5, 1.5], density=True, 
         edgecolor='black', alpha=0.7)
plt.xticks([0, 1])
plt.xlabel('Outcome')
plt.ylabel('Probability')
plt.title(f'Bernoulli Distribution (p={p})')
plt.grid(axis='y', alpha=0.3)
plt.show()
```

### Output:
```
P(X=1): 0.30
P(X=0): 0.70
```

## 🌟 Applications in Data Science

| Use Case | Description |
|----------|-------------|
| **🎯 Binary Classification** | Predicting yes/no outcomes (spam detection, churn prediction) |
| **📊 A/B Testing** | Measuring binary user actions (click/don't click) |
| **🧪 Hypothesis Testing** | Modeling success/failure experiments |
| **🧠 Probabilistic Models** | Foundation for more complex distributions |

## 🔄 Relationship with Other Distributions

| Distribution | Description | Relationship to Bernoulli |
|--------------|-------------|---------------------------|
| **Binomial** | Counts successes in n trials | Sum of n Bernoulli trials |
| **Categorical** | Generalization to >2 outcomes | Bernoulli is special case with k=2 |
| **Geometric** | Count trials until first success | Models sequence of Bernoulli trials |

## 📊 Visualizing Bernoulli Distribution

```python
# Generate visualization
plt.figure(figsize=(10, 5))

# PMF plot
plt.subplot(1, 2, 1)
plt.bar([0, 1], [1-p, p], width=0.4, color='skyblue', 
        edgecolor='black')
plt.xticks([0, 1], ['Failure (0)', 'Success (1)'])
plt.ylabel('Probability')
plt.title(f'PMF (p={p})')

# CDF plot
plt.subplot(1, 2, 2)
plt.step([-1, 0, 1, 2], [0, 0, 1-p, 1], where='post', 
         linewidth=2)
plt.xticks([0, 1], ['0', '1'])
plt.yticks([0, 1-p, 1])
plt.grid(True, alpha=0.3)
plt.title(f'CDF (p={p})')

plt.tight_layout()
plt.show()
```

## 💡 Key Takeaways

1. **Binary Outcomes**
   - Models single yes/no, success/failure scenarios
   - Only two possible outcomes: 0 or 1

2. **Single Parameter**
   - Defined by p = P(X=1)
   - P(X=0) = 1 - p

3. **Moments**
   - Mean: E[X] = p
   - Variance: Var(X) = p(1-p)
   - Skewness: (1-2p)/√[p(1-p)]

4. **When to Use**
   - Modeling single binary events
   - Foundation for more complex models
   - Quick probability calculations for yes/no scenarios

## 📚 Further Reading
- [Bernoulli Distribution - Wikipedia](https://en.wikipedia.org/wiki/Bernoulli_distribution)
- [Understanding Probability Distributions in Data Science](https://towardsdatascience.com/understanding-bernoulli-and-binomial-distributions-f1ce5a263fba)
- [Probability Distributions in Machine Learning](https://www.analyticsvidhya.com/blog/2017/09/common-probability-distributions/)

## 🛠️ Practical Tips

1. **Parameter Estimation**
   - Estimate p from data: p̂ = (number of successes) / (total trials)

2. **Zero/One Inflation**
   - Watch for imbalanced classes (p very close to 0 or 1)
   - Consider techniques like SMOTE for classification tasks

3. **Modeling Extensions**
   - For multiple trials: Use Binomial distribution
   - For modeling probability p: Use Beta distribution (conjugate prior)
