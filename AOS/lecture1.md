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



