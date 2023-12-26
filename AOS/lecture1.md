### C1


$$
\mathbb{P}(A | B) = \frac{\mathbb{P}(AB)}{\mathbb{P}(B)}
$$

$$
P(AB)=P(A|B)P(B)=P(B|A)P(A)
$$



对任意概率，都有：
$$
P(A+B)=P(A\cup B)=P(A)+P(B)-P(AB)\\
P(A-B)=P(A\cup B^c)=P(A)-P(AB)
$$




Bayes
$$
\mathbb{P}(A_i | B) = \frac{\mathbb{P}(A_i B) }{\mathbb{P}(B)} = \frac{\mathbb{P}(B | A_i) \mathbb{P}(A_i)}{\mathbb{P}(B)} = \frac{\mathbb{P}(B | A_i) \mathbb{P}(A_i)}{\sum_j \mathbb{P}(B | A_j) \mathbb{P}(A_j)}
$$
$$ P(A_i) 先验概率, P(A_i|B) A的后验概率 $$

德摩根定律 取逆交并改
$$
P(AB)=P(A)P(B) \\
A\quad set\quad of\quad events\quad \{A_i \in I \} is\quad independent\quad if\\
P( \bigcap_{i\in J} A_i) = \prod_{i\in J}P(A_i)
$$

全概率公式：

知道原因推结果

贝叶斯：

知道结果推原因

一个人发烧，那他是什么原因发烧的可能性最大

P(A)>0 P(B) >0,独立与互不相容不能同时成立
$$
P(ABC)=P(A)P(B|A)P(C|BA)
$$

### C2

定义

随机变量=映射，对每一个w赋予X(w)

分布函数=累积分布函数=CDF：表示函数$F_x:R\rightarrow [0,1]$，定义为：
$$
F_X(x)=P(X\leq x)
$$
CDF 完全决定了随机变量的分布

P：概率测度

X：随机变量

f：概率密度函数 PDF

F：分布函数 CDF

F逆：CDF的逆函数，分位数函数


$$
样本方差=
\frac{1}{n-1}\sum_{1}^{n}(X-\bar{X})^2
$$
只有n-1个样本提供了信息

样本分布函数=eCDF=EDF=经验累计分布函数=经验分布函数



离散随机变量

单点分布

均匀分布

伯努利分布

二项式分布

几何分布

泊松分布

连续随机变量

均匀分布

正态分布=高斯分布

指数分布

贝塔分布

t分布和柯西分布



二元分布

联合密度函数

边际分布

条件分布



独立同分布



# 机器学习



## 数据读取

### pandas

```python
# 创建一个data变量存储数据
data = pd.read_csv('StudentPerformance.csv')
# 展示一下数据
print(data)
# 获取首行（标签）名称
labels = list(data.columns.values)
print(labels)
 
# 查看数据特征
print(data.dtypes)
 
# 列名
print(data.columns)
 
# 索引
print(data.index)
 
#查看特征空值信息，以及数据类型
print(data.info(verbose=True))
 
#输出数据集前n个样本，默认n=5
print(data.head(n=5))
# 列名
print(df.columns)
# 索引
print(df.index)
```



### numpy

```python
b = np.loadtxt("temp.csv", delimiter=",")
print(b)                   #打印b数组
print(max(b.reshape(-1)))  #打印b数组中的最大值
print(min(b.reshape(-1)))  #打印b数组中的最小值
import numpy as np
 
a = np.arange(0,10000).reshape(100,100)
np.savetxt("temp.csv", a, delimiter=",")


import numpy as np
a1 = np.arange(10)
# 1.1 进行索引操作
print(a1[4]) # 4
# 1.2 进行切片操作
print(a1[4:6])# [4 5]
# 1.3 使用步长
print(a1[::2])# [0 2 4 6 8]
# 1.4 使用负数来作为索引
print(a1[-1]) # 9


import numpy as np
a2 = np.random.randint(0,10,size=(4,6))
print(a2)

print(a2[0])

print(a2[1:3])

print(a2[[0,2,3]]) # 获取不连续的几行的数据

print(a2[[1,3],[4,4]]) # 花式索引,(1,4)第1行4列，(3,4)3行4列，注意行和列的索引都是从0开始
a2[,[0]]取列
print(a2[1:3,4:6]) # 取1-2行，4-5列之间
'''
[[4 2 0 2 4 0]
 [9 5 5 5 7 9]
 [2 6 3 0 1 6]
 [3 6 9 0 5 4]]
**********
[4 2 0 2 4 0]
**********
[[9 5 5 5 7 9]
 [2 6 3 0 1 6]]
**********
[[4 2 0 2 4 0]
 [2 6 3 0 1 6]
 [3 6 9 0 5 4]]
--------------------
[7 5]
--------------------
[[7 9]
 [1 6]]
'''



```

### reshape

```python
①若是a.reshape(x, -1)则是将矩阵a变成行数为x，列数不规定的矩阵，具体列数按照总元素个数除行数，均分得到。
②若是a.reshape(-1, x)则是将矩阵a变成列数为x，行数不规定的矩阵，具体行数按照总元素个数除列数，均分得到。
```



数据清洗

MaxMinScaler



测试集与验证集

np.shuffle

k折法



## 线性回归

### 最小二乘法 least square

- 给定一组数据点$(t1,y1),⋯,(tm,ym)$。
- （1）选择模型，确定用于拟合数据的参数模型，例如 $ y=c1+c2t$ 
- （2）利用模型拟合数据，将数据点代入模型，得到系统 $Ax=b$
- （3）求解法线方程 $A^TA \bar{x}=A^Tb$A^TA\bar x=A^TbA^TA\bar x=A^Tb 的解

在MATLAB中提供了polyfit和polyval命令

 

```python
from sympy import symbols, diff, solve
import numpy as np

# 数据集 D
X = np.array([1.51, 1.64, 1.6, 1.73, 1.82, 1.87])
y = np.array([1.63, 1.7, 1.71, 1.72, 1.76, 1.86])

# 构造经验误差函数
w, b = symbols('w b', real=True)
RDh = 0
for (xi, yi) in zip(X, y):
	RDh += (yi - (xi*w + b))**2
RDh *= 1/len(X)

# 对 w 和 b 求偏导
eRDhw = diff(RDh, w)
eRDhb = diff(RDh, b)

# 求解方程组
ans = solve((eRDhw, eRDhb), (w, b))
print('使得经验误差函数 RD(h) 取最小值的参数为：{}'.format(ans))
```





## 损失函数





## 激活函数