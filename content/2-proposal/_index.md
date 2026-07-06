+++
title = "Proposal"
weight = 2
+++

# 🧾 Serverless AI Invoice Scanner – Solution to automate invoice extraction and management using AI on the AWS platform

> 🔍 *An intelligent system that helps users upload image or PDF invoices, automatically extract content using Amazon Textract, normalize data using OpenAI API, store structured information into Amazon DynamoDB, and manage invoices through a React web interface deployed with AWS Amplify Hosting.*

---

Summary of the project 

In the context of strong digital transformation, the automation of input invoice processing is becoming a necessity for many businesses. Invoices often exist in multiple formats such as PDFs, photos, scans, or unstructured documents. This makes it difficult to extract, test, store, and retrieve data.

**Serverless AI Invoice Scanner** is built to solve this problem through an automated invoice processing system based on artificial intelligence and serverless architecture on AWS. The system allows users to upload invoices, use **Amazon Textract** to extract text, and then use the **OpenAI API** to analyze and standardize invoice data into a clear structure such as invoice number, customer name, invoice date, total amount, currency, and related information.

The processed data is saved to **Amazon DynamoDB**, enabling fast retrieval through APIs deployed using **Amazon API Gateway** and **AWS Lambda**. The user interface is built with **ReactJS**, deployed with **AWS Amplify Hosting**, and integrates **Amazon Cognito** to support user registration and login.

{{% notice info %}}
In the current version of the project, the system uses the **OpenAI API** instead of Amazon Bedrock. The OpenAI API is a service outside of AWS, so the API key needs to be securely stored in the backend, for example in Lambda environment variables or AWS Secrets Manager.
{{% /notice %}}

### 🎯 Featured Benefits

- **Automate the data entry process**: Reduce the time it takes to read and enter invoices manually.
- **Increase accuracy**: Combines the OCR of Amazon Textract and the semantic analysis capabilities of OpenAI API.
- **Easy to retrieve data**: Invoices are saved as structured data in DynamoDB.
- **Visual management**: The frontend supports list view, detail view, search, tags, starred invoices, and Excel export.
- **User security**: Amazon Cognito integration supports registration and login.
- **Easy to scale**: The serverless architecture helps the system automatically scale with request volume.

---

## ❗ 1. Problem statement

### 🧾 Current situation

Many businesses, especially small and medium-sized enterprises, still process input invoices manually or semi-automatically. Accounting staff often have to open each invoice file, read important fields such as invoice number, issue date, customer name, total amount, tax and sales unit, then re-enter it into the management software.

This procedure has some limitations:

- Spends a lot of time when the number of invoices increases.
- Human data entry errors are likely to occur.
- Difficult to search for data when invoices are only saved as image files or PDFs.
- Difficult to collect statistics, compare and audit.
- Difficult to integrate with data management or reporting systems.

➡️ **The need** is to build a system that can receive multi-format invoices, automatically extract content, standardize data using AI, centrally store and support quick retrieval.

### ⚠️ Key challenges

1. **Diverse invoice formats**  
   Invoices can be PDFs, photos, scans or images of varying quality.

2. **Unstructured data**  
   Invoice content often does not follow the same fixed format, making it difficult to extract information.

3. **Errors when entering data manually**  
   Humans can enter wrong amounts, dates, billing codes, or customer names.

4. **Difficult to search and classify**  
   If you only save invoices as files, searching by customer, date, amount or processing status will be difficult.

5. **Data security requirements**  
   Invoices may contain important financial or business information that needs to be protected when stored and transmitted.

6. **Need to expand the system**  
   When the number of users or the number of invoices increases, the system needs to be able to scale without the need for manual server management.

### 👥 Impact on stakeholders

| Related parties | Impact |
|---|---|
| **Accounting – Finance** | Reduce repetitive data entry work, save time processing invoices. |
| **Business Management** | Have centralized invoice data, easy to check and track. |
| **Internal Audit** | Easily retrieve invoices and related data when reconciliation is needed. |
| **IT Department** | Having a serverless system is easy to deploy, easy to maintain, and does not require server operation. |
| **End User** | Has an intuitive interface to upload, view, search and manage invoices. |

### 💥 Consequences if not resolved

