---
title: "Worklog Week 8"
date: 2026-06-08
weight: 108
week: 8
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | June 8, 2026 - June 14, 2026 |
| Internship week | Week 8 |
| Phase | Project completion stage |
| Project | Serverless AI Invoice Scanner |
| Main topic | Complete frontend, end-to-end testing, deployment and documentation |
| Weekly goals | Complete the entire system, deploy the frontend using AWS Amplify Hosting, test the full processing flow and prepare the internship summary report |

---

## Orientation Week 8

Week 8 is the last week of the AWS internship and also the completion of the **Serverless AI Invoice Scanner** project. After previous weeks of deploying upload flows, AI invoice processing, and building data management APIs, this week focused on perfecting the user interface, connecting the entire system, end-to-end testing, and writing documentation.

The most important goal of this week is to ensure the system can operate in a complete flow:

```txt
User
    ↓
React Frontend
    ↓
Amazon Cognito
    ↓
Amazon API Gateway
    ↓
AWS Lambda
    ↓
Amazon S3
    ↓
Amazon Textract
    ↓
OpenAI API
    ↓
Amazon DynamoDB
    ↓
React Frontend
```

---

## Week 8 Goal

Key goals for the week include:

- Completing the React frontend interface.
- Amazon Cognito integration for user registration and login.
- Frontend integration with API Gateway endpoints.
- Completing the function of uploading invoices.
- Complete the function of viewing the list and invoice details.
- Complete the search function by customer name.
- Complete the function of updating tags and starred.
- Add filters by day, sort by day or total amount.
- Added the function of exporting invoice data to Excel.
- Deploy frontend using AWS Amplify Hosting.
- End-to-end testing of the entire system.
- Bug tracking by CloudWatch Logs.
- Complete the implementation manual and cleanup resources.
- Summarize the internship results.

---

## Content of the week

### Day 1 - Monday, June 8, 2026

The first day of week 8 focuses on reviewing the entire backend and preparing for full integration with the frontend.

Implemented content:

- Check the created Lambda functions:
  - `UploadInvoiceFileFunction`
  - `ProcessInvoiceFunction`
  - `InvoiceManagementFunction`
- Check the API Gateway routes:
  - `POST /uploads`
  - `GET /invoice`
  - `GET /invoice/{id}`
  - `GET /invoice?name=<customer_name>`
  - `PATCH /invoice/tags/{id}`
  - `PATCH /invoice/starred/{id}`
- Double check DynamoDB table `InvoiceData`.
- Double check S3 bucket and __ MASK0 __ folder.
- Check CloudWatch Logs of Lambda functions.
- Take note of outstanding errors before the frontend integration.

Results 

- Confirm the backend services are ready.
- Be able to check important endpoints.
- Prepare enough API endpoint information to configure the frontend.

---

### Day 2 - Tuesday, June 9, 2026

The second day focused on perfecting the React interface and configuring the environment variable for the frontend.

Implemented content:

- Update the __ MASK0 __file of the frontend.
- Configure Cognito User Pool ID, App Client ID and AWS Region.
- Configure endpoint APIs for upload, list, detail, search, tags and starred.
- Check the invoice upload interface.
- Check the interface of the invoice list.
- Check the invoice detail interface.
- Adjust the display of currency data according to `Currency`.
- Check data __ MASK0 __, `Starred`, `CustomerName`, `TotalAmount` and `InvoiceDate`.

Example frontend environment variable:

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

Results 

- The frontend is connected to the backend APIs.
- The interface displays invoice data more clearly.
- Environment variables are separated for easy editing when deploying.

---

### Day 3 - Wednesday, June 10, 2026

The third day focused on Amazon Cognito integration and checking login and registration flows.

Implemented content:

- Cognito integration with React via the __ MASK0 __ library.
- Check the sign-up function.
- Check the sign-in function.
- Check sign-out.
- Check the user session after logging in.
- Check that the interface only shows the main function after the user logs in.
- Note the role of Cognito in frontend authentication.

{{% notice info %}}
In this project, Cognito is used to protect the login and registration in the frontend. The API Gateway is only protected with Cognito if it has its own Cognito Authorizer configuration.
{{% /notice %}}

Results 

- Users can register and log in to the system.
- Frontend can use Cognito's session information.
- Completing the basic authentication layer for the application.

---

### Day 4 - Thursday, June 11, 2026

The fourth day focused on perfecting the frontend invoice management functions.

Implemented content:

