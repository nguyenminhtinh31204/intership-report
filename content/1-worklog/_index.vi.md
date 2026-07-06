+++
title = "Nhật ký công việc"
weight = 1
+++

# Nhật ký công việc

Trang này trình bày tổng quan quá trình thực tập của tôi trong chương trình thực tập AWS kéo dài **12 tuần**. Nội dung thực tập được chia thành hai giai đoạn chính: giai đoạn học tập kiến thức nền tảng thông qua chương trình **First Cloud Journey** và giai đoạn áp dụng kiến thức để xây dựng dự án **Serverless AI Invoice Scanner**.

Trong giai đoạn đầu, tôi tập trung tìm hiểu các khái niệm cơ bản về cloud computing, các dịch vụ cốt lõi của AWS, kiến trúc serverless, xác thực người dùng, triển khai frontend và giám sát hệ thống. Trong giai đoạn tiếp theo, tôi áp dụng các kiến thức đã học để thiết kế, triển khai, kiểm thử, deploy, viết tài liệu và hoàn thiện một hệ thống xử lý hóa đơn theo kiến trúc serverless.

Chương trình thực tập được hoàn thành trong **12 tuần**, với nội dung công việc theo từng tuần như sau:

---

**Tuần 1:** [Làm quen với AWS Cloud, First Cloud Journey, các khái niệm cloud computing, AWS Global Infrastructure, AWS Console và IAM cơ bản](/1-worklog/1.1-week1/)

**Tuần 2:** [Tìm hiểu các dịch vụ nền tảng của AWS như Amazon S3, Amazon EC2, AWS Lambda, Amazon VPC, Amazon CloudWatch và IAM permissions](/1-worklog/1.2-week2/)

**Tuần 3:** [Tìm hiểu về database, API và kiến trúc serverless trên AWS, bao gồm Amazon DynamoDB, Amazon RDS, Amazon API Gateway, Lambda và event-driven architecture](/1-worklog/1.3-week3/)

**Tuần 4:** [Tìm hiểu authentication, frontend hosting, CI/CD, Amazon Cognito, AWS Amplify Hosting và ôn tập kiến thức First Cloud Journey trước khi bắt đầu project](/1-worklog/1.4-week4/)

**Tuần 5:** [Bắt đầu project Serverless AI Invoice Scanner, phân tích yêu cầu, thiết kế kiến trúc hệ thống, tạo S3 bucket, DynamoDB table, Upload Lambda và API Gateway upload route](/1-worklog/1.5-week5/)

**Tuần 6:** [Xây dựng luồng xử lý hóa đơn bằng AI với S3 Event Trigger, AWS Lambda, Amazon Textract, OpenAI API và Amazon DynamoDB](/1-worklog/1.6-week6/)

**Tuần 7:** [Xây dựng các API quản lý hóa đơn, bao gồm lấy dữ liệu hóa đơn, tìm kiếm hóa đơn, cập nhật tags, cập nhật starred và tích hợp backend API với React frontend](/1-worklog/1.7-week7/)

**Tuần 8:** [Hoàn thiện các chức năng frontend, tích hợp Amazon Cognito, deploy React app bằng AWS Amplify Hosting, kiểm thử end-to-end và viết tài liệu cleanup resources](/1-worklog/1.8-week8/)

**Tuần 9:** [Rà soát toàn bộ hệ thống, kiểm thử lại API và frontend, kiểm tra CloudWatch Logs, rà soát chi phí AWS, hoàn thiện tài liệu và chuẩn bị demo project](/1-worklog/1.9-week9/)

**Tuần 10:** [Hoàn thiện báo cáo thực tập, rà soát proposal và tài liệu Markdown, kiểm tra tài nguyên AWS, hoàn thiện checklist cleanup và chuẩn bị nội dung trình bày cuối kỳ](/1-worklog/1.10-week10/)

**Tuần 11:** [Chỉnh sửa project sau góp ý, rà soát API Gateway routes, kiểm tra biến môi trường frontend, kiểm thử lại các chức năng chính, chuẩn bị kịch bản demo và đóng gói tài liệu bàn giao](/1-worklog/1.11-week11/)

**Tuần 12:** [Hoàn thiện bản review cuối cùng, chuẩn bị demo cuối kỳ, kiểm thử end-to-end lần cuối, rà soát cleanup resources, đóng gói source code/tài liệu và tổng kết toàn bộ quá trình thực tập](/1-worklog/1.12-week12/)

---

## Tóm tắt các giai đoạn thực tập

| Giai đoạn | Thời gian | Nội dung chính |
|---|---|---|
| Giai đoạn 1 | Tuần 1 - Tuần 4 | Học kiến thức nền tảng AWS thông qua chương trình First Cloud Journey |
| Giai đoạn 2 | Tuần 5 - Tuần 8 | Xây dựng project Serverless AI Invoice Scanner |
| Giai đoạn 3 | Tuần 9 - Tuần 12 | Rà soát, kiểm thử, viết tài liệu, chuẩn bị demo và bàn giao project |

---

## Dự án chính

Dự án chính được thực hiện trong quá trình thực tập là **Serverless AI Invoice Scanner**.

Đây là một ứng dụng web theo kiến trúc serverless, cho phép người dùng upload file hóa đơn, xử lý nội dung hóa đơn bằng AI, lưu dữ liệu hóa đơn đã trích xuất và quản lý các bản ghi hóa đơn thông qua giao diện web.

Dự án sử dụng các dịch vụ và công nghệ chính sau:

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
- React Frontend

---

## Kết quả chính đạt được

Sau khi hoàn thành quá trình thực tập, tôi đã đạt được một số kết quả chính:

- Hiểu được các khái niệm cơ bản về AWS Cloud và kiến trúc serverless.
- Biết cách sử dụng các dịch vụ AWS cốt lõi trong một project thực tế.
- Xây dựng được backend API bằng Amazon API Gateway và AWS Lambda.
- Lưu trữ file hóa đơn bằng Amazon S3.
- Xử lý nội dung hóa đơn bằng Amazon Textract và OpenAI API.
- Lưu dữ liệu hóa đơn có cấu trúc vào Amazon DynamoDB.
- Tích hợp backend với React frontend.
- Deploy frontend bằng AWS Amplify Hosting.
- Sử dụng Amazon CloudWatch Logs để theo dõi và debug lỗi.
- Viết worklog theo từng tuần, tài liệu kỹ thuật và hướng dẫn cleanup resources.

---

## Kết luận

Nhật ký công việc này giúp tổng hợp lại toàn bộ quá trình học tập và thực hiện project trong kỳ thực tập. Thông qua 12 tuần thực tập, tôi đã có cơ hội tiếp cận các dịch vụ AWS thực tế, hiểu hơn về cách xây dựng một hệ thống serverless và rèn luyện kỹ năng triển khai, kiểm thử, debug, viết tài liệu cũng như làm việc nhóm trong một project cloud.
