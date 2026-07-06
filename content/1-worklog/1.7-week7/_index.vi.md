---
title: "Worklog Tuần 7 "
date: 2026-06-01
weight: 107
week: 7
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 01/06/2026 - 07/06/2026 |
| Tuần thực tập | Tuần 7 |
| Giai đoạn | Giai đoạn thực hiện project |
| Project | Serverless AI Invoice Scanner |
| Chủ đề chính | Xây dựng API quản lý hóa đơn và tích hợp frontend |
| Mục tiêu tuần | Tạo các API truy xuất, tìm kiếm, cập nhật tags/starred và bắt đầu kết nối frontend React với backend AWS |

---

## Định hướng Tuần 7

Sau khi tuần 6 đã hoàn thành luồng xử lý hóa đơn bằng AI gồm S3 Event, Lambda, Amazon Textract, OpenAI API và DynamoDB, tuần 7 tập trung vào phần **quản lý dữ liệu hóa đơn**.

Mục tiêu chính của tuần này là xây dựng Lambda và API Gateway để frontend có thể lấy dữ liệu từ DynamoDB, hiển thị danh sách hóa đơn, xem chi tiết hóa đơn, tìm kiếm theo tên khách hàng, cập nhật tags và đánh dấu hóa đơn quan trọng.

Luồng xử lý chính trong tuần:

```txt
React Frontend / Postman
    ↓
Amazon API Gateway
    ↓
InvoiceManagementFunction
    ↓
Amazon DynamoDB InvoiceData
    ↓
Response JSON
    ↓
React Frontend
```

---

## Mục tiêu Tuần 7

Các mục tiêu chính trong tuần gồm:

- Tạo Lambda function `InvoiceManagementFunction`.
- Xây dựng API lấy danh sách hóa đơn.
- Xây dựng API lấy chi tiết hóa đơn theo ID.
- Xây dựng API tìm kiếm hóa đơn theo tên khách hàng.
- Xây dựng API cập nhật tags cho hóa đơn.
- Xây dựng API cập nhật trạng thái starred.
- Kiểm thử toàn bộ API bằng Postman.
- Chuẩn hóa dữ liệu trả về cho frontend.
- Bắt đầu tích hợp API Gateway endpoints vào React frontend.
- Kiểm tra lỗi CORS, route, method và response format.
- Theo dõi lỗi bằng CloudWatch Logs.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 01/06/2026

Ngày đầu tiên của tuần 7 tập trung vào việc phân tích các API cần thiết cho phần quản lý hóa đơn.

Nội dung đã thực hiện:

- Ôn lại cấu trúc dữ liệu đang được lưu trong DynamoDB table `InvoiceData`.
- Xác định các chức năng frontend cần lấy dữ liệu từ backend.
- Liệt kê các API cần xây dựng cho project.
- Xác định Lambda function chính xử lý các API quản lý hóa đơn:

```txt
InvoiceManagementFunction
```

Các API cần triển khai:

| Method | Route | Chức năng |
|---|---|---|
| `GET` | `/invoice` | Lấy danh sách hóa đơn |
| `GET` | `/invoice/{id}` | Lấy chi tiết hóa đơn theo ID |
| `GET` | `/invoice?name=<customer_name>` | Tìm kiếm hóa đơn theo tên khách hàng |
| `PATCH` | `/invoice/tags/{id}` | Cập nhật tags của hóa đơn |
| `PATCH` | `/invoice/starred/{id}` | Cập nhật trạng thái starred |

Kết quả đạt được:

- Xác định được các API cần thiết cho frontend.
- Nắm rõ vai trò của `InvoiceManagementFunction`.
- Có kế hoạch triển khai API quản lý hóa đơn trong tuần.

---

### Ngày 2 - Thứ ba, 02/06/2026

Ngày thứ hai tập trung vào tạo **InvoiceManagementFunction** và cấp quyền truy cập DynamoDB.

Nội dung đã thực hiện:

- Tạo Lambda function `InvoiceManagementFunction`.
- Cấu hình runtime và handler.
- Tạo hoặc cập nhật IAM execution role.
- Cấp quyền để Lambda có thể đọc và cập nhật DynamoDB.
- Kiểm tra quyền ghi log vào CloudWatch.
- Viết cấu trúc xử lý request ban đầu cho Lambda.

Các quyền DynamoDB cần chú ý:

```txt
dynamodb:Scan
dynamodb:GetItem
dynamodb:Query
dynamodb:UpdateItem
```

Luồng xử lý cơ bản của Lambda:

```txt
Nhận request từ API Gateway
    ↓
Kiểm tra method và path
    ↓
Gọi DynamoDB tương ứng
    ↓
Chuẩn hóa response JSON
    ↓
Trả dữ liệu về API Gateway
```

Kết quả đạt được:

- Tạo được `InvoiceManagementFunction`.
- Lambda có quyền truy cập DynamoDB.
- Có cấu trúc code ban đầu để xử lý nhiều API route.

---

### Ngày 3 - Thứ tư, 03/06/2026

Ngày thứ ba tập trung vào API lấy danh sách hóa đơn và xem chi tiết hóa đơn.

Nội dung đã thực hiện:

- Xây dựng API:

```txt
GET /invoice
```

- Lambda thực hiện đọc danh sách item từ DynamoDB.
- Chuẩn hóa dữ liệu trả về cho frontend.
- Xây dựng API:

```txt
GET /invoice/{id}
```

- Lambda lấy chi tiết hóa đơn theo `InvoiceId`.
- Kiểm tra trường hợp không tìm thấy hóa đơn.
- Kiểm thử hai API bằng Postman.
- Xem log lỗi trong CloudWatch nếu response không đúng.

Ví dụ response danh sách hóa đơn:

```json
[
  {
    "InvoiceId": "invoice-001",
    "CustomerName": "Customer Name",
    "InvoiceDate": "2026-06-03",
    "TotalAmount": 100000,
    "Currency": "VND",
    "Tags": [],
    "Starred": false
  }
]
```

Kết quả đạt được:

- API `GET /invoice` trả về được danh sách hóa đơn.
- API `GET /invoice/{id}` trả về được chi tiết hóa đơn theo ID.
- Hiểu cách chuẩn hóa response để frontend dễ sử dụng.

---

### Ngày 4 - Thứ năm, 04/06/2026

Ngày thứ tư tập trung vào API tìm kiếm hóa đơn theo tên khách hàng.

Nội dung đã thực hiện:

- Xây dựng API tìm kiếm:

```txt
GET /invoice?name=<customer_name>
```

- Kiểm tra query string parameter từ API Gateway.
- Lambda nhận tham số `name` và tìm kiếm trong DynamoDB.
- Xử lý trường hợp `CustomerName` nằm ở field top-level.
- Xử lý thêm trường hợp `CustomerName` nằm trong `ExtractedData`.
- Kiểm thử tìm kiếm bằng Postman với nhiều tên khách hàng khác nhau.
- Ghi chú vấn đề chữ hoa, chữ thường và dữ liệu thiếu field.

Logic tìm kiếm dự kiến:

```txt
Nếu có query parameter name
    ↓
Tìm theo CustomerName
    ↓
Nếu không có ở top-level thì kiểm tra ExtractedData.CustomerName
    ↓
Trả danh sách hóa đơn phù hợp
```

Kết quả đạt được:

- API tìm kiếm theo tên khách hàng hoạt động.
- Hiểu vấn đề dữ liệu có thể nằm ở nhiều vị trí khác nhau trong item.
- Bổ sung hướng xử lý fallback để tăng khả năng tìm kiếm.

---

### Ngày 5 - Thứ sáu, 05/06/2026

Ngày thứ năm tập trung vào API cập nhật tags và starred cho hóa đơn.

Nội dung đã thực hiện:

- Xây dựng API cập nhật tags:

```txt
PATCH /invoice/tags/{id}
```

- Lambda nhận danh sách tags từ request body.
- Cập nhật field `Tags` trong DynamoDB.
- Xây dựng API cập nhật starred:

```txt
PATCH /invoice/starred/{id}
```

