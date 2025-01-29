import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = "House_Data.csv"
df = pd.read_csv(file_path)

# Record initial statistics
initial_rows = df.shape[0]
missing_before = df.isnull().sum()
duplicates_before = df.duplicated().sum()

# Handle missing values
df['size'].fillna("Unknown", inplace=True)
df['society'].fillna("Unknown", inplace=True)
df['bath'].fillna(df['bath'].median(), inplace=True)
df['balcony'].fillna(df['balcony'].median(), inplace=True)


# Convert total_sqft (handle range values by taking the average)
def convert_sqft(sqft):
    if '-' in str(sqft):
        values = sqft.split('-')
        return (float(values[0]) + float(values[1])) / 2
    try:
        return float(sqft)
    except ValueError:
        return np.nan


df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df.dropna(subset=['total_sqft'], inplace=True)  # Remove rows with invalid conversions

# Remove duplicate values
df.drop_duplicates(inplace=True)

# Record statistics after removing duplicates
duplicates_after = df.duplicated().sum()


# Detect and remove outliers using IQR method
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]


# Record the number of rows before outlier removal
outliers_before = df.shape[0]
df = remove_outliers(df, 'bath')
df = remove_outliers(df, 'price')
outliers_after = df.shape[0]

# Compute final statistics
final_rows = df.shape[0]
missing_after = df.isnull().sum()

# Save cleaned data
cleaned_file_path = "Cleaned_House_Data.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")

# === Display statistics ===
print("\nData Cleaning Summary:")
print(f"Initial number of rows: {initial_rows}")
print(f"Number of rows after removing duplicates: {duplicates_after}")
print(f"Number of rows after removing outliers: {outliers_after}")
print("\nMissing Values (Before vs After Cleaning):")
print(pd.DataFrame({'Before': missing_before, 'After': missing_after}))

# === Data Visualization ===
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# 1. Price Histogram
sns.histplot(df['price'], bins=30, kde=True, ax=axes[0, 0])
axes[0, 0].set_title("Distribution of Price (After Cleaning)")

# 2. Bath Boxplot
sns.boxplot(x=df['bath'], ax=axes[0, 1])
axes[0, 1].set_title("Boxplot of Bath (After Cleaning)")

# 3. Total Sqft Histogram
sns.histplot(df['total_sqft'], bins=30, kde=True, ax=axes[1, 0])
axes[1, 0].set_title("Distribution of Total Sqft (After Cleaning)")

# 4. Scatter plot: Total Sqft vs Price
sns.scatterplot(x=df['total_sqft'], y=df['price'], alpha=0.5, ax=axes[1, 1])
axes[1, 1].set_title("Total Sqft vs Price")

plt.tight_layout()
plt.show()
