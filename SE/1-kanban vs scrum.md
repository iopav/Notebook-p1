## Kanban

##### procedure
- plan
- build
- test
- done
冒泡式执行

##### role
1.agile coach = scrum master
##### common
both **pull system**
felxible

##### difference
kanban is a continues system, no sprint or sprint backlog
the pull system in kanban >> work in progress limit (WIP限制 与团队能力有关，eg. lean time)
scrum is the complete agile methodology, kanban is a tool
scrum 是完整的敏捷方法论，kanban是一个工具
##### ritual
1.daily standup meeting
2.demo
3.retrospective

## Scrum

### Scrum vs Waterfall
#### waterfall
- plan
- build
- test
- review
- deploy
计划-执行-评估-复盘-部署
##### feature 
上一个阶段结束才能进行下一个阶段
每个阶段用时都长达几个月
##### drawback
lag behind market requirements
Product planning must be done before any subsequent work, and in most cases the planning process does not fully understand the project
可能落后于市场需求
产品规划必须早于后续工作之前完成，大部分情况规划环节并不能完全理解项目
通常需要从`build`环节回滚到`plan`
#### Scrum
sprint:
- plan
- build
- test
- review
  

Multi-tasking in vertical parallel reduces time at every stage from product to development and testing
Incremental releases >>  `sprints`.
A sprint usually takes only 1~3 weeks, repeating the sprint until the product is fully functional.
A sprint usually takes only 1~3 weeks, keep repeating the sprint until the product is fully functional
多任务垂直并行，减少从产品到开发测试每个阶段的时间
增量式发布>>增量发布版本incremental releases，即`sprint`
一个sprint通常只需要1~3周，不断重复sprint，直到产品功能齐全
##### role角色
1.product owner
2.scrum master
3.scrum team

##### artifact 可视化文档
1.product backlog
prioritized list of features (user story)
evolve and change with every sprint
筛选优先项，列入产品开发列表
```
user story: As a ... I need.. So that..
allow PO to specify details for team to estimate size of tasks
```
2.sprint backlog 代办列表

3.burndown chart燃尽图
show the progress during a sprint on the completion of tasks in the sprint backlog
approach zero as the work is being completed
展示代办列表的进度，趋近0时，完工

##### ceremony 会议
1.sprint plan
scrum master and team meet to discuss the user stories and estimate the relative sizes
2.daily scrum
a brief standup meeting
3.sprint review and retrospective
occurs at the end of the sprint


#### scrum workflow
product backlog
sprint planning
sprint backlog
sprint
potientially shippable product
sprint review and retropective


### scrum vs kanban
Scrum uses fixed-length sprints with predefined goals, while Kanban is more flexible and allows for continuous flow.
Scrum has distinct roles (Product Owner, Scrum Master) and events (Sprint Planning, Daily Scrum), whereas Kanban is less prescriptive about roles and events.
Scrum prioritizes a fixed set of user stories for each sprint, while Kanban focuses on managing the flow of work items without predefined iterations.
### 目的
敏捷的出现时为了解决传统项目管理方法遇到的问题
问题：?

### 结合

采用 Scrumban 的团队中最常见的方式是既使用 Scrum 中带有待办事项清单的迭代计划，又使用看板的WIP限制和周期时间。（注意：周期时间是指从任务启动到任务完成，任务在团队工作流程中流转所需的时间。）


### graph syntax
```
​```mermaid
graph TB
    start[k]
    ...

TB（Top Bottom）表示从上向下布局，另外三种是
BT
LR（Left Right）
RL
A(开始)
B[动作]
C{"选择"}
D((圆形))
-->|comments| 
带箭头线段 -->
带箭头虚线线段 -.->
带箭头加粗线段 ==>
不带箭头线段 ---
```



