+++
title = "Workshop"
weight = 5
chapter = false
pre = "<b>5. </b>"
+++

# Workshop

## Overview

In this workshop section, we will build the backend API layer for the **Serverless AI Invoice Scanner** project.

This part focuses on the tasks handled by the **Backend API Developer** role, including:

- Building **Amazon API Gateway** routes.
- Creating the **Upload Lambda** function.
- Creating the **Fetch Invoice Lambda** function.
- Connecting Lambda with **Amazon S3**.
- Connecting Lambda with **Amazon DynamoDB**.
- Configuring CORS for frontend integration.
- Testing API endpoints using Postman or frontend requests.

The goal of this section is to create a working serverless backend that allows the React frontend to upload invoice files, retrieve invoice data, search invoices, and update invoice information.

---

## Backend API Architecture

The backend API workflow of the project is shown below:

```txt
React Frontend
    ↓
Amazon API Gateway
    ↓
AWS Lambda
    ↓
Amazon S3 / Amazon DynamoDB
```

The project uses two main Lambda functions:

| Lambda Function | Purpose |
|---|---|
| `UploadInvoiceFileFunction` | Receives invoice upload requests from API Gateway, saves files to S3, and also processes files when triggered by S3. |
| `FetchInvoiceDetailsFunction` | Retrieves, searches, and updates invoice data from DynamoDB through API Gateway requests. |

---

## Workshop Sections

This workshop contains **6 smaller sections**. Each section focuses on one part of the backend API implementation.

---

### 5.1 Create S3 Bucket

[Go to section 5.1](/5-workshop/5.1-create-s3-bucket/)

In this section, we will create an **Amazon S3 Bucket** to store uploaded invoice files.

The bucket is used as the main file storage layer of the project. Uploaded invoices will be saved under the `uploads/` prefix.

Main tasks:

- Create an S3 bucket.
- Configure bucket name and AWS Region.
- Keep Block Public Access enabled.
- Prepare the `uploads/` folder prefix.
- Verify that Lambda can upload files to the bucket.

---

### 5.2 Create DynamoDB Table

[Go to section 5.2](/5-workshop/5.2-create-dynamodb-table/)

In this section, we will create the **Amazon DynamoDB** table used to store processed invoice data.

The table name used in this project is:

```txt
InvoiceData
```

Main tasks:

- Create DynamoDB table `InvoiceData`.
- Configure `InvoiceId` as the partition key.
- Prepare the table for storing extracted invoice data.
- Understand the fields used by the frontend, such as `CustomerName`, `InvoiceDate`, `TotalAmount`, `Tags`, and `Starred`.

---

### 5.3 Create Upload Lambda Function ,Configure S3 Trigger for Upload Lambda

[Go to section 5.3](/5-workshop/5.3-create-upload-lambda/)

In this section, we will create the **UploadInvoiceFileFunction**,configure an **S3 ObjectCreated trigger** for `UploadInvoiceFileFunction`

This function receives invoice files from API Gateway, decodes the base64 file content, and saves the uploaded file to Amazon S3.

Main tasks:

- Create `UploadInvoiceFileFunction`.
- Configure Lambda runtime and handler.
- Add environment variables such as `BUCKET_NAME` and `DYNAMO_TABLE_NAME`.
- Decode base64 file content from frontend upload requests.
- Save uploaded files to S3 under the `uploads/` prefix.
- Return JSON response to the frontend.
- Configure S3 Event Notification.
- Trigger Lambda when a new object is created under `uploads/`.
- Read bucket name and object key from the S3 event.
- Process supported file types: `.png`, `.jpg`, `.jpeg`, and `.pdf`.
- Prepare the function for OCR and AI processing.

---

### 5.5 Configure API Gateway Upload Route

[Go to section 5.5](/5-workshop/5.4-configure-api-gateway-upload/)

In this section, we will create the API Gateway route for uploading invoices.

The upload route is:

```txt
POST /uploads
```

Main tasks:

- Create an API Gateway API.
- Add the `POST /uploads` route.
- Connect the route to `UploadInvoiceFileFunction`.
- Enable CORS for frontend requests.
- Deploy the API stage.
- Test invoice upload using Postman or frontend.

---

### 5.6 Create Fetch Invoice Lambda Function

[Go to section 5.6](/5-workshop/5.5-create-fetch-invoice-lambda/)

In this section, we will create the **FetchInvoiceDetailsFunction**.

This function is responsible for retrieving, searching, and updating invoice data stored in DynamoDB.

Main tasks:

- Create `FetchInvoiceDetailsFunction`.
- Connect the function to DynamoDB table `InvoiceData`.
- Retrieve all invoices.
- Retrieve invoice details by `InvoiceId`.
- Search invoices by customer name.
- Update invoice tags.
- Update invoice starred status.
- Return normalized JSON data to the frontend.

---

### 5.7 Configure Invoice Management API Routes

[Go to section 5.7](/5-workshop/5.6-configure-invoice-management-api/)

In this section, we will configure the API Gateway routes for invoice management.

The invoice management routes include:

```txt
GET /invoice
GET /invoice/{id}
GET /invoice?name=<customer_name>
GET /invoice/starred
PATCH /invoice/tags/{id}
PATCH /invoice/starred/{id}
```

Main tasks:

- Create GET and PATCH routes in API Gateway.
- Connect the routes to `FetchInvoiceDetailsFunction`.
- Configure CORS headers.
- Test each API route using Postman.
- Verify data returned from DynamoDB.
- Check API Gateway and Lambda logs in CloudWatch.

---

## Expected Result

After completing this workshop section, the backend API layer will be ready for frontend integration.

The system will be able to:

- Receive invoice upload requests from the frontend.
- Save uploaded invoice files to Amazon S3.
- Trigger Lambda processing from S3 ObjectCreated events.
- Store processed invoice results in DynamoDB.
- Retrieve invoice data from DynamoDB.
- Search invoice records.
- Update tags and starred status.
- Return JSON responses to the React frontend.

---

## Backend API Flow Summary

```txt
1. User uploads an invoice from React Frontend.

2. React Frontend sends POST /uploads to API Gateway.

3. API Gateway invokes UploadInvoiceFileFunction.

4. UploadInvoiceFileFunction saves the uploaded file to S3.

5. S3 ObjectCreated trigger invokes UploadInvoiceFileFunction again.

6. UploadInvoiceFileFunction processes the file and stores the result in DynamoDB.

7. React Frontend sends GET or PATCH invoice requests to API Gateway.

8. API Gateway invokes FetchInvoiceDetailsFunction.

9. FetchInvoiceDetailsFunction queries or updates DynamoDB.

10. API Gateway returns invoice data to the frontend.
```

---

## Notes

{{% notice info %}}
This workshop section focuses on the backend API layer. Frontend UI implementation, Cognito authentication, and Amplify Hosting deployment can be documented in separate sections.
{{% /notice %}}

{{% notice warning %}}
Make sure Lambda functions have the correct IAM permissions before testing the APIs. Missing permissions may cause `AccessDenied` errors when Lambda accesses S3, DynamoDB, Textract, or CloudWatch Logs.
{{% /notice %}}

{{% notice info %}}
For testing, you can use Postman before connecting the APIs to the React frontend. This helps verify that each backend route works correctly.
{{% /notice %}}
