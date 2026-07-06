---
title: "Worklog Tuần 6 "
date: 2026-05-25
weight: 106
week: 6
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 25/05/2026 - 31/05/2026 |
| Tuần thực tập | Tuần 6 |
| Giai đoạn | Giai đoạn thực hiện project |
| Project | Serverless AI Invoice Scanner |
| Chủ đề chính | Xây dựng luồng xử lý hóa đơn bằng AI |
| Mục tiêu tuần | Cấu hình S3 trigger, tạo Lambda xử lý hóa đơn, tích hợp Amazon Textract, OpenAI API và lưu dữ liệu vào DynamoDB |

---

## Định hướng Tuần 6

Sau khi tuần 5 đã hoàn thành phần nền tảng ban đầu gồm S3 bucket, DynamoDB table, Lambda upload và API Gateway `POST /uploads`, tuần 6 tập trung vào phần quan trọng nhất của project: **xử lý hóa đơn bằng AI**.

Trong tuần này, em triển khai luồng xử lý sau khi file hóa đơn được upload vào Amazon S3. Khi có file mới trong thư mục `uploads/`, S3 sẽ kích hoạt Lambda xử lý. Lambda này gọi Amazon Textract để trích xuất văn bản từ hóa đơn, sau đó gửi nội dung OCR sang OpenAI API để chuẩn hóa dữ liệu thành JSON và lưu kết quả vào DynamoDB.

Luồng xử lý chính trong tuần:

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

## Mục tiêu Tuần 6

Các mục tiêu chính trong tuần gồm:

- Cấu hình S3 Event Notification để kích hoạt Lambda khi có file mới.
- Tạo Lambda function `ProcessInvoiceFunction`.
- Cấp quyền IAM để Lambda đọc file từ S3, gọi Textract, ghi DynamoDB và ghi log CloudWatch.
- Tích hợp Amazon Textract để OCR file hóa đơn.
- Xử lý kết quả Textract và lấy nội dung text.
- Gửi text OCR sang OpenAI API để chuẩn hóa dữ liệu hóa đơn.
- Thiết kế cấu trúc JSON đầu ra.
- Lưu dữ liệu đã xử lý vào DynamoDB table `InvoiceData`.
- Kiểm tra trạng thái xử lý bằng CloudWatch Logs.
- Ghi chú lỗi và cách khắc phục trong quá trình tích hợp AI.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 25/05/2026

Ngày đầu tiên của tuần 6 tập trung vào việc chuẩn bị luồng xử lý sau khi file được upload vào S3.

Nội dung đã thực hiện:

- Ôn lại luồng upload đã hoàn thành ở tuần 5.
- Kiểm tra S3 bucket và thư mục `uploads/`.
- Tìm hiểu cơ chế S3 Event Notification.
- Xác định loại sự kiện cần dùng:

```txt
s3:ObjectCreated:*
```

- Xác định Lambda sẽ được kích hoạt khi có file mới.
- Chuẩn bị tên function xử lý:

```txt
ProcessInvoiceFunction
```

Kết quả đạt được:

- Hiểu cách S3 có thể tự động kích hoạt Lambda.
- Xác định được vai trò của `ProcessInvoiceFunction`.
- Chuẩn bị sẵn luồng xử lý AI cho các ngày tiếp theo.

---

### Ngày 2 - Thứ ba, 26/05/2026

Ngày thứ hai tập trung vào việc tạo **ProcessInvoiceFunction** và cấu hình quyền cần thiết.

Nội dung đã thực hiện:

- Tạo Lambda function `ProcessInvoiceFunction`.
- Cấu hình runtime và handler phù hợp.
- Kiểm tra IAM execution role của Lambda.
- Bổ sung quyền cần thiết cho Lambda:
  - Đọc file từ S3.
  - Gọi Amazon Textract.
  - Ghi dữ liệu vào DynamoDB.
  - Ghi log vào CloudWatch.
- Kiểm tra Lambda có thể nhận event từ S3.
- Xem CloudWatch Logs để kiểm tra event đầu vào.

Các quyền cần chú ý:

```txt
s3:GetObject
textract:DetectDocumentText
textract:AnalyzeDocument
dynamodb:PutItem
logs:CreateLogGroup
logs:CreateLogStream
logs:PutLogEvents
```

Kết quả đạt được:

- Tạo được `ProcessInvoiceFunction`.
- Hiểu các quyền IAM cần thiết cho Lambda xử lý hóa đơn.
- Lambda bước đầu nhận được event từ S3.

---

### Ngày 3 - Thứ tư, 27/05/2026

Ngày thứ ba tập trung vào cấu hình **S3 Event Notification** để kết nối S3 với Lambda.

Nội dung đã thực hiện:

