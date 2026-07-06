---
title: "Worklog Week 2"
date: 2026-04-27
weight: 102
week: 2
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | April 27, 2026 - May 3, 2026 |
| Internship week | Week 2 |
| Phase | Stage of studying and researching documents |
| Curriculum | First Cloud Journey |
| Main topic | Learn about foundational AWS services |
| Weekly goals | Understand the roles of basic AWS services such as S3, EC2, Lambda, VPC, CloudWatch and how they are used in the cloud system |

---

## Learning orientation Week 2

After the first week of getting acquainted with cloud computing, AWS Global Infrastructure, AWS Console and IAM, week 2 continues learning the **First Cloud Journey** program. This week's focus is on understanding the foundational AWS services that appear in most cloud systems.

This week, I have not yet started implementing the main project. The goal is to learn theory, review documents, do basic practice and take notes on the role of each service to prepare for the project phase in the last 4 weeks.

---

## Week 2 learning objectives

The main goals for the week include:

- Learn about Amazon S3 and the role of object storage.
- Learn Amazon EC2 at an overview level to understand the virtual server model on the cloud.
- Learn AWS Lambda and serverless compute concepts.
- Learn Amazon VPC and basic networking concepts on AWS.
- Learn about Amazon CloudWatch used for monitoring and logging.
- Review IAM Roles and permissions when AWS services communicate with each other.
- Compare the traditional model using servers with the serverless model.
- Take notes on knowledge to apply to the **Serverless AI Invoice Scanner** project at a later stage.

---

## Content implemented during the week

### Day 1 - Monday, April 27, 2026

On the first day of week 2, I reviewed the knowledge from week 1 and started learning about foundational AWS services according to the First Cloud Journey document.

Implemented content:

- Review concepts: AWS Region, Availability Zone, IAM and AWS Console.
- Review the learning path of First Cloud Journey.
- Identify services that need to be learned in week 2.
- Notes on AWS service groups by type:
  - Compute
  - Storage
  - Database
  - Networking
  - Security
  - Monitoring
- Learn how AWS services work together in a basic cloud system.

Results achieved:

- Better understand how AWS services are classified.
- Have a specific study plan for week 2.
- Know that each AWS service plays a unique role in the cloud architecture.

---

### Day 2 - Tuesday, April 28, 2026

Day two focused on **Amazon S3** and the concept of cloud object storage.

Implemented content:

- Read documents about Amazon S3 in the curriculum.
- Learn the concepts of buckets, objects, keys and storage classes.
- Learn the difference between traditional file storage and object storage.
- See how S3 is used to store images, PDF files, backup files and static websites.
- Learn about the public access block feature.
- Note the role of S3 in serverless systems.

Results achieved:

- Understand Amazon S3 is a highly scalable object storage service.
- Know that the bucket is where the object is stored.
- Understand why it is necessary to turn on public access block to protect data.
- Understand that S3 can be used as a place to store input files for data processing systems.

---

### Day 3 - Wednesday, April 29, 2026

Day three focuses on the **Compute** services group, including Amazon EC2 and AWS Lambda.

Implemented content:

- Learn Amazon EC2 at an overview level.
- Understand the concepts of instance, AMI, instance type and security group.
- Compare EC2 with traditional physical servers.
- Learn about AWS Lambda and the serverless compute model.
- Learn the concepts of function, runtime, handler, event and trigger.
- Compare EC2 and Lambda by performance, cost, and scalability.

Basic comparison table:

| Criteria | Amazon EC2 | AWS Lambda |
|---|---|---|
| Model | Virtual Server | Serverless functions |
| Server management | Users need to manage | AWS managed |
| Cost | Calculated based on instance run time | Calculated by number of calls and processing time |
| Suitable | Application runs continuously | Event-Driven Actions |
| Scalability | Additional configuration required | Automatically scale |

Results achieved:

- Understand that EC2 represents a virtual server model on the cloud.
- Understand that Lambda is a service that runs code without needing to manage a server.
- Understand how serverless is suitable for event-based processing systems.

---

### Day 4 - Thursday, April 30, 2026

Day four focuses on **Amazon VPC** and basic networking knowledge in AWS.

Implemented content:

- Learn the concept of Amazon VPC.
- Learn about subnet, route table, internet gateway and security group.
- Distinguish between public subnet and private subnet.
- Learn why cloud resources need to be placed in a secure network environment.
- See for example an architecture with a public frontend and a private backend.
- Note the role of networking in system security.

Results achieved:

- Understand that VPC is a virtual private network in AWS.
- Know the subnet used to divide the network in VPC.
- Understand security group as a layer that controls incoming and outgoing traffic.
- Recognize the important role of network design in cloud architecture.

---

### Day 5 - Friday, May 1, 2026

