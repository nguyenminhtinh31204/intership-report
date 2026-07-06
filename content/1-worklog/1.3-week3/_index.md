---
title: "Worklog Week 3"
date: 2026-05-04
weight: 103
week: 3
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | May 4, 2026 - May 10, 2026 |
| Internship week | Week 3 |
| Phase | Stage of studying and researching documents |
| Curriculum | First Cloud Journey |
| Main topic | Database, API, and Serverless architecture on AWS |
| Weekly goals | Learn about services for storing data, building APIs and designing serverless applications |

---

## Learning orientation Week 3

After learning about platform services such as S3, EC2, Lambda, VPC, CloudWatch and IAM in week 2, week 3 continues to learn the **First Cloud Journey** program with a focus on **database**, **API** and **serverless application pattern**.

This week, I have not yet started implementing the main project. The goal is to better understand how data is stored, how the frontend communicates with the backend through APIs, and how AWS services coordinate in a serverless model.

---

## Week 3 learning objectives

The main goals for the week include:

- Learn Amazon DynamoDB and the NoSQL model.
- Learn Amazon RDS at an overview level to differentiate between SQL and NoSQL.
- Learn about Amazon API Gateway and the role of API in the cloud system.
- Learn serverless and event-driven architecture.
- Understand how Lambda combines with API Gateway, S3, and DynamoDB.
- Review IAM in the context of granting Lambda permissions to access the database.
- Learn how to monitor APIs and Lambda with CloudWatch.
- Take notes on knowledge that can be applied to the project in the last 4 weeks.

---

## Content implemented during the week

### Day 1 - Monday, May 4, 2026

The first day of week 3 focuses on reviewing the services learned and moving on to the database services group.

Implemented content:

- Review the roles of S3, Lambda, CloudWatch and IAM.
- Review how these services can be combined in a serverless system.
- Start learning about database services on AWS.
- Distinguish between file storage needs and structured data storage needs.
- Note the difference between object storage and database.

Results achieved:

- Understand that S3 is suitable for storing files, and database is suitable for storing data that needs to be queried.
- Understand why a cloud system often needs to combine many types of storage.
- Aim to continue learning about DynamoDB and RDS.

---

### Day 2 - Tuesday, May 5, 2026

Day two focuses on **Amazon DynamoDB** and the NoSQL database model.

Implemented content:

- Learn what Amazon DynamoDB is.
- Learn the concepts:
  - Table
  - Item
  - Attribute
  - Partition key
  - Sort key
- Learn the NoSQL model and how data is stored as key-value/document.
- Read the documentation about DynamoDB's auto-scaling capabilities.
- Note cases where DynamoDB should be used.

Example item structure in DynamoDB:

```json
{
  "InvoiceId": "INV-001",
  "CustomerName": "Nguyen Van A",
  "TotalAmount": 1500000,
  "Currency": "VND"
}
```

Results achieved:

- Understand DynamoDB is a NoSQL database fully managed by AWS.
- Know that DynamoDB is suitable for applications that need fast queries and good scale.
- Understand the role of partition key in identifying items.

---

### Day 3 - Wednesday, May 6, 2026

Day three focuses on **Amazon RDS** and the comparison between SQL and NoSQL.

Implemented content:

- Learn Amazon RDS at an overview level.
- Learn about database management systems supported by RDS such as MySQL, PostgreSQL, MariaDB.
- Compare RDS with DynamoDB.
- Learn when to use relational database and when to use NoSQL.
- Note the advantages of RDS in systems that need clear data relationships.
- Note the advantages of DynamoDB in serverless systems that need to scale quickly.

Basic comparison table:

| Criteria | Amazon RDS | Amazon DynamoDB |
|---|---|---|
| Data Model | SQL Relation | NoSQL key-value/document |
| Query | SQL | Query/Scan by key and index |
| Server management | AWS manages many parts, still needs to configure instances | Fully managed serverless |
| Suitable | Data has complex relationships | The application needs to scale quickly, query by key |
| Example | Order management, finance, ERP | Session, metadata, invoice records |

Results achieved:

- Distinguish between RDS and DynamoDB.
- Understand that not all systems use the same type of database.
- Know how to choose a database depending on the data structure and query method.

---

### Day 4 - Thursday, May 7, 2026

Day four focuses on **Amazon API Gateway** and how to build APIs for cloud applications.

Implemented content:

- Learn what API Gateway is.
- Learn REST API and HTTP methods.
- Learn popular methods:
  - GET
  - POST
  - PUT
  - PATCH
  - DELETE
- Learn the concepts of resources, routes, stages and endpoints.
- Learn how API Gateway connects to Lambda.
- Note the role of API Gateway in connecting frontend and backend.

Example API route:

```txt
POST /uploads
GET /items
GET /items/{id}
PATCH /items/{id}
DELETE /items/{id}
```

Results achieved:

- Understand API Gateway is the communication port between the client and the backend.
- Know that API Gateway can call Lambda to process requests.
- Understand the role of stage when deploying API.

---

### Day 5 - Friday, May 8, 2026

Day five focuses on **serverless** and **event-driven** architecture.

Implemented content:

