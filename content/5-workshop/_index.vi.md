+++
title = "Workshop"
weight = 5
chapter = false
pre = "<b>5. </b>"
+++

# Workshop

## Tổng quan

Trong mục workshop này, chúng ta sẽ xây dựng phần **Backend API** cho dự án **Serverless AI Invoice Scanner**.

Phần này tập trung vào nhiệm vụ của vai trò **Backend API Developer**, bao gồm:

- Xây dựng các route trong **Amazon API Gateway**.
- Tạo **Upload Lambda Function**.
- Tạo **Fetch Invoice Lambda Function**.
- Kết nối Lambda với **Amazon S3**.
- Kết nối Lambda với **Amazon DynamoDB**.
- Cấu hình CORS để frontend có thể gọi API.
- Kiểm thử các API endpoint bằng Postman hoặc frontend.

Mục tiêu của phần này là xây dựng một backend serverless hoạt động ổn định, cho phép React frontend upload file hóa đơn, lấy dữ liệu hóa đơn, tìm kiếm hóa đơn và cập nhật thông tin hóa đơn.

---

## Kiến trúc Backend API

Luồng backend API của dự án được mô tả như sau:

```txt
React Frontend
    ↓
Amazon API Gateway
    ↓
AWS Lambda
    ↓
Amazon S3 / Amazon DynamoDB
```

Dự án hiện tại sử dụng hai Lambda Function chính:

| Lambda Function | Chức năng |
|---|---|
| `UploadInvoiceFileFunction` | Nhận request upload hóa đơn từ API Gateway, lưu file vào S3 và xử lý file khi được S3 trigger kích hoạt. |
| `FetchInvoiceDetailsFunction` | Lấy dữ liệu, tìm kiếm và cập nhật thông tin hóa đơn trong DynamoDB thông qua request từ API Gateway. |

---

## Các mục nhỏ trong Workshop

Mục workshop này bao gồm **6 mục nhỏ**. Mỗi mục tập trung vào một phần trong quá trình xây dựng backend API.

---

### 5.1 Tạo S3 Bucket

[Đi tới mục 5.1](/5-workshop/5.1-create-s3-bucket/)

Trong mục này, chúng ta sẽ tạo **Amazon S3 Bucket** để lưu trữ các file hóa đơn được upload từ frontend.

S3 Bucket đóng vai trò là nơi lưu trữ file đầu vào của hệ thống. Các file hóa đơn sẽ được lưu trong prefix:

```txt
uploads/
```

Các công việc chính:

- Tạo S3 bucket.
- Cấu hình tên bucket và AWS Region.
- Bật Block Public Access để bảo vệ dữ liệu.
- Chuẩn bị prefix `uploads/`.
- Kiểm tra Lambda có thể upload file vào bucket.

---

### 5.2 Tạo DynamoDB Table

[Đi tới mục 5.2](/5-workshop/5.2-create-dynamodb-table/)

Trong mục này, chúng ta sẽ tạo **Amazon DynamoDB Table** để lưu dữ liệu hóa đơn đã được xử lý.

Tên bảng sử dụng trong dự án là:

```txt
InvoiceData
```

Các công việc chính:

- Tạo DynamoDB table `InvoiceData`.
- Cấu hình `InvoiceId` làm partition key.
- Chuẩn bị bảng để lưu dữ liệu hóa đơn đã trích xuất.
- Hiểu các field được frontend sử dụng như `CustomerName`, `InvoiceDate`, `TotalAmount`, `Tags` và `Starred`.

---

### 5.3 Tạo Upload Lambda Function

[Đi tới mục 5.3](/5-workshop/5.3-create-upload-lambda/)

Trong mục này, chúng ta sẽ tạo **UploadInvoiceFileFunction**, và cấu hình **S3 ObjectCreated Trigger** cho `UploadInvoiceFileFunction`

Function này nhận file hóa đơn từ API Gateway, decode nội dung file dạng base64 và lưu file đã upload vào Amazon S3.

Các công việc chính:

- Tạo `UploadInvoiceFileFunction`.
- Cấu hình runtime và handler cho Lambda.
- Thêm environment variables như `BUCKET_NAME` và `DYNAMO_TABLE_NAME`.
- Decode nội dung file base64 từ request upload của frontend.
- Lưu file đã upload vào S3 trong prefix `uploads/`.
- Trả JSON response về frontend.
- Cấu hình S3 Event Notification.
- Kích hoạt Lambda khi có object mới được tạo trong prefix `uploads/`.
- Đọc bucket name và object key từ S3 event.
- Xử lý các định dạng file được hỗ trợ: `.png`, `.jpg`, `.jpeg` và `.pdf`.
- Chuẩn bị Lambda cho bước OCR và xử lý AI.

---

