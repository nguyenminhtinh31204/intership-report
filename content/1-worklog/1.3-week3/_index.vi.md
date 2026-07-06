---
title: "Worklog Tuần 3 "
date: 2026-05-04
weight: 103
week: 3
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 04/05/2026 - 10/05/2026 |
| Tuần thực tập | Tuần 3 |
| Giai đoạn | Giai đoạn học tập và nghiên cứu tài liệu |
| Chương trình học | First Cloud Journey |
| Chủ đề chính | Database, API và kiến trúc Serverless trên AWS |
| Mục tiêu tuần | Tìm hiểu các dịch vụ phục vụ lưu trữ dữ liệu, xây dựng API và thiết kế ứng dụng serverless |

---

## Định hướng học tập Tuần 3

Sau khi đã tìm hiểu các dịch vụ nền tảng như S3, EC2, Lambda, VPC, CloudWatch và IAM ở tuần 2, tuần 3 tiếp tục học theo chương trình **First Cloud Journey** với trọng tâm là **database**, **API** và **serverless application pattern**.

Trong tuần này, em chưa bắt đầu triển khai project chính. Mục tiêu là hiểu rõ hơn cách dữ liệu được lưu trữ, cách frontend giao tiếp với backend thông qua API và cách các dịch vụ AWS phối hợp trong mô hình serverless.

---

## Mục tiêu học tập Tuần 3

Các mục tiêu chính trong tuần gồm:

- Tìm hiểu Amazon DynamoDB và mô hình NoSQL.
- Tìm hiểu Amazon RDS ở mức tổng quan để phân biệt SQL và NoSQL.
- Tìm hiểu Amazon API Gateway và vai trò của API trong hệ thống cloud.
- Tìm hiểu kiến trúc serverless và event-driven.
- Hiểu cách Lambda kết hợp với API Gateway, S3 và DynamoDB.
- Ôn lại IAM trong ngữ cảnh cấp quyền cho Lambda truy cập database.
- Tìm hiểu cách giám sát API và Lambda bằng CloudWatch.
- Ghi chú các kiến thức có thể áp dụng cho project ở 4 tuần cuối.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 04/05/2026

Ngày đầu tiên của tuần 3 tập trung vào việc ôn lại các dịch vụ đã học và chuyển sang nhóm dịch vụ database.

Nội dung đã thực hiện:

- Ôn lại vai trò của S3, Lambda, CloudWatch và IAM.
- Xem lại cách các dịch vụ này có thể kết hợp trong một hệ thống serverless.
- Bắt đầu tìm hiểu nhóm dịch vụ database trên AWS.
- Phân biệt nhu cầu lưu trữ file và lưu trữ dữ liệu có cấu trúc.
- Ghi chú sự khác nhau giữa object storage và database.

Kết quả đạt được:

- Hiểu rằng S3 phù hợp để lưu file, còn database phù hợp để lưu dữ liệu cần truy vấn.
- Nắm được lý do một hệ thống cloud thường cần kết hợp nhiều loại lưu trữ.
- Có định hướng học tiếp về DynamoDB và RDS.

---

### Ngày 2 - Thứ ba, 05/05/2026

Ngày thứ hai tập trung vào **Amazon DynamoDB** và mô hình cơ sở dữ liệu NoSQL.

Nội dung đã thực hiện:

- Tìm hiểu Amazon DynamoDB là gì.
- Tìm hiểu các khái niệm:
  - Table
  - Item
  - Attribute
  - Partition key
  - Sort key
- Tìm hiểu mô hình NoSQL và cách dữ liệu được lưu dưới dạng key-value/document.
- Đọc tài liệu về khả năng tự động mở rộng của DynamoDB.
- Ghi chú các trường hợp nên dùng DynamoDB.

Ví dụ cấu trúc item trong DynamoDB:

```json
{
  "InvoiceId": "INV-001",
  "CustomerName": "Nguyen Van A",
  "TotalAmount": 1500000,
  "Currency": "VND"
}
```

Kết quả đạt được:

- Hiểu DynamoDB là cơ sở dữ liệu NoSQL được quản lý hoàn toàn bởi AWS.
- Biết DynamoDB phù hợp với ứng dụng cần truy vấn nhanh và scale tốt.
- Hiểu vai trò của partition key trong việc xác định item.

---

### Ngày 3 - Thứ tư, 06/05/2026

Ngày thứ ba tập trung vào **Amazon RDS** và việc so sánh giữa SQL và NoSQL.

Nội dung đã thực hiện:

- Tìm hiểu Amazon RDS ở mức tổng quan.
- Tìm hiểu các hệ quản trị cơ sở dữ liệu được RDS hỗ trợ như MySQL, PostgreSQL, MariaDB.
- So sánh RDS với DynamoDB.
- Tìm hiểu khi nào nên dùng relational database và khi nào nên dùng NoSQL.
- Ghi chú ưu điểm của RDS trong các hệ thống cần quan hệ dữ liệu rõ ràng.
- Ghi chú ưu điểm của DynamoDB trong các hệ thống serverless cần scale nhanh.

