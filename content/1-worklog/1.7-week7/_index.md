---
title: "Worklog Week 7"
date: 2026-06-01
weight: 107
week: 7
chapter: false
---

## General information

| Content | Details |
|---|---|
| Time | June 1, 2026 - June 7, 2026 |
| Internship week | Week 7 |
| Phase | Project implementation phase |
| Project | Serverless AI Invoice Scanner |
| Main topic | Build invoice management API and frontend integration |
| Weekly goals | Create APIs to retrieve, search, update tags/starred and start connecting React frontend to AWS backend |

---

## Week 7 Orientation

After week 6 completed the AI ​​invoice processing flow including S3 Event, Lambda, Amazon Textract, OpenAI API and DynamoDB, week 7 focused on **invoice data management**.

The main goal this week is to build Lambda and API Gateway so that the frontend can get data from DynamoDB, display a list of invoices, view invoice details, search by customer name, update tags and mark important invoices.

Main processing flow of the week:

```txt
React Frontend / Postman
    ↓
Amazon API Gateway
    ↓
InvoiceManagementFunction
    ↓
Amazon DynamoDB InvoiceData
    ↓
Response JSON
    ↓
React Frontend
```

---

## Week 7 Goals

The main goals for the week include:

- Create Lambda function `InvoiceManagementFunction`.
- Build an API to get a list of invoices.
- Build an API to retrieve invoice details by ID.
- Build API to search invoices by customer name.
- Build an API to update tags for invoices.
- Build API to update starred status.
- Test the entire API using Postman.
- Standardize data returned to the frontend.
- Start integrating API Gateway endpoints into React frontend.
- Check CORS, route, method and response format errors.
- Track errors using CloudWatch Logs.

---

## Content implemented during the week

### Day 1 - Monday, June 1, 2026

The first day of week 7 focuses on analyzing the APIs needed for invoice management.

Implemented content:

- Review the data structure being stored in DynamoDB table `InvoiceData`.
- Identify frontend functions that need to get data from the backend.
- List the APIs that need to be built for the project.
- Identify the main Lambda function that handles invoice management APIs:

```txt
InvoiceManagementFunction
```

APIs to implement:

| Method | Route | Function |
|---|---|---|
| `GET` | `/invoice` | Get list of invoices |
| `GET` | `/invoice/{id}` | Get invoice details by ID |
| `GET` | `/invoice?name=<customer_name>` | Search invoices by customer name |
| `PATCH` | `/invoice/tags/{id}` | Update invoice tags |
| `PATCH` | `/invoice/starred/{id}` | Update status starred |

Results achieved:

- Identify the necessary APIs for the frontend.
- Understand clearly the role of `InvoiceManagementFunction`.
- Plan to deploy invoice management API within the week.

---

### Day 2 - Tuesday, June 2, 2026

Day two focuses on creating the **InvoiceManagementFunction** and granting access to DynamoDB.

Implemented content:

- Create Lambda function `InvoiceManagementFunction`.
- Configure runtime and handler.
- Create or update IAM execution role.
- Grant permissions so Lambda can read and update DynamoDB.
- Check logging permissions to CloudWatch.
- Write the initial request processing structure for Lambda.

DynamoDB permissions to pay attention to:

```txt
dynamodb:Scan
dynamodb:GetItem
dynamodb:Query
dynamodb:UpdateItem
```

Basic Lambda processing flow:

```txt
Receive request from API Gateway
    ↓
Check method and path
    ↓
Call DynamoDB accordingly
    ↓
Standardize JSON response
    ↓
Return data to API Gateway
```

Results achieved:

- Create `InvoiceManagementFunction`.
- Lambda has access to DynamoDB.
- Have an initial code structure to handle multiple API routes.

---

### Day 3 - Wednesday, June 3, 2026

Day three focuses on the API to get a list of invoices and view invoice details.

Implemented content:

- Build API:

```txt
GET /invoice
```

