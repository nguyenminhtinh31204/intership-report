---
title: "Worklog Week 10"
date: 2026-06-22
weight: 110
week: 10
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | June 22, 2026 - June 28, 2026 |
| Internship week | Week 10 |
| Phase | Report completion and summary stage |
| Project | Serverless AI Invoice Scanner |
| Main topic | Complete the final report, optimize documents, cleanup resources and summarize the internship |
| Weekly goals | Complete all internship documents, check the project one last time, prepare a report for submission and summarize the knowledge gained |

---

## Week 10 Orientation

Week 10 is used as the final summary week after the **Serverless AI Invoice Scanner** project has been completed and reviewed in week 9. In this week, the focus is no longer on developing new functionality but on completing reports, checking documents, preparing presentations, and taking steps to cleanup AWS resources if no longer in use.

The main goal of this week is to ensure the entire internship process is fully integrated, including:

- Knowledge learned from the First Cloud Journey program.
- The process of applying knowledge to real projects.
- Results achieved of the project.
- Errors encountered and how to fix them.
- AWS resources used.
- Resource cleanup process after finishing the lab.
- Next development direction of the project.

---

## Week 10 Goals

The main goals for the week include:

- Review the entire worklog from week 1 to week 9.
- Complete the week 10 workshop.
- Review proposal content and project documents.
- Standardize the description of system architecture.
- Check images, paths and Markdown document structure.
- Complete the instructions for cleanup resources.
- Check the remaining AWS resources.
- Prepare internship summary report content.
- Prepare presentation or demo content if necessary.
- Synthesise lessons learned and future development directions.

---

## Content implemented during the week

### Day 1 - Monday, June 22, 2026

The first day of week 10 focuses on reviewing all of the workbooks written during the internship.

Implemented content:

- Check the worklog for weeks 1 to 4 about the **First Cloud Journey** learning phase.
- Review the worklog from weeks 5 to 8 about the project implementation phase.
- Check the week 9 worklog about the review and handover preparation phase.
- Ensure weekly order, date and content are presented consistently.
- Take notes on sections that need to be added or edited.

Results achieved:

- Confirm a clear flow of internship content.
- Distinguish between two main stages: learning and project work.
- There is a basis for synthesizing the final report.

---

### Day 2 - Tuesday, June 23, 2026

The second day focused on checking and completing the project's proposal documents.

Implemented content:

- Review the project summary.
- Update the system architecture according to the actual project.
- Check the AWS services used.
- Make sure the content has replaced **Amazon Bedrock** with **OpenAI API**.
- Check the description of Lambda functions:
  - `UploadInvoiceFileFunction`
  - `ProcessInvoiceFunction`
  - `InvoiceManagementFunction`
- Check the API Gateway routes description.
- Check the description of DynamoDB table `InvoiceData`.

Results achieved:

- Proposal is adjusted to the actual project.
- Content about OpenAI API, Textract, Lambda, S3, DynamoDB and Amplify Hosting is more unified.
- Documents are ready to be included in the final report.

---

### Day 3 - Wednesday, June 24, 2026

Day three focuses on testing implementation documentation and Markdown structure.

Implemented content:

- Check the structure of document sections.
- Check image paths in Markdown.
- Check the front matter of each document file.
- Check title, weight and display order.
- Review Introduction, Environment Setup, AI Processing, API Gateway, Postman Test, Frontend Deploy and Cleanup.
- Check the code, command and API routes presented in the documentation.

Document items checked:

| Section | Content |
|---|---|
| Introduction | System overview and used services |
| Environment Setup | Prepare your AWS and frontend environment |
| AI Processing | Textract, OpenAI API and DynamoDB |
| API Gateway | Backend API routes |
| Test with Postman | API Testing |
| Deploying Frontend | Deploy React with Amplify Hosting |
| Cleanup | Delete AWS resources after completing lab |

Results achieved:

- Markdown documents are clearer and more consistent.
- Main sections are arranged reasonably.
- Reduce errors in wrong paths and wrong service names in documents.

