---
title: "Worklog Tuần 10 "
date: 2026-06-22
weight: 110
week: 10
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 22/06/2026 - 28/06/2026 |
| Tuần thực tập | Tuần 10 |
| Giai đoạn | Giai đoạn hoàn thiện báo cáo và tổng kết |
| Project | Serverless AI Invoice Scanner |
| Chủ đề chính | Hoàn thiện báo cáo cuối kỳ, tối ưu tài liệu, cleanup tài nguyên và tổng kết thực tập |
| Mục tiêu tuần | Hoàn thiện toàn bộ hồ sơ thực tập, kiểm tra project lần cuối, chuẩn bị báo cáo nộp và tổng kết kiến thức đã đạt được |

---

## Định hướng Tuần 10

Tuần 10 được sử dụng như tuần tổng kết cuối cùng sau khi project **Serverless AI Invoice Scanner** đã hoàn thiện và được rà soát ở tuần 9. Trong tuần này, trọng tâm không còn là phát triển chức năng mới mà tập trung vào việc hoàn thiện báo cáo, kiểm tra tài liệu, chuẩn bị phần trình bày và thực hiện các bước cleanup tài nguyên AWS nếu không còn sử dụng.

Mục tiêu chính của tuần này là đảm bảo toàn bộ quá trình thực tập được tổng hợp đầy đủ, bao gồm:

- Kiến thức đã học từ chương trình First Cloud Journey.
- Quá trình áp dụng kiến thức vào project thực tế.
- Kết quả đạt được của project.
- Các lỗi đã gặp và cách khắc phục.
- Các tài nguyên AWS đã sử dụng.
- Quy trình dọn dẹp tài nguyên sau khi kết thúc lab.
- Hướng phát triển tiếp theo của project.

---

## Mục tiêu Tuần 10

Các mục tiêu chính trong tuần gồm:

- Rà soát lại toàn bộ worklog từ tuần 1 đến tuần 9.
- Hoàn thiện worklog tuần 10.
- Kiểm tra lại nội dung proposal và tài liệu project.
- Chuẩn hóa phần mô tả kiến trúc hệ thống.
- Kiểm tra lại hình ảnh, đường dẫn và cấu trúc tài liệu Markdown.
- Hoàn thiện phần hướng dẫn cleanup resources.
- Kiểm tra lại các tài nguyên AWS còn tồn tại.
- Chuẩn bị nội dung báo cáo tổng kết thực tập.
- Chuẩn bị nội dung thuyết trình hoặc demo nếu cần.
- Tổng hợp bài học kinh nghiệm và định hướng phát triển tương lai.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 22/06/2026

Ngày đầu tiên của tuần 10 tập trung vào việc rà soát toàn bộ worklog đã viết trong quá trình thực tập.

Nội dung đã thực hiện:

- Kiểm tra lại worklog tuần 1 đến tuần 4 về giai đoạn học **First Cloud Journey**.
- Kiểm tra lại worklog tuần 5 đến tuần 8 về giai đoạn thực hiện project.
- Kiểm tra worklog tuần 9 về giai đoạn rà soát và chuẩn bị bàn giao.
- Đảm bảo thứ tự tuần, ngày tháng và nội dung được trình bày thống nhất.
- Ghi chú các phần cần bổ sung hoặc chỉnh sửa.

Kết quả đạt được:

- Xác nhận được luồng nội dung thực tập rõ ràng.
- Phân biệt được hai giai đoạn chính: học tập và làm project.
- Có cơ sở để tổng hợp báo cáo cuối kỳ.

---

### Ngày 2 - Thứ ba, 23/06/2026

Ngày thứ hai tập trung vào việc kiểm tra và hoàn thiện tài liệu proposal của project.

Nội dung đã thực hiện:

- Rà soát lại phần tóm tắt project.
- Cập nhật phần kiến trúc hệ thống theo đúng project thực tế.
- Kiểm tra lại các dịch vụ AWS được sử dụng.
- Đảm bảo nội dung đã thay **Amazon Bedrock** bằng **OpenAI API**.
- Kiểm tra phần mô tả các Lambda functions:
  - `UploadInvoiceFileFunction`
  - `ProcessInvoiceFunction`
  - `InvoiceManagementFunction`
- Kiểm tra phần mô tả API Gateway routes.
- Kiểm tra phần mô tả DynamoDB table `InvoiceData`.

Kết quả đạt được:

- Proposal được chỉnh đúng với project thực tế.
- Nội dung về OpenAI API, Textract, Lambda, S3, DynamoDB và Amplify Hosting thống nhất hơn.
- Tài liệu sẵn sàng để đưa vào báo cáo tổng kết.