Bảng so sánh cơ bản:

| Tiêu chí | Amazon RDS | Amazon DynamoDB |
|---|---|---|
| Mô hình dữ liệu | Quan hệ SQL | NoSQL key-value/document |
| Truy vấn | SQL | Query/Scan theo key và index |
| Quản lý server | AWS quản lý nhiều phần, vẫn cần cấu hình instance | Fully managed serverless |
| Phù hợp | Dữ liệu có quan hệ phức tạp | Ứng dụng cần scale nhanh, truy vấn theo key |
| Ví dụ | Quản lý đơn hàng, tài chính, ERP | Session, metadata, invoice records |

Kết quả đạt được:

- Phân biệt được RDS và DynamoDB.
- Hiểu không phải hệ thống nào cũng dùng cùng một loại database.
- Biết lựa chọn database phụ thuộc vào cấu trúc dữ liệu và cách truy vấn.

---

### Ngày 4 - Thứ năm, 07/05/2026

Ngày thứ tư tập trung vào **Amazon API Gateway** và cách xây dựng API cho ứng dụng cloud.

Nội dung đã thực hiện:

- Tìm hiểu API Gateway là gì.
- Tìm hiểu REST API và HTTP method.
- Tìm hiểu các method phổ biến:
  - GET
  - POST
  - PUT
  - PATCH
  - DELETE
- Tìm hiểu khái niệm resource, route, stage và endpoint.
- Tìm hiểu cách API Gateway kết nối với Lambda.
- Ghi chú vai trò của API Gateway trong việc kết nối frontend và backend.

Ví dụ API route:

```txt
POST /uploads
GET /items
GET /items/{id}
PATCH /items/{id}
DELETE /items/{id}
```

Kết quả đạt được:

- Hiểu API Gateway là cổng giao tiếp giữa client và backend.
- Biết API Gateway có thể gọi Lambda để xử lý request.
- Hiểu vai trò của stage khi deploy API.

---

### Ngày 5 - Thứ sáu, 08/05/2026

Ngày thứ năm tập trung vào kiến trúc **serverless** và **event-driven**.

Nội dung đã thực hiện:

- Tìm hiểu serverless application pattern.
- Ôn lại vai trò của AWS Lambda trong mô hình serverless.
- Tìm hiểu kiến trúc event-driven.
- Xem ví dụ S3 upload file có thể kích hoạt Lambda.
- Xem ví dụ API Gateway nhận request và kích hoạt Lambda.
- Tìm hiểu ưu điểm của mô hình event-driven:
  - Tự động phản ứng với sự kiện.
  - Giảm nhu cầu chạy server liên tục.
  - Dễ mở rộng theo số lượng request.
  - Tối ưu chi phí cho workload không liên tục.

Ví dụ luồng event-driven đơn giản:

```txt
User Upload File → S3 Event → Lambda Function → Save Result to Database
```

Kết quả đạt được:

- Hiểu event-driven là mô hình xử lý dựa trên sự kiện.
- Biết Lambda có thể được kích hoạt bởi nhiều nguồn khác nhau.
- Hiểu vì sao serverless phù hợp với các ứng dụng xử lý file, API và dữ liệu.

---

### Ngày 6 - Thứ bảy, 09/05/2026

Ngày thứ sáu tập trung vào bảo mật và giám sát trong các hệ thống dùng API và database.

Nội dung đã thực hiện:

- Ôn lại IAM Role cho Lambda.
- Tìm hiểu quyền Lambda cần khi truy cập DynamoDB.
- Tìm hiểu quyền Lambda cần khi ghi log vào CloudWatch.
- Tìm hiểu cơ bản về CORS trong API Gateway.
- Tìm hiểu cách CloudWatch ghi log cho Lambda.
- Ghi chú các lỗi thường gặp khi hệ thống API hoạt động không đúng.

Một số lỗi thường gặp:

| Lỗi | Nguyên nhân có thể |
|---|---|
| `AccessDenied` | Lambda thiếu quyền truy cập tài nguyên |
| `Missing Authentication Token` | Gọi sai API path, sai method hoặc chưa deploy stage |
| CORS error | API Gateway hoặc backend chưa cấu hình CORS |
| Timeout | Lambda xử lý quá lâu hoặc gọi dịch vụ ngoài chậm |
| 500 Internal Server Error | Lambda lỗi logic hoặc response sai định dạng |

Kết quả đạt được:

- Hiểu hơn vai trò của IAM trong hệ thống serverless.
- Biết CloudWatch là công cụ quan trọng để kiểm tra lỗi.
- Nắm được một số lỗi phổ biến khi làm việc với API Gateway và Lambda.

