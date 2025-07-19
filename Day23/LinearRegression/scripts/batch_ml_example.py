import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import os
from datetime import datetime
import matplotlib.pyplot as plt

# Create output directories
os.makedirs('data', exist_ok=True)
os.makedirs('models', exist_ok=True)
os.makedirs('predictions', exist_ok=True)

def generate_sample_data(n_samples=1000):
    """Generate sample data for house price prediction"""
    np.random.seed(42)
    
    # Generate synthetic data
    size = np.random.normal(1500, 500, n_samples).astype(int)
    bedrooms = np.random.randint(1, 6, n_samples)
    age = np.random.randint(0, 50, n_samples)
    
    # Generate price based on features with some noise
    price = 50000 + 200 * size + 30000 * bedrooms - 1000 * age + np.random.normal(0, 10000, n_samples)
    
    # Create DataFrame
    data = pd.DataFrame({
        'size_sqft': size,
        'bedrooms': bedrooms,
        'age_years': age,
        'price': price
    })
    
    # Save to CSV
    data.to_csv('data/house_prices.csv', index=False)
    print(f"Generated {n_samples} samples in data/house_prices.csv")
    return data

def train_batch_model():
    """Train a model using batch processing"""
    print("\n=== Starting Batch Training ===")
    
    # Load data
    data = pd.read_csv('data/house_prices.csv')
    
    # Prepare features and target
    X = data[['size_sqft', 'bedrooms', 'age_years']]
    y = data['price']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Trained model with MSE: {mse:.2f}, R²: {r2:.4f}")
    
    # Save model with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    model_path = f'models/house_price_model_{timestamp}.joblib'
    joblib.dump(model, model_path)
    print(f"Model saved to {model_path}")
    
    # Plot feature importance
    plot_feature_importance(model, X_train.columns)
    
    return model_path

def make_predictions(model_path):
    """Make predictions using the trained model"""
    print("\n=== Making Predictions ===")
    
    # Load model
    model = joblib.load(model_path)
    
    # Generate new data for prediction
    new_data = pd.DataFrame({
        'size_sqft': [1200, 1800, 2200],
        'bedrooms': [2, 3, 4],
        'age_years': [5, 10, 2]
    })
    
    # Make predictions
    predictions = model.predict(new_data)
    
    # Create results DataFrame
    results = new_data.copy()
    results['predicted_price'] = predictions.round(2)
    
    # Save predictions
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    pred_path = f'predictions/predictions_{timestamp}.csv'
    results.to_csv(pred_path, index=False)
    
    print("Predictions made for new houses:")
    print(results)
    print(f"Predictions saved to {pred_path}")
    
    return results

def plot_feature_importance(model, feature_names):
    """Plot feature importance for the model"""
    if hasattr(model, 'coef_'):
        plt.figure(figsize=(10, 6))
        importance = pd.Series(model.coef_, index=feature_names)
        importance = importance.sort_values()
        importance.plot(kind='barh')
        plt.title('Feature Importance (Coefficients)', fontsize=14)
        plt.xlabel('Coefficient Value', fontsize=12)
        plt.ylabel('Features', fontsize=12)
        plt.tight_layout()
        
        # Save the plot
        plot_path = 'models/feature_importance.png'
        plt.savefig(plot_path)
        print(f"Feature importance plot saved to {plot_path}")
        plt.close()

if __name__ == "__main__":
    print("=== Batch Processing ML Example ===\n")
    
    # Step 1: Generate sample data (if not exists)
    if not os.path.exists('data/house_prices.csv'):
        generate_sample_data()
    
    # Step 2: Train model in batch
    model_path = train_batch_model()
    
    # Step 3: Make predictions
    predictions = make_predictions(model_path)
    
    print("\n=== Batch Processing Complete ===")
    print("Model trained and predictions made successfully!")
