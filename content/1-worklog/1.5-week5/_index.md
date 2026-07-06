---
title: "Worklog Week 5"
date: 2026-05-18
weight: 105
week: 5
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | May 18, 2026 - May 24, 2026 |
| Internship week | Week 5 |
| Phase | Project implementation phase |
| Project | Serverless AI Invoice Scanner |
| Main topic | Requirements analysis, architectural design, and platform resource deployment |
| Weekly goals | Start building a project based on the knowledge learned from First Cloud Journey |

---

## Week 5 Orientation

After completing 4 weeks of studying under the **First Cloud Journey** program, week 5 begins the implementation phase of the **Serverless AI Invoice Scanner** project.

This week, the focus is on system requirements analysis, overall architecture design, and initial deployment of foundational AWS resources. This is an important preparation step before integrating AI processing with Amazon Textract and OpenAI API in the following weeks.

---

## Week 5 Goals

The main goals for the week include:

- Analyze system functional requirements.
- Determine the AWS services to use in the project.
- Design the overall architecture of the system.
- Create Amazon S3 bucket to save invoice files.
- Create DynamoDB table to store invoice data.
- Create a Lambda function to handle file uploads.
- Create API Gateway route `POST /uploads`.
- Test file upload using Postman.
- Monitor error logs with Amazon CloudWatch.
- Take note of errors encountered during deployment.

---

## Content implemented during the week

### Day 1 - Monday, May 18, 2026

The first day of week 5 focuses on analyzing project requirements and determining implementation scope.

Implemented content:

- Determine the goal of the project **Serverless AI Invoice Scanner**.
- Analyze the main functions of the system:
  - Upload invoice file.
  - Save invoice files to Amazon S3.
  - Processing invoices with AI.
  - Save invoice data to DynamoDB.
  - Display and manage data on the frontend.
- Identify the main components in the architecture.
- Take note of the AWS services you need to use.

Services expected to be used:

| Services | Role |
|---|---|
| AWS Amplify Hosting | Deploy frontend React |
| Amazon Cognito | User registration, login |
| Amazon API Gateway | Create REST API for frontend |
| AWS Lambda | Handling backend logic |
| Amazon S3 | Save invoice file |
| Amazon Textract | Extract text from invoice |
| OpenAI API | Standardize OCR data |
| Amazon DynamoDB | Save invoice data |
| Amazon CloudWatch | Logging and debugging |
| AWS IAM | Manage access rights |

Results achieved:

- Clearly define the project's goals.
- Understand the scope of functions that need to be deployed.
- There is a list of AWS services to use.

---

### Day 2 - Tuesday, May 19, 2026

The second day focuses on the overall architectural design of the system.

Implemented content:

- Draw the main processing flow of the system.
- Determine how the frontend communicates with the backend.
- Define invoice upload API.
- Determine where to save the original file and where to save the processed data.
- Determine the Lambda functions that need to be created in the project.

Overall architectural flow:

```txt
React Frontend
    ↓
Amazon API Gateway
    ↓
UploadInvoiceFileFunction
    ↓
Amazon S3
    ↓
S3 Event Trigger
    ↓
ProcessInvoiceFunction
    ↓
Amazon Textract
    ↓
OpenAI API
    ↓
Amazon DynamoDB
    ↓
InvoiceManagementFunction
    ↓
React Frontend
```

Main Lambda functions:

| Lambda Function | Role |
|---|---|
| `UploadInvoiceFileFunction` | Receive files from API Gateway and upload to S3 |
| `ProcessInvoiceFunction` | Process files from S3, call Textract and OpenAI API |
| `InvoiceManagementFunction` | Query, search and update invoice data |

Results achieved:

- Complete the overall process flow design.
- Identify 3 main Lambda functions.
- Understand the processing order from uploading files to saving data.

---

### Day 3 - Wednesday, May 20, 2026

Day three focuses on creating the **Amazon S3 bucket** for the project.

Implemented content:

- Create S3 bucket to save invoice files.
- Configure bucket according to selected region.
- Check the block public access option.
- Create logical directory `uploads/`.
- Note how to name the object when uploading.
- Check bucket access rights.

Expected storage structure:

```txt
s3://invoice-scanner-upload-bucket/uploads/
```

Role of S3 in the project:

- Save the original invoice file.
- Is the place to receive files from Lambda upload.
- Activate Lambda processing when there is a new file.
- Save PDF, PNG, JPG or JPEG files.

Results achieved:

- Create S3 bucket for project.
- Understand the role of the `uploads/` folder.
- Prepare a place to save input files for the system.

---

### Day 4 - Thursday, May 21, 2026

Day four focuses on creating a **DynamoDB table** to store invoice data.

Implemented content:

- Create DynamoDB table named `InvoiceData`.
- Determine the primary key as `InvoiceId`.
- Design the main data fields that need to be saved.
- Learn how to save JSON data in DynamoDB.
- Note fields for search, tags and starred.

Expected data structure:

```json
{
  "InvoiceId": "invoice-001",
  "CustomerName": "Customer Name",
  "InvoiceNumber": "INV-001",
  "InvoiceDate": "2026-05-21",
  "TotalAmount": 100000,
  "Currency": "VND",
  "Tags": [],
  "Starred": false,
  "ExtractedData": {}
}
```

Important fields:

| School | Role |
|---|---|
| `InvoiceId` | Invoice identifier |
| `CustomerName` | Customer name |
| `InvoiceNumber` | Invoice number |
| `InvoiceDate` | Invoice date |
| `TotalAmount` | Total amount |
| `Currency` | Currency |
| `Tags` | Invoice classification labels |
| `Starred` | Mark important invoices |
| `ExtractedData` | Extracted AI data |

