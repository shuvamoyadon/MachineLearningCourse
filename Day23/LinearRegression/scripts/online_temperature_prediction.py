#!/usr/bin/env python3
"""
Simple Online Learning for Temperature Prediction
-----------------------------------------------
A minimal implementation of online learning for temperature prediction.
This version uses a simple moving average approach for stability.
"""
import numpy as np
import matplotlib.pyplot as plt

def generate_temperature_data(days=30, noise=1.0):
    """Generate temperature data with a weekly pattern."""
    np.random.seed(42)
    x = np.arange(days)
    # Create a simple pattern with weekly seasonality
    y = 20 + 2 * np.sin(2 * np.pi * x / 7) + np.random.normal(0, noise, days)
    return x, y

def main():
    print("Simple Online Learning for Temperature Prediction\n")
    
    # Generate data
    days = 30
    x, temperatures = generate_temperature_data(days=days, noise=0.5)
    
    # Initialize prediction (start with the first temperature)
    predictions = np.zeros(days)
    predictions[0] = temperatures[0]
    
    # Simple online learning parameters
    alpha = 0.3  # Learning rate for the moving average
    
    print(f"{'Day':>4} {'Actual':>8} {'Predicted':>10} "
          f"{'Error':>10} {'MAE':>10}")
    print("-" * 60)
    
    # Track errors
    abs_errors = []
    
    # Online learning loop
    for i in range(1, days):
        # Simple prediction: weighted average of previous prediction and actual
        predictions[i] = alpha * temperatures[i-1] + (1 - alpha) * predictions[i-1]
        
        # Calculate error
        error = predictions[i] - temperatures[i]
        abs_error = abs(error)
        abs_errors.append(abs_error)
        mae = np.mean(abs_errors) if abs_errors else 0
        
        # Print progress
        if i % 5 == 0 or i == 1 or i == days-1:
            print(f"{i:4d} {temperatures[i]:8.2f}°C {predictions[i]:9.2f}°C "
                  f"{error:9.2f}°C {mae:9.2f}°C")
    
    # Calculate final metrics
    mae = np.mean(abs_errors)
    
    # Plot results
    plt.figure(figsize=(12, 6))
    
    # Plot actual vs predicted temperatures
    plt.plot(x, temperatures, 'b-', label='Actual', linewidth=2)
    plt.plot(x, predictions, 'r--', label='Predicted', linewidth=2)
    
    plt.title(f'Simple Online Temperature Prediction (MAE: {mae:.2f}°C)')
    plt.xlabel('Day')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.grid(True)
    
    # Add model info
    plt.figtext(0.5, 0.01, 
               f"Using exponential moving average with α = {alpha}",
               ha="center", fontsize=10, style='italic')
    
    # Save the plot
    plot_path = 'simple_temperature_prediction.png'
    plt.tight_layout()
    plt.savefig(plot_path)
    print(f"\nResults saved to {plot_path}")
    
    print("\nModel performance:")
    print(f"Mean Absolute Error: {mae:.2f}°C")
    print(f"Final prediction: {predictions[-1]:.2f}°C (Actual: {temperatures[-1]:.2f}°C)")

if __name__ == "__main__":
    main()
