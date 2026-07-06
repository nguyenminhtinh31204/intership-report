---
title: "Worklog Tuần 8 "
date: 2026-06-08
weight: 108
week: 8
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 08/06/2026 - 14/06/2026 |
| Tuần thực tập | Tuần 8 |
| Giai đoạn | Giai đoạn hoàn thiện project |
| Project | Serverless AI Invoice Scanner |
| Chủ đề chính | Hoàn thiện frontend, kiểm thử end-to-end, deploy và viết tài liệu |
| Mục tiêu tuần | Hoàn thiện toàn bộ hệ thống, triển khai frontend bằng AWS Amplify Hosting, kiểm thử luồng xử lý đầy đủ và chuẩn bị báo cáo tổng kết thực tập |

---

## Định hướng Tuần 8

Tuần 8 là tuần cuối cùng của kỳ thực tập AWS và cũng là tuần hoàn thiện project **Serverless AI Invoice Scanner**. Sau khi các tuần trước đã triển khai luồng upload, xử lý hóa đơn bằng AI và xây dựng các API quản lý dữ liệu, tuần này tập trung vào việc hoàn thiện giao diện người dùng, kết nối toàn bộ hệ thống, kiểm thử end-to-end và viết tài liệu hướng dẫn.

Mục tiêu quan trọng nhất của tuần này là đảm bảo hệ thống có thể hoạt động theo luồng hoàn chỉnh:

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

## Mục tiêu Tuần 8

Các mục tiêu chính trong tuần gồm:

- Hoàn thiện giao diện frontend React.
- Tích hợp Amazon Cognito cho đăng ký và đăng nhập người dùng.
- Tích hợp frontend với các API Gateway endpoints.
- Hoàn thiện chức năng upload hóa đơn.
- Hoàn thiện chức năng xem danh sách và chi tiết hóa đơn.
- Hoàn thiện chức năng tìm kiếm theo tên khách hàng.
- Hoàn thiện chức năng cập nhật tags và starred.
- Bổ sung filter theo ngày, sort theo ngày hoặc tổng tiền.
- Bổ sung chức năng export dữ liệu hóa đơn ra Excel.
- Deploy frontend bằng AWS Amplify Hosting.
- Kiểm thử end-to-end toàn bộ hệ thống.
- Theo dõi lỗi bằng CloudWatch Logs.
- Hoàn thiện tài liệu hướng dẫn triển khai và cleanup resources.
- Tổng kết kết quả thực tập.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 08/06/2026

Ngày đầu tiên của tuần 8 tập trung vào việc rà soát lại toàn bộ backend và chuẩn bị tích hợp đầy đủ với frontend.

Nội dung đã thực hiện:

- Kiểm tra lại các Lambda functions đã tạo:
  - `UploadInvoiceFileFunction`
  - `ProcessInvoiceFunction`
  - `InvoiceManagementFunction`
- Kiểm tra lại các API Gateway routes:
  - `POST /uploads`
  - `GET /invoice`
  - `GET /invoice/{id}`
  - `GET /invoice?name=<customer_name>`
  - `PATCH /invoice/tags/{id}`
  - `PATCH /invoice/starred/{id}`
- Kiểm tra lại DynamoDB table `InvoiceData`.
- Kiểm tra lại S3 bucket và thư mục `uploads/`.
- Kiểm tra CloudWatch Logs của các Lambda functions.
- Ghi chú các lỗi còn tồn tại trước khi tích hợp frontend.

Kết quả đạt được:

- Xác nhận các backend services đã sẵn sàng.
- Kiểm tra được các endpoint quan trọng.
- Chuẩn bị đủ thông tin API endpoint để cấu hình frontend.

---

### Ngày 2 - Thứ ba, 09/06/2026

Ngày thứ hai tập trung vào hoàn thiện giao diện React và cấu hình biến môi trường cho frontend.

Nội dung đã thực hiện:

- Cập nhật file `.env` của frontend.
- Cấu hình Cognito User Pool ID, App Client ID và AWS Region.
- Cấu hình các API endpoint dùng cho upload, list, detail, search, tags và starred.
- Kiểm tra giao diện upload hóa đơn.
- Kiểm tra giao diện danh sách hóa đơn.
- Kiểm tra giao diện chi tiết hóa đơn.
- Điều chỉnh hiển thị dữ liệu tiền tệ theo `Currency`.
- Kiểm tra dữ liệu `Tags`, `Starred`, `CustomerName`, `TotalAmount` và `InvoiceDate`.

Ví dụ biến môi trường frontend:

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

Kết quả đạt được:

- Frontend đã kết nối được với các API backend.
- Giao diện hiển thị dữ liệu hóa đơn rõ ràng hơn.
- Các biến môi trường được tách riêng để dễ chỉnh sửa khi deploy.