- Mở phần Event Notifications của S3 bucket.
- Tạo event notification mới cho thư mục `uploads/`.
- Chọn event type là object created.
- Kết nối event với `ProcessInvoiceFunction`.
- Upload thử một file hóa đơn vào S3 để kiểm tra trigger.
- Kiểm tra CloudWatch Logs sau khi upload file.
- Ghi chú cấu trúc event mà S3 gửi sang Lambda.

Ví dụ thông tin quan trọng trong S3 event:

```json
{
  "bucket": "invoice-scanner-upload-bucket",
  "key": "uploads/invoice-test.png"
}
```

Kết quả đạt được:

- Cấu hình được S3 trigger cho Lambda.
- Khi upload file vào S3, Lambda được kích hoạt tự động.
- Biết cách đọc bucket name và object key từ S3 event.

---

### Ngày 4 - Thứ năm, 28/05/2026

Ngày thứ tư tập trung vào tích hợp **Amazon Textract** để trích xuất văn bản từ hóa đơn.

Nội dung đã thực hiện:

- Tìm hiểu cách gọi Amazon Textract từ Lambda.
- Kiểm tra định dạng file được Textract hỗ trợ.
- Viết logic gọi Textract với file trong S3.
- Lấy kết quả OCR từ response của Textract.
- Trích xuất các dòng text từ kết quả trả về.
- Ghi log nội dung OCR để kiểm tra.

Luồng xử lý Textract:

```txt
Lambda nhận S3 event
    ↓
Lấy bucket và key
    ↓
Gọi Amazon Textract
    ↓
Nhận danh sách Blocks
    ↓
Lọc các block dạng LINE
    ↓
Ghép thành nội dung OCR text
```

Ví dụ logic xử lý kết quả:

```txt
Blocks → LINE → Text → joined OCR content
```

Kết quả đạt được:

- Gọi được Amazon Textract từ Lambda.
- Trích xuất được nội dung text từ hóa đơn.
- Hiểu cách Textract trả về dữ liệu theo dạng block.

---

### Ngày 5 - Thứ sáu, 29/05/2026

Ngày thứ năm tập trung vào tích hợp **OpenAI API** để chuẩn hóa dữ liệu OCR.

Nội dung đã thực hiện:

- Tìm hiểu cách dùng OpenAI API trong backend.
- Chuẩn bị prompt yêu cầu AI trả về JSON có cấu trúc.
- Gửi nội dung OCR từ Textract sang OpenAI API.
- Yêu cầu AI trích xuất các trường hóa đơn quan trọng.
- Kiểm tra response trả về từ OpenAI API.
- Ghi chú cách bảo mật OpenAI API key.
- Không đưa API key vào frontend.

Các trường dữ liệu mong muốn:

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
OpenAI API key là thông tin nhạy cảm. API key chỉ nên được lưu ở backend thông qua Lambda environment variables hoặc AWS Secrets Manager, không được lưu trong React frontend hoặc public repository.
{{% /notice %}}

Kết quả đạt được:

- Tích hợp được OpenAI API ở mức xử lý backend.
- Có thể chuyển OCR text thành dữ liệu JSON có cấu trúc.
- Hiểu rõ nguyên tắc bảo mật API key khi dùng dịch vụ bên ngoài AWS.

---

### Ngày 6 - Thứ bảy, 30/05/2026

Ngày thứ sáu tập trung vào lưu dữ liệu hóa đơn đã xử lý vào **Amazon DynamoDB**.

Nội dung đã thực hiện:

- Chuẩn hóa dữ liệu trả về từ OpenAI API.
- Tạo `InvoiceId` cho hóa đơn.
- Bổ sung các field phục vụ frontend như `Tags` và `Starred`.
- Lưu item vào DynamoDB table `InvoiceData`.
- Kiểm tra dữ liệu trong DynamoDB Console.
- Ghi log trạng thái xử lý thành công hoặc thất bại.
- Bổ sung field `ProcessStatus` để theo dõi trạng thái xử lý.

Cấu trúc item lưu vào DynamoDB:

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

Kết quả đạt được:

- Lưu được dữ liệu hóa đơn vào DynamoDB.
- Dữ liệu sau xử lý có cấu trúc rõ ràng.
- Có thể kiểm tra item trực tiếp trong DynamoDB Console.

---

### Ngày 7 - Chủ nhật, 31/05/2026

Ngày cuối tuần tập trung vào kiểm thử toàn bộ luồng xử lý và tổng hợp kết quả.

Nội dung đã thực hiện:

- Upload thử file hóa đơn qua API `POST /uploads`.
- Kiểm tra file được lưu trong S3.
- Kiểm tra S3 trigger kích hoạt `ProcessInvoiceFunction`.
- Kiểm tra Textract có trích xuất được text không.
- Kiểm tra OpenAI API trả về dữ liệu JSON.
- Kiểm tra DynamoDB có item mới không.
- Đọc CloudWatch Logs để kiểm tra lỗi.
- Tổng hợp các lỗi đã gặp và hướng xử lý.
- Chuẩn bị kế hoạch cho tuần 7.

