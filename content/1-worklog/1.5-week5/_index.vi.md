---
title: "Worklog Tuần 5 "
date: 2026-05-18
weight: 105
week: 5
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 18/05/2026 - 24/05/2026 |
| Tuần thực tập | Tuần 5 |
| Giai đoạn | Giai đoạn thực hiện project |
| Project | Serverless AI Invoice Scanner |
| Chủ đề chính | Phân tích yêu cầu, thiết kế kiến trúc và triển khai tài nguyên nền tảng |
| Mục tiêu tuần | Bắt đầu xây dựng project dựa trên kiến thức đã học từ First Cloud Journey |

---

## Định hướng Tuần 5

Sau khi hoàn thành 4 tuần học tập theo chương trình **First Cloud Journey**, tuần 5 bắt đầu bước vào giai đoạn thực hiện project **Serverless AI Invoice Scanner**.

Trong tuần này, trọng tâm là phân tích yêu cầu hệ thống, thiết kế kiến trúc tổng thể và triển khai các tài nguyên AWS nền tảng ban đầu. Đây là bước chuẩn bị quan trọng trước khi tích hợp xử lý AI bằng Amazon Textract và OpenAI API ở các tuần tiếp theo.

---

## Mục tiêu Tuần 5

Các mục tiêu chính trong tuần gồm:

- Phân tích yêu cầu chức năng của hệ thống.
- Xác định các dịch vụ AWS sẽ sử dụng trong project.
- Thiết kế kiến trúc tổng thể của hệ thống.
- Tạo Amazon S3 bucket để lưu file hóa đơn.
- Tạo DynamoDB table để lưu dữ liệu hóa đơn.
- Tạo Lambda function xử lý upload file.
- Tạo API Gateway route `POST /uploads`.
- Kiểm thử upload file bằng Postman.
- Theo dõi log lỗi bằng Amazon CloudWatch.
- Ghi chú các lỗi gặp phải trong quá trình triển khai.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 18/05/2026

Ngày đầu tiên của tuần 5 tập trung vào việc phân tích yêu cầu project và xác định phạm vi triển khai.

Nội dung đã thực hiện:

- Xác định mục tiêu của project **Serverless AI Invoice Scanner**.
- Phân tích các chức năng chính của hệ thống:
  - Upload file hóa đơn.
  - Lưu file hóa đơn vào Amazon S3.
  - Xử lý hóa đơn bằng AI.
  - Lưu dữ liệu hóa đơn vào DynamoDB.
  - Hiển thị và quản lý dữ liệu trên frontend.
- Xác định các thành phần chính trong kiến trúc.
- Ghi chú các dịch vụ AWS cần sử dụng.

Các dịch vụ dự kiến sử dụng:

| Dịch vụ | Vai trò |
|---|---|
| AWS Amplify Hosting | Deploy frontend React |
| Amazon Cognito | Đăng ký, đăng nhập người dùng |
| Amazon API Gateway | Tạo REST API cho frontend |
| AWS Lambda | Xử lý logic backend |
| Amazon S3 | Lưu file hóa đơn |
| Amazon Textract | Trích xuất văn bản từ hóa đơn |
| OpenAI API | Chuẩn hóa dữ liệu OCR |
| Amazon DynamoDB | Lưu dữ liệu hóa đơn |
| Amazon CloudWatch | Ghi log và debug |
| AWS IAM | Quản lý quyền truy cập |

Kết quả đạt được:

- Xác định rõ mục tiêu của project.
- Nắm được phạm vi chức năng cần triển khai.
- Có danh sách dịch vụ AWS cần sử dụng.

---

### Ngày 2 - Thứ ba, 19/05/2026

Ngày thứ hai tập trung vào thiết kế kiến trúc tổng thể của hệ thống.

Nội dung đã thực hiện:

- Vẽ luồng xử lý chính của hệ thống.
- Xác định cách frontend giao tiếp với backend.
- Xác định API upload hóa đơn.
- Xác định nơi lưu file gốc và nơi lưu dữ liệu đã xử lý.
- Xác định Lambda functions cần tạo trong project.

Luồng kiến trúc tổng thể:

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

Các Lambda functions chính:

| Lambda Function | Vai trò |
|---|---|
| `UploadInvoiceFileFunction` | Nhận file từ API Gateway và upload vào S3 |
| `ProcessInvoiceFunction` | Xử lý file từ S3, gọi Textract và OpenAI API |
| `InvoiceManagementFunction` | Truy vấn, tìm kiếm và cập nhật dữ liệu hóa đơn |

Kết quả đạt được:

- Hoàn thành thiết kế luồng xử lý tổng thể.
- Xác định được 3 Lambda functions chính.
- Hiểu rõ thứ tự xử lý từ upload file đến lưu dữ liệu.

---

### Ngày 3 - Thứ tư, 20/05/2026