Results achieved:

- Create DynamoDB table `InvoiceData`.
- Determine the initial data structure.
- Prepare the database for the next processing steps.

---

### Day 5 - Friday, May 22, 2026

Day five focuses on creating the first Lambda function: **UploadInvoiceFileFunction**.

Implemented content:

- Create a new Lambda function.
- Choose a suitable runtime for the backend.
- Configure Lambda handler.
- Create or test IAM execution role.
- Write logic to handle file upload requests.
- Learn how to decode Base64 files.
- Learn how to upload objects from Lambda to S3.
- Check Lambda run log using CloudWatch.

Lambda processing flow:

```txt
Receive request from API Gateway
    ↓
Read filename, contentType and Base64 file
    ↓
Decode Base64
    ↓
Upload files to S3 /uploads
    ↓
Return response to client
```

Results achieved:

- Create `UploadInvoiceFileFunction`.
- Understand how Lambda receives requests from API Gateway.
- Know that Lambda needs IAM permissions to write files to S3.

---

### Day 6 - Saturday, May 23, 2026

Day six focused on creating the API Gateway route for the upload function.

Implemented content:

- Create API Gateway for project.
- Create routes:

```txt
POST /uploads
```

- Connect the route to `UploadInvoiceFileFunction`.
- Configure stage deployment.
- Check the endpoint after deploying.
- Learn about common errors when calling API Gateway.
- Note the required CORS configuration when the frontend calls the API.

Errors requiring attention:

| Error | Possible causes |
|---|---|
| `Missing Authentication Token` | Wrong path, wrong method or not yet deployed API stage |
| CORS error | CORS is not configured or response headers are missing |
| 500 Internal Server Error | Lambda has logic error or returns response in wrong format |
| Access denied | Lambda lacks S3 access |

Results achieved:

- Create route `POST /uploads`.
- Connect API Gateway with Lambda upload.
- There is an endpoint for testing with Postman.

---

### Day 7 - Sunday, May 24, 2026

The weekend focuses on upload testing and synthesizing results.

Implemented content:

- Create test request on Postman.
- Send request `POST /uploads` to API Gateway.
- Check if Lambda received the request or not.
- Check if the file is saved to S3 or not.
- Read logs in CloudWatch to find errors.
- Summary of resources created during the week.
- Prepare a plan for week 6.

Example request body used for testing:

```json
{
  "filename": "invoice-test.png",
  "contentType": "image/png",
  "file": "base64_string_here"
}
```

Results achieved:

- Test the upload API using Postman.
- Check files in S3.
- Know how to debug errors using CloudWatch Logs.
- Complete the initial foundation of the project.

---

## Summary of Week 5 knowledge

In week 5, I started implementing the project **Serverless AI Invoice Scanner** after learning First Cloud Journey. The focus is on building the first invoice upload flow from API Gateway to Lambda and S3.

| Knowledge group | Implemented content |
|---|---|
| Project Analysis | Analyze requirements and project scope |
| Architecture Design | Overall process flow design |
| Storage | Create S3 bucket and directory `uploads/` |
| Database | Create DynamoDB table `InvoiceData` |
| Backend | Create `UploadInvoiceFileFunction` |
| API | Create route `POST /uploads` |
| Testing | Test upload using Postman |
| Monitoring | Debug errors using CloudWatch Logs |
| Security | Check IAM Role for Lambda Accessing S3 |

---

## Results achieved during the week

- Complete project requirements analysis.
- Complete the overall architectural design.
- Create S3 bucket to save invoice files.
- Create DynamoDB table `InvoiceData`.
- Create Lambda function `UploadInvoiceFileFunction`.
- Create API Gateway route `POST /uploads`.
- Test upload using Postman.
- Check logs with CloudWatch.
- Understand the file upload flow in serverless architecture.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| Not familiar with connecting API Gateway with Lambda | Check integration and stage deploy |
| Lambda has not uploaded files to S3 | Check IAM Role and permissions `s3:PutObject` |
| Base64 requests are easily formatted wrong | Standardize body test on Postman |
| Getting error `Missing Authentication Token` | Check the method, route and stage URL |
| Difficult to read initial Lambda errors | Use CloudWatch Logs to view details |

---

## Lesson learned

- Need to design a clear architecture before creating AWS resources.
- API Gateway is just a request receiving point, the main processing logic is in Lambda.
- Lambda needs the appropriate IAM Role to access S3 and log to CloudWatch.
- S3 should be configured to block public access to protect data.
- Postman is very useful for testing APIs before frontend integration.
- CloudWatch Logs is an important tool for debugging errors in serverless systems.

---

## Plan for Week 6

In the next week, I will continue to implement invoice processing using AI after the file has been uploaded to S3.

Expected content:

- Configure S3 Event Notification.
- Create `ProcessInvoiceFunction`.
- Connect S3 trigger with Lambda processing.
- Integrate Amazon Textract to OCR invoices.
- Learn how to get text from Textract results.
- Connect to OpenAI API to normalize OCR data.
- Save invoice data to DynamoDB.
- Check processing logs with CloudWatch.
- Note errors and complete deployment documentation.

---

## Weekend comments

Week 5 is the first week to start implementing the actual project. After learning the AWS platform for the first 4 weeks, I applied the knowledge to architectural design and created the first resources for the system. The most important result of the week is to build a basic invoice upload flow from API Gateway to Lambda and S3, which is the foundation for AI processing in the following week.