- Lambda reads the item list from DynamoDB.
- Standardize data returned to the frontend.
- Build API:

```txt
GET /invoice/{id}
```

- Lambda retrieves invoice details by `InvoiceId`.
- Check if the invoice cannot be found.
- Test two APIs using Postman.
- View error log in CloudWatch if the response is incorrect.

Example response for list of invoices:

```json
[
  {
    "InvoiceId": "invoice-001",
    "CustomerName": "Customer Name",
    "InvoiceDate": "2026-06-03",
    "TotalAmount": 100000,
    "Currency": "VND",
    "Tags": [],
    "Starred": false
  }
]
```

Results achieved:

- API `GET /invoice` returns a list of invoices.
- API `GET /invoice/{id}` returns invoice details by ID.
- Understand how to standardize responses so the frontend is easy to use.

---

### Day 4 - Thursday, June 4, 2026

Day four focuses on the invoice search API by customer name.

Implemented content:

- Build search API:

```txt
GET /invoice?name=<customer_name>
```

- Check query string parameter from API Gateway.
- Lambda receives parameter `name` and searches in DynamoDB.
- Handle the case where `CustomerName` is in a top-level field.
- Additional handling of cases where `CustomerName` is in `ExtractedData`.
- Test search using Postman with many different customer names.
- Note issues with upper and lower case letters and data with missing fields.

Expected search logic:

```txt
If there is a query parameter name
    ↓
Search by CustomerName
    ↓
If not at the top-level then check ExtractedData.CustomerName
    ↓
Return the appropriate list of invoices
```

Results achieved:

- API search by customer name works.
- Understand that data can be located in many different locations within the item.
- Added fallback handling to increase search capabilities.

---

### Day 5 - Friday, June 5, 2026

Day five focuses on API updates for tags and starred invoices.

Implemented content:

- Build tags update API:

```txt
PATCH /invoice/tags/{id}
```

- Lambda receives a list of tags from the request body.
- Update field `Tags` in DynamoDB.
- Build updated API starred:

```txt
PATCH /invoice/starred/{id}
```

- Lambda receives the value `Starred` from the request body.
- Update starred status in DynamoDB.
- Check data after updating in DynamoDB Console.
- Test API using Postman.

Example request update tags:

```json
{
  "tags": ["paid", "important", "accounting"]
}
```

Example request update starred:

```json
{
  "starred": true
}
```

{{% notice info %}}
During deployment, it is necessary to unify field names between frontend and backend. For example, the backend might store `Tags` and `Starred`, while the frontend might send `tags` or `starred`. Lambda should process and normalize the data before saving or returning the response.
{{% /notice %}}

Results achieved:

- Tags update API works.
- Active starred API update.
- Understand the importance of field name consistency between the frontend and DynamoDB.

---

### Day 6 - Saturday, June 6, 2026

Day six focuses on API Gateway routes configuration and integration testing.

Implemented content:

- Create or test routes in API Gateway.
- Connect routes with `InvoiceManagementFunction`.
- Deploy API stage after changing routes.
- Configure CORS for necessary methods.
- Test the entire API using Postman.
- Check response headers.
- Check error `Missing Authentication Token`.
- Check CORS errors when calling from the frontend.

Tested routes:

```txt
GET /invoice
GET /invoice/{id}
GET /invoice?name=<customer_name>
PATCH /invoice/tags/{id}
PATCH /invoice/starred/{id}
```

Checked errors:

| Error | Possible causes |
|---|---|
| `Missing Authentication Token` | Wrong method, wrong path or not deployed stage |
| CORS error | Missing CORS headers or not enabling CORS for route |
| 500 Internal Server Error | Lambda logic error or response in wrong format |
| 404 Not Found | Invoice not found by ID |
| AccessDenied | Lambda lacks DynamoDB | permissions

Results achieved:

- Invoice management APIs are connected to API Gateway.
- Test API using Postman.
- Know how to handle route, CORS and response format errors.

---

### Day 7 - Sunday, June 7, 2026