---

### Ngày 3 - Thứ tư, 10/06/2026

Ngày thứ ba tập trung vào tích hợp Amazon Cognito và kiểm tra luồng đăng nhập, đăng ký.

Nội dung đã thực hiện:

- Tích hợp Cognito với React thông qua thư viện `aws-amplify`.
- Kiểm tra chức năng sign-up.
- Kiểm tra chức năng sign-in.
- Kiểm tra sign-out.
- Kiểm tra session người dùng sau khi đăng nhập.
- Kiểm tra giao diện chỉ hiển thị chức năng chính sau khi người dùng đăng nhập.
- Ghi chú vai trò của Cognito trong frontend authentication.

{{% notice info %}}
Trong project này, Cognito được dùng để bảo vệ phần đăng nhập và đăng ký ở frontend. API Gateway chỉ được bảo vệ bằng Cognito nếu có cấu hình Cognito Authorizer riêng.
{{% /notice %}}

Kết quả đạt được:

- Người dùng có thể đăng ký và đăng nhập vào hệ thống.
- Frontend có thể sử dụng thông tin session của Cognito.
- Hoàn thiện lớp authentication cơ bản cho ứng dụng.

---

### Ngày 4 - Thứ năm, 11/06/2026

Ngày thứ tư tập trung vào hoàn thiện các chức năng quản lý hóa đơn trên frontend.

Nội dung đã thực hiện:

- Hoàn thiện chức năng upload hóa đơn.
- Hoàn thiện chức năng xem danh sách hóa đơn.
- Hoàn thiện chức năng xem chi tiết hóa đơn.
- Hoàn thiện tìm kiếm hóa đơn theo tên khách hàng.
- Hoàn thiện cập nhật tags cho hóa đơn.
- Hoàn thiện cập nhật starred.
- Bổ sung filter theo ngày.
- Bổ sung sort theo ngày và tổng tiền.
- Bổ sung export dữ liệu ra file Excel.
- Kiểm tra hiển thị trạng thái khi đang loading hoặc khi API lỗi.

Các chức năng frontend đã hoàn thiện:

| Chức năng | Trạng thái |
|---|---|
| Đăng ký / đăng nhập | Hoàn thành |
| Upload hóa đơn | Hoàn thành |
| Xem danh sách hóa đơn | Hoàn thành |
| Xem chi tiết hóa đơn | Hoàn thành |
| Tìm kiếm theo tên khách hàng | Hoàn thành |
| Cập nhật tags | Hoàn thành |
| Cập nhật starred | Hoàn thành |
| Filter theo ngày | Hoàn thành |
| Sort theo ngày / tổng tiền | Hoàn thành |
| Export Excel | Hoàn thành |

Kết quả đạt được:

- Frontend đã hỗ trợ đầy đủ các chức năng chính.
- Người dùng có thể thao tác với hóa đơn trực tiếp trên giao diện.
- Dữ liệu từ API được hiển thị dễ hiểu hơn.

---

### Ngày 5 - Thứ sáu, 12/06/2026

Ngày thứ năm tập trung vào deploy frontend bằng **AWS Amplify Hosting**.

Nội dung đã thực hiện:

- Đưa mã nguồn frontend lên GitHub repository.
- Kết nối GitHub repository với AWS Amplify Hosting.
- Cấu hình build settings.
- Cấu hình environment variables trên Amplify.
- Chạy build và deploy frontend.
- Kiểm tra build logs nếu có lỗi.
- Truy cập URL do Amplify cung cấp.
- Kiểm tra frontend sau khi deploy.

Luồng deploy frontend:

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

Một số lỗi cần chú ý khi deploy:

| Lỗi | Nguyên nhân có thể |
|---|---|
| Build failed | Thiếu dependency hoặc sai build command |
| Environment variable missing | Chưa cấu hình biến môi trường trong Amplify |
| API call failed | Sai API endpoint hoặc lỗi CORS |
| Login failed | Sai Cognito User Pool ID hoặc App Client ID |
| Page reload lỗi | Chưa cấu hình redirect cho React Router |

Kết quả đạt được:

- Frontend được deploy thành công bằng AWS Amplify Hosting.
- Ứng dụng có URL để truy cập trên trình duyệt.
- Biết cách đọc Amplify build logs để kiểm tra lỗi deploy.

---

### Ngày 6 - Thứ bảy, 13/06/2026

Ngày thứ sáu tập trung vào kiểm thử end-to-end toàn bộ hệ thống.

Nội dung đã thực hiện:

- Đăng ký và đăng nhập bằng Cognito.
- Upload một file hóa đơn từ frontend.
- Kiểm tra file được lưu vào S3.
- Kiểm tra S3 trigger kích hoạt `ProcessInvoiceFunction`.
- Kiểm tra Textract trích xuất text.
- Kiểm tra OpenAI API chuẩn hóa dữ liệu.
- Kiểm tra dữ liệu được lưu vào DynamoDB.
- Kiểm tra frontend hiển thị hóa đơn mới.
- Kiểm tra tìm kiếm, tags, starred, filter, sort và export Excel.
- Kiểm tra CloudWatch Logs của các Lambda functions.
- Ghi chú các lỗi cuối cùng cần xử lý.

Luồng kiểm thử end-to-end:

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

Kết quả đạt được:

- Kiểm thử được luồng hoàn chỉnh từ frontend đến backend.
- Hệ thống có thể xử lý hóa đơn và hiển thị kết quả.
- Xác định và xử lý được một số lỗi cuối cùng trước khi hoàn thiện project.

---

### Ngày 7 - Chủ nhật, 14/06/2026

Ngày cuối cùng tập trung vào hoàn thiện tài liệu, cleanup resources và tổng kết thực tập.

Nội dung đã thực hiện:

- Hoàn thiện tài liệu hướng dẫn triển khai project.
- Hoàn thiện tài liệu test bằng Postman.
- Hoàn thiện tài liệu deploy frontend.
- Viết phần cleanup resources.
- Ghi chú các tài nguyên cần xóa sau khi kết thúc lab:
  - API Gateway
  - Lambda Functions
  - S3 Bucket
  - DynamoDB Table
  - Cognito User Pool
  - Amplify Hosting App
  - CloudWatch Log Groups
  - IAM Roles and Policies
  - Optional resources như Route 53 hoặc Secrets Manager
- Tổng hợp kết quả project.
- Viết báo cáo tổng kết tuần 8 và tổng kết kỳ thực tập.

Kết quả đạt được:

- Hoàn thiện project **Serverless AI Invoice Scanner**.
- Hoàn thiện tài liệu hướng dẫn.
- Có checklist cleanup tài nguyên AWS.
- Tổng kết được toàn bộ quá trình thực tập 8 tuần.

---

## Tổng kết kiến thức Tuần 8

Trong tuần 8, em đã hoàn thiện phần frontend, deploy ứng dụng bằng AWS Amplify Hosting, kiểm thử toàn bộ hệ thống và hoàn thiện tài liệu project.

| Nhóm kiến thức | Nội dung đã thực hiện |
|---|---|
| Frontend | Hoàn thiện React UI và các chức năng quản lý hóa đơn |
| Authentication | Tích hợp Amazon Cognito sign-up, sign-in, sign-out |
| Hosting | Deploy frontend bằng AWS Amplify Hosting |
| API Integration | Kết nối frontend với API Gateway endpoints |
| Testing | Kiểm thử end-to-end toàn bộ hệ thống |
| Monitoring | Kiểm tra CloudWatch Logs và Amplify build logs |
| Documentation | Hoàn thiện hướng dẫn triển khai, test và cleanup |
| Cleanup | Chuẩn bị danh sách tài nguyên cần xóa sau lab |

---

## Kết quả đạt được trong tuần

- Hoàn thiện frontend React.
- Tích hợp được Cognito authentication.
- Kết nối frontend với API Gateway.
- Hoàn thiện chức năng upload hóa đơn.
- Hoàn thiện chức năng xem danh sách và chi tiết hóa đơn.
- Hoàn thiện tìm kiếm, tags và starred.
- Bổ sung filter, sort và export Excel.
- Deploy frontend bằng AWS Amplify Hosting.
- Kiểm thử end-to-end toàn bộ hệ thống.
- Hoàn thiện tài liệu triển khai và cleanup.
- Hoàn thành project cuối kỳ thực tập.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Frontend gọi API bị lỗi CORS | Kiểm tra CORS headers ở API Gateway và Lambda response |
| Cognito login chưa hoạt động đúng | Kiểm tra User Pool ID, App Client ID và Region |
| Amplify build failed | Kiểm tra build logs, dependencies và environment variables |
| Dữ liệu frontend hiển thị sai format | Chuẩn hóa response từ Lambda và mapping lại field |
| Export Excel thiếu field | Kiểm tra dữ liệu trước khi export |
| API chạy được trên Postman nhưng lỗi trên frontend | Kiểm tra URL, CORS và request headers |

---

## Bài học rút ra

