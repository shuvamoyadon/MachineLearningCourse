import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Mean and standard deviation
mu = 70
sigma = 10

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)

plt.plot(x, y, label='Normal Distribution')
plt.axvline(mu, color='red', linestyle='--', label='Mean')
plt.title('Normal Distribution Curve')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend()
plt.grid()
plt.show()
