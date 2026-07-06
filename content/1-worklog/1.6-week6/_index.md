---
title: "Worklog Week 6"
date: 2026-05-25
weight: 106
week: 6
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | May 25, 2026 - May 31, 2026 |
| Internship week | Week 6 |
| Phase | Project implementation phase |
| Project | Serverless AI Invoice Scanner |
| Main topic | Building an invoice processing flow using AI |
| Weekly goals | Configure S3 triggers, create an invoice processing Lambda, integrate Amazon Textract, OpenAI API and save data to DynamoDB |

---

## Week 6 Orientation

After week 5 completed the initial foundation including S3 bucket, DynamoDB table, Lambda upload and API Gateway `POST /uploads`, week 6 focused on the most important part of the project: **invoice processing using AI**.

This week, I implemented the processing flow after the invoice file was uploaded to Amazon S3. When there is a new file in the `uploads/` directory, S3 will trigger Lambda to process. This lambda calls Amazon Textract to extract text from the invoice, then sends the OCR content to the OpenAI API to normalize the data to JSON and saves the results to DynamoDB.

Main processing flow of the week:

```txt
S3 uploads/
    ↓
S3 Event Notification
    ↓
ProcessInvoiceFunction
    ↓
Amazon Textract
    ↓
OpenAI API
    ↓
Amazon DynamoDB InvoiceData
```

---

## Week 6 Goals

The main goals for the week include:

- Configure S3 Event Notification to trigger Lambda when there is a new file.
- Create Lambda function `ProcessInvoiceFunction`.
- Grant IAM permission to Lambda to read files from S3, call Textract, write to DynamoDB and log CloudWatch.
- Integrate Amazon Textract to OCR invoice files.
- Process Textract results and get text content.
- Send OCR text to OpenAI API to standardize invoice data.
- Design the output JSON structure.
- Save processed data to DynamoDB table `InvoiceData`.
- Check processing status using CloudWatch Logs.
- Note errors and solutions during the AI ​​integration process.

---

## Content implemented during the week

### Day 1 - Monday, May 25, 2026

The first day of week 6 focuses on preparing the processing flow after the file is uploaded to S3.

Implemented content:

- Review the upload flow completed in week 5.
- Check S3 bucket and directory `uploads/`.
- Learn the S3 Event Notification mechanism.
- Determine the type of event to use:

```txt
s3:ObjectCreated:*
```

- Determine which Lambda will be activated when a new file becomes available.
- Prepare the handler function name:

```txt
ProcessInvoiceFunction
```

Results achieved:

- Understand how S3 can trigger Lambda automatically.
- Identify the role of `ProcessInvoiceFunction`.
- Prepare AI processing flow for the next days.

---

### Day 2 - Tuesday, May 26, 2026

Day two focuses on creating the **ProcessInvoiceFunction** and configuring the necessary permissions.

Implemented content:

- Create Lambda function `ProcessInvoiceFunction`.
- Configure runtime and handler appropriately.
- Check Lambda's IAM execution role.
- Add necessary permissions for Lambda:
- Read files from S3.
- Call Amazon Textract.
- Write data to DynamoDB.
- Record logs to CloudWatch.
- Check that Lambda can receive events from S3.
- View CloudWatch Logs to check input events.

Permissions to note:

```txt
s3:GetObject
textract:DetectDocumentText
textract:AnalyzeDocument
dynamodb:PutItem
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
```

Results achieved:

- Create `ProcessInvoiceFunction`.
- Understand the IAM permissions required for Lambda to process invoices.
- Lambda initially receives events from S3.

---

### Day 3 - Wednesday, May 27, 2026

Day three focuses on configuring **S3 Event Notification** to connect S3 to Lambda.

Implemented content:

- Open the Event Notifications section of the S3 bucket.
- Create new event notification for folder `uploads/`.
- Select event type as created object.
- Connect event with `ProcessInvoiceFunction`.
- Try uploading an invoice file to S3 to test the trigger.
- Check CloudWatch Logs after uploading files.
- Note the event structure that S3 sends to Lambda.

Example important information in S3 event:

```json
{
  "bucket": "invoice-scanner-upload-bucket",
  "key": "uploads/invoice-test.png"
}
```

Results achieved:

- Configure S3 trigger for Lambda.
- When uploading files to S3, Lambda is automatically activated.
- Know how to read bucket name and object key from S3 event.

---

### Day 4 - Thursday, May 28, 2026

Day four focuses on integrating **Amazon Textract** to extract text from invoices.

Implemented content:

- Learn how to call Amazon Textract from Lambda.
- Check the file formats supported by Textract.
- Write logic to call Textract with files in S3.
- Get OCR results from Textract response.
- Extract text lines from returned results.
- Log OCR content for checking.

Textract processing flow:

```txt
Lambda receives S3 events
    ↓
Get bucket and key
    ↓
Call Amazon Textract
    ↓
Get list of Blocks
    ↓
Filter blocks in LINE format
    ↓
Merge into OCR text content
```

Example result processing logic:

```txt
Blocks → LINE → Text → joined OCR content
```

Results achieved:

- Call Amazon Textract from Lambda.
- Extract text content from invoices.
- Understand how Textract returns data in block format.

---

### Day 5 - Friday, May 29, 2026

Day five focuses on integrating the **OpenAI API** to standardize OCR data.

Implemented content:

- Learn how to use OpenAI API in the backend.
- Prepare a prompt asking the AI ​​to return structured JSON.
- Send OCR content from Textract to OpenAI API.
- Ask AI to extract important invoice fields.
- Check the response returned from OpenAI API.
- Note how to secure OpenAI API key.
- Do not include the API key in the frontend.

Desired data fields:

