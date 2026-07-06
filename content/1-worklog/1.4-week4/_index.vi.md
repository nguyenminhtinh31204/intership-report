---
title: "Worklog Tuần 4 "
date: 2026-05-11
weight: 104
week: 4
chapter: false
---

## Thông tin chung

| Nội dung | Chi tiết |
|---|---|
| Thời gian | 11/05/2026 - 17/05/2026 |
| Tuần thực tập | Tuần 4 |
| Giai đoạn | Giai đoạn học tập và nghiên cứu tài liệu |
| Chương trình học | First Cloud Journey |
| Chủ đề chính | Authentication, Frontend Hosting, CI/CD và tổng hợp kiến thức AWS |
| Mục tiêu tuần | Hoàn thành giai đoạn học First Cloud Journey và chuẩn bị kế hoạch triển khai project ở 4 tuần cuối |

---

## Định hướng học tập Tuần 4

Tuần 4 là tuần cuối cùng của giai đoạn học tập theo chương trình **First Cloud Journey**. Sau ba tuần đầu tìm hiểu về cloud computing, AWS infrastructure, storage, compute, database, API và serverless architecture, tuần này tập trung vào các nội dung phục vụ triển khai ứng dụng hoàn chỉnh.

Các nội dung chính gồm:

- Xác thực người dùng với Amazon Cognito.
- Triển khai frontend với AWS Amplify Hosting.
- Tìm hiểu CI/CD cơ bản với GitHub và Amplify.
- Tìm hiểu monitoring, security và best practices.
- Ôn tập lại toàn bộ kiến thức đã học trong 4 tuần.
- Chuẩn bị kế hoạch bước vào project **Serverless AI Invoice Scanner** từ tuần 5.

---

## Mục tiêu học tập Tuần 4

Các mục tiêu chính trong tuần gồm:

- Hiểu vai trò của Amazon Cognito trong xác thực người dùng.
- Tìm hiểu User Pool, App Client, sign-up và sign-in.
- Hiểu AWS Amplify Hosting dùng để deploy frontend.
- Tìm hiểu cách kết nối GitHub repository với Amplify Hosting.
- Hiểu khái niệm CI/CD ở mức cơ bản.
- Tìm hiểu AWS Well-Architected Framework ở mức tổng quan.
- Ôn lại các dịch vụ đã học trong chương trình First Cloud Journey.
- Xác định các dịch vụ sẽ dùng trong project thực tế.
- Lập kế hoạch triển khai project trong 4 tuần cuối.

---

## Nội dung thực hiện trong tuần

### Ngày 1 - Thứ hai, 11/05/2026

Ngày đầu tiên của tuần 4 tập trung vào việc ôn lại kiến thức tuần 3 và bắt đầu tìm hiểu về xác thực người dùng trên AWS.

Nội dung đã thực hiện:

- Ôn lại các dịch vụ đã học ở tuần 3:
  - Amazon DynamoDB
  - Amazon RDS
  - Amazon API Gateway
  - AWS Lambda
  - CloudWatch Logs
- Tìm hiểu vai trò của authentication trong ứng dụng web.
- Tìm hiểu Amazon Cognito là gì.
- Ghi chú sự khác nhau giữa authentication và authorization.
- Xem cách Cognito có thể hỗ trợ đăng ký và đăng nhập người dùng.

Kết quả đạt được:

- Hiểu vì sao ứng dụng cần có lớp xác thực người dùng.
- Biết Amazon Cognito là dịch vụ hỗ trợ quản lý user và authentication.
- Có nền tảng để tiếp tục tìm hiểu User Pool và App Client.

---

### Ngày 2 - Thứ ba, 12/05/2026

Ngày thứ hai tập trung vào **Amazon Cognito User Pool** và các thành phần cơ bản trong quá trình đăng nhập.

Nội dung đã thực hiện:

- Tìm hiểu khái niệm User Pool.
- Tìm hiểu App Client trong Cognito.
- Tìm hiểu luồng đăng ký và đăng nhập người dùng.
- Tìm hiểu các thông tin frontend thường cần cấu hình:
  - AWS Region
  - User Pool ID
  - App Client ID
- Tìm hiểu token trong Cognito ở mức cơ bản.
- Ghi chú vai trò của Cognito trong việc bảo vệ ứng dụng frontend.

Ví dụ cấu hình frontend thường gặp:

```txt
REACT_APP_AWS_REGION=ap-southeast-1
REACT_APP_USER_POOL_ID=ap-southeast-1_xxxxxxxxx
REACT_APP_USER_POOL_CLIENT_ID=xxxxxxxxxxxxxxxxxxxxxxxxxx
```

Kết quả đạt được:

- Hiểu User Pool là nơi quản lý người dùng.
- Biết App Client được frontend sử dụng để kết nối với Cognito.
- Nắm được các thông tin cần thiết khi tích hợp Cognito vào ứng dụng React.

---

### Ngày 3 - Thứ tư, 13/05/2026

Ngày thứ ba tập trung vào **AWS Amplify Hosting** và cách triển khai ứng dụng frontend.

Nội dung đã thực hiện:

- Tìm hiểu AWS Amplify Hosting.
- Tìm hiểu cách Amplify Hosting deploy ứng dụng frontend.
- Xem luồng kết nối GitHub repository với Amplify.
- Tìm hiểu build settings và environment variables.
- Ghi chú sự khác nhau giữa Amplify Hosting và Amplify backend.
- Tìm hiểu cách frontend có thể sử dụng biến môi trường để gọi API Gateway.

Kết quả đạt được:

- Hiểu Amplify Hosting dùng để build và deploy frontend.
- Biết Amplify có thể tự động deploy khi có commit mới từ GitHub.
- Hiểu rằng trong project sau này, Amplify sẽ dùng chủ yếu cho hosting frontend React.

{{% notice info %}}
Trong project Serverless AI Invoice Scanner, Amplify được dùng cho **Hosting frontend**, còn Cognito và backend AWS services sẽ được cấu hình riêng.
{{% /notice %}}

---

### Ngày 4 - Thứ năm, 14/05/2026

Ngày thứ tư tập trung vào khái niệm **CI/CD** và quy trình triển khai ứng dụng hiện đại.

Nội dung đã thực hiện:

- Tìm hiểu CI/CD là gì.
- Tìm hiểu Continuous Integration và Continuous Deployment.
- Xem ví dụ luồng deploy frontend:

```txt
Developer Commit Code → GitHub Repository → Amplify Build → Amplify Deploy → Public Website
```

- Tìm hiểu vai trò của build command và output directory.
- Ghi chú các lỗi có thể gặp khi deploy frontend:
  - Sai biến môi trường.
  - Build failed.
  - Sai package dependency.
  - Sai cấu hình redirect.
- Tìm hiểu cách kiểm tra build logs trong Amplify.

Kết quả đạt được:

- Hiểu CI/CD giúp tự động hóa quá trình build và deploy.
- Biết GitHub có thể kết nối với Amplify Hosting.
- Hiểu build logs rất quan trọng khi deploy frontend lỗi.

---

### Ngày 5 - Thứ sáu, 15/05/2026

Ngày thứ năm tập trung vào **AWS Well-Architected Framework** và các nguyên tắc thiết kế hệ thống cloud.

Nội dung đã thực hiện:

- Tìm hiểu tổng quan AWS Well-Architected Framework.
- Ghi chú các trụ cột chính:
  - Operational Excellence
  - Security
  - Reliability
  - Performance Efficiency
  - Cost Optimization
  - Sustainability
- Liên hệ từng trụ cột với các dịch vụ đã học.
- Tìm hiểu vì sao cần thiết kế hệ thống vừa bảo mật, vừa tối ưu chi phí.
- Ghi chú các best practices khi làm việc với AWS.

Bảng ghi chú ngắn:

| Trụ cột | Ý nghĩa |
|---|---|
| Operational Excellence | Vận hành hệ thống ổn định, dễ theo dõi và cải tiến. |
| Security | Bảo vệ dữ liệu, tài khoản và quyền truy cập. |
| Reliability | Hệ thống có khả năng phục hồi khi có lỗi. |
| Performance Efficiency | Sử dụng tài nguyên phù hợp với nhu cầu. |
| Cost Optimization | Tối ưu chi phí, tránh lãng phí tài nguyên. |
| Sustainability | Sử dụng tài nguyên hiệu quả và bền vững. |

Kết quả đạt được:

- Hiểu được các nguyên tắc cơ bản khi thiết kế hệ thống trên AWS.
- Nhận thức rõ hơn về bảo mật, giám sát và tối ưu chi phí.
- Có tư duy thiết kế hệ thống thay vì chỉ tạo tài nguyên riêng lẻ.

---

### Ngày 6 - Thứ bảy, 16/05/2026

Ngày thứ sáu tập trung vào việc ôn tập toàn bộ kiến thức đã học trong 4 tuần đầu.

Nội dung đã thực hiện:

- Ôn lại các nhóm dịch vụ:
  - Compute: EC2, Lambda
  - Storage: S3
  - Database: DynamoDB, RDS
  - Networking: VPC
  - Security: IAM, Cognito
  - API: API Gateway
  - Monitoring: CloudWatch
  - Hosting: Amplify Hosting
- Tổng hợp vai trò của từng dịch vụ.
- Ghi chú dịch vụ nào sẽ được dùng trong project.
- Liên hệ kiến thức First Cloud Journey với project **Serverless AI Invoice Scanner**.
- Chuẩn bị danh sách tài nguyên cần tạo ở tuần 5.

Kết quả đạt được:

- Tổng hợp được kiến thức chính sau 4 tuần học.
- Xác định được các dịch vụ phù hợp với project.
- Có kế hoạch rõ hơn cho giai đoạn triển khai thực tế.

---

### Ngày 7 - Chủ nhật, 17/05/2026

Ngày cuối của tuần dùng để tổng kết giai đoạn học tập và chuẩn bị bước sang giai đoạn làm project.

Nội dung đã thực hiện:

- Viết báo cáo tổng kết tuần 4.
- Tổng hợp nội dung đã học trong giai đoạn First Cloud Journey.
- Xác định project sẽ bắt đầu từ tuần 5.
- Lập kế hoạch triển khai project trong 4 tuần cuối.
- Xác định luồng xử lý dự kiến của project:

```txt
React Frontend → API Gateway → Lambda → S3 → Textract → OpenAI API → DynamoDB
```

- Ghi chú các dịch vụ cần triển khai:
  - AWS Amplify Hosting
  - Amazon Cognito
  - Amazon API Gateway
  - AWS Lambda
  - Amazon S3
  - Amazon Textract
  - OpenAI API
  - Amazon DynamoDB
  - Amazon CloudWatch
  - AWS IAM

Kết quả đạt được:

- Hoàn thành giai đoạn học First Cloud Journey.
- Chuẩn bị sẵn định hướng cho project.
- Có nền tảng để bắt đầu triển khai hệ thống Serverless AI Invoice Scanner.

---

## Tổng kết kiến thức Tuần 4

Trong tuần 4, em đã học các nội dung liên quan đến xác thực người dùng, triển khai frontend, CI/CD và các nguyên tắc thiết kế hệ thống cloud.

| Nhóm kiến thức | Nội dung đã học |
|---|---|
| Authentication | Amazon Cognito, User Pool, App Client, sign-up, sign-in |
| Frontend Hosting | AWS Amplify Hosting, deploy React app, GitHub integration |
| CI/CD | Build, deploy, build logs, environment variables |
| Cloud Best Practices | AWS Well-Architected Framework |
| Security | IAM, Cognito, principle of least privilege |
| Monitoring | CloudWatch, Amplify build logs |
| Project Preparation | Xác định dịch vụ cần dùng cho Serverless AI Invoice Scanner |

