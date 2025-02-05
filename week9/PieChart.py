import matplotlib.pyplot as plt

# 构造示例数据：比如一家公司四个产品在市场中的占比
labels = ['Product A', 'Product B', 'Product C', 'Product D']
sizes = [35, 25, 25, 15]  # 百分比或数量均可

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart Example: Product Market Share')
plt.show()

# sizes 列表中的数值可直接代表各类别的数量或比例。
# autopct 用于在扇区上显示百分比，startangle 控制饼图的起始角度。
# 适用于直观展示各部分在整体中所占的份额。