```json
{
  "CustomerName": "",
  "InvoiceNumber": "",
  "InvoiceDate": "",
  "TotalAmount": 0,
  "Currency": "",
  "Items": []
}
```

{{% notice warning %}}
OpenAI API key is sensitive information. API keys should only be saved on the backend via Lambda environment variables or AWS Secrets Manager, not in the React frontend or public repository.
{{% /notice %}}

Results achieved:

- Integrate OpenAI API at the backend processing level.
- Can convert OCR text into structured JSON data.
- Understand API key security principles when using services outside of AWS.

---

### Day 6 - Saturday, May 30, 2026

Day six focuses on saving processed invoice data to **Amazon DynamoDB**.

Implemented content:

- Standardize data returned from OpenAI API.
- Create `InvoiceId` for invoices.
- Added frontend fields such as `Tags` and `Starred`.
- Save items to DynamoDB table `InvoiceData`.
- Check data in DynamoDB Console.
- Log successful or failed processing status.
- Added field `ProcessStatus` to track processing status.

Item structure saved to DynamoDB:

```json
{
  "InvoiceId": "invoice-xxxx",
  "CustomerName": "Customer Name",
  "InvoiceNumber": "INV-001",
  "InvoiceDate": "2026-05-30",
  "TotalAmount": 100000,
  "Currency": "VND",
  "Tags": [],
  "Starred": false,
  "ProcessStatus": "SUCCESS",
  "ExtractedData": {}
}
```

Results achieved:

- Save invoice data to DynamoDB.
- Post-processed data has a clear structure.
- Can check items directly in DynamoDB Console.

---

### Day 7 - Sunday, May 31, 2026

The weekend focuses on testing the entire processing flow and synthesizing the results.

Implemented content:

- Try uploading the invoice file via API `POST /uploads`.
- Check files saved in S3.
- Check S3 trigger activation `ProcessInvoiceFunction`.
- Check if Textract can extract text.
- Test OpenAI API returns JSON data.
- Check if DynamoDB has new items.
- Read CloudWatch Logs to check for errors.
- Summary of errors encountered and solutions.
- Prepare a plan for week 7.

Weekend testing flow:

```txt
Postman / Frontend Upload
    ↓
API Gateway
    ↓
UploadInvoiceFileFunction
    ↓
S3 uploads/
    ↓
ProcessInvoiceFunction
    ↓
Textract
    ↓
OpenAI API
    ↓
DynamoDB InvoiceData
```

Results achieved:

- Test the AI ​​processing flow from S3 to DynamoDB.
- Understand how to debug step by step using CloudWatch Logs.
- Complete the AI ​​processing platform for the project.

---

## Summary of Week 6 knowledge

In week 6, I implemented AI invoice processing for the project **Serverless AI Invoice Scanner**. This is an important part that helps the system convert from raw invoice files to structured data.

| Knowledge group | Implemented content |
|---|---|
| Event-driven | Configure S3 Event Notification |
| Lambda | Create `ProcessInvoiceFunction` |
| OCR | Amazon Textract Integration |
| AI | Send OCR text to OpenAI API for standardization |
| Database | Save data to DynamoDB `InvoiceData` |
| Security | Secure OpenAI API key in backend |
| Monitoring | Track errors with CloudWatch Logs |
| IAM | Grant Lambda permission to read S3, call Textract, write to DynamoDB |

---

## Results achieved during the week

- Create `ProcessInvoiceFunction`.
- Configure S3 Event Notification.
- Lambda automatically runs when there is a new file in S3.
- Integrate with Amazon Textract to OCR invoices.
- Extract text content from invoice file.
- Integrate OpenAI API to standardize OCR data.
- Save processed data to DynamoDB.
- Monitor and debug processing using CloudWatch Logs.
- Complete the main processing flow of the system.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| Lambda has not been activated by S3 trigger | Check the event notification, prefix `uploads/` and invoke Lambda permission |
| Textract cannot read some files | Check file format and invoice quality |
| Lambda lacks permission to call Textract | Add appropriate IAM permission |
| OpenAI API returns malformed JSON | Adjust prompt and validate response |
| DynamoDB data is missing field | Normalize the data before `PutItem` |
| Difficult to debug many processing steps | Logging step by step in CloudWatch |

---

## Lesson learned

- Event-driven architecture helps automate processing after files are uploaded.
- S3 Event Notification is an effective way to trigger Lambda when a new file becomes available.
- Amazon Textract is suitable for extracting text from image or PDF invoices.
- OpenAI API helps standardize OCR text into structured data that is easy to store.
- Need to check and validate AI returned data before saving to DynamoDB.
- CloudWatch Logs are very important when processing multi-step pipelines.
- API keys of external services must be protected at the backend.

---

## Plan for Week 7

In the next week, I will deploy the invoice management API and start connecting to the frontend.

Expected content:

- Create `InvoiceManagementFunction`.
- Build API to get list of invoices:

```txt
GET /invoice
```

- Build API to get invoice details:

```txt
GET /invoice/{id}
```

- Build a search API by customer name:

```txt
GET /invoice?name=<customer_name>
```

- Build tags update API:

```txt
PATCH /invoice/tags/{id}
```

- Build updated API starred:

```txt
PATCH /invoice/starred/{id}
```

- Test APIs using Postman.
- Start integrating React frontend with API Gateway.
- Check CORS errors and data returned to the frontend.

---

## Weekend comments

Week 6 is the week of implementing the most important AI processing part of the project. After this week, the system was able to automatically receive files from S3, extract content using Amazon Textract, normalize data using OpenAI API and save results to DynamoDB. This is a big step forward in the project because the system has begun to process invoices according to the original goal. The next week will focus on building the invoice data management API and connecting to the frontend.