- Learn serverless application pattern.
- Review the role of AWS Lambda in the serverless model.
- Learn event-driven architecture.
- See the example of S3 uploading files that can trigger Lambda.
- See the example of API Gateway receiving requests and activating Lambda.
- Learn the advantages of the event-driven model:
  - Automatically react to events.
  - Reduces the need to run the server continuously.
  - Easy to expand according to the number of requests.
  - Optimize costs for intermittent workloads.

Simple event-driven flow example:

```txt
User Upload File → S3 Event → Lambda Function → Save Result to Database
```

Results achieved:

- Understand that event-driven is an event-based processing model.
- Know Lambda can be triggered by many different sources.
- Understand why serverless is suitable for applications that process files, APIs and data.

---

### Day 6 - Saturday, May 9, 2026

Friday focuses on security and monitoring in systems that use APIs and databases.

Implemented content:

- Review IAM Role for Lambda.
- Learn what permissions Lambda needs when accessing DynamoDB.
- Learn what permissions Lambda needs when logging to CloudWatch.
- Learn the basics of CORS in API Gateway.
- Learn how CloudWatch logs Lambda.
- Note common errors when the API system does not work properly.

Some common errors:

| Error | Possible causes |
|---|---|
| `AccessDenied` | Lambda lacks resource access |
| `Missing Authentication Token` | Calling the wrong API path, wrong method or not deployed stage |
| CORS error | API Gateway or backend does not have CORS configured |
| Timeouts | Lambda processing takes too long or calls to external services are slow |
| 500 Internal Server Error | Lambda logic error or malformed response |

Results achieved:

- Better understand the role of IAM in serverless systems.
- Know that CloudWatch is an important tool for error checking.
- Understand some common errors when working with API Gateway and Lambda.

---

### Day 7 - Sunday, May 10, 2026

The weekend is used to synthesize knowledge and contact the project that will be done at the next stage.

Implemented content:

- Review DynamoDB, RDS, API Gateway, Lambda and serverless pattern.
- Synthesize notes according to architectural diagrams.
- Connect the knowledge you have learned with the project **Serverless AI Invoice Scanner**.
- Record services that are likely to be used in the project.
- Write week 3 workshop report.
- Prepare a study plan for week 4.

Results achieved:

- Complete the third week of study under the First Cloud Journey program.
- Understand how database, API and Lambda coordinate in serverless systems.
- Have a foundation to learn more about authentication, deployment and monitoring in the next week.

---

## Summary of Week 3 knowledge

In week 3, I learned more deeply about the service group for building cloud applications, especially database, API and serverless architecture.

| Knowledge group | Learned content |
|---|---|
| Database | DynamoDB, RDS, SQL, NoSQL |
| API | API Gateway, REST API, method, route, stage, endpoint |
| Serverless | Lambda, event-driven, serverless application pattern |
| Security | IAM Role, permission for Lambda to access database |
| Monitoring | CloudWatch Logs, API debugging and Lambda |
| Architecture | How to combine API Gateway, Lambda, and DynamoDB |

---

## Results achieved during the week

- Understand Amazon DynamoDB and the NoSQL model.
- Understand Amazon RDS at an overview level.
- Distinguish between SQL and NoSQL.
- Understand the role of API Gateway in the cloud system.
- Know how API Gateway connects to Lambda.
- Understand serverless and event-driven models.
- Know common errors when working with API Gateway, Lambda and IAM.
- Can relate the knowledge learned to the project that will be done in the last 4 weeks.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| It's easy to confuse DynamoDB with RDS | Create a table comparing SQL and NoSQL |
| Difficult to understand partition key and sort key | See a simple item example and how to query by key |
| API Gateway has many new concepts | Separate routes, methods, resources, stages and endpoints to learn |
| Event-driven is still quite abstract | Diagram the event flow from S3 to Lambda |
| IAM permission involves many services | Note each permission according to each use case |

---

## Lesson learned

- Choosing a database depends on how to store and query data.
- DynamoDB is suitable for serverless architecture because it has good scalability and does not require server management.
- API Gateway is an important component for the frontend to communicate with the backend.
- Serverless does not mean there is no backend, but it means there is no need to manage the server yourself.
- CloudWatch and IAM are two parts to pay attention to when deploying any AWS system.
- You should learn the architecture according to the processing flow instead of just learning each individual service.

---

## Plan for Week 4

Week 4 is the last week of the learning phase following First Cloud Journey before moving on to the project implementation phase.

Expected content:

- Learn Amazon Cognito.
- Learn about AWS Amplify Hosting.
- Learn basic CI/CD with GitHub and Amplify.
- Learn about AWS Well-Architected Framework at an overview level.
- Review the services learned in the first 3 weeks.
- Synthesize knowledge to prepare for the project **Serverless AI Invoice Scanner**.
- Develop a project implementation plan for weeks 5 to 8.

---

## Weekend comments

Week 3 helps you better understand how to build a cloud application using database, API and Lambda. Knowledge of DynamoDB, API Gateway and serverless event-driven is a very important foundation to prepare for the project in the later stages. After this week, I have a clearer view of how the frontend can send requests to the backend, how Lambda processes business, and how data is saved in the database on AWS.