- Khi hoàn thiện một project cloud, frontend và backend cần thống nhất dữ liệu và endpoint.
- Amplify Hosting giúp deploy frontend nhanh nhưng cần cấu hình đúng biến môi trường.
- Cognito giúp triển khai xác thực người dùng mà không cần tự xây dựng hệ thống login từ đầu.
- Kiểm thử end-to-end rất quan trọng vì từng phần riêng lẻ hoạt động chưa chắc toàn hệ thống đã chạy đúng.
- CloudWatch Logs và Amplify build logs là công cụ quan trọng để debug lỗi.
- Cleanup resources là bước cần thiết để tránh phát sinh chi phí sau khi kết thúc lab.
- Tài liệu triển khai giúp người khác có thể tái tạo lại project dễ dàng hơn.

---

## Tổng kết giai đoạn 4 tuần project

Trong 4 tuần cuối của kỳ thực tập, em đã áp dụng kiến thức từ First Cloud Journey để xây dựng project **Serverless AI Invoice Scanner**.

| Tuần | Nội dung chính |
|---|---|
| Tuần 5 | Phân tích yêu cầu, thiết kế kiến trúc, tạo S3, DynamoDB, Lambda upload và API `POST /uploads` |
| Tuần 6 | Cấu hình S3 trigger, tích hợp Textract, OpenAI API và lưu dữ liệu vào DynamoDB |
| Tuần 7 | Xây dựng API quản lý hóa đơn và tích hợp frontend với backend |
| Tuần 8 | Hoàn thiện frontend, Cognito, Amplify Hosting, end-to-end testing, tài liệu và cleanup |

---

## Tổng kết 8 tuần thực tập

Sau 8 tuần thực tập AWS, quá trình học tập và thực hiện project được chia thành hai giai đoạn:

| Giai đoạn | Thời gian | Kết quả |
|---|---|---|
| Giai đoạn học tập | Tuần 1 - Tuần 4 | Hoàn thành học và nghiên cứu tài liệu theo First Cloud Journey |
| Giai đoạn project | Tuần 5 - Tuần 8 | Hoàn thành project Serverless AI Invoice Scanner |

Các kiến thức và kỹ năng đạt được:

- Hiểu nền tảng AWS Cloud.
- Biết sử dụng AWS Management Console.
- Hiểu các dịch vụ AWS cốt lõi như S3, Lambda, API Gateway, DynamoDB, Cognito, Amplify Hosting và CloudWatch.
- Hiểu mô hình serverless và event-driven.
- Biết triển khai frontend bằng AWS Amplify Hosting.
- Biết xây dựng backend bằng Lambda và API Gateway.
- Biết xử lý file bằng S3 Event Notification.
- Biết tích hợp Textract và OpenAI API để xử lý hóa đơn bằng AI.
- Biết lưu và quản lý dữ liệu bằng DynamoDB.
- Biết kiểm thử API bằng Postman.
- Biết debug lỗi bằng CloudWatch Logs.
- Biết viết tài liệu triển khai và cleanup tài nguyên.

---

## Kết quả cuối cùng của project

Project **Serverless AI Invoice Scanner** đã hoàn thành các chức năng chính:

| Chức năng | Trạng thái |
|---|---|
| Đăng ký / đăng nhập người dùng bằng Cognito | Hoàn thành |
| Upload hóa đơn từ frontend | Hoàn thành |
| Lưu file hóa đơn vào S3 | Hoàn thành |
| Tự động xử lý file bằng S3 trigger | Hoàn thành |
| Trích xuất văn bản bằng Amazon Textract | Hoàn thành |
| Chuẩn hóa dữ liệu bằng OpenAI API | Hoàn thành |
| Lưu dữ liệu vào DynamoDB | Hoàn thành |
| Lấy danh sách hóa đơn | Hoàn thành |
| Xem chi tiết hóa đơn | Hoàn thành |
| Tìm kiếm hóa đơn | Hoàn thành |
| Cập nhật tags | Hoàn thành |
| Cập nhật starred | Hoàn thành |
| Filter, sort và export Excel | Hoàn thành |
| Deploy frontend bằng Amplify Hosting | Hoàn thành |
| Viết tài liệu cleanup resources | Hoàn thành |

---

## Nhận xét cuối kỳ thực tập

Tuần 8 là tuần hoàn thiện và tổng kết project. Sau quá trình học tập từ First Cloud Journey và áp dụng vào project thực tế, em đã hiểu rõ hơn cách xây dựng một ứng dụng serverless trên AWS từ frontend đến backend. Project giúp em thực hành nhiều dịch vụ quan trọng như Amplify Hosting, Cognito, API Gateway, Lambda, S3, Textract, DynamoDB và CloudWatch.

Kết thúc kỳ thực tập, em đã hoàn thành được một hệ thống xử lý hóa đơn bằng AI theo kiến trúc serverless, đồng thời có thêm kinh nghiệm về thiết kế kiến trúc, triển khai, kiểm thử, debug và viết tài liệu cho một project cloud thực tế.
