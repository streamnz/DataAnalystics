import matplotlib.pyplot as plt

# 根据图片中提供的数据
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_scores = [50, 55, 65, 70, 72, 78, 85, 88, 92, 95]

# 绘制散点图
plt.scatter(study_hours, test_scores, color='blue', edgecolors='black')

# 添加坐标轴与标题
plt.xlabel('Study Hours')
plt.ylabel('Test Scores')
plt.title('Relationship between Study Hours and Test Scores')

# 可选：添加网格线，方便观察数据点分布
plt.grid(True)

# 显示图表
plt.show()
