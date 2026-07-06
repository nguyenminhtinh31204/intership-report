---
title: "Tạo API Gateway (GET)"
weight: 504
chapter: false
pre: " <b> 5.4 </b> "
---

#### Tổng quan

Phần này hướng dẫn bạn tạo REST API tên **GetInvoiceAPI** với các route để truy vấn và cập nhật dữ liệu hóa đơn. Mỗi route được kết nối với Lambda và bật CORS, sau đó deploy với stage dev.

---

#### Bước 1: Tạo REST API

1. Đăng nhập vào AWS Management Console, tìm và truy cập **API Gateway**.

![Open API Gateway](/images/5-Workshop/5.4-configure-api-gateway-upload/001-openapigateway.png)

2. Nhấn **Create an API**.

![Create API](/images/5-Workshop/5.4-configure-api-gateway-upload/002-createapi.png)

3. Chọn loại **REST API**, sau đó nhấn **Build**.

![Build REST API](/images/5-Workshop/5.4-configure-api-gateway-upload/003-buildrestapi.png)

4. Trong phần cấu hình:

    - **API name**: `GetInvoiceAPI`
    - **Description**: `Post Invoice File by API Gateway`
    - **Endpoint Type**: chọn **Regional**.

![API Details](/images/5-Workshop/5.4-configure-api-gateway-upload/004-apidetails.png)

5. Nhấn **Create API** để hoàn tất.

![Create API](/images/5-Workshop/5.4-configure-api-gateway-upload/005-createapi.png)

---

#### Bước 2: Tạo các Resource & Method

##### Resource: /invoice

1.  Trong API **GetInvoiceAPI**, chọn **Create resource**.

![Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/006-createresource.png)

2.  Nhập thông tin:

    -   **Resource path**: `/`
    -   **Resource name**: `invoice`

3.  Nhấn **Create resource**.

![Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/006-createresource.png)

4.  Sau khi resource **`/invoice`** được tạo, chọn lại nó trong cây tài nguyên.

![resource /invoice](/images/5-Workshop/5.4-configure-api-gateway-upload/007-resourceinvoice.png)

5.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/008-createmethod.png)

6.  Cấu hình trong phần **Create method**:

    -   **Method type**: GET.
    -   **Integration type**: Lambda function.
    -   **Lambda proxy integration**: Bật.
    -   **Lambda function**: FetchInvoiceDetailsFunction.

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/09-configuration.png)

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/010-configuration.png)

7.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/011-createmethod.png)

8.  API Gateway sẽ được tạo và chuyển đến trang cấu hình chi tiết của API Gateway.

![Configuration details](/images/5-Workshop/5.4-configure-api-gateway-upload/012-configurationdetails.png)

##### Resource: /invoice/{id}

1.  Trong cây tài nguyên, chọn resource **`/invoice`**.

![resource /invoice](/images/5-Workshop/5.4-configure-api-gateway-upload/013-resourceinvoice.png)

2.  Nhấn **Create resource**.

![Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/014-createresource.png)

3.  Nhập thông tin:

    -   **Resource path**: `/invoice/`
    -   **Resource name**: `{id}`

4.  Nhấn **Create resource**.

![Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/015-createresource.png)

5.  Sau khi resource **`/invoice/{id}`** được tạo, chọn lại nó trong cây tài nguyên.

![Resource /invoice/{id}](/images/5-Workshop/5.4-configure-api-gateway-upload/016-resource-invoice-id.png)

6.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/017-create-method.png)

7.  Cấu hình trong phần **Create method**:

    -   **Method type**: GET.
    -   **Integration type**: Lambda function.
    -   **Lambda proxy integration**: Bật.
    -   **Lambda function**: FetchInvoiceDetailsFunction.

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/018-configuration.png)

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/019-configuration.png)

8.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/011-createmethod.png)

9.  Tiếp tục thêm method **PATCH**.

    -   Chọn lại nó trong cây tài nguyên và nhấn **Create method**.

![Choose resource & click create method](/images/5-Workshop/5.4-configure-api-gateway-upload/020-resource-and-createmethod.png)

-   Thực hiện cấu hình tương tự như trên:

    -   **Method type**: PATCH
    -   **Integration type**: Lambda Function
    -   **Use Lambda Proxy integration**: Bật
    -   **Lambda Function**: FetchInvoiceDetailsFunction

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/021-configuration.png)

10. Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/011-createmethod.png)

##### Resource: /invoice/starred

1.  Trong API **GetInvoiceAPI**, chọn resource **`/invoice`**.

![resource /invoice](/images/5-Workshop/5.4-configure-api-gateway-upload/022-resourceinvoice.png)

2.  Nhấn **Create resource**.

![Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/023-createresource.png)

3.  Cấu hình:

    -   **Resource path**: `/invoice/`
    -   **Resource name**: `starred`

4.  Nhấn **Create resource**.

