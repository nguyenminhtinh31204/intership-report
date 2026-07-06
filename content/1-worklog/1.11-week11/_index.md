---
title: "Worklog Week 11"
date: 2026-06-29
weight: 111
week: 11
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | June 29, 2026 - July 5, 2026 |
| Internship week | Week 11 |
| Phase | Completion stage after reporting |
| Project | Serverless AI Invoice Scanner |
| Main topic | Edit after comments, complete demo, check cleanup and package documents |
| Weekly goals | Final review of the project, editing according to comments, completing the submitted documents and ensuring AWS resources are fully tested |

---

## Week 11 Orientation

After week 10 has completed the summary report, proposal, Markdown document and cleanup checklist, week 11 focuses on final editing before official submission or presentation.

This week's focus is:

- Reread all written documents.
- Edit inconsistent content.
- Standardize terminology in reports.
- Check images, paths and Markdown structure.
- Prepare demo project according to a clear scenario.
- Final check of AWS resources.
- Pack documents and source code for handover.

---

## Week 11 Goals

The main goals for the week include:

- Review the entire document from Introduction to Cleanup.
- Correct confusion between Amazon Bedrock and OpenAI API.
- Standardize service names such as AWS Amplify Hosting, Amazon Textract, Amazon Cognito, and Amazon DynamoDB.
- Check the API routes in the documentation.
- Check the architectural diagram again.
- Check frontend and backend source code.
- Retest some important functions before demo.
- Prepare project presentation content.
- Check the availability of AWS resources to avoid incurring costs.
- Complete the final handover.

---

## Content implemented during the week

### Day 1 - Monday, June 29, 2026

The first day of week 11 focuses on re-reading the entire document and checking for content errors.

Implemented content:

- Review the project introduction documents.
- Recheck the system architecture description.
- Check the list of AWS services used.
- Test the parts that replaced Amazon Bedrock with OpenAI API.
- Check the Amazon Textract role description.
- Check the OpenAI API role description.
- Take notes on sections that need to be edited to make the document more consistent.

Results achieved:

- Detected some content that needs to be edited about the service name.
- Standardize project descriptions according to the actual system.
- Introduction documents are clearer and more accurate.

---

### Day 2 - Tuesday, June 30, 2026

Day two focuses on reviewing API Gateway and API documentation.

Implemented content:

- Review the list of API routes.
- Check the method and path of each endpoint.
- Compare the API in the documentation with the implemented API.
- Check the test with Postman.
- Check request body and sample response.
- Note common errors when calling API Gateway.

List of APIs reviewed:

```txt
POST /uploads
GET /invoice
GET /invoice/{id}
GET /invoice?name=<customer_name>
PATCH /invoice/tags/{id}
PATCH /invoice/starred/{id}
```

Results achieved:

- API routes in documentation are standardized.
- Test content using Postman is clearer.
- Reduce the possibility of wrong routes when others read and practice again.

---

### Day 3 - Wednesday, July 1, 2026

Day three focuses on testing source code and frontend environment variables.

Implemented content:

- Check the frontend environment configuration file again.
- Test API endpoints in React app.
- Check Cognito configuration:
  - AWS Region
  - User Pool ID
  - User Pool Client ID
- Check API upload configuration.
- Check invoice management API configuration.
- Check the variable `REACT_APP_SEND_AUTH_TOKEN`.
- Note the necessary environment variables when deploying with Amplify Hosting.

Environment variable example:

```txt
REACT_APP_AWS_REGION=ap-southeast-1
REACT_APP_USER_POOL_ID=ap-southeast-1_xxxxxxxxx
REACT_APP_USER_POOL_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxx
REACT_APP_API_UPLOAD_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/uploads
REACT_APP_API_INVOICE_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice
REACT_APP_API_UPDATE_TAGS_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice/tags
REACT_APP_API_UPDATE_STARRED_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice/starred
REACT_APP_SEND_AUTH_TOKEN=false
```

Results achieved:

- Identify required environment variables when deploying.
- Frontend is easier to reconfigure when switching environments.
- Reduce errors due to wrong endpoints or missing environment variables.

---

### Day 4 - Thursday, July 2, 2026

The fourth day focuses on retesting important functions of the system.

Implemented content:

- Test login and logout using Cognito.
- Test uploading invoices.
- Check uploaded files in S3.
- Check Lambda processing after a new file is available.
- Check data saved in DynamoDB.
- Test to see the invoice list.
- Test to see invoice details.
- Test search, tags and starred.
- Test Excel export.
- Check CloudWatch Logs for errors.

Results achieved:

- Main functions still work stably.
- Note some minor errors in data display.
- Prepare better for the final demo.

---

### Day 5 - Friday, July 3, 2026

Day five focuses on preparing demo scripts and presentation content.

Implemented content:

