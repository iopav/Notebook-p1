# 2023

## 1

The distributed components architectural pattern has several components which provide common service and a communication middleware to connect clients and components.

It allow the system designer to delay decisions on when and how services are provided.

pros: flexible, scalable, easy to extend, auto-reconfiguration

cons: complex, no universal standard

## 2

differences:

V: 1.go back to the previous stage; 2. care about quality and combine test with the beginning of the project

W: go to the next stage when the previous stage is finished; start test after some activities.

same:

both pull system, plan driven

## 3

Norming: conflict solved, teammate flexible, know role and job, (go back to s/g if necessary)

Performing: process in place, synergy

Goal understand and be committed to a goal

Role know their role, part of job, what expected, how to hold accountability and responsibility

Interpersonal Relationship coordinate and communicate to increase trust, deal with conflict and make progress

Process: sys defined to make progress make decision, sys and procedure defined to complete project

## 

Comparison:

| tuck                       | grip       |
| -------------------------- | ---------- |
| have forming               | no forming |
| go back                    | no go back |
| emphasize on communication |            |

Questions I am not sure about:

**2023:**

 **4.a (3/14 points) Explain step by step the pre-checking activity, with special emphasis on which are the actors involved and what is their role**

1. check-in is inspected by <u>the owner of the module.</u> 
2. <u>The module owner</u> will go though everything and give a check-in message.
3. if any bugs or mistakes existed, the <u>programmer</u> should fix it.
4. the inspection is done when programmer finished

owner of the module: knowledgeable reviewer

programmer: who wrote the code 

**4.b**

pair programing: review happened naturally while another pair member read code

ad: everything is checked by two

**5.a (5/14 points) Explain step by step the process of requirements engineering, with special emphasis on which actors and/or stakeholders are responsible for each step of the process and what are their responsibilities**

The process of requirement engineering:

1.Requirements elicitation 

<u>Developers</u> understand the need of <u>stakeholders</u>

<u>Developers</u> should prepare for elicitation, then perform elicitation activities and follow up after elicitation, document open issues.

2.Requirements specification

<u>Developers</u> use natural languages and models to structure the needs as user case/user story

Identify the actors first, then lay out how the domain influences actors, and define the use cases for activities where actors and systems interact.

3.requirements validation 

<u>Users</u> review of requirements, models, prototypes and test cases.

<u>Developers</u> detect conflicts and classify.

4.system requirements document

<u>Developers</u> document requirements

**2021**

**Question 1. [2 points]. Compare plan-based cost models and budget-limited cost models: Indicate at least two (2) differences between them. Two (2) in total**

| plan based                                                   | budget based                                         |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| have detailed plan before activity, calculate budget based on the plan | have a budget first, create a plan within the budget |
| suitable for project with low uncertainty                    | suitable for project with high uncertainty           |
|                                                              |                                                      |

 **Question 2. [2 points]. Define what are plan driven software processes**

Plan driven software process is a process that plan and schedule all of the process activities before starting development. And progress measured against plan.

 **Question 3. [2 points]. Compare iteration planning and release planning: Indicate at least two (2) differences and one (1) similarity between them. Three (3) in total.**

Is it same to compare agile approach and plan-driven approach?

| release:                                                     | iteration:                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| suitable for big system                                      | suitable for small system                                    |
| Looks ahead for several  months                              | Shorter term outlook,  and focuses on planning  the next increment of a  system. |
| Decides on the features  that should be included  in a release of a system. | “Sprint” ~ 2-4 weeks of  work for the team.                  |
| suitable for stable development environment                  | suitable for dynamic development environment                 |
| involve prioritizing the work to be done                     |                                                              |
| Works well with small teams & systems- “Organic growth” may cause problems for SW structure and dependencies |                                                              |

 **4.b (3/5 points) Would it be reasonable to use a layered architecture in combination with a master-slave architecture? Justify your answer with an example or a counterexample.** 

Yes. One example of such a combination is a web application to watch video online that uses a three-tier layered architecture, consisting of 

<u>presentation</u>(handles user interactions and requests), 

<u>business</u>(components responsible for user authentication, content recommendation, and video play control), 

and <u>data layers</u>(responsible for managing the storage and retrieval of video content), and employs a master-slave database architecture in the data layer to improve performance and availability

- **Master Database:** source of video content. 
- **Slave Databases:** copies of the master database, used for read operations. They can be distributed to enhance performance and availability. 
- For instance, users in different regions can connect to the nearest slave database, reducing latency and improving their video-watching experience.

 **5.a (2/5 points) Describe with a diagram how you will decide if your company is using the right process in a particular software engineering project.**

**=描述standardize的图**

This question aims at asking you about the quality-based process and how you can use that model to decide if the process you have been following is correct or it needs adjustment.



**2020**

**Question 6. [8 points].** 
VR glasses
**6.b (3/8 points) Assume that the team has decided to use a 2-tier architecture. Would it be reasonable to use a 2-tier architecture in combination with the logical architecture you have chosen? Justify your answer with an example or a counterexample.** 

Yes. I chose **client and server** in the first question. We can have a 2-tier structure within the client(VR glasses)

Then, the client is split into 2 tiers: a display tier and a logic tier. In the display tier, it deals with rendering of the virtual world. In the logic tier, it deals with the game rules sending commands to the display tier.

```css
  [VR Glasses (Client)]
    /            \
[Display Tier] [Logic Tier]
        \            /
       [Mobile Device (Server)]
         |
[Game Application & Puzzle Data]
```