![Configuration & Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/024-configuration-createresource.png)

5.  Sau khi resource được tạo, chọn lại **`/invoice/starred`** trong cây tài nguyên.

![Resource /invoice/starred](/images/5-Workshop/5.4-configure-api-gateway-upload/025-resource-invoice-starred.png)

6.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/026-createmethod.png)

7.  Cấu hình trong phần **Create method**:

    -   **Method type**: GET.
    -   **Integration type**: Lambda function.
    -   **Lambda proxy integration**: Bật.
    -   **Lambda function**: FetchInvoiceDetailsFunction.

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/027-configuration.png)

8.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/011-createmethod.png)

##### Resource: /invoice/starred/{id}

1.  Trong API **GetInvoiceAPI**, chọn resource **`/invoice/starred`**.

![Resource /invoice/starred](/images/5-Workshop/5.4-configure-api-gateway-upload/028-resource-invoice-starred.png)

2.  Nhấn **Create resource**.

![Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/029-createresource.png)

3.  Cấu hình:

    -   **Resource path**: `/invoice/starred/`
    -   **Resource name**: `{id}`

4.  Nhấn **Create resource**.

![Configuration & Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/030-configuration-createresource.png)

5.  Sau khi resource được tạo, chọn lại **`/invoice/starred/{id}`** trong cây tài nguyên.
6.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/031-createmethod.png)

7.  Cấu hình trong phần **Create method**:

    -   **Method type**: PATCH.
    -   **Integration type**: Lambda function.
    -   **Lambda proxy integration**: Bật.
    -   **Lambda function**: FetchInvoiceDetailsFunction.

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/032-configuration.png)

8.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/011-createmethod.png)

##### Resource: /invoice/tags

1.  Trong API **GetInvoiceAPI**, chọn resource **`/invoice`**.

![Resource /invoice](/images/5-Workshop/5.4-configure-api-gateway-upload/033-resource-invoice.png)

2.  Nhấn **Create resource**.

![Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/034-createresource.png)

3.  Cấu hình:

    -   **Resource path**: `/invoice/`
    -   **Resource name**: `tags`

4.  Nhấn **Create resource**.

![Configuration & Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/035-configuration-createresource.png)

##### Resource: /invoice/tags/{id}

1.  Trong cây tài nguyên, chọn lại **`/invoice/tags`**.
2.  Nhấn **Create resource**.

![Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/036-createresource.png)

3.  Cấu hình:

    -   **Resource path**: `/invoice/tags/`
    -   **Resource name**: `{id}`

4.  Nhấn **Create resource**.

![Configuration & Create resource](/images/5-Workshop/5.4-configure-api-gateway-upload/037-configuration-createresource.png)

5.  Sau khi resource được tạo, chọn lại **`/invoice/tags/{id}`** trong cây tài nguyên.
6.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/038-createmethod.png)

7.  Cấu hình trong phần **Create method**:

    -   **Method type**: PATCH.
    -   **Integration type**: Lambda function.
    -   **Lambda proxy integration**: Bật.
    -   **Lambda function**: FetchInvoiceDetailsFunction.

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/032-configuration.png)

8.  Nhấn **Create method**.

![Create method](/images/5-Workshop/5.4-configure-api-gateway-upload/011-createmethod.png)

#### Bước 3: Bật CORS cho các method

1.  Trong cây tài nguyên của API **GetInvoiceAPI**, chọn resource **`/invoice/{id}`**.
2.  Nhấn **Enable CORS**.

![Enable CORS](/images/5-Workshop/5.4-configure-api-gateway-upload/039-enable-cors.png)

3.  Tại **Access-Control-Allow-Methods**, bật CORS cho:

    -   GET
    -   PATCH

4.  Nhấn **Save**.

![Save CORS](/images/5-Workshop/5.4-configure-api-gateway-upload/040-save-cors.png)

5.  Lặp lại các bước trên cho từng resource còn lại:

    -   **/invoice/starred/{id}**: bật CORS cho `PATCH`
    -   **/invoice/tags/{id}**: bật CORS cho `PATCH`

![Result](/images/5-Workshop/5.4-configure-api-gateway-upload/041-result-cors.png)

![Result](/images/5-Workshop/5.4-configure-api-gateway-upload/042-result-cors.png)

#### Bước 4: Deploy API

1. Nhấn **Deploy API**.

![Deploy API](/images/5-Workshop/5.4-configure-api-gateway-upload/043-deploy-api.png)

2. Trong modal **Deploy API**:

    - Stage: **[New Stage]**.
    - Stage name: `dev`.
    - Deployment description: `Test API Method GET`.
    - Nhấn **Deploy**.

![New stage](/images/5-Workshop/5.4-configure-api-gateway-upload/044-newstage.png)

![Configuration](/images/5-Workshop/5.4-configure-api-gateway-upload/045-configuration.png)