Day five focuses on **Amazon CloudWatch** and system monitoring on AWS.

Implemented content:

- Learn about Amazon CloudWatch.
- Learn about log groups, log streams and log events.
- Learn metrics and alarms.
- See how CloudWatch is used to monitor Lambda, API Gateway, and EC2.
- Note the role of CloudWatch in debugging system errors.
- Learn why logs are so important when operating cloud systems.

Results achieved:

- Understand that CloudWatch is a monitoring and logging service.
- Know log groups and log streams used to organize logs.
- Understand that when a Lambda or API fails, CloudWatch is an important place to check for the cause.
- Knowing that alarms can be used to warn when the system shows signs of abnormality.

---

### Day 6 - Saturday, May 2, 2026

Day six focuses on reviewing **IAM** and the relationship between IAM and the AWS services learned.

Implemented content:

- Review IAM User, IAM Role and IAM Policy.
- Learn why each service needs appropriate access permissions.
- See example Lambda needs IAM Role to log to CloudWatch.
- See the example where Lambda needs permission to read or write files to S3.
- Learn the principle of least privilege.
- Note common errors when IAM permissions are missing.

Example of errors that may occur when permissions are missing:

```txt
AccessDenied
UnauthorizedOperation
User is not authorized to perform action
```

Results achieved:

- Better understand the role of IAM in AWS security.
- Know that AWS services do not automatically have access to each other.
- Understand the need to grant the correct permissions for the service to operate safely.

---

### Day 7 - Sunday, May 3, 2026

The last day of the week is used to synthesize learned knowledge and prepare for the next week.

Implemented content:

- Review the services learned during the week:
  - Amazon S3
  - Amazon EC2
  - AWS Lambda
  - Amazon VPC
  - Amazon CloudWatch
  - AWS IAM
- Summarize notes by each service group.
- Redraw a simple diagram showing how cloud services can work together.
- Record unclear questions to continue learning next week.
- Write week 2 workshop report.

Results achieved:

- Complete the second week of study under the First Cloud Journey program.
- Understand the role of foundational AWS services.
- Have a better foundation to learn database, API and serverless in the following weeks.

---

## Summary of Week 2 knowledge

In week 2, I learned about the underlying AWS services commonly used in many cloud systems. This knowledge helps me better understand how a system on AWS is built from many independent components.

| Knowledge group | Learned content |
|---|---|
| Storage | Amazon S3, bucket, object, block public access |
| Compute | Amazon EC2, AWS Lambda, serverless compute |
| Networking | Amazon VPC, subnet, route table, security group |
| Monitoring | Amazon CloudWatch, log group, metrics, alarm |
| Security | IAM Role, IAM Policy, permission, least privilege |
| Cloud architecture | How services coordinate in the AWS system |

---

## Results achieved during the week

- Understand Amazon S3 and the role of object storage.
- Know that Amazon EC2 is a virtual server service on AWS.
- Understand that AWS Lambda is a serverless compute service.
- Distinguish between EC2 and Lambda.
- Understand Amazon VPC at a basic level.
- Know how CloudWatch is used for logging and monitoring.
- Understand IAM is a key component to access control.
- Understand the relationship between storage, compute, networking, monitoring and security.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| There are many AWS services to keep in mind | Divide services into groups: compute, storage, network, security |
| Easy to confuse between EC2 and Lambda | Compare according to server management criteria, costs and running methods |
| The concept of VPC is still abstract Draw a simple network diagram for easier understanding |
| IAM Policy is difficult to read because it uses JSON | Focus on understanding actions, resources and effects first
| CloudWatch has many new concepts | Separately note log group, log stream, metrics and alarm |

---

## Lesson learned

- AWS is organized into multiple service groups, each addressing a unique need.
- You should not learn each service individually, but rather understand their role in the overall architecture.
- S3, Lambda, IAM and CloudWatch are important foundation services in the serverless model.
- Security needs to be taken care of from the beginning, especially IAM and resource access.
- Logging and monitoring help detect errors faster when the system operates.

---

## Plan for Week 3

In week 3, I will continue to study the First Cloud Journey program, focusing more on databases, APIs and serverless architecture.

Expected content:

- Learn Amazon DynamoDB.
- Learn Amazon RDS at an overview level to compare SQL and NoSQL.
- Learn about Amazon API Gateway.
- Learn event-driven architecture.
- Learn serverless application pattern.
- Practice looking at documents and note how services can be combined in a real application.
- Prepare background knowledge for the project in the last 4 weeks.

---

## Weekend comments

Week 2 helps me better understand foundational AWS services, especially S3, Lambda, VPC, CloudWatch, and IAM. These are important services in many cloud systems and are also the necessary foundation to implement the project in the final weeks. After this week, I have a clearer view of how AWS organizes resources and how services work together in a cloud architecture.
