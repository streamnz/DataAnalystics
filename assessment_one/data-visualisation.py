import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------
# 1. 构造（或读取）示例数据
# ---------------------------
# 下述数据与题目给出的6行水质数据、6行鱼群数据类似
water_data = {
    'SiteID': ['AV-1','AV-2','AV-3','AV-1','AV-2','AV-3'],
    'Date': ['2023-10-25','2023-10-25','2023-10-25',
             '2023-11-15','2023-11-15','2023-11-15'],
    'Temperature_C': [15.2, 14.8, 13.6, 12.4, 11.9, 10.8],
    'pH':             [7.8, 7.5, 7.3, 7.6, 7.4, 7.2],
    'DO_mgL':         [8.5, 7.9, 6.8, 8.2, 7.7, 6.2]  # 溶解氧
}

fish_data = {
    'SiteID': ['AV-1','AV-2','AV-3','AV-1','AV-2','AV-3'],
    'Date':   ['2023-10-25','2023-10-25','2023-10-25',
               '2023-11-15','2023-11-15','2023-11-15'],
    'Species': ['Brown Trout','Shortfin Eel','Freshwater Shrimp',
                'Rainbow Trout','Kokopu','No fish observed'],
    'Count':   [50, 75, 120, 35, 40, 0],
    'AvgSize_cm': [32, 45, 2, 28, 18, None]  # 无鱼时用 None
}

df_water = pd.DataFrame(water_data)
df_fish = pd.DataFrame(fish_data)

# 如果是CSV文件，可以用：
# df_water = pd.read_csv("water_quality.csv")
# df_fish = pd.read_csv("fish_population.csv")

# 把日期转成 datetime 格式，方便后续排序/分析
df_water['Date'] = pd.to_datetime(df_water['Date'])
df_fish['Date'] = pd.to_datetime(df_fish['Date'])

# ---------------------------
# 2. 生成时间序列折线图：溶解氧对比
# ---------------------------
plt.figure(figsize=(8,5))
sns.lineplot(data=df_water, x='Date', y='DO_mgL', hue='SiteID', marker='o')
plt.title("Time-series of Dissolved Oxygen at Different Sites")
plt.xlabel("Date")
plt.ylabel("Dissolved Oxygen (mg/L)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("time_series_DO.png", dpi=300)  # 保存图片
plt.show()

# ---------------------------
# 3. 生成柱状图：比较不同站点在同一天的鱼群数量
# ---------------------------
# 示例：只对 2023-11-15 数据进行对比
df_fish_1115 = df_fish[df_fish['Date'] == pd.to_datetime("2023-11-15")]

plt.figure(figsize=(6,4))
sns.barplot(data=df_fish_1115, x='SiteID', y='Count', hue='Species')
plt.title("Fish Count by Site on 2023-11-15")
plt.xlabel("Site ID")
plt.ylabel("Count of Fish")
plt.legend(title='Species', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("fish_count_bar.png", dpi=300)
plt.show()

# ---------------------------
# 4. （可选）生成热力图：查看相关性
# ---------------------------
# 为了做相关分析，需要把水质与鱼类信息合并(相同站点+日期)
df_merged = pd.merge(df_water, df_fish, on=["SiteID","Date"], how="inner")

# 一些指标可能为 None，需要先去掉空值
df_merged_clean = df_merged.dropna(subset=["AvgSize_cm"])

# 选取数值型列来做相关分析
cols_for_corr = ["Temperature_C", "pH", "DO_mgL", "Count", "AvgSize_cm"]
corr_matrix = df_merged_clean[cols_for_corr].corr()

plt.figure(figsize=(6,5))
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Correlation Heatmap among Water Quality & Fish Metrics")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", dpi=300)
plt.show()
