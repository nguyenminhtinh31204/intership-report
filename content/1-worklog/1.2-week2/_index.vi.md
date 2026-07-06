---
title: "Worklog Tuần 2"
date: 2026-04-27
weight: 102
week: 2
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 27/04/2026 - 03/05/2026 |
| Tuần thực tập | Tuần 2 |
| Giai đoạn | Giai đoạn học tập và nghiên cứu tài liệu |
| Chương trình học | First Cloud Journey |
| Chủ đề chính | Tìm hiểu các dịch vụ AWS nền tảng |
| Mục tiêu tuần | Nắm vai trò của các dịch vụ AWS cơ bản như S3, EC2, Lambda, VPC, CloudWatch và cách chúng được sử dụng trong hệ thống cloud |

---

## Định hướng học tập Tuần 2

Sau tuần đầu tiên làm quen với điện toán đám mây, AWS Global Infrastructure, AWS Console và IAM, tuần 2 tiếp tục học theo chương trình **First Cloud Journey**. Trọng tâm của tuần này là tìm hiểu các dịch vụ AWS nền tảng thường xuất hiện trong hầu hết các hệ thống cloud.

Trong tuần này, em chưa bắt đầu triển khai project chính. Mục tiêu là học lý thuyết, xem tài liệu, thực hành cơ bản và ghi chú lại vai trò của từng dịch vụ để chuẩn bị cho giai đoạn làm project ở 4 tuần cuối.

---

## Mục tiêu học tập Tuần 2

Các mục tiêu chính trong tuần gồm:

- Tìm hiểu Amazon S3 và vai trò của object storage.
- Tìm hiểu Amazon EC2 ở mức tổng quan để hiểu mô hình máy chủ ảo trên cloud.
- Tìm hiểu AWS Lambda và khái niệm serverless compute.
- Tìm hiểu Amazon VPC và các khái niệm mạng cơ bản trên AWS.
- Tìm hiểu Amazon CloudWatch dùng để giám sát và ghi log.
- Ôn lại IAM Role và permission khi các dịch vụ AWS giao tiếp với nhau.
- So sánh mô hình truyền thống dùng server với mô hình serverless.
- Ghi chú kiến thức để áp dụng cho project **Serverless AI Invoice Scanner** ở giai đoạn sau.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 27/04/2026

Trong ngày đầu tiên của tuần 2, em ôn lại kiến thức tuần 1 và bắt đầu học về các dịch vụ AWS nền tảng theo tài liệu First Cloud Journey.

Nội dung đã thực hiện:

- Ôn lại các khái niệm: AWS Region, Availability Zone, IAM và AWS Console.
- Xem lại lộ trình học của First Cloud Journey.
- Xác định các dịch vụ cần tìm hiểu trong tuần 2.
- Ghi chú nhóm dịch vụ AWS theo từng loại:
  - Compute
  - Storage
  - Database
  - Networking
  - Security
  - Monitoring
- Tìm hiểu cách các dịch vụ AWS phối hợp trong một hệ thống cloud cơ bản.

Kết quả đạt được:

- Hiểu rõ hơn cách phân loại dịch vụ AWS.
- Có kế hoạch học tập cụ thể cho tuần 2.
- Biết rằng mỗi dịch vụ AWS đảm nhận một vai trò riêng trong kiến trúc cloud.

---

### Ngày 2 - Thứ ba, 28/04/2026

Ngày thứ hai tập trung vào **Amazon S3** và khái niệm lưu trữ đối tượng trên cloud.

Nội dung đã thực hiện:

- Đọc tài liệu về Amazon S3 trong chương trình học.
- Tìm hiểu khái niệm bucket, object, key và storage class.
- Tìm hiểu sự khác nhau giữa lưu trữ file truyền thống và object storage.
- Xem cách S3 được dùng để lưu ảnh, file PDF, file backup và static website.
- Tìm hiểu tính năng block public access.
- Ghi chú vai trò của S3 trong các hệ thống serverless.

Kết quả đạt được:

- Hiểu Amazon S3 là dịch vụ lưu trữ đối tượng có khả năng mở rộng cao.
- Biết bucket là nơi chứa object.
- Hiểu vì sao cần bật block public access để bảo vệ dữ liệu.
- Nắm được S3 có thể dùng làm nơi lưu file đầu vào cho các hệ thống xử lý dữ liệu.

---

### Ngày 3 - Thứ tư, 29/04/2026

Ngày thứ ba tập trung vào nhóm dịch vụ **Compute**, bao gồm Amazon EC2 và AWS Lambda.

Nội dung đã thực hiện:

- Tìm hiểu Amazon EC2 ở mức tổng quan.
- Hiểu khái niệm instance, AMI, instance type và security group.
- So sánh EC2 với máy chủ vật lý truyền thống.
- Tìm hiểu AWS Lambda và mô hình serverless compute.
- Tìm hiểu khái niệm function, runtime, handler, event và trigger.
- So sánh EC2 và Lambda theo cách vận hành, chi phí và khả năng mở rộng.

Bảng so sánh cơ bản:

| Tiêu chí | Amazon EC2 | AWS Lambda |
|---|---|---|
| Mô hình | Máy chủ ảo | Serverless function |
| Quản lý server | Người dùng cần quản lý | AWS quản lý |
| Chi phí | Tính theo thời gian chạy instance | Tính theo số lần gọi và thời gian xử lý |
| Phù hợp | Ứng dụng chạy liên tục | Tác vụ theo sự kiện |
| Khả năng mở rộng | Cần cấu hình thêm | Tự động scale |

Kết quả đạt được:

- Hiểu EC2 đại diện cho mô hình máy chủ ảo trên cloud.
- Hiểu Lambda là dịch vụ chạy code không cần quản lý server.
- Nắm được serverless phù hợp với các hệ thống xử lý theo sự kiện.

---

### Ngày 4 - Thứ năm, 30/04/2026

Ngày thứ tư tập trung vào **Amazon VPC** và kiến thức mạng cơ bản trong AWS.

Nội dung đã thực hiện:

- Tìm hiểu khái niệm Amazon VPC.
- Tìm hiểu subnet, route table, internet gateway và security group.
- Phân biệt public subnet và private subnet.
- Tìm hiểu vì sao tài nguyên cloud cần được đặt trong môi trường mạng an toàn.
- Xem ví dụ một kiến trúc có frontend public và backend private.
- Ghi chú vai trò của networking trong bảo mật hệ thống.

Kết quả đạt được:

- Hiểu VPC là mạng riêng ảo trong AWS.
- Biết subnet dùng để chia nhỏ mạng trong VPC.
- Hiểu security group giống như lớp kiểm soát traffic vào và ra.
- Nhận thức được vai trò quan trọng của network design trong kiến trúc cloud.

---

### Ngày 5 - Thứ sáu, 01/05/2026

Ngày thứ năm tập trung vào **Amazon CloudWatch** và việc giám sát hệ thống trên AWS.

Nội dung đã thực hiện:

- Tìm hiểu Amazon CloudWatch.
- Tìm hiểu log group, log stream và log event.
- Tìm hiểu metrics và alarm.
- Xem cách CloudWatch được dùng để theo dõi Lambda, API Gateway và EC2.
- Ghi chú vai trò của CloudWatch trong debug lỗi hệ thống.
- Tìm hiểu vì sao log rất quan trọng khi vận hành hệ thống cloud.

Kết quả đạt được:

- Hiểu CloudWatch là dịch vụ giám sát và ghi log.
- Biết log group và log stream dùng để tổ chức log.
- Hiểu rằng khi Lambda hoặc API gặp lỗi, CloudWatch là nơi quan trọng để kiểm tra nguyên nhân.
- Biết alarm có thể dùng để cảnh báo khi hệ thống có dấu hiệu bất thường.

---

### Ngày 6 - Thứ bảy, 02/05/2026

Ngày thứ sáu tập trung vào việc ôn lại **IAM** và mối liên hệ giữa IAM với các dịch vụ AWS đã học.

Nội dung đã thực hiện:

- Ôn lại IAM User, IAM Role và IAM Policy.
- Tìm hiểu vì sao mỗi dịch vụ cần quyền truy cập phù hợp.
- Xem ví dụ Lambda cần IAM Role để ghi log vào CloudWatch.
- Xem ví dụ Lambda cần quyền để đọc hoặc ghi file vào S3.
- Tìm hiểu nguyên tắc least privilege.
- Ghi chú các lỗi thường gặp khi thiếu quyền IAM.

Ví dụ lỗi có thể gặp khi thiếu quyền:

```txt
AccessDenied
UnauthorizedOperation
User is not authorized to perform action
```

Kết quả đạt được:

- Hiểu rõ hơn vai trò của IAM trong bảo mật AWS.
- Biết rằng các dịch vụ AWS không tự động có quyền truy cập lẫn nhau.
- Nắm được cần cấp đúng quyền để dịch vụ hoạt động an toàn.

---

### Ngày 7 - Chủ nhật, 03/05/2026

Ngày cuối của tuần dùng để tổng hợp kiến thức đã học và chuẩn bị cho tuần tiếp theo.

Nội dung đã thực hiện:

- Ôn tập lại các dịch vụ đã học trong tuần:
  - Amazon S3
  - Amazon EC2
  - AWS Lambda
  - Amazon VPC
  - Amazon CloudWatch
  - AWS IAM