The weekend focused on starting to integrate the React frontend with API Gateway.

Implemented content:

- Update API endpoints to the frontend's `.env` file.
- Connect frontend with API to get list of invoices.
- Check the invoice list display on the interface.
- Check the function to view invoice details.
- Check search by customer name.
- Check for updated tags and starred from the frontend.
- Note frontend errors when returned data is not in the correct format.
- Summarize results of week 7 and prepare plans for week 8.

Example frontend environment variable:

```txt
REACT_APP_API_INVOICE_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice
REACT_APP_API_UPDATE_TAGS_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice/tags
REACT_APP_API_UPDATE_STARRED_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice/starred
```

Results achieved:

- Frontend starts getting invoice data from backend.
- Main APIs have been tested via Postman.
- Identify points that need to be improved in week 8 such as interface, filter, sort, export Excel and deploy frontend.

---

## Summary of Week 7 knowledge

In week 7, I built the invoice management API for the project **Serverless AI Invoice Scanner**. This is the part that helps the frontend retrieve and update data that has been processed by AI.

| Knowledge group | Implemented content |
|---|---|
| Lambda | Create `InvoiceManagementFunction` |
| API Gateway | Create GET and PATCH routes |
| DynamoDB | Scan, GetItem, Query, UpdateItem |
| Frontend Integration | Configure API endpoint in React |
| Testing | API Testing with Postman |
| Debugging | Check for errors using CloudWatch Logs |
| CORS | Configure the frontend to call the API |
| Data Mapping | Normalize `Tags/tags`, `Starred/starred`, `CustomerName` |

---

## Results achieved during the week

- Create `InvoiceManagementFunction`.
- Built an API to get a list of invoices.
- Built an API to view invoice details by ID.
- Built a search API by customer name.
- Built an API to update tags.
- Built updated API starred.
- Test APIs using Postman.
- Start integrating React frontend with API backend.
- Handle some errors related to CORS, route and response format.
- Complete the backend API for invoice data management.

---

## Difficulties encountered

| Difficulty | Processing directions |
|---|---|
| Data in DynamoDB has heterogeneous fields | Normalize the response in Lambda before returning it to the frontend |
| Search by unstable customer name | Check both `CustomerName` and `ExtractedData.CustomerName` |
| API Gateway is prone to wrong routes | Check the method, path and stage URL |
| CORS causes error when frontend calls API | Add CORS headers in Lambda response and API Gateway |
| PATCH update field is not correct | Normalize `tags/Tags` and `starred/Starred` |
| Frontend does not display data correctly | Check the JSON response format from API |

---

## Lesson learned

- When building APIs, it is necessary to clearly unify data between frontend, Lambda and DynamoDB.
- DynamoDB stores data flexibly but needs to standardize fields for easy processing by the frontend.
- API Gateway needs to properly configure methods, routes and stages to avoid `Missing Authentication Token` error.
- CORS is an important part when the frontend runs on a different domain than the API Gateway.
- Postman helps test API independently before integrating into frontend.
- CloudWatch Logs helps find errors quickly when Lambda does not return the correct response.
- Need to check both happy cases and error cases for each API.

---

## Plan for Week 8

Week 8 is the last week of the internship and also the week of completing the project.

Expected content:

- Complete React frontend interface.
- Fully integrated Cognito login/sign-up.
- Integrates upload, list, detail, search, tags and starred.
- Added filter by date, sort by date/total amount and export to Excel.
- Deploy frontend using AWS Amplify Hosting.
- End-to-end testing of the entire system.
- Check CloudWatch Logs and fix remaining errors.
- Complete implementation documentation.
- Write the cleanup resources section.
- Summary of project and internship results.

---

## Weekend comments

Week 7 focuses on building invoice management APIs and connecting the backend to the frontend. After this week, the system can not only process invoices using AI but can also retrieve, search and update processed data. This is an important step to prepare to complete the user interface and deploy the end-to-end system in the last week.
