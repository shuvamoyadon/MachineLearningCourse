# 📊 Normal Distribution Cheatsheet

## 🎯 1. What is Normal Distribution?

A normal distribution (also called Gaussian) is a bell-shaped curve that shows how data is spread around the mean (average).

- Most values are close to the mean
- Fewer values are very high or very low
- Perfectly symmetrical around the mean

## 🌟 2. Why is Normal Distribution Important?

| Reason | Why it matters |
|--------|---------------|
| ✅ Common in real life | Heights, test scores, weights, errors often follow normal distribution |
| ✅ Foundation for statistics | Many statistical methods assume normality |
| ✅ Used in ML models | Algorithms like Naive Bayes, Linear Regression assume normality for some variables |
| ✅ Central Limit Theorem | Says averages of many things become normal (even if raw data isn't) |

## 🧮 3. Normal Distribution Formula (PDF)

$$
f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \cdot e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

### Where:

| Symbol | Meaning |
|--------|---------|
| x | Value for which we calculate PDF |
| μ (mu) | Mean (center of the curve) |
| σ (sigma) | Standard deviation (spread of the curve) |
| π, e | Math constants (3.1415..., 2.718...) |

## 🛠️ 4. Parameters of Normal Distribution

| Parameter | Meaning | Effect |
|-----------|---------|--------|
| Mean (μ) | Average value | Shifts the curve left or right |
| Standard Deviation (σ) | Spread of data | Wider = flatter curve, Smaller = sharper peak |

## 📏 The 68-95-99.7 Rule (Empirical Rule)

### 1 Standard Deviation (σ) rule:

| Range | Approx. % of Data |
|-------|-------------------|
| μ ± 1σ | 68% |
| μ ± 2σ | 95% |
| μ ± 3σ | 99.7% |

### Visual Representation

```
<mean = μ>
     |---1σ---||---1σ---|
     |----68%----|
     |-----------95%-----------|
     |----------------99.7%----------------|
<----|---------|---------|---------|---------|----->
    μ-3σ     μ-2σ      μ-σ       μ       μ+σ     μ+2σ     μ+3σ
```

## 🧠 5. Intuition (Simple Way to Think)

Imagine students' scores in a math exam:

- Most score around the average (say 70%)
- Few score very high (95%+) or very low (40%-)
- If you plot the scores, you'll see a bell-shaped curve

🔔 **That's a normal distribution!**

## 📊 Example with Heights

- **Mean (μ)**: 170 cm
- **Standard Deviation (σ)**: 10 cm

This means:
- 68% of people are between 160cm and 180cm
- 95% are between 150cm and 190cm
- 99.7% are between 140cm and 200cm

## 💡 Key Takeaways

1. The curve is symmetric and bell-shaped
2. Mean = Median = Mode at the center
3. Total area under the curve = 1 (100% probability)
4. Never actually reaches zero on the x-axis
5. Described by just two parameters: mean (μ) and standard deviation (σ)
