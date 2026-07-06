---
title: "Worklog Week 4"
date: 2026-05-11
weight: 104
week: 4
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | May 11, 2026 - May 17, 2026 |
| Internship week | Week 4 |
| Phase | Stage of studying and researching documents |
| Curriculum | First Cloud Journey |
| Main topic | Authentication, Frontend Hosting, CI/CD and AWS knowledge synthesis |
| Weekly goals | Complete the First Cloud Journey learning phase and prepare a project implementation plan in the last 4 weeks |

---

## Learning orientation Week 4

Week 4 is the last week of the learning period under the **First Cloud Journey** program. After the first three weeks of learning about cloud computing, AWS infrastructure, storage, compute, database, API and serverless architecture, this week focuses on content serving complete application deployment.

The main contents include:

- Authenticate users with Amazon Cognito.
- Deploy frontend with AWS Amplify Hosting.
- Learn basic CI/CD with GitHub and Amplify.
- Learn monitoring, security and best practices.
- Review all the knowledge learned in 4 weeks.
- Prepare a plan to enter the **Serverless AI Invoice Scanner** project from week 5.

---

## Week 4 Learning Objectives

The main goals for the week include:

- Understand Amazon Cognito's role in user authentication.
- Learn User Pool, App Client, sign-up and sign-in.
- Understand how AWS Amplify Hosting is used to deploy the frontend.
- Learn how to connect GitHub repository with Amplify Hosting.
- Understand CI/CD concepts at a basic level.
- Learn about AWS Well-Architected Framework at an overview level.
- Review the services learned in the First Cloud Journey program.
- Determine the services to be used in the actual project.
- Plan project implementation in the last 4 weeks.

---

## Content implemented during the week

### Day 1 - Monday, May 11, 2026

The first day of week 4 focuses on reviewing knowledge from week 3 and starting to learn about user authentication on AWS.

Implemented content:

- Review the services learned in week 3:
  - Amazon DynamoDB
  - Amazon RDS
  - Amazon API Gateway
  - AWS Lambda
  - CloudWatch Logs
- Learn the role of authentication in web applications.
- Learn what Amazon Cognito is.
- Note the difference between authentication and authorization.
- See how Cognito can support user registration and login.

Results achieved:

- Understand why the application needs a user authentication layer.
- Know that Amazon Cognito is a service that supports user management and authentication.
- Have a foundation to continue learning about User Pool and App Client.

---

### Day 2 - Tuesday, May 12, 2026

Day two focuses on **Amazon Cognito User Pool** and the basic components of the login process.

Implemented content:

- Learn the concept of User Pool.
- Learn App Client in Cognito.
- Learn the flow of user registration and login.
- Find out the frontend information that often needs configuration:
  - AWS Region
  - User Pool ID
  - App Client ID
- Learn tokens in Cognito at a basic level.
- Note Cognito's role in protecting frontend applications.

Common frontend configuration examples:

```txt
REACT_APP_AWS_REGION=ap-southeast-1
REACT_APP_USER_POOL_ID=ap-southeast-1_xxxxxxxxx
REACT_APP_USER_POOL_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxx
```

Results achieved:

- Understand User Pool is where users are managed.
- Know the App Client used by the frontend to connect to Cognito.
- Grasp the necessary information when integrating Cognito into React applications.

---

### Day 3 - Wednesday, May 13, 2026

Day three focuses on **AWS Amplify Hosting** and how to deploy a frontend application.

Implemented content:

- Learn about AWS Amplify Hosting.
- Learn how Amplify Hosting deploys frontend applications.
- See the GitHub repository connection flow with Amplify.
- Learn build settings and environment variables.
- Note the difference between Amplify Hosting and Amplify backend.
- Learn how the frontend can use environment variables to call API Gateway.

Results achieved:

- Understand how Amplify Hosting is used to build and deploy frontend.
- Know that Amplify can automatically deploy when there is a new commit from GitHub.
- Understand that in the future project, Amplify will be used mainly for hosting the React frontend.

{{% notice info %}}
In the Serverless AI Invoice Scanner project, Amplify is used for **Hosting frontend**, while Cognito and backend AWS services will be configured separately.
{{% /notice %}}

---

### Day 4 - Thursday, May 14, 2026

Day four focuses on **CI/CD** concepts and modern application deployment workflows.

Implemented content:

- Learn what CI/CD is.
- Learn about Continuous Integration and Continuous Deployment.
- See example frontend deploy flow:

```txt
Developer Commit Code → GitHub Repository → Amplify Build → Amplify Deploy → Public Website
```

- Learn the role of build command and output directory.
- Take note of possible errors when deploying the frontend:
  - Environmental variables.
  - Build failed.
  - Sai package dependency.
- Wrong redirect configuration.
- Learn how to check build logs in Amplify.

Results achieved:

- Understanding CI/CD helps automate the build and deploy process.
- Know that GitHub can connect to Amplify Hosting.
- Understanding build logs is very important when deploying frontend errors.

---

### Day 5 - Friday, May 15, 2026

Day five focuses on the **AWS Well-Architected Framework** and cloud system design principles.

Implemented content:

- Learn overview of AWS Well-Architected Framework.
- Note the main pillars:
  - Operational Excellence
  - Security
  - Reliability
  - Performance Efficiency
  - Cost Optimization
  - Sustainability
- Contact each pillar with learned services.
- Learn why it is necessary to design a system that is both secure and cost-effective.
- Take notes on best practices when working with AWS.

Short notes:

| Pillar | Meaning |
|---|---|
| Operational Excellence | System operation is stable, easy to monitor and improve. |
| Security | Protect data, accounts, and access. |
| Reliability | The system has the ability to recover when there is an error. |
| Performance Efficiency | Use resources in accordance with needs. |
| Cost Optimization | Optimize costs, avoid wasting resources. |
| Sustainability | Use resources effectively and sustainably. |

Results achieved:

- Understand the basic principles when designing systems on AWS.
- Greater awareness of security, monitoring and cost optimization.
- Have system design thinking instead of just creating individual resources.

---

### Day 6 - Saturday, May 16, 2026

Day six focuses on reviewing all the knowledge learned in the first 4 weeks.

Implemented content:

- Review service groups:
  - Compute: EC2, Lambda
  - Storage: S3
  - Database: DynamoDB, RDS
  - Networking: VPC
  - Security: IAM, Cognito
  - API: API Gateway
  - Monitoring: CloudWatch
  - Hosting: Amplify Hosting
- Summary of the role of each service.
- Note which services will be used in the project.
- Contact First Cloud Journey knowledge with the project **Serverless AI Invoice Scanner**.
- Prepare a list of resources to create in week 5.

Results achieved:

- Synthesize key knowledge after 4 weeks of study.
- Identify services suitable for the project.
- Have a clearer plan for the actual implementation phase.

---

### Day 7 - Sunday, May 17, 2026

The last day of the week is used to summarize the learning phase and prepare to enter the project phase.

Implemented content:

- Write a summary report for week 4.
- Synthesize the content learned in the First Cloud Journey phase.
- Determine which project will start from week 5.
- Plan project implementation in the last 4 weeks.
- Determine the expected processing flow of the project:

```txt
React Frontend → API Gateway → Lambda → S3 → Textract → OpenAI API → DynamoDB
```

- Note the services that need to be implemented:
  - AWS Amplify Hosting
  - Amazon Cognito
  - Amazon API Gateway
  - AWS Lambda
  - Amazon S3
  - Amazon Textract
  - OpenAI API
  - Amazon DynamoDB
  - Amazon CloudWatch
  - AWS IAM

Results achieved:

- Complete the First Cloud Journey learning phase.
- Prepare project orientation.
- Have the foundation to start implementing the Serverless AI Invoice Scanner system.

---

## Summary of Week 4 knowledge

In week 4, I learned content related to user authentication, frontend deployment, CI/CD, and cloud system design principles.

| Knowledge group | Learned content |
|---|---|
| Authentication | Amazon Cognito, User Pool, App Client, sign-up, sign-in |
| Frontend Hosting | AWS Amplify Hosting, deploy React app, GitHub integration |
| CI/CD | Build, deploy, build logs, environment variables |
| Cloud Best Practices | AWS Well-Architected Framework |
| Security | IAM, Cognito, principle of least privilege |
| Monitoring | CloudWatch, Amplify build logs |
| Project Preparation | Determine the service needed for Serverless AI Invoice Scanner |

---

## Results achieved during the week

- Understand Amazon Cognito and its role in user authentication.
- Know User Pool and App Client used for frontend integration.
- Understand how AWS Amplify Hosting is used to deploy the frontend.
- Know the process of connecting GitHub to Amplify Hosting.
- Understand basic CI/CD concepts.
- Get an overview of the AWS Well-Architected Framework.
- Review knowledge from the first 4 weeks.
- Prepare project implementation plan for weeks 5 to 8.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| It's easy to confuse Amplify Hosting and Amplify backend | Note clearly that the project only uses Amplify Hosting for the frontend |
| Cognito has many configurations such as User Pool, App Client, token | Separate each component to study separately |
| CI/CD is still new | See the flow of GitHub → Build → Deploy for easy understanding |
| Well-Architected has many concepts | Take short notes on each pillar and relate them to examples |
| Need to connect knowledge of many services | Draw an overall architectural diagram for easy visualization |

---

## Lesson learned

- A complete cloud application not only has a backend but also needs authentication, hosting, monitoring and security.
- Cognito helps reduce the effort of building a login system yourself.
- Amplify Hosting is suitable for quick frontend deployment from GitHub.
- CI/CD helps the application update process faster and more stable.
- Well-Architected Framework helps guide system design that is safe, reliable and cost-optimized.
- The first 4 weeks of learning the foundation are necessary before starting the actual project.

---

## Summary of the first 4 weeks

After 4 weeks of studying the **First Cloud Journey** program, I have grasped the necessary foundational knowledge about AWS Cloud.

Groups of knowledge learned:

| Week | Main topic |
|---|---|
| Week 1 | Cloud computing, AWS Global Infrastructure, AWS Console, basic IAM |
| Week 2 | S3, EC2, Lambda, VPC, CloudWatch, IAM |
| Week 3 | DynamoDB, RDS, API Gateway, Serverless, Event-driven |
| Week 4 | Cognito, Amplify Hosting, CI/CD, Well-Architected Framework |

This knowledge will be applied to the project **Serverless AI Invoice Scanner** in the next 4 weeks.

---

## Plan for Week 5

From week 5, I will begin the implementation phase of the project **Serverless AI Invoice Scanner**.

Expected content for week 5:

- Analyze project requirements.
- System architecture design.
- Create S3 bucket to store invoice files.
- Create DynamoDB table `InvoiceData`.
- Create a Lambda function to handle file uploads.
- Configure API Gateway route `POST /uploads`.
- Test upload using Postman.
- Logging and debugging with CloudWatch.

---

## Weekend comments

Week 4 marks the completion of the learning phase under the First Cloud Journey program. After this week, I have an overview of important AWS services and understand how they coordinate in a cloud system. This is the necessary foundation to move on to the implementation phase of the **Serverless AI Invoice Scanner** project in the last 4 weeks of the internship.
