import matplotlib.pyplot as plt

# 数据：100 名学生喜欢的水果分布
fruits = ["Apple", "Banana", "Grape", "Orange"]
sizes = [30, 25, 20, 25]    # 分别代表每种水果对应的人数
colors = ["red", "yellow", "purple", "orange"]  # 为不同水果设置不同颜色

# 生成饼图
plt.figure(figsize=(6,6))
plt.pie(
    sizes,
    labels=fruits,
    colors=colors,
    autopct='%1.1f%%',  # 在扇区上显示百分比
    startangle=140      # 起始角度，可根据需求调整
)

plt.title("Favorite Fruits of 100 Students")

# axis('equal') 使饼图在视觉上呈现正圆形
plt.axis('equal')
plt.show()

# 可选：在控制台打印与活动相关的说明
print("Activity:")
print("这幅饼图展示了 100 名学生最喜欢的水果分布。")
print("30% 喜欢苹果（Apple），25% 喜欢香蕉（Banana），20% 喜欢葡萄（Grape），其余 25% 喜欢橙子（Orange）。")
print("问题：有多少学生喜欢橙子？答案：25 名，占 25%。")