Ngày thứ ba tập trung vào việc tạo **Amazon S3 bucket** cho project.

Nội dung đã thực hiện:

- Tạo S3 bucket để lưu file hóa đơn.
- Cấu hình bucket theo region đã chọn.
- Kiểm tra tùy chọn block public access.
- Tạo thư mục logic `uploads/`.
- Ghi chú cách đặt tên object khi upload.
- Kiểm tra quyền truy cập bucket.

Cấu trúc lưu trữ dự kiến:

```txt
s3://invoice-scanner-upload-bucket/uploads/
```

Vai trò của S3 trong project:

- Lưu file hóa đơn gốc.
- Là nơi nhận file từ Lambda upload.
- Kích hoạt Lambda xử lý khi có file mới.
- Lưu các file PDF, PNG, JPG hoặc JPEG.

Kết quả đạt được:

- Tạo được S3 bucket cho project.
- Hiểu rõ vai trò của thư mục `uploads/`.
- Chuẩn bị được nơi lưu file đầu vào cho hệ thống.

---

### Ngày 4 - Thứ năm, 21/05/2026

Ngày thứ tư tập trung vào việc tạo **DynamoDB table** để lưu dữ liệu hóa đơn.

Nội dung đã thực hiện:

- Tạo DynamoDB table tên `InvoiceData`.
- Xác định khóa chính là `InvoiceId`.
- Thiết kế các trường dữ liệu chính cần lưu.
- Tìm hiểu cách lưu dữ liệu dạng JSON trong DynamoDB.
- Ghi chú các trường phục vụ tìm kiếm, tags và starred.

Cấu trúc dữ liệu dự kiến:

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

Các trường quan trọng:

| Trường | Vai trò |
|---|---|
| `InvoiceId` | Định danh hóa đơn |
| `CustomerName` | Tên khách hàng |
| `InvoiceNumber` | Số hóa đơn |
| `InvoiceDate` | Ngày hóa đơn |
| `TotalAmount` | Tổng tiền |
| `Currency` | Loại tiền tệ |
| `Tags` | Nhãn phân loại hóa đơn |
| `Starred` | Đánh dấu hóa đơn quan trọng |
| `ExtractedData` | Dữ liệu AI đã trích xuất |

Kết quả đạt được:

- Tạo được DynamoDB table `InvoiceData`.
- Xác định được cấu trúc dữ liệu ban đầu.
- Chuẩn bị được database cho các bước xử lý tiếp theo.

---

### Ngày 5 - Thứ sáu, 22/05/2026

Ngày thứ năm tập trung vào việc tạo Lambda function đầu tiên: **UploadInvoiceFileFunction**.

Nội dung đã thực hiện:

- Tạo Lambda function mới.
- Chọn runtime phù hợp cho backend.
- Cấu hình Lambda handler.
- Tạo hoặc kiểm tra IAM execution role.
- Viết logic xử lý request upload file.
- Tìm hiểu cách decode file Base64.
- Tìm hiểu cách upload object từ Lambda lên S3.
- Kiểm tra log chạy Lambda bằng CloudWatch.

Luồng xử lý của Lambda:

```txt
Nhận request từ API Gateway
    ↓
Đọc filename, contentType và file Base64
    ↓
Decode Base64
    ↓
Upload file vào S3 /uploads
    ↓
Trả response về client
```

Kết quả đạt được:

- Tạo được `UploadInvoiceFileFunction`.
- Hiểu cách Lambda nhận request từ API Gateway.
- Biết Lambda cần quyền IAM để ghi file vào S3.

---

### Ngày 6 - Thứ bảy, 23/05/2026

Ngày thứ sáu tập trung vào việc tạo API Gateway route cho chức năng upload.

Nội dung đã thực hiện:

- Tạo API Gateway cho project.
- Tạo route:

```txt
POST /uploads
```

- Kết nối route với `UploadInvoiceFileFunction`.
- Cấu hình stage deploy.
- Kiểm tra endpoint sau khi deploy.
- Tìm hiểu lỗi thường gặp khi gọi API Gateway.
- Ghi chú cấu hình CORS cần thiết khi frontend gọi API.

Các lỗi cần chú ý:

| Lỗi | Nguyên nhân có thể |
|---|---|
| `Missing Authentication Token` | Sai path, sai method hoặc chưa deploy API stage |
| CORS error | Chưa cấu hình CORS hoặc thiếu response headers |
| 500 Internal Server Error | Lambda lỗi logic hoặc trả response sai format |
| Access denied | Lambda thiếu quyền truy cập S3 |

Kết quả đạt được:

- Tạo được route `POST /uploads`.
- Kết nối được API Gateway với Lambda upload.
- Có endpoint để kiểm thử bằng Postman.

---

### Ngày 7 - Chủ nhật, 24/05/2026

Ngày cuối tuần tập trung vào kiểm thử upload và tổng hợp kết quả.

