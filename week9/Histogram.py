import matplotlib.pyplot as plt
import numpy as np

# 构造示例数据：假设样本服从正态分布，均值为 0，标准差为 1，共 1000 个数据点
np.random.seed(1)
data = np.random.normal(0, 1, 1000)

plt.figure(figsize=(6, 4))
plt.hist(data, bins=20, color='purple', alpha=0.7, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example: Normal Distribution')
plt.grid(True)
plt.show()


# 使用 np.random.normal 生成 1000 个服从均值 0、标准差 1 的正态分布数据点。
# 通过调整 bins 数量，可以控制每个区间的宽度，从而观察分布的形状（是否集中、是否有长尾等）。
# 该示例能快速展示数据在各区间的频次分布情况，判断数据的集中趋势、离散程度以及是否存在偏态。