---

### Ngày 7 - Chủ nhật, 10/05/2026

Ngày cuối tuần dùng để tổng hợp kiến thức và liên hệ với project sẽ làm ở giai đoạn sau.

Nội dung đã thực hiện:

- Ôn lại DynamoDB, RDS, API Gateway, Lambda và serverless pattern.
- Tổng hợp ghi chú theo sơ đồ kiến trúc.
- Liên hệ kiến thức đã học với project **Serverless AI Invoice Scanner**.
- Ghi lại những dịch vụ có khả năng sẽ sử dụng trong project.
- Viết báo cáo worklog tuần 3.
- Chuẩn bị kế hoạch học cho tuần 4.

Kết quả đạt được:

- Hoàn thành tuần học thứ ba theo chương trình First Cloud Journey.
- Hiểu cách database, API và Lambda phối hợp trong hệ thống serverless.
- Có nền tảng để học thêm về authentication, deployment và monitoring ở tuần tiếp theo.

---

## Tổng kết kiến thức Tuần 3

Trong tuần 3, em đã học sâu hơn về nhóm dịch vụ phục vụ xây dựng ứng dụng cloud, đặc biệt là database, API và serverless architecture.

| Nhóm kiến thức | Nội dung đã học |
|---|---|
| Database | DynamoDB, RDS, SQL, NoSQL |
| API | API Gateway, REST API, method, route, stage, endpoint |
| Serverless | Lambda, event-driven, serverless application pattern |
| Security | IAM Role, permission cho Lambda truy cập database |
| Monitoring | CloudWatch Logs, debug API và Lambda |
| Architecture | Cách kết hợp API Gateway, Lambda và DynamoDB |

---

## Kết quả đạt được trong tuần

- Hiểu Amazon DynamoDB và mô hình NoSQL.
- Hiểu Amazon RDS ở mức tổng quan.
- Phân biệt được SQL và NoSQL.
- Hiểu vai trò của API Gateway trong hệ thống cloud.
- Biết cách API Gateway kết nối với Lambda.
- Hiểu mô hình serverless và event-driven.
- Biết các lỗi thường gặp khi làm việc với API Gateway, Lambda và IAM.
- Có thể liên hệ các kiến thức đã học với project sẽ làm ở 4 tuần cuối.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Dễ nhầm DynamoDB với RDS | Lập bảng so sánh SQL và NoSQL |
| Khó hiểu partition key và sort key | Xem ví dụ item đơn giản và cách truy vấn theo key |
| API Gateway có nhiều khái niệm mới | Tách riêng route, method, resource, stage và endpoint để học |
| Event-driven còn khá trừu tượng | Vẽ sơ đồ luồng sự kiện từ S3 đến Lambda |
| IAM permission liên quan nhiều dịch vụ | Ghi chú từng quyền theo từng trường hợp sử dụng |

---

## Bài học rút ra

- Việc chọn database phụ thuộc vào cách lưu trữ và truy vấn dữ liệu.
- DynamoDB phù hợp với kiến trúc serverless vì có khả năng scale tốt và không cần quản lý server.
- API Gateway là thành phần quan trọng để frontend giao tiếp với backend.
- Serverless không có nghĩa là không có backend, mà là không cần tự quản lý server.
- CloudWatch và IAM là hai phần cần chú ý khi triển khai bất kỳ hệ thống AWS nào.
- Nên học kiến trúc theo luồng xử lý thay vì chỉ học từng dịch vụ riêng lẻ.

---

## Kế hoạch cho Tuần 4

Tuần 4 là tuần cuối của giai đoạn học tập theo First Cloud Journey trước khi chuyển sang giai đoạn thực hiện project.

Nội dung dự kiến:

- Tìm hiểu Amazon Cognito.
- Tìm hiểu AWS Amplify Hosting.
- Tìm hiểu CI/CD cơ bản với GitHub và Amplify.
- Tìm hiểu AWS Well-Architected Framework ở mức tổng quan.
- Ôn tập lại các dịch vụ đã học trong 3 tuần đầu.
- Tổng hợp kiến thức để chuẩn bị bước vào project **Serverless AI Invoice Scanner**.
- Xây dựng kế hoạch triển khai project cho tuần 5 đến tuần 8.

---

## Nhận xét cuối tuần

Tuần 3 giúp em hiểu rõ hơn về cách xây dựng một ứng dụng cloud sử dụng database, API và Lambda. Các kiến thức về DynamoDB, API Gateway và serverless event-driven là nền tảng rất quan trọng để chuẩn bị cho project ở giai đoạn sau. Sau tuần này, em đã có cái nhìn rõ hơn về cách frontend có thể gửi request đến backend, cách Lambda xử lý nghiệp vụ và cách dữ liệu được lưu trong database trên AWS.