Nội dung đã thực hiện:

- Tạo request test trên Postman.
- Gửi request `POST /uploads` đến API Gateway.
- Kiểm tra Lambda có nhận được request hay không.
- Kiểm tra file có được lưu vào S3 hay không.
- Đọc log trong CloudWatch để tìm lỗi.
- Tổng hợp các tài nguyên đã tạo trong tuần.
- Chuẩn bị kế hoạch cho tuần 6.

Ví dụ request body dùng để test:

```json
{
  "filename": "invoice-test.png",
  "contentType": "image/png",
  "file": "base64_string_here"
}
```

Kết quả đạt được:

- Kiểm thử được API upload bằng Postman.
- Kiểm tra được file trong S3.
- Biết cách debug lỗi bằng CloudWatch Logs.
- Hoàn thành nền tảng ban đầu của project.

---

## Tổng kết kiến thức Tuần 5

Trong tuần 5, em đã bắt đầu triển khai project **Serverless AI Invoice Scanner** sau giai đoạn học First Cloud Journey. Trọng tâm là xây dựng luồng upload hóa đơn đầu tiên từ API Gateway đến Lambda và S3.

| Nhóm kiến thức | Nội dung đã thực hiện |
|---|---|
| Project Analysis | Phân tích yêu cầu và phạm vi project |
| Architecture Design | Thiết kế luồng xử lý tổng thể |
| Storage | Tạo S3 bucket và thư mục `uploads/` |
| Database | Tạo DynamoDB table `InvoiceData` |
| Backend | Tạo `UploadInvoiceFileFunction` |
| API | Tạo route `POST /uploads` |
| Testing | Kiểm thử upload bằng Postman |
| Monitoring | Debug lỗi bằng CloudWatch Logs |
| Security | Kiểm tra IAM Role cho Lambda truy cập S3 |

---

## Kết quả đạt được trong tuần

- Hoàn thành phân tích yêu cầu project.
- Hoàn thành thiết kế kiến trúc tổng thể.
- Tạo được S3 bucket để lưu file hóa đơn.
- Tạo được DynamoDB table `InvoiceData`.
- Tạo được Lambda function `UploadInvoiceFileFunction`.
- Tạo được API Gateway route `POST /uploads`.
- Kiểm thử upload bằng Postman.
- Kiểm tra log bằng CloudWatch.
- Hiểu rõ luồng upload file trong kiến trúc serverless.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Chưa quen kết nối API Gateway với Lambda | Kiểm tra lại integration và stage deploy |
| Lambda chưa upload được file vào S3 | Kiểm tra IAM Role và quyền `s3:PutObject` |
| Request Base64 dễ sai định dạng | Chuẩn hóa body test trên Postman |
| Gặp lỗi `Missing Authentication Token` | Kiểm tra lại method, route và stage URL |
| Khó đọc lỗi Lambda ban đầu | Sử dụng CloudWatch Logs để xem chi tiết |

---

## Bài học rút ra

- Cần thiết kế kiến trúc rõ ràng trước khi tạo tài nguyên AWS.
- API Gateway chỉ là điểm nhận request, logic xử lý chính nằm ở Lambda.
- Lambda cần IAM Role phù hợp để truy cập S3 và ghi log vào CloudWatch.
- S3 nên được cấu hình block public access để bảo vệ dữ liệu.
- Postman rất hữu ích để kiểm thử API trước khi tích hợp frontend.
- CloudWatch Logs là công cụ quan trọng để debug lỗi trong hệ thống serverless.

---

## Kế hoạch cho Tuần 6

Trong tuần tiếp theo, em sẽ tiếp tục triển khai phần xử lý hóa đơn bằng AI sau khi file đã được upload vào S3.

Nội dung dự kiến:

- Cấu hình S3 Event Notification.
- Tạo `ProcessInvoiceFunction`.
- Kết nối S3 trigger với Lambda xử lý.
- Tích hợp Amazon Textract để OCR hóa đơn.
- Tìm hiểu cách lấy text từ kết quả Textract.
- Kết nối OpenAI API để chuẩn hóa dữ liệu OCR.
- Lưu dữ liệu hóa đơn vào DynamoDB.
- Kiểm tra log xử lý bằng CloudWatch.
- Ghi chú lỗi và hoàn thiện tài liệu triển khai.

---

## Nhận xét cuối tuần

Tuần 5 là tuần đầu tiên bắt đầu triển khai project thực tế. Sau khi học nền tảng AWS trong 4 tuần đầu, em đã áp dụng kiến thức vào việc thiết kế kiến trúc và tạo các tài nguyên đầu tiên cho hệ thống. Kết quả quan trọng nhất của tuần là xây dựng được luồng upload hóa đơn cơ bản từ API Gateway đến Lambda và S3, làm nền tảng cho phần xử lý AI ở tuần tiếp theo.
