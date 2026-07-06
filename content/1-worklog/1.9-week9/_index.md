---
title: "Worklog Week 9"
date: 2026-06-15
weight: 109
week: 9
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | June 15, 2026 - June 21, 2026 |
| Internship week | Week 9 |
| Phase | Additional phase after project completion |
| Project | Serverless AI Invoice Scanner |
| Main topic | Review the system, optimize, complete documents and prepare for handover |
| Weekly goals | Review the entire project, handle remaining errors, complete reports, prepare demos and clean up AWS resources |

---

## Orientation Week 9

After week 8 has completed the **Serverless AI Invoice Scanner** project, week 9 is used as an additional week to review the entire system, check for outstanding errors, optimize documents and prepare to hand over the internship results.

This week's focus is not on building new mega-functions, but on:

- Check the entire operation flow of the system.
- Fix small errors that still exist.
- Optimize the user experience on the frontend.
- Review CloudWatch Logs.
- Examine AWS costs and resources.
- Finalize the internship report.
- Prepare project demo content.
- Implement or note the cleanup resources process.

---

## Week 9 Goals

The main goals for the week include:

- Retest the entire end-to-end flow.
- Test deployed APIs.
- Review data in DynamoDB.
- Check the invoice file in S3.
- Check Lambda and API Gateway logs in CloudWatch.
- Check the frontend again after deploying with Amplify Hosting.
- Complete system user manual documents.
- Complete cleanup resources documentation.
- Prepare slides or demo presentation content.
- Summary of achieved results and limitations of the project.
- Propose future development directions.

---

## Content implemented during the week

### Day 1 - Monday, June 15, 2026

The first day of week 9 focuses on reviewing the overall system after completion in week 8.

Implemented content:

- Check the overall architecture of the project.
- Reconcile created AWS resources with the architecture diagram.
- Test Lambda functions:
  - `UploadInvoiceFileFunction`
  - `ProcessInvoiceFunction`
  - `InvoiceManagementFunction`
- Check API Gateway routes.
- Check S3 bucket and directory `uploads/`.
- Check DynamoDB table `InvoiceData`.
- Take notes on points that need to be edited or optimized.

Results achieved:

- Confirm major system components still work.
- Understand the list of AWS resources in use.
- There is a list of small errors and points that need to be improved during the week.

---

### Day 2 - Tuesday, June 16, 2026

The second day focused on backend API testing using Postman.

Implemented content:

- Test the invoice upload API:

```txt
POST /uploads
```

- Test the API to get a list of invoices:

```txt
GET /invoice
```

- Test API to get invoice details:

```txt
GET /invoice/{id}
```

- Test API to search invoices by customer name:

```txt
GET /invoice?name=<customer_name>
```

- Test tags update API:

```txt
PATCH /invoice/tags/{id}
```

- Testing the updated API starred:

```txt
PATCH /invoice/starred/{id}
```

- Check the response format of each API.
- Check for error cases such as wrong ID, missing body or wrong route.

Results achieved:

- Confirm the main APIs work stably.
- Detect and note some small errors in response format.
- Better understand how to test APIs before handing over the project.

---

### Day 3 - Wednesday, June 17, 2026

Day three focuses on frontend testing and user experience.

Implemented content:

- Test the registration and login interface with Cognito.
- Test the invoice upload function from the frontend.
- Check the invoice list interface.
- Check the invoice details page.
- Test the search function.
- Check the tags and starred function.
- Check filter by date.
- Check sort by date and total amount.
- Check Excel export.
- Note down points that need to be improved in the interface.

Some test points on the frontend:

| Function | Test content |
|---|---|
| Login / Sign-up | Users can login and register |
| Upload | File is sent correctly to API |
| Invoice List | Invoice list displays correctly |
| Details | Invoice information is fully displayed |
| Search | Find invoices by customer name |
| Tags | Added and updated tags successfully |
| Starred | Mark important invoices |
| Export Excel | Export invoice data to Excel file |

Results achieved:

- Frontend works properly with main functions.
- Note minor errors in data display.
- Improved user experience before demo.

---

### Day 4 - Thursday, June 18, 2026

Day four focuses on log review, system errors, and resource costs.

Implemented content:

- Check CloudWatch Log Groups of Lambda functions.
- Review the invoice upload error log.
- Review Textract and OpenAI API processing logs.
- Check DynamoDB errors if any.
- Check logs related to CORS or API Gateway.
- Check if AWS resources are still active.
- Note resources that may incur costs.

Resources to watch out for:

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

- Understand the system log status.
- Determine which resources need to be kept for demo.
- Determine which resources need to be cleaned up after the internship ends.

---

### Day 5 - Friday, June 19, 2026

The fifth day focuses on completing documents and project reports.

Implemented content:

- Review project introduction documents.
- Update system architecture.
- Updated the description of the AWS services used.
- Update API Gateway routes section.
- Updated Lambda functions section.
- Update the DynamoDB table section.
- Update the frontend and Amplify Hosting.
- Update the cleanup resources section.
- Review the written content to ensure consistency.

Documents reviewed:

| Documents | Content |
|---|---|
| Introduction | Project overview and used services |
| Architecture | System diagram and processing flow |
| API Gateway | List of endpoints |
| Lambda | Description of backend functions |
| Frontend | Instructions for deploying and using |
| Testing | Testing with Postman and frontend |
| Cleanup | Delete the AWS resource after lab |

Results achieved:

- Project documents are clearer and more consistent.
- OpenAI API usage parts have been updated instead of Bedrock.
- Cleanup resources content is more complete.

---

### Day 6 - Saturday, June 20, 2026

The sixth day focuses on demo preparation and synthesizing practice results.

Implemented content:

- Prepare project demo script.
- Arrange presentation order:
  1. Introduce the problem.
  2. Introduction to architecture.
  3. Demo login.
  4. Demo invoice upload.
  5. AI processing demo.
  6. Demo view invoice list.
  7. Demo search, tags, starred and export Excel.
  8. Demo CloudWatch Logs.
9. Present cleanup resources.
- Take notes on project highlights.
- Note any remaining limitations.
- Propose further development directions.

Results achieved:

- There is a clear demo script.
- Have content presenting project results.
- Prepare a summary for the internship report.

---

### Day 7 - Sunday, June 21, 2026

The weekend is used to summarize week 9 and complete the handover content.

Implemented content:

- Summary of all achieved results.
- Review document files, worklogs and reports.
- Complete the list of resources that need to be cleaned up.
- Take notes on lessons learned after doing the project.
- Summary of future development directions.
- Write the week 9 workshop report.

Results achieved:

- Complete the additional week after the project.
- Project is ready for presentation and handover.
- Have complete documents and cleanup checklist.
- Have an improvement orientation if the project continues to develop.

---

## Summary of Week 9 knowledge

In week 9, I focused on reviewing, optimizing, retesting and completing documents for the project **Serverless AI Invoice Scanner**.

| Work group | Implemented content |
|---|---|
| System Review | Recheck all AWS resources |
| Backend Testing | API Testing with Postman |
| Frontend Testing | Test user interface and functionality |
| Monitoring | Review CloudWatch Logs |
| Cost Review | Checking resources may incur costs |
| Documentation | Complete deployment documentation and cleanup |
| Demo Preparation | Prepare demo project script |
| Handover | Summary of results and handover content |

---

## Results achieved during the week

- Review the entire system.
- Retest main APIs.
- Check the frontend after deploying.
- Check CloudWatch Logs.
- Complete project documents.
- Complete the cleanup resources checklist.
- Prepare demo script.
- Summarize the results and limitations of the project.
- Prepare to hand over the project after the internship.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| There are many AWS resources to check | Make a list of each service to review |
| Some errors only appear when testing end-to-end | Check out each step from frontend to backend |
| Response API has inconsistent fields | Re-standardize data mapping in Lambda and frontend |
| CloudWatch Logs has many logs that are difficult to track | Filter by time and by Lambda function |
| Need to prepare a brief but meaningful demo Write a demo script with each main step |
| Cleanup easily deletes resources by mistake | Specify the name of the resource belonging to the project before deleting |

---

## Lesson learned

- After completing the function, it is necessary to have time to retest the entire system.
- A cloud project needs to check both backend, frontend, database, logs and costs.
- Clear documentation makes the project handover and presentation process easier.
- Cleaning up resources is an important step to avoid incurring unwanted costs.
- When demoing a project, you should prepare sample data and presentation scripts.
- Reviewing the architecture helps detect inconsistencies in documentation and implementation.

---

## Future development direction

If the project continues to develop, the following functions can be added:

- More detailed user permissions.
- Protect API Gateway with Cognito Authorizer.
- Save OpenAI API key using AWS Secrets Manager.
- Add SQS queue for asynchronous invoice processing.
- Add realtime processing status to the frontend.
- Automatically classify invoices by expense type.
- Integrate statistical dashboard with Amazon QuickSight.
- Add function to edit invoice data after AI extracts.
- Integrate email notification after invoice processing is completed.
- Supports more invoice formats and currencies.

---

## Weekend comments

Week 9 is an additional week to help you review and complete the project after the main implementation phase. Through retesting the system, checking logs, reviewing costs, completing documents and preparing demos, I better understand that a cloud project does not just stop at running functions but also needs to be tested, monitored, optimized, written documents and prepared to cleanup resources.

After this week, the **Serverless AI Invoice Scanner** project is ready for presentation, handover and can continue to develop further in the future.
