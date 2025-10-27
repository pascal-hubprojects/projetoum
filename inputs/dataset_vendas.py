import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate date range for 3 years
start_date = datetime(2021, 1, 1)
end_date = datetime(2023, 12, 31)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Define constants
cone_sizes = ['Small', 'Medium', 'Large']
flavors = ['Chocolate', 'Strawberry']

# Rio de Janeiro temperature patterns (approximate)
# Summer: Dec-Feb (hot), Winter: Jun-Aug (milder but still warm)
def generate_rio_temperature(date):
    base_temp = 25  # Base temperature in Celsius
    seasonal_variation = 5 * np.sin(2 * np.pi * (date.timetuple().tm_yday - 80) / 365)
    
    # Rio has warm winters, so less seasonal variation than other places
    daily_variation = np.random.normal(0, 2)
    
    temp = base_temp + seasonal_variation + daily_variation
    return max(15, min(40, temp))  # Keep within realistic bounds

# Generate base sales pattern
def generate_daily_sales(date, temperature):
    # Base sales rate
    base_sales = 100
    
    # Weekend effect (higher sales)
    weekday = date.weekday()
    weekend_boost = 1.5 if weekday >= 5 else 1.0
    
    # Seasonal effect (higher in summer)
    month = date.month
    seasonal_boost = 1.3 if month in [12, 1, 2] else (1.1 if month in [3, 4, 11] else 1.0)
    
    # Temperature effect (quadratic - optimal around 30°C)
    temp_effect = -0.01 * (temperature - 30)**2 + 1.2
    
    # Holiday effects (Carnival, New Year, etc.)
    is_holiday = 0
    # Carnival (approximate dates)
    carnival_period = (date.month == 2 and date.day >= 10 and date.day <= 20) or \
                     (date.month == 3 and date.day <= 5)
    # New Year
    new_year_period = (date.month == 12 and date.day >= 20) or \
                     (date.month == 1 and date.day <= 5)
    
    holiday_boost = 2.0 if carnival_period or new_year_period else 1.0
    
    # Random variation
    random_variation = np.random.normal(1, 0.2)
    
    total_sales = base_sales * weekend_boost * seasonal_boost * temp_effect * holiday_boost * random_variation
    
    return max(20, total_sales)  # Ensure minimum sales

# Generate the dataset
records = []
current_date = start_date

while current_date <= end_date:
    temperature = generate_rio_temperature(current_date)
    daily_total_sales = generate_daily_sales(current_date, temperature)
    
    # Distribute sales across cone sizes and flavors
    size_distribution = {'Small': 0.4, 'Medium': 0.35, 'Large': 0.25}
    flavor_distribution = {'Chocolate': 0.55, 'Strawberry': 0.45}
    
    for size in cone_sizes:
        for flavor in flavors:
            # Calculate sales for this combination
            size_ratio = size_distribution[size]
            flavor_ratio = flavor_distribution[flavor]
            
            # Temperature affects size preference (hotter days = more large cones)
            if temperature > 30:
                size_adjustment = {'Small': 0.9, 'Medium': 1.0, 'Large': 1.2}
            else:
                size_adjustment = {'Small': 1.1, 'Medium': 1.0, 'Large': 0.9}
            
            adjusted_size_ratio = size_ratio * size_adjustment[size]
            
            # Normalize ratios
            total_ratio = sum(size_distribution[s] * size_adjustment[s] for s in cone_sizes)
            normalized_ratio = (adjusted_size_ratio / total_ratio) * flavor_ratio
            
            sales = int(daily_total_sales * normalized_ratio + np.random.normal(0, 2))
            sales = max(0, sales)  # Ensure non-negative sales
            
            records.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'day_of_week': current_date.strftime('%A'),
                'is_weekend': 1 if current_date.weekday() >= 5 else 0,
                'cone_size': size,
                'flavor': flavor,
                'temperature': round(temperature, 1),
                'daily_sales': sales
            })
    
    current_date += timedelta(days=1)

# Create DataFrame
df = pd.DataFrame(records)

# Add some missing data patterns (realistic for retail)
# Randomly set 2% of records to 0 sales (could represent stockouts, etc.)
missing_mask = np.random.random(len(df)) < 0.02
df.loc[missing_mask, 'daily_sales'] = 0

# Save to CSV
df.to_csv('rio_ice_cream_sales.csv', index=False)

# Print some summary statistics
print("Dataset created successfully!")
print(f"Total records: {len(df)}")
print(f"Date range: {df['date'].min()} to {df['date'].max()}")
print(f"Total sales: {df['daily_sales'].sum():,}")
print("\nSales by cone size:")
print(df.groupby('cone_size')['daily_sales'].sum())
print("\nSales by flavor:")
print(df.groupby('flavor')['daily_sales'].sum())
print("\nAverage temperature:", round(df['temperature'].mean(), 1), "°C")

# Correlation analysis
print("\nCorrelation matrix:")
correlation_matrix = df[['temperature', 'daily_sales', 'is_weekend']].corr()
print(correlation_matrix)