- Increased operating costs due to heavy reliance on manual data entry.
- Accounting data errors easily arise.
- Difficult to find old invoices when needing to compare.
- Delays in the inspection and approval process.
- Difficult to expand when the number of invoices increases.
- Obstructing the digital transformation process of businesses.

---

## 🏗️ 2. Solution architecture

### 🧩 Architecture overview

The **Serverless AI Invoice Scanner** system is built according to serverless and event-driven architecture on AWS. The main processing flow includes:

```txt
React Frontend
    ↓
Amazon Cognito
    ↓
Amazon API Gateway
    ↓
UploadInvoiceFileFunction
    ↓
Amazon S3 /uploads
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
API Gateway
    ↓
React Frontend
```

This architecture helps clearly separate functions:

- Frontend is used to interact with users.
- API Gateway acts as the entry point of the backend.
- Lambda processes business.
- S3 saves the original invoice file.
- Textract extracts text.
- OpenAI API normalizes data.
- DynamoDB stores invoice data.
- CloudWatch supports log monitoring and debugging.

### 🎯 Architectural design goals

- Automate the invoice processing process from upload to storage.
- No need to manage physical servers or EC2 servers.
- Separate frontend, API, AI processing and data storage.
- Easy to expand according to number of requests and number of invoices.
- Easy to test using Postman, AWS Console and React frontend.
- Ability to add advanced functions such as tags, starred, search and Excel export.

---

## 🔄 3. Data processing flow

### 3.1. User login flow

1. User accesses frontend deployed using **AWS Amplify Hosting**.
2. Frontend uses **Amazon Cognito User Pool** to support registration and login.
3. After successfully logging in, users can use system functions such as uploading invoices, viewing lists and searching for invoices.

{{% notice info %}}
In the current project, Cognito is mainly used for frontend authentication. API Gateway is only protected with Cognito if there is a separate Cognito Authorizer configuration.
{{% /notice %}}

### 3.2. Invoice upload flow

1. User selects invoice file from React interface.
2. Frontend converts the file to Base64.
3. Frontend sends request to API Gateway:

```txt
POST /uploads
```

4. API Gateway transfers request to Lambda:

```txt
UploadInvoiceFileFunction
```

5. Lambda decodes the Base64 content and uploads the file to Amazon S3, usually in the directory:

```txt
uploads/
```

6. After the file is saved to S3, S3 Event Notification triggers Lambda to process the invoice.

### 3.3. AI invoice processing flow

1. **ProcessInvoiceFunction** is triggered when there is a new file in S3.
2. Lambda reads files from S3.
3. Lambda calls **Amazon Textract** to extract text from the invoice.
4. OCR results are sent to **OpenAI API** for analysis and normalization.
5. Data after normalization is saved to DynamoDB table:

```txt
InvoiceData
```

Data may include:

| Data field | Description |
|---|---|
| `InvoiceId` | Unique identifier of the invoice. |
| `CustomerName` | Name of customer or related unit. |
| `InvoiceNumber` | Invoice number. |
| `InvoiceDate` | Invoice issuance date. |
| `TotalAmount` | Total amount on invoice. |
| `Currency` | Currency like `VND`, `USD`, `EUR`. |
| `Tags` | List of user labels attached to invoices. |
| `Starred` | Status of marking important invoices. |
| `ProcessStatus` | Processing status, for example `SUCCESS` or `FAILED`. |
| `ExtractedData` | Invoice data was extracted and standardized. |

### 3.4. Invoice retrieval and management flow

Users can call APIs through the frontend or Postman:

```txt
GET /invoice
GET /invoice/{id}
GET /invoice?name=<customer_name>
PATCH /invoice/tags/{id}
PATCH /invoice/starred/{id}
```

These requests are routed by API Gateway to:

```txt
InvoiceManagementFunction
```

This lambda queries or updates data in DynamoDB, then returns the results to the frontend.

---

## 🧱 4. Main functional blocks

### 4.1. Frontend Layer

Frontend is built with **ReactJS** and deployed with **AWS Amplify Hosting**. Support interface:

