---
title: "Worklog Tuần 12 "
date: 2026-07-06
weight: 112
week: 12
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 06/07/2026 - 12/07/2026 |
| Tuần thực tập | Tuần 12 |
| Giai đoạn | Giai đoạn kết thúc thực tập |
| Project | Serverless AI Invoice Scanner |
| Chủ đề chính | Hoàn thiện bản cuối, trình bày project, bàn giao và tổng kết thực tập |
| Mục tiêu tuần | Hoàn tất toàn bộ tài liệu, trình bày kết quả project, bàn giao source code/tài liệu và tổng kết những kiến thức đã đạt được trong kỳ thực tập |

---

## Định hướng Tuần 12

Tuần 12 là tuần cuối cùng của quá trình thực tập AWS. Sau khi project **Serverless AI Invoice Scanner** đã được xây dựng, kiểm thử, rà soát và chỉnh sửa ở các tuần trước, tuần này tập trung vào việc hoàn thiện bản cuối cùng, chuẩn bị phần trình bày, bàn giao tài liệu và tổng kết toàn bộ quá trình thực tập.

Trọng tâm của tuần này gồm:

- Kiểm tra lại toàn bộ project lần cuối.
- Hoàn thiện bản báo cáo cuối cùng.
- Chuẩn bị nội dung trình bày project.
- Tổng hợp source code và tài liệu.
- Kiểm tra cleanup tài nguyên AWS.
- Ghi nhận kết quả đạt được.
- Đánh giá hạn chế và đề xuất hướng phát triển.
- Tổng kết kỹ năng và kiến thức học được sau kỳ thực tập.

---

## Mục tiêu Tuần 12

Các mục tiêu chính trong tuần gồm:

- Rà soát lần cuối source code frontend và backend.
- Kiểm tra lại các tài liệu Markdown đã viết.
- Hoàn thiện báo cáo thực tập cuối cùng.
- Chuẩn bị nội dung demo project.
- Kiểm tra lại các chức năng chính của hệ thống.
- Xác nhận danh sách tài nguyên AWS cần giữ hoặc cần xóa.
- Chuẩn bị file bàn giao gồm source code, tài liệu và worklog.
- Tổng hợp bài học kinh nghiệm.
- Đưa ra hướng phát triển trong tương lai.
- Hoàn thành worklog tuần 12.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 06/07/2026

Ngày đầu tiên của tuần 12 tập trung vào kiểm tra lại toàn bộ project trước khi chuẩn bị bản nộp cuối cùng.

Nội dung đã thực hiện:

- Kiểm tra lại source code frontend React.
- Kiểm tra lại các Lambda functions:
  - `UploadInvoiceFileFunction`
  - `ProcessInvoiceFunction`
  - `InvoiceManagementFunction`
- Kiểm tra lại API Gateway routes.
- Kiểm tra lại DynamoDB table `InvoiceData`.
- Kiểm tra lại S3 bucket lưu file hóa đơn.
- Kiểm tra lại cấu hình Cognito.
- Kiểm tra lại Amplify Hosting App.
- Ghi chú các phần đã hoàn thành và các điểm còn hạn chế.

Kết quả đạt được:

- Xác nhận project đã đầy đủ các thành phần chính.
- Nắm được trạng thái cuối cùng của hệ thống.
- Có danh sách nội dung cần đưa vào báo cáo tổng kết.

---

### Ngày 2 - Thứ ba, 07/07/2026

Ngày thứ hai tập trung vào hoàn thiện báo cáo thực tập và tài liệu mô tả project.

Nội dung đã thực hiện:

- Rà soát lại phần giới thiệu project.
- Kiểm tra phần mô tả vấn đề và mục tiêu hệ thống.
- Hoàn thiện phần kiến trúc serverless.
- Cập nhật phần mô tả các dịch vụ AWS đã sử dụng.
- Kiểm tra phần mô tả OpenAI API thay cho Amazon Bedrock.
- Cập nhật phần API routes và Lambda functions.
- Kiểm tra phần kết quả đạt được của project.

Các thành phần được mô tả trong báo cáo:

| Thành phần | Vai trò |
|---|---|
| AWS Amplify Hosting | Deploy frontend React |
| Amazon Cognito | Đăng ký và đăng nhập người dùng |
| Amazon API Gateway | Cung cấp REST API |
| AWS Lambda | Xử lý backend logic |
| Amazon S3 | Lưu file hóa đơn |
| Amazon Textract | Trích xuất văn bản từ hóa đơn |
| OpenAI API | Chuẩn hóa dữ liệu OCR |
| Amazon DynamoDB | Lưu dữ liệu hóa đơn |
| Amazon CloudWatch | Theo dõi log và debug |

Kết quả đạt được:

