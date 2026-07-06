+++
title = "Blog 1"
weight = 301
+++

![AWS Summit New York 2026 - Agentic AI](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2026/06/17/2026-aws-ny-summit-keynote.jpg)

## AWS và định hướng xây dựng AI Agent cho doanh nghiệp

AWS muốn trở thành nền tảng chính giúp doanh nghiệp xây dựng, kiểm soát và vận hành **AI agent** ở quy mô production.

Tại **AWS Summit New York 2026**, Swami Sivasubramanian, Phó chủ tịch AWS phụ trách Agentic AI, đã trình bày nhiều công bố quan trọng liên quan đến AI agent, bảo mật AI, hiện đại hóa phần mềm và dữ liệu cho các workflow tự động.

---

## 1. Các công bố chính tại AWS Summit New York 2026

### Amazon Bedrock AgentCore có nhiều năng lực mới

AWS giới thiệu các tính năng mới giúp AI agent kết nối với tri thức nội bộ doanh nghiệp, web và các nguồn dữ liệu trả phí.

Mục tiêu là giúp doanh nghiệp:

- Xây dựng agent nhanh hơn.
- Kiểm soát agent tốt hơn.
- Liên tục cải thiện agent khi đưa vào môi trường production.

---

### Amazon Bedrock Managed Knowledge Base

Amazon Bedrock Managed Knowledge Base giúp doanh nghiệp xây dựng pipeline **RAG** dễ dàng hơn.

Dịch vụ này hỗ trợ:

- Connector dữ liệu.
- Xử lý nhiều định dạng tài liệu.
- Cơ chế truy xuất thông minh cho các truy vấn nhiều bước.

![Amazon Bedrock AgentCore Knowledge Layers](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2026/06/16/knowledge-layers.png)

---

### Web Search trên Amazon Bedrock AgentCore

Tính năng Web Search cho phép AI agent tìm kiếm thông tin mới từ web theo cách được quản lý sẵn.

Agent có thể:

- Lấy thông tin mới nhất từ internet.
- Trích dẫn nguồn rõ ràng.
- Giữ dữ liệu trong môi trường bảo mật của khách hàng AWS.

---

### AWS WAF hỗ trợ kiếm tiền từ lưu lượng AI bot

AWS WAF bổ sung khả năng giúp nhà xuất bản nội dung kiểm soát lưu lượng truy cập từ AI bot hoặc AI agent.

Nhà xuất bản có thể:

- Định giá quyền truy cập nội dung hoặc API.
- Đo lường lưu lượng AI bot.
- Thu phí khi bot hoặc agent truy cập nội dung.

---

### Bedrock AgentCore Harness đã khả dụng rộng rãi

Bedrock AgentCore Harness giúp nhà phát triển chạy AI agent ở mức production-grade mà không cần tự viết toàn bộ logic điều phối.

Nhà phát triển có thể cấu hình:

- Model.
- Tool.
- Skill.
- Instruction.

---

### AWS Continuum và Security Agent

AWS giới thiệu các công cụ bảo mật sử dụng AI nhằm tăng tốc quá trình phát hiện và xử lý rủi ro bảo mật.

Các năng lực chính gồm:

- Ưu tiên lỗ hổng theo tác động kinh doanh.
- Xác minh khả năng bị khai thác.
- Hỗ trợ threat modeling theo mô hình STRIDE.
- Quét pull request.
- Đề xuất sửa lỗi ngay trong workflow của developer.

---

### Kiro cho iOS

Kiro có ứng dụng iOS native, cho phép developer làm việc với các session ngay trên điện thoại.

Developer có thể:

- Khởi tạo session.
- Theo dõi tiến trình.
- Điều hướng session.
- Xem diff.
- Duyệt thay đổi từ thiết bị di động.

---

### AWS DevOps Agent có năng lực quản lý release

AWS DevOps Agent được bổ sung khả năng quản lý release.

Agent có thể:

- Đánh giá mức độ sẵn sàng trước khi release.
- Chạy kiểm thử tự động.
- Kiểm thử trong môi trường giống production.

---

### AWS Transform Continuous Modernization

AWS Transform hỗ trợ phân tích repository liên tục để phát hiện và xử lý technical debt.

Công cụ này có thể:

- Phân tích codebase liên tục.
- Phát hiện technical debt.
- Ưu tiên các vấn đề cần xử lý.
- Tự tạo pull request để sửa lỗi.

---

### Amazon S3 Annotations

Amazon S3 Annotations cho phép gắn metadata và ngữ cảnh phong phú trực tiếp vào object.

Điều này hữu ích cho:

- AI agent.
- Workflow tự động.
- Các hệ thống cần hiểu dữ liệu ở quy mô lớn.

---

## 2. Vấn đề được đặt ra

Các doanh nghiệp muốn ứng dụng AI agent nhưng vẫn gặp nhiều rào cản:

- Dữ liệu nằm rải rác trong nhiều hệ thống, khó đưa vào AI một cách chính xác.
- AI agent cần thông tin mới từ web nhưng vẫn phải đảm bảo bảo mật và có trích dẫn nguồn.
- Khi agent ngày càng mạnh hơn, rủi ro về kiểm soát, quyền truy cập và governance cũng tăng lên.
- Bảo mật phần mềm hiện nay còn chậm so với tốc độ phát triển và release.
- Technical debt tích tụ trong codebase, nhưng việc phân tích và sửa lỗi thường mất nhiều tuần.
- Nội dung số bị AI bot truy cập, nhưng chủ sở hữu nội dung khó kiểm soát hoặc thu phí.
- Metadata dữ liệu cho AI thường phải quản lý bằng hệ thống riêng, gây phức tạp.

---

## 3. Giải pháp AWS đưa ra

AWS đưa ra một nhóm giải pháp xoay quanh tự động hóa bằng AI, bao gồm:

- **Bedrock AgentCore**: Xây dựng và vận hành AI agent có kiểm soát.
- **Managed Knowledge Base + Web Search**: Giúp agent truy cập tri thức doanh nghiệp và web đáng tin cậy.
- **AWS WAF AI Traffic Monetization**: Giúp chủ nội dung kiểm soát và thu phí AI bot.
- **AWS Continuum / Security Agent**: Phát hiện, ưu tiên và hỗ trợ sửa lỗi bảo mật nhanh hơn.
- **DevOps Agent**: Đánh giá release và kiểm thử trước production.
- **AWS Transform**: Phát hiện và giảm technical debt tự động.
- **S3 Annotations**: Bổ sung ngữ cảnh cho dữ liệu phục vụ AI agent và workflow tự động.

---

## 4. Kết luận

Các công bố tại AWS Summit New York 2026 cho thấy AWS đang tập trung mạnh vào việc đưa AI agent vào môi trường doanh nghiệp thực tế.

Không chỉ dừng lại ở việc tạo chatbot hay trợ lý AI đơn giản, AWS muốn cung cấp một hệ sinh thái đầy đủ để doanh nghiệp có thể:

- Kết nối agent với dữ liệu nội bộ.
- Cho agent truy cập web một cách an toàn.
- Quản lý quyền truy cập và governance.
- Tự động hóa bảo mật phần mềm.
- Giảm technical debt.
- Tối ưu quy trình release.
- Quản lý metadata dữ liệu ở quy mô lớn.

Điều này cho thấy AI agent đang dần trở thành một phần quan trọng trong hạ tầng công nghệ doanh nghiệp hiện đại.

---

## Tài liệu tham khảo

[AWS News Blog - Top announcements of the AWS Summit in New York, 2026](https://aws.amazon.com/blogs/aws/top-announcements-of-the-aws-summit-in-new-york-2026/)

[link bài blog](https://www.facebook.com/share/p/1JZGyMeqEd/)