---

### Day 4 - Thursday, June 25, 2026

Day four focuses on a final check of the AWS system and the resources in use.

Implemented content:

- Check API Gateway.
- Test Lambda functions.
- Check S3 bucket and data in folder `uploads/`.
- Check DynamoDB table `InvoiceData`.
- Check Cognito User Pool.
- Check out Amplify Hosting App.
- Check CloudWatch Log Groups.
- Check related IAM Roles and Policies.
- Check optional resources such as Secrets Manager or Route 53 if used.

List of resources to review:

```txt
API Gateway
Lambda Functions
S3 Bucket
DynamoDB Table
Cognito User Pool
Amplify Hosting App
CloudWatch Log Groups
IAM Roles and Policies
Secrets Manager
Route 53
```

Results achieved:

- Understand the status of each AWS resource.
- Determine which resources to keep for demo.
- Determine which resources can be deleted after finishing the lab.

---

### Day 5 - Friday, June 26, 2026

Day five focuses on completing the resources cleanup and checking costs.

Implemented content:

- Review checklist cleanup resources.
- Check resource deletion order to avoid dependency errors.
- Note the resources that need to be deleted after the project:
  - API Gateway
  - Lambda Functions
  - S3 Bucket
  - DynamoDB Table
  - Cognito User Pool
  - Amplify Hosting App
  - CloudWatch Log Groups
  - IAM Roles and Policies
  - Optional resources
- Check AWS Billing or Cost Explorer at a basic level.
- Note services that may incur costs if not deleted.

Recommended cleanup order:

```txt
1. API Gateway
2. Lambda Functions
3. S3 Bucket
4. DynamoDB Table
5. Cognito User Pool
6. Amplify Hosting App
7. CloudWatch Log Groups
8. IAM Roles and Policies
9. Optional Resources
```

Results achieved:

- Have a clear cleanup checklist.
- Understand why resources need to be deleted after completing the lab.
- Reduce the risk of unexpected costs.

---

### Day 6 - Saturday, June 27, 2026

Friday focuses on report preparation and final presentation content.

Implemented content:

- Prepare an outline for the internship summary report.
- Synthesize knowledge learned in 4 weeks of First Cloud Journey.
- Summarize the project making process in the following weeks.
- Prepare a description of the system architecture.
- Prepare demo project.
- Prepare the results section.
- Prepare for difficult parts and lessons learned.
- Prepare future development directions.

Expected summary report structure:

| Part | Content |
|---|---|
| Introduction | Internship and project goals |
| Knowledge learned | First Cloud Journey and AWS services |
| Project architecture | Serverless AI Invoice Scanner |
| Deployment | Steps to build a system |
| Testing | Postman, frontend, CloudWatch |
| Results | Complete function |
| Cleanup | AWS Resource Cleanup |
| Conclusion | Lessons and development directions |

Results achieved:

- Have a clear final report outline.
- There is content prepared for the demo presentation.
- Summarize the most important points of the project.

---

### Day 7 - Sunday, June 28, 2026

The last day focuses on summarizing week 10 and summarizing the entire internship process.

Implemented content:

- Write the week 10 worklog.
- Summarize the entire internship process.
- Check the documents that need to be submitted.
- Review the project one last time.
- Note the project's strengths.
- Note any remaining limitations.
- Propose future development directions.
- Complete the handover content.

Results achieved:

- Complete the final review week.
- Complete documents and internship reports.
- Project is ready for presentation, submission or handover.
- Have an overview of the entire process of learning and deploying projects on AWS.

---

## Summary of knowledge from Week 10

In week 10, I focused on completing reports, reviewing documents, checking AWS resources and preparing for project handover.

| Work group | Implemented content |
|---|---|
| Worklog Review | Review the worklog from week 1 to week 9 |
| Proposal Review | Edit proposal content according to actual project |
| Documentation | Check Markdown, images, document structure |
| AWS Resource Review | Check the AWS resources in use |
| Cleanup | Complete the resource cleaning checklist |
| Cost Review | Checking resources may incur costs |
| Final Report | Prepare internship summary report |
| Demo Preparation | Prepare project presentation content |

