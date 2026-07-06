---
title: "Worklog Week 12"
date: 2026-07-06
weight: 112
week: 12
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | July 6, 2026 - July 12, 2026 |
| Internship week | Week 12 |
| Phase | End of internship period |
| Project | Serverless AI Invoice Scanner |
| Main topic | Complete the final version, present the project, hand over and summarize the internship |
| Weekly goals | Complete all documents, present project results, hand over source code/documents and summarize the knowledge gained during the internship |

---

## Week 12 Orientation

Week 12 is the final week of the AWS internship. After the project **Serverless AI Invoice Scanner** was built, tested, reviewed and edited in the previous weeks, this week focused on completing the final version, preparing the presentation, handing over documents and summarizing the entire internship process.

This week's focus includes:

- Check the entire project one last time.
- Complete the final report.
- Prepare project presentation content.
- Synthesize source code and documents.
- Check AWS resource cleanup.
- Record the results achieved.
- Evaluate limitations and propose development directions.
- Summarize skills and knowledge learned after the internship.

---

## Week 12 Goals

The main goals for the week include:

- Final review of frontend and backend source code.
- Review written Markdown documents.
- Complete the final internship report.
- Prepare demo project content.
- Recheck the main functions of the system.
- Confirm the list of AWS resources to keep or delete.
- Prepare handover files including source code, documents and worklog.
- Summary of lessons learned.
- Provide future development directions.
- Complete the week 12 workshop.

---

## Content implemented during the week

### Day 1 - Monday, July 6, 2026

The first day of week 12 focuses on reviewing the entire project before preparing the final submission.

Implemented content:

- Check the React frontend source code again.
- Check the Lambda functions again:
  - `UploadInvoiceFileFunction`
  - `ProcessInvoiceFunction`
  - `InvoiceManagementFunction`
- Check API Gateway routes again.
- Check DynamoDB table `InvoiceData` again.
- Check the S3 bucket to save the invoice file.
- Recheck Cognito configuration.
- Check Amplify Hosting App again.
- Take notes on completed parts and limited points.

Results achieved:

- Confirm the project has all main components.
- Grasp the final state of the system.
- Have a list of content that needs to be included in the summary report.

---

### Day 2 - Tuesday, July 7, 2026

The second day focuses on completing the internship report and project description documents.

Implemented content:

- Review the project introduction.
- Check the problem description and system goals.
- Complete the serverless architecture.
- Updated the description of used AWS services.
- Check the OpenAI API description instead of Amazon Bedrock.
- Update API routes and Lambda functions section.
- Check the results achieved of the project.

Components described in the report:

| Ingredients | Role |
|---|---|
| AWS Amplify Hosting | Deploy frontend React |
| Amazon Cognito | User registration and login |
| Amazon API Gateway | Provides REST API |
| AWS Lambda | Handling backend logic |
| Amazon S3 | Save invoice file |
| Amazon Textract | Extract text from invoice |
| OpenAI API | Standardize OCR data |
| Amazon DynamoDB | Save invoice data |
| Amazon CloudWatch | Monitor logs and debug |

Results achieved:

- The report has content consistent with the actual project.
- AWS services are clearly described.
- The architecture and processing flow are easier to understand.

---

### Day 3 - Wednesday, July 8, 2026

The third day focuses on preparing demo project content.

Implemented content:

- Prepare the final demo script.
- Prepare a test account to log in.
- Prepare sample invoice files for upload.
- Prepare sample data in DynamoDB.
- Check the frontend website deployed with Amplify.
- Check the demo steps in the correct order.
- Take notes on the architectural explanation when presenting.

Final demo script:

| Step | Presentation content |
|---|---|
| 1 | Introducing the problem of manual invoice processing |
| 2 | Presenting Serverless AI Invoice Scanner architecture |
| 3 | Login to the system with Cognito |
| 4 | Upload invoices from frontend |
| 5 | Check files in S3 |
| 6 | Check Lambda processing and CloudWatch Logs |
| 7 | Check data in DynamoDB |
| 8 | View list of invoices on frontend |
| 9 | Demo search, tags, starred, filter, sort and export Excel |
| 10 | Presenting cleanup resources and development direction |

Results achieved:

- Has complete demo script.
- Prepare data and sample files.
- Ready to present the project in a clear flow.

