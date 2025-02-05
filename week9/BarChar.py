import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 1, 8]

# 为每个柱条设置不同的颜色
colors = ['red', 'green', 'blue', 'orange']

plt.bar(categories, values, color=colors)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.show()
