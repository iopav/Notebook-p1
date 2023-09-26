

## Model

#### definition
- abstraction: remove detail, focus in viewpoint
- dynamic

### prototypes 原型
#### usage
风险降低
+ requirements elicitation
+ requirements validation
+ proof of concept
+ 信息反馈
#### difference between product

### UML

- component diagram组件图
  - context type
- use case diagram用例图
  - interaction type
- sequence diagram时序图
  - interaction type
- class diagram类图
  - structure type
- state diagram状态图
  - behavior type
- activity diagram活动图
  - behavior type
- 

```mermaid
graph LR
ac[action]
t[time]
cust[user/stakeholder]
input["generate input(L)"]
input2["secondary(R)"]
cust--> input
cust--> input2
ac-->cust
t-->cust
```

### UML sequence diagram
```
component/class []
life line -->[]--
-->|v|[life line] :call with value to start
<--|v|[life line] :return with value to end
组件/类的生命周期跟随调用和返回

框架 通常标注类型
frame: for/while/if
condition  -.-虚线划分条件空间




```



物理结构

client-service

构造简单

master-slave

负载均衡

避免单点故障

动态扩展

bus总线型

逻辑结构

top down

bottom up

层级结构模型

MCV-jsp框架

driver属于m的扩展



```
component in master slave structure. 

master slave structure sim and diff with layered structure.

example of software application of master slave structure.


```







### 2023年9月18日

BDD>TDD



test suite - a set of tests run together for a single purpose

test case - consists on :

- procedure
- test data
- exp outcome
- exp behavior 

the oracle problem

correct answer - flexible



