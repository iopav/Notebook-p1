

## L1



## L2

[分类损失函数(margin 损失函数)——以二分类为例（∈{−1,+1}）_margin loss-CSDN博客](https://blog.csdn.net/Robin_Pi/article/details/105889918)



损失函数的作用：衡量真实值 y 和预测值 f(x) 之间不一致的程度
如何衡量差别？或者说如何定义构造损失函数的策略？
两种思路：①定义为错误分类的数量 ②错误分类点到超平面的距离③拟合和优化 0-1 损失函数？
损失函数如何惩罚：增大损失函数？
通过权重控制——随着𝑚𝑎𝑟𝑔𝑖𝑛→−∞而加大惩罚（结合图）
关键：抓住了 𝑦𝑓(𝑥) 就抓住了分类模型损失函数的核心。

#### 1.

In what type of problems is that missclassification error an unsuitable performance measure?

哪种问题下，错误分类 并非表现的衡量指标

**如何衡量差别**？或者说如何定义构造损失函数的策略？
两种思路：①定义为错误分类的数量 ②错误分类点到超平面的距离③拟合和优化 0-1 损失函数？

eg medical problem


$$
L(x,y,\theta)= \mathbb{I}(y \neq (x,\theta))
$$


not all errors are common surable

### 2.

$$
L(x,y,\theta) =  \mathbb{I}(y \neq sign(X^T c\cdot \theta))= \mathbb{I}(y\neq sign(x^T \theta)) (c>0)
$$





---

2023年11月13日

A0

how to extend logistic classifier to M classes

compare odds of each y=m against class y=m
$$
\frac{P(y=m|x;\theta)}{P(y=M|x;\theta)} = e^{x^T \theta_m}
$$
m=1,2,…
$$
P(y=m|x,\theta) = P(y=M|x,\theta) \cdot e^{x^T \theta_m}
$$

$$
P(y=m|x,\theta) = 1-\sum_{m=1}^{m-1}P(y=m|x,\theta)
$$

np.ceil(insert(x))?

$=\frac{1}{1+\sum_{k=1}^{m-1}e^T\theta_k}$