---

### Ngày 3 - Thứ tư, 24/06/2026

Ngày thứ ba tập trung vào kiểm tra tài liệu triển khai và cấu trúc Markdown.

Nội dung đã thực hiện:

- Kiểm tra cấu trúc các mục tài liệu.
- Kiểm tra đường dẫn hình ảnh trong Markdown.
- Kiểm tra front matter của từng file tài liệu.
- Kiểm tra tiêu đề, weight và thứ tự hiển thị.
- Rà soát lại phần Introduction, Environment Setup, AI Processing, API Gateway, Postman Test, Frontend Deploy và Cleanup.
- Kiểm tra các đoạn code, command và API route được trình bày trong tài liệu.

Các mục tài liệu được kiểm tra:

| Mục | Nội dung |
|---|---|
| Introduction | Tổng quan hệ thống và dịch vụ sử dụng |
| Environment Setup | Chuẩn bị môi trường AWS và frontend |
| AI Processing | Textract, OpenAI API và DynamoDB |
| API Gateway | Các route API backend |
| Test with Postman | Kiểm thử API |
| Deploying Frontend | Deploy React bằng Amplify Hosting |
| Cleanup | Xóa tài nguyên AWS sau khi hoàn thành lab |

Kết quả đạt được:

- Tài liệu Markdown rõ ràng và thống nhất hơn.
- Các mục chính được sắp xếp hợp lý.
- Giảm lỗi sai đường dẫn và sai tên dịch vụ trong tài liệu.

---

### Ngày 4 - Thứ năm, 25/06/2026

Ngày thứ tư tập trung vào kiểm tra lần cuối hệ thống AWS và các tài nguyên đang sử dụng.

Nội dung đã thực hiện:

- Kiểm tra API Gateway.
- Kiểm tra Lambda functions.
- Kiểm tra S3 bucket và dữ liệu trong thư mục `uploads/`.
- Kiểm tra DynamoDB table `InvoiceData`.
- Kiểm tra Cognito User Pool.
- Kiểm tra Amplify Hosting App.
- Kiểm tra CloudWatch Log Groups.
- Kiểm tra IAM Roles và Policies liên quan.
- Kiểm tra các tài nguyên tùy chọn như Secrets Manager hoặc Route 53 nếu có sử dụng.

Danh sách tài nguyên cần rà soát:

```txt
API Gateway
Lambda Functions
S3 Bucket
DynamoDB Table
Cognito User Pool
Amplify Hosting App
CloudWatch Log Groups
IAM Roles and Policies
Secrets Manager
Route 53
```

Kết quả đạt được:

- Nắm được trạng thái của từng tài nguyên AWS.
- Xác định tài nguyên nào cần giữ lại để demo.
- Xác định tài nguyên nào có thể xóa sau khi kết thúc lab.

---

### Ngày 5 - Thứ sáu, 26/06/2026

Ngày thứ năm tập trung vào hoàn thiện phần cleanup resources và kiểm tra chi phí.

Nội dung đã thực hiện:

- Rà soát checklist cleanup resources.
- Kiểm tra thứ tự xóa tài nguyên để tránh lỗi phụ thuộc.
- Ghi chú các tài nguyên cần xóa sau project:
  - API Gateway
  - Lambda Functions
  - S3 Bucket
  - DynamoDB Table
  - Cognito User Pool
  - Amplify Hosting App
  - CloudWatch Log Groups
  - IAM Roles and Policies
  - Optional resources
- Kiểm tra AWS Billing hoặc Cost Explorer ở mức cơ bản.
- Ghi chú các dịch vụ có thể phát sinh chi phí nếu không xóa.

Thứ tự cleanup đề xuất:

```txt
1. API Gateway
2. Lambda Functions
3. S3 Bucket
4. DynamoDB Table
5. Cognito User Pool
6. Amplify Hosting App
7. CloudWatch Log Groups
8. IAM Roles and Policies
9. Optional Resources
```

Kết quả đạt được:

- Có checklist cleanup rõ ràng.
- Hiểu vì sao cần xóa tài nguyên sau khi hoàn thành lab.
- Giảm rủi ro phát sinh chi phí không mong muốn.

---

### Ngày 6 - Thứ bảy, 27/06/2026

Ngày thứ sáu tập trung vào chuẩn bị báo cáo và nội dung trình bày cuối kỳ.

Nội dung đã thực hiện:

- Chuẩn bị dàn ý báo cáo tổng kết thực tập.
- Tổng hợp kiến thức đã học trong 4 tuần First Cloud Journey.
- Tổng hợp quá trình làm project trong các tuần tiếp theo.
- Chuẩn bị phần mô tả kiến trúc hệ thống.
- Chuẩn bị phần demo project.
- Chuẩn bị phần kết quả đạt được.
- Chuẩn bị phần khó khăn và bài học kinh nghiệm.
- Chuẩn bị phần hướng phát triển trong tương lai.

Cấu trúc báo cáo tổng kết dự kiến:

| Phần | Nội dung |
|---|---|
| Giới thiệu | Mục tiêu thực tập và project |
| Kiến thức học được | First Cloud Journey và AWS services |
| Kiến trúc project | Serverless AI Invoice Scanner |
| Triển khai | Các bước xây dựng hệ thống |
| Kiểm thử | Postman, frontend, CloudWatch |
| Kết quả | Chức năng hoàn thành |
| Cleanup | Dọn dẹp tài nguyên AWS |
| Kết luận | Bài học và hướng phát triển |

Kết quả đạt được:

- Có dàn ý báo cáo cuối kỳ rõ ràng.
- Có nội dung chuẩn bị cho phần trình bày demo.
- Tổng hợp được các điểm quan trọng nhất của project.

---

### Ngày 7 - Chủ nhật, 28/06/2026

Ngày cuối cùng tập trung vào tổng kết tuần 10 và tổng kết toàn bộ quá trình thực tập.

Nội dung đã thực hiện:

- Viết worklog tuần 10.
- Tổng hợp lại toàn bộ quá trình thực tập.
- Kiểm tra lại các tài liệu cần nộp.
- Rà soát lại project lần cuối.
- Ghi chú các điểm mạnh của project.
- Ghi chú các hạn chế còn tồn tại.
- Đề xuất hướng phát triển trong tương lai.
- Hoàn thiện nội dung bàn giao.

Kết quả đạt được:

- Hoàn thành tuần tổng kết cuối cùng.
- Hoàn thiện tài liệu và báo cáo thực tập.
- Project sẵn sàng để trình bày, nộp hoặc bàn giao.
- Có cái nhìn tổng thể về toàn bộ quá trình học tập và triển khai project trên AWS.

---

## Tổng kết kiến thức Tuần 10

Trong tuần 10, em tập trung vào việc hoàn thiện báo cáo, rà soát tài liệu, kiểm tra tài nguyên AWS và chuẩn bị bàn giao project.

| Nhóm công việc | Nội dung đã thực hiện |
|---|---|
| Worklog Review | Rà soát worklog từ tuần 1 đến tuần 9 |
| Proposal Review | Chỉnh sửa nội dung proposal theo project thực tế |
| Documentation | Kiểm tra Markdown, hình ảnh, cấu trúc tài liệu |
| AWS Resource Review | Kiểm tra lại tài nguyên AWS đang sử dụng |
| Cleanup | Hoàn thiện checklist dọn dẹp tài nguyên |
| Cost Review | Kiểm tra tài nguyên có thể phát sinh chi phí |
| Final Report | Chuẩn bị báo cáo tổng kết thực tập |
| Demo Preparation | Chuẩn bị nội dung trình bày project |

---

## Kết quả đạt được trong tuần

- Rà soát toàn bộ worklog thực tập.
- Hoàn thiện proposal project.
- Kiểm tra và chỉnh sửa tài liệu Markdown.
- Rà soát tài nguyên AWS đang sử dụng.
- Hoàn thiện checklist cleanup resources.
- Chuẩn bị báo cáo tổng kết thực tập.
- Chuẩn bị nội dung demo và bàn giao project.
- Tổng hợp bài học kinh nghiệm và hướng phát triển tương lai.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Nhiều tài liệu cần rà soát | Chia theo từng nhóm: worklog, proposal, project docs, cleanup |
| Dễ không thống nhất tên dịch vụ | Chuẩn hóa lại tên như OpenAI API, AWS Amplify Hosting, Amazon Textract |
| Cleanup có nhiều tài nguyên phụ thuộc | Sắp xếp thứ tự xóa tài nguyên theo checklist |
| Báo cáo cần tổng hợp nhiều tuần | Tóm tắt theo giai đoạn: học tập và project |
| Cần trình bày project ngắn gọn | Chuẩn bị kịch bản demo theo luồng xử lý chính |

---

## Bài học rút ra