Luồng kiểm thử cuối tuần:

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

Kết quả đạt được:

- Kiểm thử được luồng xử lý AI từ S3 đến DynamoDB.
- Hiểu rõ cách debug từng bước bằng CloudWatch Logs.
- Hoàn thành phần nền tảng AI processing cho project.

---

## Tổng kết kiến thức Tuần 6

Trong tuần 6, em đã triển khai phần xử lý hóa đơn bằng AI cho project **Serverless AI Invoice Scanner**. Đây là phần quan trọng giúp hệ thống chuyển từ file hóa đơn thô sang dữ liệu có cấu trúc.

| Nhóm kiến thức | Nội dung đã thực hiện |
|---|---|
| Event-driven | Cấu hình S3 Event Notification |
| Lambda | Tạo `ProcessInvoiceFunction` |
| OCR | Tích hợp Amazon Textract |
| AI | Gửi OCR text sang OpenAI API để chuẩn hóa |
| Database | Lưu dữ liệu vào DynamoDB `InvoiceData` |
| Security | Bảo mật OpenAI API key ở backend |
| Monitoring | Theo dõi lỗi bằng CloudWatch Logs |
| IAM | Cấp quyền Lambda đọc S3, gọi Textract, ghi DynamoDB |

---

## Kết quả đạt được trong tuần

- Tạo được `ProcessInvoiceFunction`.
- Cấu hình được S3 Event Notification.
- Lambda tự động chạy khi có file mới trong S3.
- Tích hợp được Amazon Textract để OCR hóa đơn.
- Trích xuất được nội dung text từ file hóa đơn.
- Tích hợp được OpenAI API để chuẩn hóa dữ liệu OCR.
- Lưu được dữ liệu đã xử lý vào DynamoDB.
- Theo dõi và debug được quá trình xử lý bằng CloudWatch Logs.
- Hoàn thành luồng xử lý chính của hệ thống.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Lambda chưa được S3 trigger kích hoạt | Kiểm tra event notification, prefix `uploads/` và quyền invoke Lambda |
| Textract không đọc được một số file | Kiểm tra định dạng file và chất lượng hóa đơn |
| Lambda thiếu quyền gọi Textract | Bổ sung IAM permission phù hợp |
| OpenAI API trả về JSON chưa đúng định dạng | Điều chỉnh prompt và validate response |
| Dữ liệu DynamoDB bị thiếu field | Chuẩn hóa dữ liệu trước khi `PutItem` |
| Khó debug nhiều bước xử lý | Ghi log từng bước trong CloudWatch |

---

## Bài học rút ra

- Kiến trúc event-driven giúp tự động hóa xử lý sau khi file được upload.
- S3 Event Notification là cách hiệu quả để kích hoạt Lambda khi có file mới.
- Amazon Textract phù hợp để trích xuất text từ hóa đơn dạng ảnh hoặc PDF.
- OpenAI API giúp chuẩn hóa text OCR thành dữ liệu có cấu trúc dễ lưu trữ.
- Cần kiểm tra và validate dữ liệu AI trả về trước khi lưu vào DynamoDB.
- CloudWatch Logs rất quan trọng khi xử lý pipeline nhiều bước.
- API key của dịch vụ bên ngoài phải được bảo vệ ở backend.

---

## Kế hoạch cho Tuần 7

Trong tuần tiếp theo, em sẽ triển khai phần API quản lý hóa đơn và bắt đầu kết nối với frontend.

Nội dung dự kiến:

- Tạo `InvoiceManagementFunction`.
- Xây dựng API lấy danh sách hóa đơn:

```txt
GET /invoice
```

- Xây dựng API lấy chi tiết hóa đơn:

```txt
GET /invoice/{id}
```

- Xây dựng API tìm kiếm theo tên khách hàng:

```txt
GET /invoice?name=<customer_name>
```

- Xây dựng API cập nhật tags:

```txt
PATCH /invoice/tags/{id}
```

- Xây dựng API cập nhật starred:

```txt
PATCH /invoice/starred/{id}
```

- Kiểm thử các API bằng Postman.
- Bắt đầu tích hợp frontend React với API Gateway.
- Kiểm tra lỗi CORS và dữ liệu trả về cho frontend.

---

## Nhận xét cuối tuần

Tuần 6 là tuần triển khai phần xử lý AI quan trọng nhất của project. Sau tuần này, hệ thống đã có khả năng tự động nhận file từ S3, trích xuất nội dung bằng Amazon Textract, chuẩn hóa dữ liệu bằng OpenAI API và lưu kết quả vào DynamoDB. Đây là bước tiến lớn trong project vì hệ thống đã bắt đầu xử lý được hóa đơn theo đúng mục tiêu ban đầu. Tuần tiếp theo sẽ tập trung vào việc xây dựng API quản lý dữ liệu hóa đơn và kết nối với frontend.