---

### Day 4 - Thursday, July 9, 2026

Day four focuses on retesting the entire end-to-end flow before the presentation.

Implemented content:

- Login to the frontend with Cognito.
- Upload invoice file from the interface.
- Check files saved in S3.
- Check S3 trigger calling `ProcessInvoiceFunction`.
- Check out Amazon Textract to extract text.
- Test OpenAI API for data normalization.
- Check data saved to DynamoDB.
- Check API to get list of invoices.
- Test the frontend displaying new data.
- Check tags, starred, search, filter, sort and export Excel.

End-to-end flow tested:

```txt
Cognito Login
    ↓
React Frontend Upload
    ↓
API Gateway
    ↓
UploadInvoiceFileFunction
    ↓
S3 uploads/
    ↓
ProcessInvoiceFunction
    ↓
Amazon Textract
    ↓
OpenAI API
    ↓
DynamoDB InvoiceData
    ↓
InvoiceManagementFunction
    ↓
React Frontend Display
```

Results achieved:

- The main processing thread operates stably.
- Frontend interface displays invoice data.
- Invoice management functions are ready for demo.

---

### Day 5 - Friday, July 10, 2026

Day five focuses on cleaning up resources and checking costs after project completion.

Implemented content:

- Review the list of created AWS resources.
- Check resources that need to be kept for demo.
- Check resources that can be deleted after submitting the report.
- Review the cleanup checklist.
- Check CloudWatch Log Groups.
- Check IAM Roles and Policies are no longer in use.
- Check Secrets Manager if OpenAI API key is saved.
- Check Route 53 if using a custom domain.
- Check AWS Billing/Cost Explorer at a basic level.

Final cleanup checklist:

```txt
1. Delete API Gateway
2. Delete Lambda Functions
3. Empty and delete S3 Bucket
4. Delete DynamoDB Table
5. Delete Cognito User Pool
6. Delete Amplify Hosting App
7. Delete CloudWatch Log Groups
8. Delete unused IAM Roles and Policies
9. Review Route 53, Secrets Manager and Parameter Store
10. Review AWS Billing / Cost Explorer
```

Results achieved:

- Have a clear list of resources that need to be cleaned up.
- Understand resource deletion order to avoid dependency errors.
- Reduce the risk of incurring costs after the internship ends.

---

### Day 6 - Saturday, July 11, 2026

Friday focuses on packing documents and preparing for handover.

Implemented content:

- Rearrange frontend source code.
- Rearrange Lambda/backend code.
- Synthesize Markdown document files.
- Summary of worklog from week 1 to week 12.
- Check the edited proposal.
- Check cleanup documentation.
- Check images and links in documents.
- Prepare a list of files that need to be submitted or handed over.

Handover content includes:

| Ingredients | Content |
|---|---|
| Source code frontend | React app |
| Backend code | Lambda functions |
| Documentation | Instructions for deployment and use |
| Proposal | Edited project proposal |
| Worklog | Weekly internship diary |
| Cleanup guide | Instructions for deleting AWS resources |
| Demo script | Project presentation script |

Results achieved:

- Documents and source code are clearly organized.
- There is enough content to submit or hand over.
- Limit errors when summarizing internships.

---

### Day 7 - Sunday, July 12, 2026

The last day focuses on summarizing the entire internship period.

Implemented content:

- Write the week 12 worklog.
- Summarize the learning and project making process.
- Evaluate achieved results.
- Record difficulties encountered.
- Summary of lessons learned.
- Propose future development directions.
- Complete the final handover.

Results achieved:

- Complete the week 12 workshop.
- Complete the internship summary.
- Project is ready for submission, demo or handover.
- Have an overview of the entire process of learning AWS and implementing serverless projects.

---

## Summary of knowledge for Week 12

In week 12, I focused on completing the final version, preparing demo, cleanup and handing over the project.

| Work group | Implemented content |
|---|---|
| Final Review | Check your project and AWS resources |
| Report Completion | Completing the internship report |
| Demo Preparation | Prepare the final demo script |
| End-to-End Testing | Retest the entire system flow |
| Cleanup Review | Check AWS resources and costs |
| Handover | Packaging source code and documentation |
| Final Summary | Summary of knowledge, skills and results achieved |

---

## Results achieved during the week