- Prepare demo scripts in clear order.
- Prepare sample invoice files for upload.
- Prepare data available in DynamoDB for illustration.
- Prepare an explanation of serverless architecture.
- Prepare a section explaining the role of each service.
- Prepare the AI ​​processing flow presentation.
- Prepare the cleanup resources presentation.

Expected demo scenario:

| Step | Demo content |
|---|---|
| 1 | Introducing the issue of manual invoice processing |
| 2 | Presenting Serverless AI Invoice Scanner architecture |
| 3 | Login to the frontend using Cognito |
| 4 | Upload invoice |
| 5 | Check files in S3 |
| 6 | Check data in DynamoDB |
| 7 | View list and invoice details |
| 8 | Demo search, tags, starred and export Excel |
| 9 | Check out CloudWatch Logs |
| 10 | Present cleanup resources |

Results achieved:

- Has a complete and easy-to-present demo script.
- Prepare sample data for demo.
- Content presented more clearly.

---

### Day 6 - Saturday, July 4, 2026

Day six focuses on examining cleanup resources and resources that may incur costs.

Implemented content:

- Check API Gateway again.
- Check Lambda Functions again.
- Check S3 Bucket.
- Check DynamoDB Table.
- Check Cognito User Pool.
- Check out Amplify Hosting App.
- Check CloudWatch Log Groups.
- Check IAM Roles and Policies.
- Check Secrets Manager if OpenAI API key is saved.
- Check Route 53 if there is a custom domain.

Checklist cleanup reviewed:

```txt
1. Delete API Gateway
2. Delete Lambda Functions
3. Empty and delete S3 Bucket
4. Delete DynamoDB Table
5. Delete Cognito User Pool
6. Delete Amplify Hosting App
7. Delete CloudWatch Log Groups
8. Delete unused IAM Roles and Policies
9. Review optional resources: Route 53, Secrets Manager, Parameter Store
```

Results achieved:

- Identify resources that need to be deleted after demo.
- Reduce the risk of unexpected costs.
- Checklist cleanup is more complete.

---

### Day 7 - Sunday, July 5, 2026

The weekend focuses on packing documents and summarizing week 11.

Implemented content:

- Synthesis of Markdown documents.
- Check file names and order of items.
- Check the worklog again.
- Check the edited proposal.
- Check cleanup documentation.
- Prepare folders or files for submission.
- Write the worklog for week 11.
- Take notes on the contents that need to be presented when defending the project.

Results achieved:

- Documents have been fully reviewed and arranged.
- Project is ready for demo, submission or handover.
- Complete the week of editing and finalizing the report.

---

## Summary of knowledge from Week 11

In week 11, I focus on editing, reviewing and completing the final content after the project is completed.

| Work group | Implemented content |
|---|---|
| Documentation Review | Check out the documentation Introduction, API, Frontend, Cleanup |
| API Review | Compare API routes with deployed system |
| Frontend Review | Check environment variables and Cognito/API configuration |
| Testing | Retest main functions |
| Demo Preparation | Prepare demo script and sample data |
| Cleanup Review | Review the AWS resources that need to be deleted |
| Handover | Packaging documents and handover content |

---

## Results achieved during the week

- Edit and standardize project documents.
- Check API Gateway routes again.
- Check the frontend configuration again.
- Retest main functions.
- Prepare project demo script.
- Review the cleanup checklist.
- Pack documents for handover.
- Project is ready for final presentation.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| Some document contents are not consistent | Review according to the actual architecture of the project |
| It's easy to confuse Amplify Hosting and Amplify backend | Specify that Amplify is only used to deploy frontend |
| Need to standardize many API routes | Create a table of methods, routes and functions |
| Demo needs to be brief but complete | Prepare the script according to the main processing flow |
| Cleanup has many resources to check out | Use checklist for each AWS service |

---

## Lesson learned

- After completing a project, reviewing documents is as important as writing code.
- Service names and architectural flows need to be consistent throughout the report.
- Demo project should follow a simple, easy-to-understand flow and demonstrate the main functionality.
- Checking cleanup helps avoid incurring costs after finishing the lab.
- Preparing sample data in advance helps make the demo smoother.
- Project cloud needs clear documentation so others can redeploy it.

---

## Development direction after week 11

If you continue to expand the project, you can do:

- Enable Cognito Authorizer for API Gateway.
- Transfer OpenAI API key to AWS Secrets Manager.
- Add SQS for asynchronous invoice processing.
- Add realtime processing status on frontend.
- Add invoice statistics dashboard.
- Add feature to edit extracted AI data.
- Add user permissions by role.
- Add report export function by month or by customer.

---

## Weekend comments

Week 11 is the week of editing and finishing after the project has been built. Through reviewing documents, re-testing APIs, preparing demos and checking cleanup, I better understand the process of completing a cloud project before handing over.

After this week, the **Serverless AI Invoice Scanner** project has more complete documentation, a clearer demo script and is ready for presentation or final report submission.