- Register and log in with Cognito.
- Upload invoices using file selection button or drag-and-drop.
- View list of processed invoices.
- View invoice details.
- Search invoices by customer ID or name.
- Filter by tags.
- Filter by date.
- Sort by date or total amount.
- Attach tags to invoices.
- Mark important invoices with starred.
- Export invoice data to Excel file.
- Display Cognito connection status, upload API and invoice API.

### 4.2. Authentication Layer

Amazon Cognito provides functionality:

- User Pool.
- Sign up.
- Sign in.
- Sign out.
- Manage user sessions.
- Integration with frontend via `aws-amplify` and `@aws-amplify/ui-react`.

### 4.3. API Gateway Layer

API Gateway provides REST API for frontend and Postman.

Main APIs:

| Method | Route | Function |
|---|---|---|
| `POST` | `/uploads` | Upload invoice file. |
| `GET` | `/invoice` | Get a list of invoices. |
| `GET` | `/invoice/{id}` | Get invoice details by ID. |
| `GET` | `/invoice?name=<customer_name>` | Search invoices by customer name. |
| `PATCH` | `/invoice/tags/{id}` | Update invoice tags. |
| `PATCH` | `/invoice/starred/{id}` | Update starred status. |

### 4.4. Lambda Layer

The system uses three main Lambda functions:

| Lambda Function | Role |
|---|---|
| `UploadInvoiceFileFunction` | Receive Base64 file from frontend, decode and upload to S3. |
| `ProcessInvoiceFunction` | Process new file from S3, call Textract, call OpenAI API and save data to DynamoDB. |
| `InvoiceManagementFunction` | Handles APIs to get list, view details, search, update tags and starred. |

### 4.5. AI Processing Layer

AI Processing Layer consists of two components:

| Ingredients | Role |
|---|---|
| Amazon Textract | OCR and extract text from invoices. |
| OpenAI API | Parse OCR content and normalize to structured JSON. |

Example of data after normalization:

```json
{
  "InvoiceNumber": "INV-001",
  "CustomerName": "John Smith",
  "InvoiceDate": "2025-06-20",
  "TotalAmount": 125.50,
  "Currency": "USD"
}
```

### 4.6. Storage Layer

The system uses two types of storage:

| Services | Purpose |
|---|---|
| Amazon S3 | Save the original invoice file. |
| Amazon DynamoDB | Save processed invoice data. |

DynamoDB main table:

```txt
InvoiceData
```

Indexes that can be used:

```txt
CustomerName-index
StarredInvoicesIndex
```

### 4.7. Monitoring Layer

Amazon CloudWatch is used to:

- Monitor Lambda logs.
- Debug upload errors.
- Debug Textract errors.
- Debug OpenAI API errors.
- Debug DynamoDB errors.
- Check for CORS or API Gateway errors.
- Monitor invoice processing status.

---

## 🧰 5. Services used

| Services | Role in project |
|---|---|
| **AWS Amplify Hosting** | Deploy React frontend from GitHub. |
| **Amazon Cognito** | User authentication for frontend. |
| **Amazon API Gateway** | Provides REST API endpoints. |
| **AWS Lambda** | Handle backend logic according to the serverless model. |
| **Amazon S3** | Store the original invoice file in the `uploads/` folder. |
| **Amazon Textract** | Extract text and data from invoice files. |
| **OpenAI API** | Normalize OCR data into structured JSON. |
| **Amazon DynamoDB** | Save processed invoice data. |
| **Amazon CloudWatch** | Logging and system monitoring support. |
| **AWS IAM** | Grant Lambda access to S3, Textract, DynamoDB, and CloudWatch. |
| **AWS Secrets Manager** *(optional)* | Save your OpenAI API key securely. |
| **Route 53** *(optional)* | Configure custom domain if needed. |

{{% notice warning %}}
Route 53 is an optional component. If the project does not use a custom domain, there is no need to include Route 53 in the required deployment.
{{% /notice %}}

---

## 🔐 6. Security architecture

### 6.1. User authentication

- User logs in through Amazon Cognito.
- Frontend saves sessions through the AWS Amplify library.
- Information such as User Pool ID, App Client ID and Region are configured in the frontend.

### 6.2. API protection

API Gateway can be protected with Cognito Authorizer if deployed at production level. In the demo or MVP, the API may not have authorizers enabled to simplify testing.