### 5.5 Cấu hình API Gateway Upload Route

[Đi tới mục 5.4](/5-workshop/5.4-configure-api-gateway-upload/)

Trong mục này, chúng ta sẽ tạo route API Gateway cho chức năng upload hóa đơn.

Route upload là:

```txt
POST /uploads
```

Các công việc chính:

- Tạo API trong Amazon API Gateway.
- Thêm route `POST /uploads`.
- Kết nối route với `UploadInvoiceFileFunction`.
- Bật CORS để frontend có thể gọi API.
- Deploy API stage.
- Kiểm thử upload hóa đơn bằng Postman hoặc frontend.

---

### 5.6 Tạo Fetch Invoice Lambda Function

[Đi tới mục 5.6](/5-workshop/5.6-create-fetch-invoice-lambda/)

Trong mục này, chúng ta sẽ tạo **FetchInvoiceDetailsFunction**.

Function này chịu trách nhiệm lấy dữ liệu, tìm kiếm và cập nhật thông tin hóa đơn được lưu trong DynamoDB.

Các công việc chính:

- Tạo `FetchInvoiceDetailsFunction`.
- Kết nối function với DynamoDB table `InvoiceData`.
- Lấy danh sách tất cả hóa đơn.
- Lấy chi tiết hóa đơn theo `InvoiceId`.
- Tìm kiếm hóa đơn theo tên khách hàng.
- Cập nhật tags của hóa đơn.
- Cập nhật trạng thái starred.
- Trả dữ liệu JSON đã được chuẩn hóa về frontend.

---

### 5.7 Cấu hình các API Route quản lý hóa đơn

[Đi tới mục 5.7](/5-workshop/5.7-configure-invoice-management-api/)

Trong mục này, chúng ta sẽ cấu hình các route API Gateway cho phần quản lý hóa đơn.

Các route quản lý hóa đơn bao gồm:

```txt
GET /invoice
GET /invoice/{id}
GET /invoice?name=<customer_name>
GET /invoice/starred
PATCH /invoice/tags/{id}
PATCH /invoice/starred/{id}
```

Các công việc chính:

- Tạo các route GET và PATCH trong API Gateway.
- Kết nối các route với `FetchInvoiceDetailsFunction`.
- Cấu hình CORS headers.
- Kiểm thử từng API route bằng Postman.
- Kiểm tra dữ liệu trả về từ DynamoDB.
- Kiểm tra log của API Gateway và Lambda trong CloudWatch.

---

## Kết quả mong đợi

Sau khi hoàn thành mục workshop này, phần backend API sẽ sẵn sàng để tích hợp với frontend.

Hệ thống có thể:

- Nhận request upload hóa đơn từ frontend.
- Lưu file hóa đơn đã upload vào Amazon S3.
- Kích hoạt Lambda xử lý thông qua S3 ObjectCreated event.
- Lưu kết quả xử lý hóa đơn vào DynamoDB.
- Lấy dữ liệu hóa đơn từ DynamoDB.
- Tìm kiếm hóa đơn.
- Cập nhật tags và trạng thái starred.
- Trả JSON response về React frontend.

---

## Tóm tắt luồng Backend API

```txt
1. Người dùng upload hóa đơn từ React Frontend.

2. React Frontend gửi request POST /uploads đến API Gateway.

3. API Gateway gọi UploadInvoiceFileFunction.

4. UploadInvoiceFileFunction lưu file đã upload vào S3.

5. S3 ObjectCreated trigger gọi lại UploadInvoiceFileFunction.

6. UploadInvoiceFileFunction xử lý file và lưu kết quả vào DynamoDB.

7. React Frontend gửi các request GET hoặc PATCH đến API Gateway để quản lý hóa đơn.

8. API Gateway gọi FetchInvoiceDetailsFunction.

9. FetchInvoiceDetailsFunction truy vấn hoặc cập nhật dữ liệu trong DynamoDB.

10. API Gateway trả dữ liệu hóa đơn về frontend.
```

---

## Ghi chú

{{% notice info %}}
Mục workshop này tập trung vào phần backend API. Phần giao diện frontend, xác thực bằng Cognito và deploy bằng Amplify Hosting có thể được trình bày ở các mục riêng.
{{% /notice %}}

{{% notice warning %}}
Hãy đảm bảo các Lambda Function có đúng IAM permissions trước khi kiểm thử API. Thiếu quyền có thể gây lỗi `AccessDenied` khi Lambda truy cập S3, DynamoDB, Textract hoặc CloudWatch Logs.
{{% /notice %}}

{{% notice info %}}
Trong quá trình kiểm thử, bạn có thể sử dụng Postman trước khi kết nối API với React frontend. Điều này giúp kiểm tra từng backend route hoạt động đúng hay chưa.
{{% /notice %}}