- Báo cáo có nội dung thống nhất với project thực tế.
- Các dịch vụ AWS được mô tả rõ ràng.
- Phần kiến trúc và luồng xử lý dễ hiểu hơn.

---

### Ngày 3 - Thứ tư, 08/07/2026

Ngày thứ ba tập trung vào chuẩn bị nội dung demo project.

Nội dung đã thực hiện:

- Chuẩn bị kịch bản demo cuối cùng.
- Chuẩn bị tài khoản test để đăng nhập.
- Chuẩn bị file hóa đơn mẫu để upload.
- Chuẩn bị dữ liệu mẫu trong DynamoDB.
- Kiểm tra lại website frontend được deploy bằng Amplify.
- Kiểm tra các bước demo theo đúng thứ tự.
- Ghi chú phần giải thích kiến trúc khi trình bày.

Kịch bản demo cuối cùng:

| Bước | Nội dung trình bày |
|---|---|
| 1 | Giới thiệu bài toán xử lý hóa đơn thủ công |
| 2 | Trình bày kiến trúc Serverless AI Invoice Scanner |
| 3 | Đăng nhập hệ thống bằng Cognito |
| 4 | Upload hóa đơn từ frontend |
| 5 | Kiểm tra file trong S3 |
| 6 | Kiểm tra Lambda xử lý và CloudWatch Logs |
| 7 | Kiểm tra dữ liệu trong DynamoDB |
| 8 | Xem danh sách hóa đơn trên frontend |
| 9 | Demo search, tags, starred, filter, sort và export Excel |
| 10 | Trình bày cleanup resources và hướng phát triển |

Kết quả đạt được:

- Có kịch bản demo hoàn chỉnh.
- Chuẩn bị sẵn dữ liệu và file mẫu.
- Sẵn sàng trình bày project theo luồng rõ ràng.

---

### Ngày 4 - Thứ năm, 09/07/2026

Ngày thứ tư tập trung vào kiểm thử lại toàn bộ luồng end-to-end trước khi trình bày.

Nội dung đã thực hiện:

- Đăng nhập frontend bằng Cognito.
- Upload file hóa đơn từ giao diện.
- Kiểm tra file được lưu trong S3.
- Kiểm tra S3 trigger gọi `ProcessInvoiceFunction`.
- Kiểm tra Amazon Textract trích xuất text.
- Kiểm tra OpenAI API chuẩn hóa dữ liệu.
- Kiểm tra dữ liệu được lưu vào DynamoDB.
- Kiểm tra API lấy danh sách hóa đơn.
- Kiểm tra frontend hiển thị dữ liệu mới.
- Kiểm tra tags, starred, search, filter, sort và export Excel.

Luồng end-to-end được kiểm thử:

```txt
Cognito Login
    ↓
React Frontend Upload
    ↓
API Gateway
    ↓
UploadInvoiceFileFunction
    ↓
S3 uploads/
    ↓
ProcessInvoiceFunction
    ↓
Amazon Textract
    ↓
OpenAI API
    ↓
DynamoDB InvoiceData
    ↓
InvoiceManagementFunction
    ↓
React Frontend Display
```

Kết quả đạt được:

- Luồng xử lý chính hoạt động ổn định.
- Giao diện frontend hiển thị được dữ liệu hóa đơn.
- Các chức năng quản lý hóa đơn đã sẵn sàng để demo.

---

### Ngày 5 - Thứ sáu, 10/07/2026

Ngày thứ năm tập trung vào cleanup resources và kiểm tra chi phí sau khi hoàn thành project.

Nội dung đã thực hiện:

- Rà soát danh sách tài nguyên AWS đã tạo.
- Kiểm tra tài nguyên cần giữ lại để demo.
- Kiểm tra tài nguyên có thể xóa sau khi nộp báo cáo.
- Rà soát checklist cleanup.
- Kiểm tra CloudWatch Log Groups.
- Kiểm tra IAM Roles và Policies không còn sử dụng.
- Kiểm tra Secrets Manager nếu có lưu OpenAI API key.
- Kiểm tra Route 53 nếu có dùng custom domain.
- Kiểm tra AWS Billing/Cost Explorer ở mức cơ bản.

Checklist cleanup cuối cùng:

```txt
1. Delete API Gateway
2. Delete Lambda Functions
3. Empty and delete S3 Bucket
4. Delete DynamoDB Table
5. Delete Cognito User Pool
6. Delete Amplify Hosting App
7. Delete CloudWatch Log Groups
8. Delete unused IAM Roles and Policies
9. Review Route 53, Secrets Manager and Parameter Store
10. Review AWS Billing / Cost Explorer
```

Kết quả đạt được:

- Có danh sách tài nguyên cần cleanup rõ ràng.
- Hiểu thứ tự xóa tài nguyên để tránh lỗi phụ thuộc.
- Giảm nguy cơ phát sinh chi phí sau khi kết thúc thực tập.

