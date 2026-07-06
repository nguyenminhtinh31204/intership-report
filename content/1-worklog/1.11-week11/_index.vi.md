---
title: "Worklog Tuần 11 "
date: 2026-06-29
weight: 111
week: 11
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 29/06/2026 - 05/07/2026 |
| Tuần thực tập | Tuần 11 |
| Giai đoạn | Giai đoạn hoàn thiện sau báo cáo |
| Project | Serverless AI Invoice Scanner |
| Chủ đề chính | Chỉnh sửa sau góp ý, hoàn thiện demo, kiểm tra cleanup và đóng gói tài liệu |
| Mục tiêu tuần | Rà soát lần cuối project, chỉnh sửa theo góp ý, hoàn thiện bộ tài liệu nộp và đảm bảo tài nguyên AWS được kiểm tra đầy đủ |

---

## Định hướng Tuần 11

Sau khi tuần 10 đã hoàn thiện báo cáo tổng kết, proposal, tài liệu Markdown và checklist cleanup, tuần 11 tập trung vào việc chỉnh sửa lần cuối trước khi nộp hoặc trình bày chính thức.

Trọng tâm của tuần này là:

- Đọc lại toàn bộ tài liệu đã viết.
- Chỉnh sửa nội dung chưa thống nhất.
- Chuẩn hóa thuật ngữ trong báo cáo.
- Kiểm tra lại hình ảnh, đường dẫn và cấu trúc Markdown.
- Chuẩn bị demo project theo kịch bản rõ ràng.
- Kiểm tra lần cuối các tài nguyên AWS.
- Đóng gói tài liệu và source code để bàn giao.

---

## Mục tiêu Tuần 11

Các mục tiêu chính trong tuần gồm:

- Kiểm tra lại toàn bộ tài liệu từ Introduction đến Cleanup.
- Chỉnh sửa các phần còn nhầm giữa Amazon Bedrock và OpenAI API.
- Chuẩn hóa tên dịch vụ như AWS Amplify Hosting, Amazon Textract, Amazon Cognito và Amazon DynamoDB.
- Kiểm tra lại API routes trong tài liệu.
- Kiểm tra lại sơ đồ kiến trúc.
- Kiểm tra source code frontend và backend.
- Kiểm thử lại một số chức năng quan trọng trước demo.
- Chuẩn bị nội dung trình bày project.
- Kiểm tra tài nguyên AWS còn tồn tại để tránh phát sinh chi phí.
- Hoàn thiện bản bàn giao cuối cùng.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 29/06/2026

Ngày đầu tiên của tuần 11 tập trung vào việc đọc lại toàn bộ tài liệu và rà soát lỗi nội dung.

Nội dung đã thực hiện:

- Kiểm tra lại tài liệu giới thiệu project.
- Kiểm tra lại phần mô tả kiến trúc hệ thống.
- Kiểm tra lại danh sách dịch vụ AWS sử dụng.
- Kiểm tra các phần đã thay Amazon Bedrock bằng OpenAI API.
- Kiểm tra phần mô tả vai trò của Amazon Textract.
- Kiểm tra phần mô tả vai trò của OpenAI API.
- Ghi chú các đoạn cần chỉnh sửa để tài liệu thống nhất hơn.

Kết quả đạt được:

- Phát hiện được một số nội dung cần chỉnh sửa về tên dịch vụ.
- Chuẩn hóa lại hướng mô tả project theo đúng hệ thống thực tế.
- Tài liệu giới thiệu rõ ràng và chính xác hơn.

---

### Ngày 2 - Thứ ba, 30/06/2026

Ngày thứ hai tập trung vào kiểm tra lại API Gateway và tài liệu API.

Nội dung đã thực hiện:

- Rà soát lại danh sách API routes.
- Kiểm tra method và path của từng endpoint.
- Đối chiếu API trong tài liệu với API đã triển khai.
- Kiểm tra phần test với Postman.
- Kiểm tra request body và response mẫu.
- Ghi chú các lỗi thường gặp khi gọi API Gateway.

Danh sách API được rà soát:

```txt
POST /uploads
GET /invoice
GET /invoice/{id}
GET /invoice?name=<customer_name>
PATCH /invoice/tags/{id}
PATCH /invoice/starred/{id}
```

Kết quả đạt được:

- API routes trong tài liệu được chuẩn hóa.
- Nội dung test bằng Postman rõ ràng hơn.
- Giảm khả năng nhầm route khi người khác đọc và thực hành lại.

---

### Ngày 3 - Thứ tư, 01/07/2026

Ngày thứ ba tập trung vào kiểm tra source code và biến môi trường của frontend.

Nội dung đã thực hiện:

- Kiểm tra lại file cấu hình môi trường frontend.
- Kiểm tra các endpoint API trong React app.
- Kiểm tra cấu hình Cognito:
  - AWS Region
  - User Pool ID
  - User Pool Client ID
- Kiểm tra cấu hình upload API.
- Kiểm tra cấu hình invoice management API.
- Kiểm tra biến `REACT_APP_SEND_AUTH_TOKEN`.
- Ghi chú các biến môi trường cần thiết khi deploy bằng Amplify Hosting.

Ví dụ biến môi trường:

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

- Xác định được các biến môi trường cần có khi deploy.
- Frontend dễ cấu hình lại hơn khi chuyển môi trường.
- Giảm lỗi do sai endpoint hoặc thiếu biến môi trường.

---

### Ngày 4 - Thứ năm, 02/07/2026

Ngày thứ tư tập trung vào kiểm thử lại các chức năng quan trọng của hệ thống.

Nội dung đã thực hiện:

- Kiểm thử đăng nhập và đăng xuất bằng Cognito.
- Kiểm thử upload hóa đơn.
- Kiểm tra file upload trong S3.
- Kiểm tra Lambda xử lý sau khi có file mới.
- Kiểm tra dữ liệu được lưu trong DynamoDB.
- Kiểm thử xem danh sách hóa đơn.
- Kiểm thử xem chi tiết hóa đơn.
- Kiểm thử search, tags và starred.
- Kiểm thử export Excel.
- Kiểm tra CloudWatch Logs nếu có lỗi.

Kết quả đạt được:

- Các chức năng chính vẫn hoạt động ổn định.
- Ghi nhận một số lỗi nhỏ về hiển thị dữ liệu.
- Chuẩn bị tốt hơn cho phần demo cuối.

---

### Ngày 5 - Thứ sáu, 03/07/2026

Ngày thứ năm tập trung vào chuẩn bị kịch bản demo và nội dung trình bày.

Nội dung đã thực hiện:

- Chuẩn bị kịch bản demo theo thứ tự rõ ràng.
- Chuẩn bị file hóa đơn mẫu để upload.
- Chuẩn bị dữ liệu có sẵn trong DynamoDB để minh họa.
- Chuẩn bị phần giải thích kiến trúc serverless.
- Chuẩn bị phần giải thích vai trò từng dịch vụ.
- Chuẩn bị phần trình bày luồng xử lý AI.
- Chuẩn bị phần trình bày cleanup resources.

Kịch bản demo dự kiến:

| Bước | Nội dung demo |
|---|---|
| 1 | Giới thiệu vấn đề xử lý hóa đơn thủ công |
| 2 | Trình bày kiến trúc Serverless AI Invoice Scanner |
| 3 | Đăng nhập vào frontend bằng Cognito |
| 4 | Upload hóa đơn |
| 5 | Kiểm tra file trong S3 |
| 6 | Kiểm tra dữ liệu trong DynamoDB |
| 7 | Xem danh sách và chi tiết hóa đơn |
| 8 | Demo search, tags, starred và export Excel |
| 9 | Kiểm tra CloudWatch Logs |
| 10 | Trình bày cleanup resources |

Kết quả đạt được:

- Có kịch bản demo đầy đủ và dễ trình bày.
- Chuẩn bị được dữ liệu mẫu để demo.
- Nội dung trình bày rõ ràng hơn.

---

### Ngày 6 - Thứ bảy, 04/07/2026

Ngày thứ sáu tập trung vào kiểm tra cleanup resources và tài nguyên có thể phát sinh chi phí.

Nội dung đã thực hiện:

- Kiểm tra lại API Gateway.
- Kiểm tra lại Lambda Functions.
- Kiểm tra S3 Bucket.
- Kiểm tra DynamoDB Table.
- Kiểm tra Cognito User Pool.
- Kiểm tra Amplify Hosting App.
- Kiểm tra CloudWatch Log Groups.
- Kiểm tra IAM Roles và Policies.
- Kiểm tra Secrets Manager nếu có lưu OpenAI API key.
- Kiểm tra Route 53 nếu có custom domain.

Checklist cleanup được rà soát:

```txt
1. Delete API Gateway
2. Delete Lambda Functions
3. Empty and delete S3 Bucket
4. Delete DynamoDB Table
5. Delete Cognito User Pool
6. Delete Amplify Hosting App
7. Delete CloudWatch Log Groups
8. Delete unused IAM Roles and Policies
9. Review optional resources: Route 53, Secrets Manager, Parameter Store
```

Kết quả đạt được:

- Xác định được các tài nguyên cần xóa sau khi demo.
- Giảm nguy cơ phát sinh chi phí không mong muốn.
- Checklist cleanup hoàn thiện hơn.