- Lambda nhận giá trị `Starred` từ request body.
- Cập nhật trạng thái starred trong DynamoDB.
- Kiểm tra dữ liệu sau khi update trong DynamoDB Console.
- Kiểm thử API bằng Postman.

Ví dụ request update tags:

```json
{
  "tags": ["paid", "important", "accounting"]
}
```

Ví dụ request update starred:

```json
{
  "starred": true
}
```

{{% notice info %}}
Trong quá trình triển khai, cần thống nhất tên field giữa frontend và backend. Ví dụ backend có thể lưu `Tags` và `Starred`, trong khi frontend có thể gửi `tags` hoặc `starred`. Lambda nên xử lý và chuẩn hóa dữ liệu trước khi lưu hoặc trả response.
{{% /notice %}}

Kết quả đạt được:

- API cập nhật tags hoạt động.
- API cập nhật starred hoạt động.
- Hiểu tầm quan trọng của việc thống nhất tên field giữa frontend và DynamoDB.

---

### Ngày 6 - Thứ bảy, 06/06/2026

Ngày thứ sáu tập trung vào cấu hình API Gateway routes và kiểm thử tích hợp.

Nội dung đã thực hiện:

- Tạo hoặc kiểm tra các route trong API Gateway.
- Kết nối các route với `InvoiceManagementFunction`.
- Deploy API stage sau khi thay đổi route.
- Cấu hình CORS cho các method cần thiết.
- Kiểm thử toàn bộ API bằng Postman.
- Kiểm tra response headers.
- Kiểm tra lỗi `Missing Authentication Token`.
- Kiểm tra lỗi CORS khi gọi từ frontend.

Các route được kiểm thử:

```txt
GET /invoice
GET /invoice/{id}
GET /invoice?name=<customer_name>
PATCH /invoice/tags/{id}
PATCH /invoice/starred/{id}
```

Các lỗi đã kiểm tra:

| Lỗi | Nguyên nhân có thể |
|---|---|
| `Missing Authentication Token` | Sai method, sai path hoặc chưa deploy stage |
| CORS error | Thiếu CORS headers hoặc chưa enable CORS cho route |
| 500 Internal Server Error | Lambda lỗi logic hoặc response sai format |
| 404 Not Found | Không tìm thấy hóa đơn theo ID |
| AccessDenied | Lambda thiếu quyền DynamoDB |

Kết quả đạt được:

- Các API quản lý hóa đơn được kết nối với API Gateway.
- Kiểm thử được API bằng Postman.
- Biết cách xử lý lỗi route, CORS và response format.

---

### Ngày 7 - Chủ nhật, 07/06/2026

Ngày cuối tuần tập trung vào bắt đầu tích hợp frontend React với API Gateway.

Nội dung đã thực hiện:

- Cập nhật các API endpoint vào file `.env` của frontend.
- Kết nối frontend với API lấy danh sách hóa đơn.
- Kiểm tra hiển thị danh sách hóa đơn trên giao diện.
- Kiểm tra chức năng xem chi tiết hóa đơn.
- Kiểm tra tìm kiếm theo tên khách hàng.
- Kiểm tra update tags và starred từ frontend.
- Ghi chú lỗi frontend khi dữ liệu trả về không đúng format.
- Tổng hợp kết quả tuần 7 và chuẩn bị kế hoạch tuần 8.

Ví dụ biến môi trường frontend:

```txt
REACT_APP_API_INVOICE_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice
REACT_APP_API_UPDATE_TAGS_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice/tags
REACT_APP_API_UPDATE_STARRED_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/dev/invoice/starred
```

Kết quả đạt được:

- Frontend bắt đầu lấy được dữ liệu hóa đơn từ backend.
- Các API chính đã được kiểm thử qua Postman.
- Xác định các điểm cần hoàn thiện ở tuần 8 như giao diện, filter, sort, export Excel và deploy frontend.

---

## Tổng kết kiến thức Tuần 7

Trong tuần 7, em đã xây dựng phần API quản lý hóa đơn cho project **Serverless AI Invoice Scanner**. Đây là phần giúp frontend truy xuất và cập nhật dữ liệu đã được xử lý bởi AI.