---

### Ngày 6 - Thứ bảy, 11/07/2026

Ngày thứ sáu tập trung vào đóng gói tài liệu và chuẩn bị bàn giao.

Nội dung đã thực hiện:

- Sắp xếp lại source code frontend.
- Sắp xếp lại code Lambda/backend.
- Tổng hợp file tài liệu Markdown.
- Tổng hợp worklog từ tuần 1 đến tuần 12.
- Kiểm tra proposal đã chỉnh sửa.
- Kiểm tra tài liệu cleanup.
- Kiểm tra hình ảnh và đường dẫn trong tài liệu.
- Chuẩn bị danh sách các file cần nộp hoặc bàn giao.

Nội dung bàn giao gồm:

| Thành phần | Nội dung |
|---|---|
| Source code frontend | React app |
| Backend code | Lambda functions |
| Documentation | Hướng dẫn triển khai và sử dụng |
| Proposal | Bản đề xuất project đã chỉnh sửa |
| Worklog | Nhật ký thực tập theo tuần |
| Cleanup guide | Hướng dẫn xóa tài nguyên AWS |
| Demo script | Kịch bản trình bày project |

Kết quả đạt được:

- Tài liệu và source code được tổ chức rõ ràng.
- Có đủ nội dung để nộp hoặc bàn giao.
- Hạn chế thiếu sót khi tổng kết thực tập.

---

### Ngày 7 - Chủ nhật, 12/07/2026

Ngày cuối cùng tập trung vào tổng kết toàn bộ kỳ thực tập.

Nội dung đã thực hiện:

- Viết worklog tuần 12.
- Tổng hợp lại quá trình học tập và làm project.
- Đánh giá kết quả đạt được.
- Ghi nhận các khó khăn đã gặp.
- Tổng hợp bài học kinh nghiệm.
- Đề xuất hướng phát triển trong tương lai.
- Hoàn thiện bản bàn giao cuối cùng.

Kết quả đạt được:

- Hoàn thành worklog tuần 12.
- Hoàn thành tổng kết kỳ thực tập.
- Project sẵn sàng để nộp, demo hoặc bàn giao.
- Có cái nhìn tổng thể về toàn bộ quá trình học AWS và triển khai project serverless.

---

## Tổng kết kiến thức Tuần 12

Trong tuần 12, em tập trung vào việc hoàn thiện bản cuối, chuẩn bị demo, cleanup và bàn giao project.

| Nhóm công việc | Nội dung đã thực hiện |
|---|---|
| Final Review | Kiểm tra lại project và tài nguyên AWS |
| Report Completion | Hoàn thiện báo cáo thực tập |
| Demo Preparation | Chuẩn bị kịch bản demo cuối cùng |
| End-to-End Testing | Kiểm thử lại toàn bộ luồng hệ thống |
| Cleanup Review | Kiểm tra tài nguyên AWS và chi phí |
| Handover | Đóng gói source code và tài liệu |
| Final Summary | Tổng kết kiến thức, kỹ năng và kết quả đạt được |

---

## Kết quả đạt được trong tuần

- Kiểm tra lần cuối toàn bộ project.
- Hoàn thiện báo cáo thực tập.
- Chuẩn bị kịch bản demo cuối cùng.
- Kiểm thử lại luồng end-to-end.
- Rà soát tài nguyên AWS và checklist cleanup.
- Đóng gói source code, tài liệu và worklog.
- Tổng kết kết quả thực tập.
- Hoàn thành tuần cuối của kỳ thực tập AWS.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Cần tổng hợp nhiều tài liệu khác nhau | Sắp xếp theo nhóm: source code, docs, worklog, proposal, cleanup |
| Demo cần thể hiện đủ chức năng nhưng không quá dài | Chuẩn bị kịch bản theo luồng xử lý chính |
| Cleanup có thể ảnh hưởng demo nếu xóa sớm | Chỉ ghi checklist, giữ tài nguyên cần thiết đến khi demo xong |
| Một số thông tin trong tài liệu cần thống nhất | Rà soát lại tên dịch vụ và luồng kiến trúc |
| Cần tổng kết quá trình dài nhiều tuần | Chia thành hai giai đoạn: học First Cloud Journey và làm project |

---

## Bài học rút ra

- Một project cloud cần được hoàn thiện cả về chức năng, tài liệu, kiểm thử và cleanup.
- Demo hiệu quả cần có kịch bản rõ ràng và dữ liệu mẫu chuẩn bị trước.
- Tài nguyên AWS cần được theo dõi và dọn dẹp sau khi không còn sử dụng.
- Việc học theo First Cloud Journey giúp xây dựng nền tảng trước khi làm project thực tế.
- Khi làm project serverless, cần hiểu rõ vai trò từng dịch vụ và cách chúng kết nối với nhau.
- CloudWatch Logs, Postman và tài liệu triển khai là những công cụ rất quan trọng trong quá trình phát triển.
- Báo cáo thực tập nên phản ánh đầy đủ cả quá trình học, quá trình làm và kết quả đạt được.

