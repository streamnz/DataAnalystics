import pandas as pd
from sklearn import datasets

# 加载 iris 数据集
iris = datasets.load_iris()

# 将 Bunch 格式转换为 Pandas DataFrame
iris_df = pd.DataFrame(iris.data)
iris_df['class'] = iris.target

# 为列重新命名
iris_df.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']

#### ===> TASK 1: 这里可以再补充两行代码来查看缺失值数量并计算缺失值的均值
# 下面这行示例是清除全空行（仅供参考）
iris_df.dropna(how="all", inplace=True)  # 删除所有值均为空的行

# 从前五行数据中取出指定列，示例这里是列索引0,1,2,3
iris_X = iris_df.iloc[:5, [0, 1, 2, 3]]
print(iris_X)

### TASK 2: 可在此撰写 README，解释上述代码如何运作，并介绍如何计算各特征间的相关系数等。