{{% notice info %}}
If Cognito Authorizer is enabled, the frontend needs to send the Authorization header and API Gateway CORS must allow the `Authorization` header.
{{% /notice %}}

### 6.3. Data protection

- S3 should enable public access block.
- DynamoDB is not published directly to the internet.
- Lambda uses IAM Role with minimal permissions.
- OpenAI API key cannot be hardcoded in the frontend.
- Do not log the entire request if the request contains tokens or sensitive data.

### 6.4. Operational protection

- CloudWatch is used to track errors.
- IAM Role only grants necessary permissions.
- You can use AWS Secrets Manager to manage secrets.
- Can add CloudTrail or WAF if put into production environment.

---

## ⚙️ 7. Technical implementation

### 📌 Implementation stages

#### Phase 1: Prepare the AWS environment

- Create S3 bucket to save invoices.
- Create DynamoDB table `InvoiceData`.
- Create Cognito User Pool.
- Create Lambda functions.
- Configure IAM Roles.
- Configure API Gateway routes.
- Prepare OpenAI API key in the backend.

#### Phase 2: Build upload flow

- Create `POST /uploads` on API Gateway.
- Create `UploadInvoiceFileFunction`.
- Frontend converts files to Base64.
- Lambda decodes Base64 and uploads files to S3.
- Test upload using frontend and Postman.

#### Phase 3: Building AI processing flow

- Configure S3 Event Notification.
- Create `ProcessInvoiceFunction`.
- Lambda calls Amazon Textract for OCR.
- Lambda sends OCR results to OpenAI API.
- Lambda saves normalized data to DynamoDB.
- Record processing logs to CloudWatch.

#### Phase 4: Building invoice management API

- Create `InvoiceManagementFunction`.
- Create API routes:
  - `GET /invoice`
  - `GET /invoice/{id}`
  - `GET /invoice?name=<customer_name>`
  - `PATCH /invoice/tags/{id}`
  - `PATCH /invoice/starred/{id}`
- Test API using Postman.
- Standardize data returned to the frontend.

#### Phase 5: Building the frontend

- Build React apps.
- Cognito integration using `aws-amplify`.
- Integrate API Gateway endpoints using `.env`.
- Create upload interface, list, details, search, tags, starred, sort, filter and export Excel.
- Deploy frontend using AWS Amplify Hosting.

#### Phase 6: Testing and completion

- Test uploading invoices.
- Test to get list of invoices.
- Test searching by customer ID and name.
- Test updated tags and starred.
- Testing CORS.
- Check CloudWatch Logs.
- Correct data errors such as `Tags/tags`, `Starred/IsStarred`, `CustomerName` top-level or in `ExtractedData`.

---

## 🧪 8. Testing strategy

### 8.1. Functional testing

| Function | Expected results |
|---|---|
| Upload invoice | The file is saved to S3. |
| S3 triggers | Lambda processing is enabled. |
| Textract OCR | Extract text from invoices. |
| OpenAI normalization | Returns structured invoice JSON. |
| Save DynamoDB | Item is saved to table `InvoiceData`. |
| GET `/invoice` | Returns a list of invoices. |
| GET `/invoice/{id}` | Returns invoice details. |
| GET `/invoice?name=` | Find invoices by customer. |
| PATCH tags | Updated tags successfully. |
| PATCH starred | Successfully updated starred status. |

### 8.2. Security testing

- Check CORS.
- Check that the OpenAI API key is not exposed on the frontend.
- Check Lambda's IAM Role.
- Check S3 bucket is not public.
- Check Cognito login/logout.
- If using Cognito Authorizer, check the request with and without token.

### 8.3. Error testing

| Error case | How to handle |
|---|---|
| Invalid file | Frontend displays error message. |
| API Gateway wrong route | Check for error `Missing Authentication Token`. |
| Lambda missing environment variable | Check CloudWatch Logs. |
| DynamoDB does not have item | Returns the appropriate 404 error. |
| Textract error | Write `ProcessStatus = FAILED`. |
| OpenAI API error | Log and return failed processing status. |

---

## 🗺️ 9. Roadmap and milestones

