import pandas as pd
import numpy as np

# 读取数据
file_path = "House_Data.csv"
df = pd.read_csv(file_path)

# 处理缺失值
df['size'].fillna("Unknown", inplace=True)
df['society'].fillna("Unknown", inplace=True)
df['bath'].fillna(df['bath'].median(), inplace=True)
df['balcony'].fillna(df['balcony'].median(), inplace=True)

# 处理 total_sqft (范围数据转换为均值)
def convert_sqft(sqft):
    if '-' in str(sqft):
        values = sqft.split('-')
        return (float(values[0]) + float(values[1])) / 2
    try:
        return float(sqft)
    except ValueError:
        return np.nan

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df.dropna(subset=['total_sqft'], inplace=True)  # 移除转换失败的行

# 删除重复值
df.drop_duplicates(inplace=True)

# 使用IQR方法检测并删除异常值
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]

df = remove_outliers(df, 'bath')
df = remove_outliers(df, 'price')

# 保存清理后的数据
cleaned_file_path = "Cleaned_House_Data.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"清理后的数据已保存到 {cleaned_file_path}")