- Completing the function of uploading invoices.
- Complete the function of viewing the list of invoices.
- Complete the function of viewing invoice details.
- Complete the invoice search by customer name.
- Complete updating tags for invoices.
- Completing starred update.
- Add filters on a daily basis.
- Replenish sort by day and total amount.
- Add and export data to Excel file.
- Check the status display when loading or when the API fails.

Completed frontend functions:

| Functionality | Status |
|---|---|
| Sign up / login | Complete |
| Invoice Upload | Completion |
| View Invoice List | Complete |
| View Invoice Details | Complete |
| Search by Client Name | Complete |
| Update tags | Complete |
| Update starred | Complete |
| Filter by date | Completed |
| Sort by date / total | Complete |
| Export Excel | Complete |

Results 

- Frontend has fully supported the main functions.
- Users can manipulate invoices directly on the interface.
- The data from the API is easier to understand.

---

### Day 5 - Friday, June 12, 2026

The fifth day focused on deploying frontend with **AWS Amplify Hosting**.

Implemented content:

- Put the frontend source code on GitHub repository.
- Connect GitHub repository to AWS Amplify Hosting.
- Configure build settings.
- Configure environment variables on Amplify.
- Run build and deploy frontend.
- Check build logs for errors.
- Go to the URL provided by Amplify.
- Check the frontend after deployment.

Frontend deployment flow:

```txt
GitHub Repository
    ↓
AWS Amplify Hosting
    ↓
Build React App
    ↓
Deploy
    ↓
Amplify Public URL
```

Some errors to pay attention to when deploying:

| Error | Possible Cause |
|---|---|
| Build failed | Lack of dependency or false build command |
| Environment variable missing | Environment variable not configured in Amplify |
| API call failed | Wrong API endpoint or CORS ERROR |
| Login failed | Wrong Cognito User Pool ID or App Client ID |
| Page reload error | No redirect configured for React Router |

Results 

- Frontend deployed successfully with AWS Amplify Hosting.
- The application has a URL to access on the browser.
- Know how to read Amplify build logs to check for deployment errors.

---

### Day 6 - Saturday, June 13, 2026

Day six focuses on end-to-end testing of the entire system.

Implemented content:

- Sign up and log in with Cognito.
- Upload an invoice file from the frontend.
- Check the file saved to S3.
- Check S3 trigger activates `ProcessInvoiceFunction`.
- Check Textract extract text.
- Check OpenAI API data standardization.
- Check the data saved to DynamoDB.
- Check the frontend showing new invoices.
- Check search, tags, starred, filter, sort and export Excel.
- Check CloudWatch Logs of Lambda functions.
- Make a note of the final errors to be handled.

End-to-end test flow:

```txt
Login
    ↓
Upload Invoice
    ↓
S3 Storage
    ↓
AI Processing
    ↓
DynamoDB Storage
    ↓
Invoice Management API
    ↓
Frontend Display
```

Results 

- Test the complete flow from frontend to backend.
- The system can process invoices and display results.
- Identify and handle some final errors before completing the project.

---

### Day 7 - Sunday, 6/14/2026

The last day focuses on completing documents, cleanup resources and summarizing internships.

Implemented content:

- Completing the project implementation manual.
- Complete the test documents with Postman.
- Finalize documents to deploy frontend.
- Write cleanup resources.
- Note the resources to be deleted after the end of the lab:
  - API Gateway
  - Lambda Functions
  - S3 Bucket
  - DynamoDB Table
  - Cognito User Pool
  - Amplify Hosting App
  - CloudWatch Log Groups
  - IAM Roles and Policies
- Optional resources such as Route 53 or Secrets Manager
- Summarize project results.
- Write a report on the end of week 8 and the end of the internship.

Results 

- Complete the project **Serverless AI Invoice Scanner**.
- Completing the manual.
- There is an AWS resource cleanup checklist.
- Summarize the entire internship process of 8 weeks.

---

## Review Week 8

In week 8, I completed the frontend, deployed the application with AWS Amplify Hosting, tested the entire system and completed the project documentation.

| Knowledge Group | Implemented Content |
|---|---|
| Frontend | Complete React UI and invoice management functions |
| Authentication | Amazon Cognito sign-up, sign-in, sign-out integration |
| Hosting | Deploy frontend using AWS Amplify Hosting |
| API Integration | Connecting frontend to API Gateway endpoints |
| Testing | End-to-end testing of the entire system |
| Monitoring | Check CloudWatch Logs and Amplify build logs |
| Documentation | Finalize deployment, test, and cleanup instructions |
| Cleanup | Prepare a list of resources to delete after the lab |

