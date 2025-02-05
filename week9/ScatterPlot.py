import matplotlib.pyplot as plt
import numpy as np

# 构造示例数据：假设有一组 x 随机分布在 [0, 50]，并让 y 大致与 x 呈正相关，同时加入噪声。
np.random.seed(0)  # 固定随机种子便于复现结果
x = np.linspace(0, 50, 50)
y = x + np.random.normal(0, 5, 50)  # 均值为 0、标准差为 5 的噪声

plt.figure(figsize=(6, 4))
plt.scatter(x, y, color='steelblue', alpha=0.7, edgecolors='k')
plt.xlabel('Feature X')
plt.ylabel('Feature Y')
plt.title('Scatter Plot Example: Relationship Between X and Y')
plt.grid(True)
plt.show()

# 通过 np.linspace 生成 0 到 50 之间的等间距点，作为自变量 x。
# y 值在 x 的基础上添加正态分布噪声，模拟出真实数据中常见的随机波动。
# 该示例可以帮助我们观察 X 和 Y 之间是否存在显著的线性相关。