| Nhóm kiến thức | Nội dung đã thực hiện |
|---|---|
| Lambda | Tạo `InvoiceManagementFunction` |
| API Gateway | Tạo GET và PATCH routes |
| DynamoDB | Scan, GetItem, Query, UpdateItem |
| Frontend Integration | Cấu hình API endpoint trong React |
| Testing | Kiểm thử API bằng Postman |
| Debugging | Kiểm tra lỗi bằng CloudWatch Logs |
| CORS | Cấu hình để frontend gọi API |
| Data Mapping | Chuẩn hóa `Tags/tags`, `Starred/starred`, `CustomerName` |

---

## Kết quả đạt được trong tuần

- Tạo được `InvoiceManagementFunction`.
- Xây dựng được API lấy danh sách hóa đơn.
- Xây dựng được API xem chi tiết hóa đơn theo ID.
- Xây dựng được API tìm kiếm theo tên khách hàng.
- Xây dựng được API cập nhật tags.
- Xây dựng được API cập nhật starred.
- Kiểm thử các API bằng Postman.
- Bắt đầu tích hợp frontend React với backend API.
- Xử lý được một số lỗi liên quan đến CORS, route và response format.
- Hoàn thiện phần backend API quản lý dữ liệu hóa đơn.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Dữ liệu trong DynamoDB có field không đồng nhất | Chuẩn hóa response trong Lambda trước khi trả về frontend |
| Tìm kiếm theo tên khách hàng chưa ổn định | Kiểm tra cả `CustomerName` và `ExtractedData.CustomerName` |
| API Gateway dễ lỗi sai route | Kiểm tra lại method, path và stage URL |
| CORS gây lỗi khi frontend gọi API | Thêm CORS headers trong Lambda response và API Gateway |
| PATCH update chưa đúng field | Chuẩn hóa `tags/Tags` và `starred/Starred` |
| Frontend không hiển thị đúng dữ liệu | Kiểm tra format JSON response từ API |

---

## Bài học rút ra

- Khi xây dựng API, cần thống nhất rõ dữ liệu giữa frontend, Lambda và DynamoDB.
- DynamoDB lưu dữ liệu linh hoạt nhưng cần chuẩn hóa field để frontend dễ xử lý.
- API Gateway cần cấu hình đúng method, route và stage để tránh lỗi `Missing Authentication Token`.
- CORS là phần quan trọng khi frontend chạy trên domain khác với API Gateway.
- Postman giúp kiểm thử API độc lập trước khi tích hợp vào frontend.
- CloudWatch Logs giúp tìm lỗi nhanh khi Lambda không trả response đúng.
- Cần kiểm tra cả happy case và error case cho từng API.

---

## Kế hoạch cho Tuần 8

Tuần 8 là tuần cuối của kỳ thực tập và cũng là tuần hoàn thiện project.

Nội dung dự kiến:

- Hoàn thiện giao diện frontend React.
- Tích hợp đầy đủ Cognito login/sign-up.
- Tích hợp upload, list, detail, search, tags và starred.
- Bổ sung filter theo ngày, sort theo ngày/tổng tiền và export Excel.
- Deploy frontend bằng AWS Amplify Hosting.
- Kiểm thử end-to-end toàn bộ hệ thống.
- Kiểm tra CloudWatch Logs và sửa lỗi còn lại.
- Hoàn thiện tài liệu hướng dẫn triển khai.
- Viết phần cleanup resources.
- Tổng kết project và kết quả thực tập.

---

## Nhận xét cuối tuần

Tuần 7 tập trung vào việc xây dựng các API quản lý hóa đơn và kết nối backend với frontend. Sau tuần này, hệ thống không chỉ xử lý được hóa đơn bằng AI mà còn có thể truy xuất, tìm kiếm và cập nhật dữ liệu đã xử lý. Đây là bước quan trọng để chuẩn bị hoàn thiện giao diện người dùng và triển khai hệ thống end-to-end trong tuần cuối.
