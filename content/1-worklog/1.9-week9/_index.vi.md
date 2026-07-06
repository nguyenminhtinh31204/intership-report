---
title: "Worklog Tuần 9 "
date: 2026-06-15
weight: 109
week: 9
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 15/06/2026 - 21/06/2026 |
| Tuần thực tập | Tuần 9 |
| Giai đoạn | Giai đoạn bổ sung sau hoàn thiện project |
| Project | Serverless AI Invoice Scanner |
| Chủ đề chính | Rà soát hệ thống, tối ưu, hoàn thiện tài liệu và chuẩn bị bàn giao |
| Mục tiêu tuần | Kiểm tra lại toàn bộ project, xử lý lỗi còn tồn tại, hoàn thiện báo cáo, chuẩn bị demo và dọn dẹp tài nguyên AWS |

---

## Định hướng Tuần 9

Sau khi tuần 8 đã hoàn thiện project **Serverless AI Invoice Scanner**, tuần 9 được dùng như một tuần bổ sung để rà soát lại toàn bộ hệ thống, kiểm tra lỗi còn tồn tại, tối ưu tài liệu và chuẩn bị bàn giao kết quả thực tập.

Trọng tâm của tuần này không phải là xây dựng thêm chức năng lớn mới, mà là:

- Kiểm tra lại toàn bộ luồng hoạt động của hệ thống.
- Sửa các lỗi nhỏ còn tồn tại.
- Tối ưu trải nghiệm người dùng trên frontend.
- Rà soát CloudWatch Logs.
- Kiểm tra chi phí và tài nguyên AWS.
- Hoàn thiện báo cáo thực tập.
- Chuẩn bị nội dung demo project.
- Thực hiện hoặc ghi chú quy trình cleanup resources.

---

## Mục tiêu Tuần 9

Các mục tiêu chính trong tuần gồm:

- Kiểm thử lại toàn bộ luồng end-to-end.
- Kiểm tra các API đã triển khai.
- Rà soát dữ liệu trong DynamoDB.
- Kiểm tra file hóa đơn trong S3.
- Kiểm tra log của Lambda và API Gateway trong CloudWatch.
- Kiểm tra lại frontend sau khi deploy bằng Amplify Hosting.
- Hoàn thiện tài liệu hướng dẫn sử dụng hệ thống.
- Hoàn thiện tài liệu cleanup resources.
- Chuẩn bị slide hoặc nội dung trình bày demo.
- Tổng hợp kết quả đạt được và hạn chế của project.
- Đề xuất hướng phát triển trong tương lai.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 15/06/2026

Ngày đầu tiên của tuần 9 tập trung vào rà soát tổng thể hệ thống sau khi đã hoàn thiện ở tuần 8.

Nội dung đã thực hiện:

- Kiểm tra lại kiến trúc tổng thể của project.
- Đối chiếu các tài nguyên AWS đã tạo với sơ đồ kiến trúc.
- Kiểm tra các Lambda functions:
  - `UploadInvoiceFileFunction`
  - `ProcessInvoiceFunction`
  - `InvoiceManagementFunction`
- Kiểm tra các API Gateway routes.
- Kiểm tra S3 bucket và thư mục `uploads/`.
- Kiểm tra DynamoDB table `InvoiceData`.
- Ghi chú các điểm cần chỉnh sửa hoặc tối ưu.

Kết quả đạt được:

- Xác nhận các thành phần chính của hệ thống vẫn hoạt động.
- Nắm được danh sách tài nguyên AWS đang sử dụng.
- Có danh sách lỗi nhỏ và điểm cần hoàn thiện trong tuần.

---

### Ngày 2 - Thứ ba, 16/06/2026

Ngày thứ hai tập trung vào kiểm thử lại các API backend bằng Postman.

Nội dung đã thực hiện:

- Kiểm thử API upload hóa đơn:

```txt
POST /uploads
```

- Kiểm thử API lấy danh sách hóa đơn:

```txt
GET /invoice
```

- Kiểm thử API lấy chi tiết hóa đơn:

```txt
GET /invoice/{id}
```

- Kiểm thử API tìm kiếm hóa đơn theo tên khách hàng:

```txt
GET /invoice?name=<customer_name>
```

- Kiểm thử API cập nhật tags:

```txt
PATCH /invoice/tags/{id}
```

- Kiểm thử API cập nhật starred:

```txt
PATCH /invoice/starred/{id}
```

- Kiểm tra response format của từng API.
- Kiểm tra các trường hợp lỗi như sai ID, thiếu body hoặc sai route.

Kết quả đạt được:

- Xác nhận các API chính hoạt động ổn định.
- Phát hiện và ghi chú một số lỗi nhỏ về response format.
- Hiểu rõ hơn cách kiểm thử API trước khi bàn giao project.

---

### Ngày 3 - Thứ tư, 17/06/2026

Ngày thứ ba tập trung vào kiểm tra frontend và trải nghiệm người dùng.

Nội dung đã thực hiện:

- Kiểm tra giao diện đăng ký và đăng nhập bằng Cognito.
- Kiểm tra chức năng upload hóa đơn từ frontend.
- Kiểm tra giao diện danh sách hóa đơn.
- Kiểm tra trang chi tiết hóa đơn.
- Kiểm tra chức năng tìm kiếm.
- Kiểm tra chức năng tags và starred.
- Kiểm tra filter theo ngày.
- Kiểm tra sort theo ngày và tổng tiền.
- Kiểm tra export Excel.
- Ghi chú các điểm cần cải thiện về giao diện.

Một số điểm kiểm tra trên frontend:

| Chức năng | Nội dung kiểm tra |
|---|---|
| Login / Sign-up | Người dùng có thể đăng nhập và đăng ký |
| Upload | File được gửi đúng đến API |
| Invoice List | Danh sách hóa đơn hiển thị đúng |
| Detail | Thông tin hóa đơn hiển thị đầy đủ |
| Search | Tìm được hóa đơn theo tên khách hàng |
| Tags | Thêm và cập nhật tags thành công |
| Starred | Đánh dấu hóa đơn quan trọng |
| Export Excel | Xuất dữ liệu hóa đơn ra file Excel |

Kết quả đạt được:

- Frontend hoạt động đúng với các chức năng chính.
- Ghi nhận các lỗi nhỏ về hiển thị dữ liệu.
- Cải thiện được trải nghiệm sử dụng trước khi demo.

---

### Ngày 4 - Thứ năm, 18/06/2026

Ngày thứ tư tập trung vào rà soát log, lỗi hệ thống và chi phí tài nguyên.

Nội dung đã thực hiện:

- Kiểm tra CloudWatch Log Groups của các Lambda functions.
- Xem lại log lỗi upload hóa đơn.
- Xem lại log xử lý Textract và OpenAI API.
- Kiểm tra lỗi DynamoDB nếu có.
- Kiểm tra log liên quan đến CORS hoặc API Gateway.
- Kiểm tra tài nguyên AWS đang còn hoạt động.
- Ghi chú các tài nguyên có thể phát sinh chi phí.

Các tài nguyên cần chú ý:

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

- Nắm được trạng thái log của hệ thống.
- Xác định được tài nguyên nào cần giữ lại để demo.
- Xác định được tài nguyên nào cần cleanup sau khi kết thúc thực tập.

---

### Ngày 5 - Thứ sáu, 19/06/2026

Ngày thứ năm tập trung vào hoàn thiện tài liệu và báo cáo project.

Nội dung đã thực hiện:

- Rà soát lại tài liệu giới thiệu project.
- Cập nhật phần kiến trúc hệ thống.
- Cập nhật phần mô tả các dịch vụ AWS sử dụng.
- Cập nhật phần API Gateway routes.
- Cập nhật phần Lambda functions.
- Cập nhật phần DynamoDB table.
- Cập nhật phần frontend và Amplify Hosting.
- Cập nhật phần cleanup resources.
- Kiểm tra lại các nội dung đã viết để đảm bảo thống nhất.

Các tài liệu được rà soát:

| Tài liệu | Nội dung |
|---|---|
| Introduction | Tổng quan project và dịch vụ sử dụng |
| Architecture | Sơ đồ và luồng xử lý hệ thống |
| API Gateway | Danh sách endpoint |
| Lambda | Mô tả các function backend |
| Frontend | Hướng dẫn deploy và sử dụng |
| Testing | Kiểm thử bằng Postman và frontend |
| Cleanup | Xóa tài nguyên AWS sau lab |

Kết quả đạt được:

- Tài liệu project rõ ràng và thống nhất hơn.
- Các phần dùng OpenAI API đã được cập nhật thay cho Bedrock.
- Nội dung cleanup resources đầy đủ hơn.

---

### Ngày 6 - Thứ bảy, 20/06/2026

Ngày thứ sáu tập trung vào chuẩn bị demo và tổng hợp kết quả thực tập.

Nội dung đã thực hiện:

- Chuẩn bị kịch bản demo project.
- Sắp xếp thứ tự trình bày:
  1. Giới thiệu vấn đề.
  2. Giới thiệu kiến trúc.
  3. Demo đăng nhập.
  4. Demo upload hóa đơn.
  5. Demo xử lý AI.
  6. Demo xem danh sách hóa đơn.
  7. Demo tìm kiếm, tags, starred và export Excel.
  8. Demo CloudWatch Logs.
  9. Trình bày cleanup resources.
- Ghi chú các điểm nổi bật của project.
- Ghi chú các hạn chế còn tồn tại.
- Đề xuất hướng phát triển tiếp theo.

Kết quả đạt được:

- Có kịch bản demo rõ ràng.
- Có nội dung trình bày kết quả project.
- Chuẩn bị được phần tổng kết cho báo cáo thực tập.

---

### Ngày 7 - Chủ nhật, 21/06/2026

Ngày cuối tuần dùng để tổng kết tuần 9 và hoàn thiện nội dung bàn giao.

Nội dung đã thực hiện:

- Tổng hợp toàn bộ kết quả đã đạt được.
- Kiểm tra lại file tài liệu, worklog và báo cáo.
- Hoàn thiện danh sách tài nguyên cần cleanup.
- Ghi chú bài học rút ra sau khi làm project.
- Tổng hợp hướng phát triển trong tương lai.
- Viết báo cáo worklog tuần 9.

Kết quả đạt được:

- Hoàn thiện tuần bổ sung sau project.
- Project sẵn sàng để trình bày và bàn giao.
- Có tài liệu và checklist cleanup đầy đủ.
- Có định hướng cải tiến nếu tiếp tục phát triển project.

---

## Tổng kết kiến thức Tuần 9

Trong tuần 9, em tập trung vào việc rà soát, tối ưu, kiểm thử lại và hoàn thiện tài liệu cho project **Serverless AI Invoice Scanner**.

| Nhóm công việc | Nội dung đã thực hiện |
|---|---|
| System Review | Kiểm tra lại toàn bộ tài nguyên AWS |
| Backend Testing | Kiểm thử API bằng Postman |
| Frontend Testing | Kiểm tra giao diện và chức năng người dùng |
| Monitoring | Rà soát CloudWatch Logs |
| Cost Review | Kiểm tra tài nguyên có thể phát sinh chi phí |
| Documentation | Hoàn thiện tài liệu triển khai và cleanup |
| Demo Preparation | Chuẩn bị kịch bản demo project |
| Handover | Tổng hợp kết quả và nội dung bàn giao |

---

## Kết quả đạt được trong tuần

- Rà soát lại toàn bộ hệ thống.
- Kiểm thử lại các API chính.
- Kiểm tra frontend sau khi deploy.
- Kiểm tra CloudWatch Logs.
- Hoàn thiện tài liệu project.
- Hoàn thiện checklist cleanup resources.
- Chuẩn bị kịch bản demo.
- Tổng hợp kết quả và hạn chế của project.
- Chuẩn bị bàn giao project sau kỳ thực tập.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Có nhiều tài nguyên AWS cần kiểm tra | Lập danh sách theo từng dịch vụ để rà soát |
| Một số lỗi chỉ xuất hiện khi test end-to-end | Kiểm tra từng bước từ frontend đến backend |
| Response API có field chưa đồng nhất | Chuẩn hóa lại mapping dữ liệu ở Lambda và frontend |
| CloudWatch Logs có nhiều log khó theo dõi | Lọc theo thời gian và theo Lambda function |
| Cần chuẩn bị demo ngắn gọn nhưng đủ ý | Viết kịch bản demo theo từng bước chính |
| Cleanup dễ xóa nhầm tài nguyên | Ghi rõ tên tài nguyên thuộc project trước khi xóa |

---

## Bài học rút ra

- Sau khi hoàn thành chức năng, cần có thời gian kiểm thử lại toàn bộ hệ thống.
- Một project cloud cần được kiểm tra cả backend, frontend, database, log và chi phí.
- Tài liệu rõ ràng giúp quá trình bàn giao và trình bày project dễ hơn.
- Cleanup resources là bước quan trọng để tránh phát sinh chi phí không mong muốn.
- Khi demo project, nên chuẩn bị sẵn dữ liệu mẫu và kịch bản trình bày.
- Việc rà soát lại kiến trúc giúp phát hiện các điểm chưa thống nhất trong tài liệu và triển khai.

---

## Hướng phát triển trong tương lai

Nếu tiếp tục phát triển project, có thể bổ sung các chức năng sau:

- Phân quyền người dùng chi tiết hơn.
- Bảo vệ API Gateway bằng Cognito Authorizer.
- Lưu OpenAI API key bằng AWS Secrets Manager.
- Thêm hàng đợi SQS để xử lý hóa đơn bất đồng bộ.
- Thêm trạng thái xử lý realtime cho frontend.
- Tự động phân loại hóa đơn theo loại chi phí.
- Tích hợp dashboard thống kê với Amazon QuickSight.
- Thêm chức năng chỉnh sửa dữ liệu hóa đơn sau khi AI trích xuất.
- Tích hợp gửi email thông báo sau khi xử lý hóa đơn xong.
- Hỗ trợ nhiều định dạng hóa đơn và nhiều loại tiền tệ hơn.

---

## Nhận xét cuối tuần

Tuần 9 là tuần bổ sung giúp em rà soát và hoàn thiện project sau giai đoạn triển khai chính. Thông qua việc kiểm thử lại hệ thống, kiểm tra log, rà soát chi phí, hoàn thiện tài liệu và chuẩn bị demo, em hiểu rõ hơn rằng một project cloud không chỉ dừng lại ở việc chạy được chức năng mà còn cần được kiểm thử, giám sát, tối ưu, viết tài liệu và chuẩn bị cleanup tài nguyên.

Sau tuần này, project **Serverless AI Invoice Scanner** đã sẵn sàng để trình bày, bàn giao và có thể tiếp tục phát triển thêm trong tương lai.