- Tổng hợp ghi chú theo từng nhóm dịch vụ.
- Vẽ lại sơ đồ đơn giản thể hiện cách các dịch vụ cloud có thể kết hợp với nhau.
- Ghi lại các câu hỏi còn chưa rõ để tiếp tục tìm hiểu ở tuần sau.
- Viết báo cáo worklog tuần 2.

Kết quả đạt được:

- Hoàn thành tuần học thứ hai theo chương trình First Cloud Journey.
- Hiểu vai trò của các dịch vụ AWS nền tảng.
- Có nền tảng tốt hơn để học database, API và serverless ở các tuần tiếp theo.

---

## Tổng kết kiến thức Tuần 2

Trong tuần 2, em đã tìm hiểu các dịch vụ AWS nền tảng thường được sử dụng trong nhiều hệ thống cloud. Các kiến thức này giúp em hiểu rõ hơn cách một hệ thống trên AWS được xây dựng từ nhiều thành phần độc lập.

| Nhóm kiến thức | Nội dung đã học |
|---|---|
| Storage | Amazon S3, bucket, object, block public access |
| Compute | Amazon EC2, AWS Lambda, serverless compute |
| Networking | Amazon VPC, subnet, route table, security group |
| Monitoring | Amazon CloudWatch, log group, metrics, alarm |
| Security | IAM Role, IAM Policy, permission, least privilege |
| Cloud architecture | Cách các dịch vụ phối hợp trong hệ thống AWS |

---

## Kết quả đạt được trong tuần

- Hiểu Amazon S3 và vai trò của object storage.
- Biết Amazon EC2 là dịch vụ máy chủ ảo trên AWS.
- Hiểu AWS Lambda là dịch vụ serverless compute.
- Phân biệt được EC2 và Lambda.
- Hiểu Amazon VPC ở mức cơ bản.
- Biết CloudWatch dùng để ghi log và giám sát.
- Hiểu IAM là thành phần quan trọng để kiểm soát quyền truy cập.
- Nắm được mối liên hệ giữa storage, compute, networking, monitoring và security.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Có nhiều dịch vụ AWS cần ghi nhớ | Chia dịch vụ theo nhóm: compute, storage, network, security |
| Dễ nhầm giữa EC2 và Lambda | So sánh theo tiêu chí quản lý server, chi phí và cách chạy |
| Khái niệm VPC còn trừu tượng | Vẽ sơ đồ mạng đơn giản để dễ hiểu hơn |
| IAM Policy khó đọc do dùng JSON | Tập trung hiểu action, resource và effect trước |
| CloudWatch có nhiều khái niệm mới | Ghi chú riêng log group, log stream, metrics và alarm |

---

## Bài học rút ra

- AWS được tổ chức thành nhiều nhóm dịch vụ, mỗi nhóm giải quyết một nhu cầu riêng.
- Không nên học từng dịch vụ riêng lẻ mà nên hiểu vai trò của chúng trong kiến trúc tổng thể.
- S3, Lambda, IAM và CloudWatch là các dịch vụ nền tảng quan trọng trong mô hình serverless.
- Security cần được quan tâm ngay từ đầu, đặc biệt là IAM và quyền truy cập tài nguyên.
- Việc ghi log và giám sát giúp phát hiện lỗi nhanh hơn khi hệ thống vận hành.

---

## Kế hoạch cho Tuần 3

Trong tuần 3, em sẽ tiếp tục học theo chương trình First Cloud Journey, tập trung nhiều hơn vào database, API và kiến trúc serverless.

Nội dung dự kiến:

- Tìm hiểu Amazon DynamoDB.
- Tìm hiểu Amazon RDS ở mức tổng quan để so sánh SQL và NoSQL.
- Tìm hiểu Amazon API Gateway.
- Tìm hiểu kiến trúc event-driven.
- Tìm hiểu serverless application pattern.
- Thực hành xem tài liệu và ghi chú cách các dịch vụ có thể kết hợp trong một ứng dụng thực tế.
- Chuẩn bị kiến thức nền cho project ở 4 tuần cuối.

---

## Nhận xét cuối tuần

Tuần 2 giúp em hiểu rõ hơn các dịch vụ AWS nền tảng, đặc biệt là S3, Lambda, VPC, CloudWatch và IAM. Đây là những dịch vụ quan trọng trong nhiều hệ thống cloud và cũng là nền tảng cần thiết để thực hiện project ở các tuần cuối. Sau tuần này, em đã có cái nhìn rõ hơn về cách AWS tổ chức tài nguyên và cách các dịch vụ phối hợp với nhau trong một kiến trúc cloud.