- Giai đoạn cuối project cần dành thời gian để rà soát tài liệu và tài nguyên.
- Tài liệu tốt giúp project dễ được hiểu, dễ demo và dễ bàn giao.
- Cleanup tài nguyên AWS là bước quan trọng để tránh phát sinh chi phí.
- Khi sử dụng nhiều dịch vụ AWS, cần ghi chú rõ tên tài nguyên và vai trò của từng dịch vụ.
- Báo cáo thực tập nên trình bày theo quá trình: học kiến thức, áp dụng vào project, kiểm thử và tổng kết.
- Việc chuẩn bị demo trước giúp quá trình trình bày tự tin và mạch lạc hơn.

---

## Tổng kết toàn bộ quá trình thực tập

Trong quá trình thực tập, em đã trải qua hai giai đoạn chính:

| Giai đoạn | Nội dung |
|---|---|
| Giai đoạn học tập | Học và nghiên cứu tài liệu theo chương trình First Cloud Journey |
| Giai đoạn project | Xây dựng hệ thống Serverless AI Invoice Scanner trên AWS |

Các kiến thức và kỹ năng chính đã đạt được:

- Hiểu tổng quan về AWS Cloud.
- Hiểu các dịch vụ AWS cốt lõi như S3, Lambda, API Gateway, DynamoDB, Cognito, Amplify Hosting, CloudWatch và IAM.
- Hiểu kiến trúc serverless và event-driven.
- Biết thiết kế hệ thống xử lý file theo sự kiện.
- Biết tích hợp Amazon Textract để OCR hóa đơn.
- Biết tích hợp OpenAI API để chuẩn hóa dữ liệu.
- Biết lưu trữ dữ liệu bằng DynamoDB.
- Biết deploy frontend bằng AWS Amplify Hosting.
- Biết kiểm thử API bằng Postman.
- Biết debug lỗi bằng CloudWatch Logs.
- Biết viết tài liệu hướng dẫn triển khai và cleanup tài nguyên.

---

## Kết quả cuối cùng của project

Project **Serverless AI Invoice Scanner** đã hoàn thành các chức năng chính:

| Chức năng | Trạng thái |
|---|---|
| Đăng ký / đăng nhập bằng Cognito | Hoàn thành |
| Upload hóa đơn từ frontend | Hoàn thành |
| Lưu file vào S3 | Hoàn thành |
| Trigger Lambda khi có file mới | Hoàn thành |
| OCR hóa đơn bằng Amazon Textract | Hoàn thành |
| Chuẩn hóa dữ liệu bằng OpenAI API | Hoàn thành |
| Lưu dữ liệu vào DynamoDB | Hoàn thành |
| API lấy danh sách hóa đơn | Hoàn thành |
| API xem chi tiết hóa đơn | Hoàn thành |
| API tìm kiếm hóa đơn | Hoàn thành |
| API cập nhật tags | Hoàn thành |
| API cập nhật starred | Hoàn thành |
| Frontend filter, sort, export Excel | Hoàn thành |
| Deploy frontend bằng Amplify Hosting | Hoàn thành |
| Viết tài liệu cleanup resources | Hoàn thành |

---

## Hướng phát triển trong tương lai

Nếu tiếp tục phát triển project, có thể bổ sung:

- Cognito Authorizer cho API Gateway.
- AWS Secrets Manager để lưu OpenAI API key.
- Amazon SQS để xử lý hóa đơn bất đồng bộ.
- Trạng thái xử lý realtime trên frontend.
- Chức năng chỉnh sửa dữ liệu sau khi AI trích xuất.
- Dashboard thống kê doanh thu, số lượng hóa đơn và tổng tiền.
- Tích hợp Amazon QuickSight hoặc Power BI.
- Tích hợp email notification sau khi xử lý hóa đơn.
- Hỗ trợ phân quyền theo vai trò người dùng.
- Hỗ trợ nhiều loại chứng từ khác như biên lai, hợp đồng hoặc phiếu thu.

---

## Nhận xét cuối kỳ

Tuần 10 là tuần tổng kết và hoàn thiện toàn bộ nội dung thực tập. Sau quá trình học tập theo First Cloud Journey và thực hiện project Serverless AI Invoice Scanner, em đã có thêm kiến thức thực tế về cách xây dựng một hệ thống serverless trên AWS.

Project giúp em hiểu rõ hơn cách các dịch vụ AWS phối hợp với nhau, từ frontend, authentication, API, backend, storage, AI processing, database đến monitoring và cleanup. Đây là trải nghiệm quan trọng giúp em củng cố kiến thức cloud và có nền tảng tốt hơn để tiếp tục học tập, phát triển các hệ thống trên AWS trong tương lai.