- Final check of the entire project.
- Complete the internship report.
- Prepare the final demo script.
- Retest the end-to-end flow.
- Review AWS resources and cleanup checklist.
- Package source code, documents and worklogs.
- Summary of practice results.
- Complete the last week of the AWS internship.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| Need to synthesize many different documents | Arrange by group: source code, docs, worklog, proposal, cleanup |
| The demo needs to show enough functionality but not be too long Prepare the script according to the main processing flow |
| Cleanup may affect the demo if deleted prematurely | Just write down the checklist, keep the necessary resources until the demo is finished |
| Some information in the document needs to be unified | Review service names and architectural flows |
| Need to summarize the weeks-long process | Divided into two stages: learning First Cloud Journey and doing projects |

---

## Lesson learned

- A cloud project needs to be complete in terms of functionality, documentation, testing and cleanup.
- Effective demos need a clear script and pre-prepared sample data.
- AWS resources need to be monitored and cleaned up after they are no longer in use.
- Learning from First Cloud Journey helps build a foundation before working on a real project.
- When working on a serverless project, you need to clearly understand the role of each service and how they connect with each other.
- CloudWatch Logs, Postman and deployment documentation are very important tools in the development process.
- The internship report should fully reflect the learning process, the work process and the results achieved.

---

## Summary of the entire internship period

The internship process is divided into two main stages:

| Phase | Time | Content |
|---|---|---|
| Phase 1 | Week 1 - Week 4 | Study and research documents according to the First Cloud Journey program |
| Phase 2 | Week 5 - Week 12 | Deploy, complete, review, demo and hand over the Serverless AI Invoice Scanner project |

During the learning phase, I became familiar with the fundamental knowledge of AWS Cloud, IAM, S3, Lambda, API Gateway, DynamoDB, CloudWatch, Cognito and Amplify Hosting.

During the project phase, I applied knowledge to build an AI invoice processing system based on serverless architecture, combining Amazon Textract, OpenAI API, Lambda, S3, DynamoDB and React frontend.

---

## Final result of the project

Project **Serverless AI Invoice Scanner** has completed the following main functions:

| Function | Status |
|---|---|
| Frontend React | Complete |
| Deploy using AWS Amplify Hosting | Complete |
| Sign up/log in with Cognito | Complete |
| Upload invoice | Complete |
| Save files to S3 | Complete |
| S3 trigger Lambda processing | Complete |
| OCR using Amazon Textract | Complete |
| Normalize data using OpenAI API | Complete |
| Save data to DynamoDB | Complete |
| Invoice Management API | Complete |
| Search, tags, starred | Complete |
| Filter, sort, export Excel | Complete |
| CloudWatch Logs | Complete |
| Cleanup documentation | Complete |

---

## Limitations still exist

Although the project has completed its main functions, there are still some limitations:

- API Gateway does not require Cognito Authorizer protection in all routes.
- OpenAI API keys should be managed using AWS Secrets Manager in production environments.
- There is no asynchronous processing queue using SQS.
- There is no realtime status for invoice processing.
- There is no function to edit invoice data after AI has extracted it.
- There is no advanced statistics dashboard yet.
- There is no detailed authorization according to user roles.

---

## Future development direction

If continued development, the project can expand further:

- Add Cognito Authorizer to API Gateway.
- Save OpenAI API key using AWS Secrets Manager.
- Add Amazon SQS for asynchronous invoice processing.
- Add realtime processing status on frontend.
- Allows users to edit extracted AI data.
- Integrate statistical dashboard using Amazon QuickSight or Power BI.
- Integrate email notification when invoice processing is complete.
- Supports many other types of documents such as receipts, contracts and receipts.
- Added user/admin permissions.
- Optimize prompt and validation to increase accuracy when extracting data.

---

## Final comments

Week 12 is the final week of the AWS internship. After completing the First Cloud Journey curriculum and the Serverless AI Invoice Scanner project, I have gained more practical knowledge about AWS Cloud, serverless architecture and the process of deploying a complete cloud application.

Through the project, I understood how to design the system, deploy frontend, build API, process files with Lambda, integrate AI, save data into DynamoDB, test with Postman, debug with CloudWatch and write resource cleanup documents.

The internship helps me consolidate my cloud computing knowledge and gain more hands-on experience with AWS services in a real-life problem.