---

### Ngày 7 - Chủ nhật, 05/07/2026

Ngày cuối tuần tập trung vào đóng gói tài liệu và tổng kết tuần 11.

Nội dung đã thực hiện:

- Tổng hợp tài liệu Markdown.
- Kiểm tra tên file và thứ tự các mục.
- Kiểm tra lại worklog.
- Kiểm tra proposal đã chỉnh sửa.
- Kiểm tra tài liệu cleanup.
- Chuẩn bị thư mục hoặc file nộp.
- Viết worklog tuần 11.
- Ghi chú các nội dung cần trình bày khi bảo vệ project.

Kết quả đạt được:

- Tài liệu đã được rà soát và sắp xếp đầy đủ.
- Project sẵn sàng để demo, nộp hoặc bàn giao.
- Hoàn thành tuần chỉnh sửa và hoàn thiện sau báo cáo.

---

## Tổng kết kiến thức Tuần 11

Trong tuần 11, em tập trung vào việc chỉnh sửa, rà soát và hoàn thiện các nội dung cuối cùng sau khi project đã hoàn thành.

| Nhóm công việc | Nội dung đã thực hiện |
|---|---|
| Documentation Review | Kiểm tra tài liệu Introduction, API, Frontend, Cleanup |
| API Review | Đối chiếu API routes với hệ thống đã triển khai |
| Frontend Review | Kiểm tra biến môi trường và cấu hình Cognito/API |
| Testing | Kiểm thử lại các chức năng chính |
| Demo Preparation | Chuẩn bị kịch bản demo và dữ liệu mẫu |
| Cleanup Review | Rà soát tài nguyên AWS cần xóa |
| Handover | Đóng gói tài liệu và nội dung bàn giao |

---

## Kết quả đạt được trong tuần

- Chỉnh sửa và chuẩn hóa tài liệu project.
- Kiểm tra lại API Gateway routes.
- Kiểm tra lại cấu hình frontend.
- Kiểm thử lại các chức năng chính.
- Chuẩn bị kịch bản demo project.
- Rà soát lại checklist cleanup.
- Đóng gói tài liệu để bàn giao.
- Project sẵn sàng cho phần trình bày cuối cùng.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Một số nội dung tài liệu chưa thống nhất | Rà soát lại theo kiến trúc thực tế của project |
| Dễ nhầm giữa Amplify Hosting và Amplify backend | Ghi rõ Amplify chỉ dùng để deploy frontend |
| Cần chuẩn hóa nhiều API route | Lập bảng method, route và chức năng |
| Demo cần ngắn gọn nhưng đầy đủ | Chuẩn bị kịch bản theo luồng xử lý chính |
| Cleanup có nhiều tài nguyên cần kiểm tra | Dùng checklist theo từng dịch vụ AWS |

---

## Bài học rút ra

- Sau khi hoàn thành project, việc rà soát tài liệu cũng quan trọng như việc viết code.
- Tên dịch vụ và luồng kiến trúc cần thống nhất trong toàn bộ báo cáo.
- Demo project nên đi theo một luồng đơn giản, dễ hiểu và thể hiện được chức năng chính.
- Kiểm tra cleanup giúp tránh phát sinh chi phí sau khi kết thúc lab.
- Việc chuẩn bị dữ liệu mẫu trước giúp demo mượt hơn.
- Project cloud cần có tài liệu rõ ràng để người khác có thể triển khai lại.

---

## Hướng phát triển sau tuần 11

Nếu tiếp tục mở rộng project, có thể thực hiện:

- Bật Cognito Authorizer cho API Gateway.
- Chuyển OpenAI API key sang AWS Secrets Manager.
- Thêm SQS để xử lý hóa đơn bất đồng bộ.
- Thêm trạng thái xử lý realtime trên frontend.
- Thêm dashboard thống kê hóa đơn.
- Thêm tính năng chỉnh sửa dữ liệu AI trích xuất.
- Thêm phân quyền người dùng theo vai trò.
- Thêm chức năng xuất báo cáo theo tháng hoặc theo khách hàng.

---

## Nhận xét cuối tuần

Tuần 11 là tuần chỉnh sửa và hoàn thiện sau khi project đã được xây dựng xong. Thông qua việc rà soát tài liệu, kiểm tra lại API, chuẩn bị demo và kiểm tra cleanup, em hiểu rõ hơn quy trình hoàn thiện một project cloud trước khi bàn giao.

Sau tuần này, project **Serverless AI Invoice Scanner** đã có tài liệu đầy đủ hơn, kịch bản demo rõ ràng hơn và sẵn sàng cho việc trình bày hoặc nộp báo cáo cuối cùng.
