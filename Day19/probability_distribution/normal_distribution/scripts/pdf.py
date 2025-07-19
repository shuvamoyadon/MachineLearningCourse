import numpy as np
import matplotlib.pyplot as plt
import math

# 🧮 PDF formula (manual implementation)
def normal_pdf(x, mean, std_dev):
    exponent = math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))
    return (1 / (math.sqrt(2 * math.pi) * std_dev)) * exponent

# 🧠 Set mean and standard deviation
mean = 170   # average height in cm
std_dev = 10 # standard deviation

# 🎯 Choose a value to calculate PDF for
x_point = 180
pdf_value = normal_pdf(x_point, mean, std_dev)

print(f"PDF at x = {x_point}: {pdf_value:.4f}")

# 📊 Plot the PDF curve
x_values = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 100)
y_values = [normal_pdf(x, mean, std_dev) for x in x_values]

plt.plot(x_values, y_values, label="Normal PDF", color='blue')
plt.axvline(x_point, color='red', linestyle='--', label=f"x = {x_point}")
plt.scatter([x_point], [pdf_value], color='red')
plt.title("Normal Distribution PDF")
plt.xlabel("x (e.g. Height in cm)")
plt.ylabel("Probability Density")
plt.grid(True)
plt.legend()
plt.show()