---

## Tổng kết toàn bộ kỳ thực tập

Quá trình thực tập được chia thành hai giai đoạn chính:

| Giai đoạn | Thời gian | Nội dung |
|---|---|---|
| Giai đoạn 1 | Tuần 1 - Tuần 4 | Học tập và nghiên cứu tài liệu theo chương trình First Cloud Journey |
| Giai đoạn 2 | Tuần 5 - Tuần 12 | Triển khai, hoàn thiện, rà soát, demo và bàn giao project Serverless AI Invoice Scanner |

Trong giai đoạn học tập, em đã làm quen với các kiến thức nền tảng về AWS Cloud, IAM, S3, Lambda, API Gateway, DynamoDB, CloudWatch, Cognito và Amplify Hosting.

Trong giai đoạn project, em đã áp dụng kiến thức để xây dựng hệ thống xử lý hóa đơn bằng AI theo kiến trúc serverless, kết hợp Amazon Textract, OpenAI API, Lambda, S3, DynamoDB và frontend React.

---

## Kết quả cuối cùng của project

Project **Serverless AI Invoice Scanner** đã hoàn thành các chức năng chính:

| Chức năng | Trạng thái |
|---|---|
| Frontend React | Hoàn thành |
| Deploy bằng AWS Amplify Hosting | Hoàn thành |
| Đăng ký / đăng nhập bằng Cognito | Hoàn thành |
| Upload hóa đơn | Hoàn thành |
| Lưu file vào S3 | Hoàn thành |
| S3 trigger Lambda xử lý | Hoàn thành |
| OCR bằng Amazon Textract | Hoàn thành |
| Chuẩn hóa dữ liệu bằng OpenAI API | Hoàn thành |
| Lưu dữ liệu vào DynamoDB | Hoàn thành |
| API quản lý hóa đơn | Hoàn thành |
| Search, tags, starred | Hoàn thành |
| Filter, sort, export Excel | Hoàn thành |
| CloudWatch Logs | Hoàn thành |
| Cleanup documentation | Hoàn thành |

---

## Hạn chế còn tồn tại

Mặc dù project đã hoàn thành các chức năng chính, vẫn còn một số hạn chế:

- API Gateway chưa bắt buộc bảo vệ bằng Cognito Authorizer trong mọi route.
- OpenAI API key nên được quản lý bằng AWS Secrets Manager ở môi trường production.
- Chưa có hàng đợi xử lý bất đồng bộ bằng SQS.
- Chưa có trạng thái realtime cho quá trình xử lý hóa đơn.
- Chưa có chức năng chỉnh sửa dữ liệu hóa đơn sau khi AI trích xuất.
- Chưa có dashboard thống kê nâng cao.
- Chưa có phân quyền chi tiết theo vai trò người dùng.

---

## Hướng phát triển trong tương lai

Nếu tiếp tục phát triển, project có thể mở rộng thêm:

- Bổ sung Cognito Authorizer cho API Gateway.
- Lưu OpenAI API key bằng AWS Secrets Manager.
- Thêm Amazon SQS để xử lý hóa đơn bất đồng bộ.
- Thêm trạng thái xử lý realtime trên frontend.
- Cho phép người dùng chỉnh sửa dữ liệu AI trích xuất.
- Tích hợp dashboard thống kê bằng Amazon QuickSight hoặc Power BI.
- Tích hợp email notification khi xử lý hóa đơn xong.
- Hỗ trợ nhiều loại chứng từ khác như biên lai, hợp đồng và phiếu thu.
- Bổ sung phân quyền user/admin.
- Tối ưu prompt và validation để tăng độ chính xác khi trích xuất dữ liệu.

---

## Nhận xét cuối kỳ

Tuần 12 là tuần kết thúc quá trình thực tập AWS. Sau khi hoàn thành chương trình học First Cloud Journey và project Serverless AI Invoice Scanner, em đã có thêm nhiều kiến thức thực tế về AWS Cloud, kiến trúc serverless và quy trình triển khai một ứng dụng cloud hoàn chỉnh.

Thông qua project, em đã hiểu cách thiết kế hệ thống, triển khai frontend, xây dựng API, xử lý file bằng Lambda, tích hợp AI, lưu dữ liệu vào DynamoDB, kiểm thử bằng Postman, debug bằng CloudWatch và viết tài liệu cleanup tài nguyên.

Kỳ thực tập giúp em củng cố kiến thức cloud computing và có thêm kinh nghiệm thực hành với các dịch vụ AWS trong một bài toán thực tế.