---

## Results of the week

- Complete frontend React.
- Integrate Cognito authentication.
- Connect the frontend to the API Gateway.
- Completing the function of uploading invoices.
- Complete the function of viewing the list and invoice details.
- Complete search, tags and starred.
- Added filter, sort and export Excel.
- Deploy frontend using AWS Amplify Hosting.
- End-to-end testing of the entire system.
- Finalize implementation documents and cleanup.
- Complete the project at the end of the internship.

---

## Difficulties encountered

| Difficulties | Directions |
|---|---|
| Frontend call CORS faulty API | Check CORS HEADERS in API Gateway and Lambda response |
| Cognito login not working properly | Check User Pool ID, App Client ID and Region |
| Amplify build failed | Check build logs, dependencies and environment variables |
| The frontend data shows the wrong format | Normalize the response from Lambda and re-map the field |
| Export Excel is missing fields | Check data before exporting |
| API run on Postman but error on frontend | Check URL, CORS and request headers |

---

Key learning

- When completing a cloud project, the frontend and backend need to unify data and endpoints.
- Amplify Hosting helps deploy frontend quickly but needs to configure the right environment variable.
- Cognito helps implement user authentication without building a login system from scratch.
- End-to-end testing is important because each individual part does not necessarily work properly.
- CloudWatch Logs and Amplify build logs are important tools for debugging bugs.
- Cleanup resources is a necessary step to avoid incurring costs after the end of the lab.
- Implementation documents make it easier for others to recreate the project.

---

## Wrap up the 4-week project

During the last 4 weeks of the internship, I applied the knowledge from First Cloud Journey to build the **Serverless AI Invoice Scanner** project.

| Week | Main content |
|---|---|
| Week 5 | Requirements analysis, architectural design, creation of S3, DynamoDB, Lambda upload, and API `POST /uploads` |
| Week 6 | Configure S3 trigger, Textract integration, OpenAI API and save data to DynamoDB |
| Week 7 | Building an Invoice Management API and frontend integration with backend |
| Week 8 | Finalize frontend, Cognito, Amplify Hosting, end-to-end testing, documentation, and cleanup |

---

## Wrap up 8 weeks of internship

After 8 weeks of AWS internship, the project learning and implementation process is divided into two phases:

| Period | Period | Outcome |
|---|---|---|
| Learning Period | Week 1 - Week 4 | First Cloud Journey Completion |
| Project Phase | Week 5 - Week 8 | Completion of the Serverless AI Invoice Scanner project |

Acquired knowledge and skills:

- Understand the AWS Cloud platform.
- Know how to use AWS Management Console.
- Understand core AWS services such as S3, Lambda, API Gateway, DynamoDB, Cognito, Amplify Hosting, and CloudWatch.
- Understand serverless and event-driven models.
- Know how to deploy frontend with AWS Amplify Hosting.
- Know how to build a backend with Lambda and API Gateway.
- Be able to process files with S3 Event Notification.
- Be able to integrate Textract and OpenAI API for AI invoice processing.
- Be able to save and manage data using DynamoDB.
- Know how to test APIs using Postman.
- Know how to debug errors with CloudWatch Logs.
- Be able to write implementation documents and cleanup resources.

---

## The final result of the project

Project **Serverless AI Invoice Scanner** has completed the main functions:

| Functionality | Status |
|---|---|
| Signing up / logging in users with Cognito | Complete |
| Upload invoice from frontend | Complete |
| Save invoice file to S3 | Complete |
| Automatically process files with S3 trigger | Complete |
| Extract text with Amazon Textract | Done |
| Standardize data using the OpenAI API | Complete |
| Save data to DynamoDB | Complete |
| Get Invoice List | Complete |
| View Invoice Details | Complete |
| Invoice Search | Complete |
| Update tags | Complete |
| Update starred | Complete |
| Filter, sort, and export Excel | Done |
| Deploy frontend using Amplify Hosting | Complete |
| Write cleanup resources document | Complete |

---

## End-of-Internship Comments

Week 8 is the completion and finalization of the project. After learning from First Cloud Journey and applying it to real projects, I have a better understanding of how to build a serverless application on AWS from frontend to backend. The project helps me practice many important services such as Amplify Hosting, Cognito, API Gateway, Lambda, S3, Textract, DynamoDB and CloudWatch.

At the end of the internship, I completed an AI-based invoice processing system with a serverless architecture, and gained experience in architectural design, deployment, testing, debugging, and documenting an actual cloud project.
