import matplotlib.pyplot as plt
import numpy as np

# 构造示例数据：假设有三组测量数据，每组 50 个观测值
np.random.seed(2)
group1 = np.random.normal(50, 5, 50)   # 组1，均值50，标准差5
group2 = np.random.normal(55, 10, 50)  # 组2，均值55，标准差10
group3 = np.random.normal(60, 8, 50)   # 组3，均值60，标准差8

data = [group1, group2, group3]
labels = ['Group 1', 'Group 2', 'Group 3']

plt.figure(figsize=(6, 4))
plt.boxplot(data, labels=labels, patch_artist=True,
            boxprops=dict(facecolor='lightblue', color='blue'),
            medianprops=dict(color='red'))
plt.ylabel('Observed Values')
plt.title('Box Plot Example: Comparison Among Three Groups')
plt.grid(True, axis='y')
plt.show()

# 这里构造了三组服从正态分布但均值和标准差不同的虚拟数据，用以模拟在不同实验条件或分组下测量的结果。
# 箱线图能展示每组数据的中位数（红线）、上下四分位数所在的“箱体”以及离群点（在箱体外的圆点）。
# 可以直观比较三组数据在位置（中位数）和离散程度（箱体大小、须状线长度）上的差异