---

## Kết quả đạt được trong tuần

- Hiểu Amazon Cognito và vai trò trong xác thực người dùng.
- Biết User Pool và App Client dùng để tích hợp frontend.
- Hiểu AWS Amplify Hosting dùng để deploy frontend.
- Biết quy trình kết nối GitHub với Amplify Hosting.
- Hiểu khái niệm CI/CD cơ bản.
- Nắm tổng quan AWS Well-Architected Framework.
- Ôn tập lại kiến thức 4 tuần đầu.
- Chuẩn bị kế hoạch triển khai project cho tuần 5 đến tuần 8.

---

## Khó khăn gặp phải

| Khó khăn | Hướng xử lý |
|---|---|
| Dễ nhầm giữa Amplify Hosting và Amplify backend | Ghi chú rõ project chỉ dùng Amplify Hosting cho frontend |
| Cognito có nhiều cấu hình như User Pool, App Client, token | Tách từng thành phần để học riêng |
| CI/CD còn mới | Xem theo luồng GitHub → Build → Deploy để dễ hiểu |
| Well-Architected có nhiều khái niệm | Ghi chú ngắn từng trụ cột và liên hệ với ví dụ |
| Cần kết nối kiến thức nhiều dịch vụ | Vẽ sơ đồ kiến trúc tổng quan để dễ hình dung |

---

## Bài học rút ra

- Một ứng dụng cloud hoàn chỉnh không chỉ có backend mà còn cần authentication, hosting, monitoring và security.
- Cognito giúp giảm công sức tự xây dựng hệ thống đăng nhập.
- Amplify Hosting phù hợp để triển khai frontend nhanh chóng từ GitHub.
- CI/CD giúp quá trình cập nhật ứng dụng nhanh và ổn định hơn.
- Well-Architected Framework giúp định hướng thiết kế hệ thống an toàn, tin cậy và tối ưu chi phí.
- 4 tuần đầu học nền tảng là cần thiết trước khi bắt đầu project thực tế.

---

## Tổng kết giai đoạn 4 tuần đầu

Sau 4 tuần học theo chương trình **First Cloud Journey**, em đã nắm được các kiến thức nền tảng cần thiết về AWS Cloud.

Các nhóm kiến thức đã học:

| Tuần | Chủ đề chính |
|---|---|
| Tuần 1 | Cloud computing, AWS Global Infrastructure, AWS Console, IAM cơ bản |
| Tuần 2 | S3, EC2, Lambda, VPC, CloudWatch, IAM |
| Tuần 3 | DynamoDB, RDS, API Gateway, Serverless, Event-driven |
| Tuần 4 | Cognito, Amplify Hosting, CI/CD, Well-Architected Framework |

Những kiến thức này sẽ được áp dụng vào project **Serverless AI Invoice Scanner** trong 4 tuần tiếp theo.

---

## Kế hoạch cho Tuần 5

Từ tuần 5, em sẽ bắt đầu giai đoạn triển khai project **Serverless AI Invoice Scanner**.

Nội dung dự kiến tuần 5:

- Phân tích yêu cầu project.
- Thiết kế kiến trúc hệ thống.
- Tạo S3 bucket lưu file hóa đơn.
- Tạo DynamoDB table `InvoiceData`.
- Tạo Lambda function xử lý upload file.
- Cấu hình API Gateway route `POST /uploads`.
- Kiểm thử upload bằng Postman.
- Ghi log và debug bằng CloudWatch.

---

## Nhận xét cuối tuần

Tuần 4 đánh dấu việc hoàn thành giai đoạn học tập theo chương trình First Cloud Journey. Sau tuần này, em đã có cái nhìn tổng quan về các dịch vụ AWS quan trọng và hiểu cách chúng phối hợp trong một hệ thống cloud. Đây là nền tảng cần thiết để chuyển sang giai đoạn thực hiện project **Serverless AI Invoice Scanner** trong 4 tuần cuối của kỳ thực tập.