---

## Results achieved during the week

- Review the entire internship worklog.
- Complete proposal project.
- Check and edit Markdown documents.
- Review AWS resources in use.
- Complete the cleanup resources checklist.
- Prepare internship summary report.
- Prepare demo content and project handover.
- Synthesize lessons learned and future development directions.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| Many documents need to be reviewed | Divide into groups: worklog, proposal, project docs, cleanup |
| Easy to disagree on service names | Standardize names such as OpenAI API, AWS Amplify Hosting, Amazon Textract |
| Cleanup has many resource dependencies | Arrange the order of deleting resources according to checklist |
| The report needs to be compiled for many weeks | Summary by stage: learning and project |
| Need to present the project briefly | Prepare demo script according to main processing flow |

---

## Lesson learned

- The final phase of the project requires time to review documents and resources.
- Good documentation makes the project easy to understand, easy to demo and easy to hand over.
- Cleaning up AWS resources is an important step to avoid incurring costs.
- When using multiple AWS services, clearly note the resource name and role of each service.
- The internship report should be presented according to the process: learning knowledge, applying it to the project, testing and summarizing.
- Preparing a demo in advance helps the presentation process be more confident and coherent.

---

## Summary of the entire internship process

During the internship, I went through two main stages:

| Phase | Content |
|---|---|
| Learning phase | Study and research documents according to the First Cloud Journey program |
| Project phase | Building a Serverless AI Invoice Scanner system on AWS |

Main knowledge and skills gained:

- Understand an overview of AWS Cloud.
- Understand core AWS services such as S3, Lambda, API Gateway, DynamoDB, Cognito, Amplify Hosting, CloudWatch, and IAM.
- Understand serverless and event-driven architecture.
- Know how to design an event-based file processing system.
- Know how to integrate Amazon Textract to OCR invoices.
- Know how to integrate OpenAI API to standardize data.
- Know how to store data using DynamoDB.
- Know how to deploy frontend using AWS Amplify Hosting.
- Know how to test API using Postman.
- Know how to debug errors using CloudWatch Logs.
- Know how to write deployment documentation and resource cleanup.

---

## Final result of the project

Project **Serverless AI Invoice Scanner** has completed the following main functions:

| Function | Status |
|---|---|
| Sign up/log in with Cognito | Complete |
| Upload invoices from frontend | Complete |
| Save files to S3 | Complete |
| Trigger Lambda when there is a new file | Complete |
| OCR invoices with Amazon Textract | Complete |
| Normalize data using OpenAI API | Complete |
| Save data to DynamoDB | Complete |
| API to get list of invoices | Complete |
| API to view invoice details | Complete |
| Invoice Search API | Complete |
| Tags update API | Complete |
| API update starred | Complete |
| Frontend filter, sort, export Excel | Complete |
| Deploy frontend with Amplify Hosting | Complete |
| Write cleanup resources documents | Complete |

---

## Future development direction

If we continue to develop the project, we can add:

- Cognito Authorizer cho API Gateway.
- AWS Secrets Manager to save OpenAI API key.
- Amazon SQS for asynchronous invoice processing.
- Realtime processing status on the frontend.
- Data editing function after AI extraction.
- Dashboard statistics on revenue, number of invoices and total amount.
- Amazon QuickSight or Power BI integration.
- Integrate email notification after processing invoices.
- Support decentralization according to user roles.
- Supports many other types of documents such as receipts, contracts or receipts.

---

## Final comments

Week 10 is the week of summarizing and completing all internship content. After studying along First Cloud Journey and implementing the Serverless AI Invoice Scanner project, I have gained more practical knowledge on how to build a serverless system on AWS.

The project helps me better understand how AWS services work together, from frontend, authentication, API, backend, storage, AI processing, database to monitoring and cleanup. This is an important experience that helps me consolidate my cloud knowledge and have a better foundation to continue learning and developing systems on AWS in the future.
