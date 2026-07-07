# Internship Report

This repository contains my internship report website built with **Hugo** and deployed using **GitHub Pages**.

The report documents my learning process during the **First Cloud AI Journey** program and the implementation of the project **Serverless AI Invoice Scanner**.

## Project Overview

**Serverless AI Invoice Scanner** is a serverless web application that allows users to upload invoice files, process invoice content using AI, and manage extracted invoice data through a web interface.

The project uses AWS services to build a complete cloud-based invoice processing system, including file storage, backend API, OCR processing, AI data normalization, database storage, authentication, hosting, monitoring, and cleanup documentation.

## Main Features

- Upload invoice files from the web application.
- Store uploaded invoice files in Amazon S3.
- Trigger backend processing when a new file is uploaded.
- Extract text from invoices using Amazon Textract.
- Normalize OCR text into structured invoice data using OpenAI API.
- Store invoice results in Amazon DynamoDB.
- Retrieve invoice records through API Gateway and Lambda.
- Search invoices by customer name.
- Update invoice tags.
- Mark invoices as starred.
- Deploy frontend using AWS Amplify Hosting.
- Monitor backend logs using Amazon CloudWatch.

## Technologies Used

### Static Site and Documentation

- Hugo
- Markdown
- GitHub Pages
- GitHub Actions

### Frontend

- React
- AWS Amplify UI
- Amazon Cognito

### Backend and Cloud Services

- Amazon API Gateway
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon Textract
- Amazon CloudWatch
- AWS IAM

### AI Integration

- OpenAI API

## AWS Architecture

The main system architecture is:

```txt
User
  ↓
AWS Amplify Hosting / React Frontend
  ↓
Amazon Cognito
  ↓
Amazon API Gateway
  ↓
AWS Lambda
  ↓
Amazon S3 / Amazon Textract / OpenAI API / Amazon DynamoDB
  ↓
Amazon CloudWatch Logs
```

The backend API layer uses two main Lambda functions:

| Lambda Function | Purpose |
|---|---|
| `UploadInvoiceFileFunction` | Handles invoice upload requests, saves files to S3, and processes uploaded files from S3 trigger. |
| `FetchInvoiceDetailsFunction` | Retrieves, searches, and updates invoice data from DynamoDB. |

## Repository Structure

```txt
intership-report/
├── archetypes/
├── assets/
├── content/
│   ├── 1-worklog/
│   ├── 2-introduction/
│   ├── 3-proposal/
│   ├── 4-architecture/
│   ├── 5-workshop/
│   ├── 6-self-assessment/
│   └── 7-feedback/
├── layouts/
├── static/
│   └── images/
├── themes/
├── hugo.toml
├── README.md
└── .github/
    └── workflows/
        └── hugo.yml
```

## Main Report Sections

The report website includes the following main sections:

| Section | Description |
|---|---|
| Work diary | Weekly internship progress from Week 1 to Week 12. |
| Introduction | Overview of the internship program and project background. |
| Proposal | Project proposal for Serverless AI Invoice Scanner. |
| Architecture | System architecture and AWS service workflow. |
| Workshop | Step-by-step implementation documentation. |
| Self-assessment | Personal reflection and evaluation after the internship. |
| Feedback | Sharing experience and suggestions for the program. |
| Cleanup | Instructions to remove AWS resources after completing the project. |

## Workshop Scope

The main workshop section focuses on the Backend API Developer role.

The tasks include:

- Create Amazon S3 bucket.
- Create Amazon DynamoDB table.
- Create `UploadInvoiceFileFunction`.
- Configure S3 ObjectCreated trigger.
- Configure API Gateway upload route.
- Create `FetchInvoiceDetailsFunction`.
- Configure invoice management API routes.
- Connect Lambda with S3 and DynamoDB.
- Test APIs using Postman and frontend requests.

## Work Diary Summary

The internship was completed in **12 weeks**.

| Week | Main Content |
|---|---|
| Week 1 | Get familiar with AWS Cloud and First Cloud Journey. |
| Week 2 | Study AWS foundational services. |
| Week 3 | Learn AWS database, API, and serverless architecture. |
| Week 4 | Study Cognito, Amplify Hosting, and prepare for the project. |
| Week 5 | Start Serverless AI Invoice Scanner and create core AWS resources. |
| Week 6 | Build AI invoice processing workflow using S3, Lambda, Textract, OpenAI, and DynamoDB. |
| Week 7 | Develop invoice management APIs and integrate backend with frontend. |
| Week 8 | Complete frontend integration, Cognito, Amplify deployment, and cleanup documentation. |
| Week 9 | Review the system, retest APIs, check logs, and prepare demo. |
| Week 10 | Finalize report, documentation, and presentation content. |
| Week 11 | Revise project after feedback and prepare handover documents. |
| Week 12 | Final review, demo preparation, cleanup review, and internship summary. |

## Local Development

To run this Hugo website locally, install Hugo first.

Then run:

```bash
hugo server
```

Open the local website at:

```txt
http://localhost:1313/
```

If the project uses a theme as a Git submodule, run:

```bash
git submodule update --init --recursive
```

## Build Site

To build the static website:

```bash
hugo --gc --minify
```

The generated static files will be created in:

```txt
public/
```

## Deploy to GitHub Pages

This repository uses **GitHub Actions** to deploy the Hugo site to GitHub Pages.

The workflow file is located at:

```txt
.github/workflows/hugo.yml
```

The GitHub Pages URL format is:

```txt
https://<username>.github.io/intership-report/
```

For this repository, the expected URL is:

```txt
https://nguyenminhtinh31204.github.io/intership-report/
```

## GitHub Pages Configuration

In GitHub repository settings:

```txt
Settings → Pages → Build and deployment → Source → GitHub Actions
```

After pushing code to the `main` branch, GitHub Actions will automatically build and deploy the Hugo website.

## Notes

- Do not commit the `public/` folder if the site is deployed using GitHub Actions.
- Make sure `baseURL` in `hugo.toml` matches the GitHub Pages URL.
- Make sure the Hugo theme exists inside the `themes/` folder or is configured correctly as a Git submodule.
- If the website has missing CSS or broken links, check the `baseURL` configuration.
- If GitHub Actions fails, check the build logs in the **Actions** tab.

## Author

**Nguyen Minh Tinh**

Repository: `intership-report`

## Acknowledgement

I would like to thank the **First Cloud AI Journey** program, mentors, and team members for supporting me during the internship and helping me gain practical experience with AWS Cloud and serverless application development.