### 📆 Project roadmap

| Week | Phase | Goal |
|---|---|---|
| Week 1 | Architecture design and setup of AWS | Create S3, DynamoDB, Lambda, Cognito, API Gateway. |
| Week 2 | Upload flow | Frontend uploads files via API Gateway to S3. |
| Week 3 | AI processing flow | S3 trigger Lambda, Textract OCR, OpenAI API normalization. |
| Week 4 | Invoice management API | GET/PATCH APIs, DynamoDB query/update. |
| Week 5 | Complete Frontend | Upload, list, details, search, tags, starred, export Excel. |
| Week 6 | Testing and deploying | Postman test, CloudWatch debug, deploy Amplify Hosting. |

### 📌 Important milestone

| STT | Milestone | Output |
|---|---|---|
| 1 | Complete architectural diagram | Correct flow diagram of AWS + OpenAI API. |
| 2 | Upload invoice successfully | The file is saved in S3 `uploads/`. |
| 3 | Successful invoice processing | Textract + OpenAI returns structured data. |
| 4 | DynamoDB saved successfully | Item appears in `InvoiceData`. |
| 5 | Activity Retrieval API | GET and PATCH work using Postman. |
| 6 | Fully integrated frontend | Users can manage invoices on the web. |
| 7 | Deploy Amplify Hosting | There is a public URL to access the frontend. |
| 8 | Complete documents | There are instructions for deployment, testing and cleanup. |

---

## 💰 10. Estimate budget

### 📦 AWS infrastructure costs

| Services | Estimated cost/month | Notes |
|---|---:|---|
| Amazon S3 | ~$0.23 | Save small invoice files. |
| AWS Lambda | ~$1 – $3 | Depending on the number of calls and running time. |
| Amazon Textract | ~$4 – $6 | Depending on the number of pages processed per month. |
| Amazon DynamoDB | ~$1 – $3 | Use On-Demand for MVP. |
| API Gateway | ~$1 – $3 | Depends on request number. |
| Amazon Cognito | ~$0 – $1 | Suitable for MVP with a small number of users. |
| Amplify Hosting | ~$1 – $3 | Frontend hosting and low bandwidth. |
| CloudWatch Logs | ~$0 – $2 | Depends on log capacity. |
| Secrets Manager *(optional)* | ~$0.40/secret/month | If used to save OpenAI API key. |
| Route 53 *(optional)* | ~$0.50/month + domain | Only use if you have a custom domain. |

### 🤖 OpenAI API cost

OpenAI API is a service outside of AWS. Cost depends on:

- Model used.
- Number of invoices processed.
- Length of OCR content sent to the model.
- Number of input and output tokens.

During the MVP phase, it is possible to limit prompts and send only the necessary OCR portion to reduce costs.

{{% notice info %}}
OpenAI API costs should be tracked separately in the OpenAI dashboard as they are not visible in AWS Billing.
{{% /notice %}}

### 👉 Total estimated cost

With a small MVP scale, AWS costs can range around:

```txt
~$10 – $30 USD/month
```

OpenAI API and optional domain costs are not included.

---

## ⚠️ 11. Risk assessment

### 📋 Risk matrix

| ID | Risk | Level of impact | Likelihood | Risk level |
|---|---|---|---|---|
| R1 | Textract misreads blurry invoices or scans incorrectly | Average | Cao | Cao |
| R2 | OpenAI API incorrectly normalizes data fields | Cao | Average | Cao |
| R3 | OpenAI API key exposed | Very high | Low | Cao |
| R4 | Lambda error due to missing IAM permissions | Cao | Average | Cao |
| R5 | API Gateway CORS error or wrong route | Average | Cao | Cao |
| R6 | DynamoDB stores wrong fields like `Tags/tags`, `Starred/IsStarred` | Average | Average | Average |
| R7 | Cost increases due to many logs or requests Average | Average | Average |
| R8 | Users upload files that are too large or in the wrong format | Average | Average | Average |

### 🛡️ Mitigation solution

| Risk | Measures |
|---|---|
| R1 | Clear file upload instructions, support for checking files before processing. |
| R2 | Design a clear prompt, validate the returned JSON, save error status if parsing fails. |
| R3 | Don't store keys in the frontend, use Lambda env or Secrets Manager. |
| R4 | Grant IAM Roles according to the principle of least privilege. |
| R5 | Full CORS configuration, testing with Postman and frontend. |
| R6 | Normalize the fields returned in Lambda before sending to the frontend. |
| R7 | Configure logs properly, cleanup CloudWatch Logs after lab. |
| R8 | Limit file type and upload capacity. |

---

## 🎯 12. Expected results

After completing the project, the system achieves the following results:

- Users can register and log in using Amazon Cognito.
- Frontend React is deployed on AWS Amplify Hosting.
- Users can upload invoices from the web interface.
- Invoice files are saved to Amazon S3.
- S3 trigger activates Lambda to process invoices.
- Amazon Textract can extract invoice content.
- OpenAI API normalizes OCR content into structured data.
- Data is saved to DynamoDB table `InvoiceData`.
- User can view invoice list and details.
- Users can search by customer ID or name.
- Users can update tags and starred.
- Users can filter, sort and export data to Excel.
- CloudWatch supports log monitoring and error debugging.

### 📊 Success assessment index

| Index | Goal |
|---|---|
| Upload successful | ≥ 95% with valid files. |
| OCR success | ≥ 90% with clear invoice. |
| API works stably | GET/PATCH/POST returns the correct response. |
| Data is stored in the correct structure | There are `InvoiceId`, `ExtractedData`, `TotalAmount`, `Currency`. |
| Frontend can be used | Users can manipulate the entire main thread. |
| MVP Cost | Maintains a low level, suitable for demo/lab. |

---

## 📎 Appendix

### A. Technical specifications

| Category | Technical information |
|---|---|
| Frontend | ReactJS, AWS Amplify Hosting |
| Authentication | Amazon Cognito User Pool |
| Frontend libraries | `aws-amplify`, `@aws-amplify/ui-react`, `xlsx` |
| Backend | AWS Lambda |
| Lambda runtime | Python with boto3 |
| API | Amazon API Gateway REST API |
| File storage | Amazon S3 |
| OCR | Amazon Textract |
| AI normalization | OpenAI API |
| Database | Amazon DynamoDB |
| Monitoring | Amazon CloudWatch |
| Optional secret storage | AWS Secrets Manager |
| Optional DNS | Amazon Route 53 |
| Architecture | Serverless, event-driven |

### B. API routes

| Method | Route | Lambda |
|---|---|---|
| `POST` | `/uploads` | `UploadInvoiceFileFunction` |
| `GET` | `/invoice` | `InvoiceManagementFunction` |
| `GET` | `/invoice/{id}` | `InvoiceManagementFunction` |
| `GET` | `/invoice?name=<customer_name>` | `InvoiceManagementFunction` |
| `PATCH` | `/invoice/tags/{id}` | `InvoiceManagementFunction` |
| `PATCH` | `/invoice/starred/{id}` | `InvoiceManagementFunction` |

### C. Environment variables frontend

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

### D. DynamoDB table

```txt
Table name: InvoiceData
Primary key: InvoiceId
Optional GSI:
- CustomerName-index
- StarredInvoicesIndex
```

### E. References

1. Amazon Textract Documentation  
2. AWS Lambda Documentation  
3. Amazon API Gateway Documentation  
4. Amazon DynamoDB Documentation  
5. Amazon Cognito Documentation  
6. AWS Amplify Hosting Documentation  
7. OpenAI API Documentation  
8. AWS CloudWatch Documentation  

---

## ✅ Conclusion

The proposal **Serverless AI Invoice Scanner** fits the goal of building an automated invoice processing system that is easy to deploy and easy to expand. Compared to the original proposal version, this update has adjusted to the actual project:

- Replace Amazon Bedrock with OpenAI API.
- Clarifying the role of AWS Amplify Hosting.
- Clarify Cognito used for frontend authentication.
- Added three main Lambda functions.
- Added actual routes API.
- Added tags, starred, search, filter, sort and Excel export.
- Update the correct processing flow: API Gateway → Upload Lambda → S3 → Processing Lambda → Textract → OpenAI API → DynamoDB.
- Added cleanup and monitoring via CloudWatch.
