---
title: "Create DynamoDB Table"
weight: 502
chapter: false
pre: " <b> 5.2 </b> "
---

#### Overview

In this step, you will create a **DynamoDB Table** to store invoice information after it is processed by the Lambda function. The table will use **on-demand** mode and have 2 additional **Global Secondary Indexes (GSIs)** to support queries by customer name and starred invoices.

---

#### Step 1: Access DynamoDB Console

1. Log in to [AWS Console](https://console.aws.amazon.com/), search for **DynamoDB**, then select **DynamoDB** in the results.

![Open DynamoDB](/images/5-Workshop/5.2-create-dynamodb-table/001-opendynamodb.png)

{{% notice info %}}
💡 **Note:** Before clicking **Create table**, make sure you have selected the correct **region as ap-southeast-1(Singapore)** in the upper right corner of the AWS Console screen.

{{% /notice %}}

2. Click **Create table** to start creating a new table.

![Create Table](/images/5-Workshop/5.2-create-dynamodb-table/002-createtable.png)

---

#### Step 2: Configure DynamoDB table

1. **Table name**: `InvoiceData`

2. **Partition key**:

-   **Name**: `InvoiceId`
-   **Type**: `String`

3. Skip the **Sort key** section (not necessary).

![Table Key](/images/5-Workshop/5.2-create-dynamodb-table/003-tablekeys.png)

4. In the **Table settings** section, Select **Default settings** to switch to **On-demand capacity** mode.

![Billing Mode](/images/5-Workshop/5.2-create-dynamodb-table/004-ondemand.png)

5. Click **Create table** to finish.

![Create Table](/images/5-Workshop/5.2-create-dynamodb-table/005-finishcreate.png)

---

#### Step 3: Add Global Secondary Index (GSI)

Once the **InvoiceData** table is successfully created, you will add two secondary indexes:

---

##### GSI #1: CustomerName-index

1. In the table details page, select the **Indexes** tab.

![Create Index](/images/5-Workshop/5.2-create-dynamodb-table/006-indexes.png)

2. Click **Create index**.

![Create Index](/images/5-Workshop/5.2-create-dynamodb-table/007-createindex.png)

3. Configuration:

-   **Partition key**: `CustomerName`
-   **Data type**: String
-   **Sort key**: _(leave blank)_
-   **Projected attributes**: select **All**

![GSI 1](/images/5-Workshop/5.2-create-dynamodb-table/008-gsi1.png)

![GSI 1](/images/5-Workshop/5.2-create-dynamodb-table/009-gsi1.png)

4. Click **Create index**.

![GSI 1](/images/5-Workshop/5.2-create-dynamodb-table/010-gsi1.png)

---

##### GSI #2: StarredInvoicesIndex

1. Click **Create index** again to create the second GSI.

![GSI 2](/images/5-Workshop/5.2-create-dynamodb-table/011-gsi2.png)

2. Configuration:

-   **Partition key**: `IsStarred` (type **String**)
-   **Sort key**: `CreatedAt` (type **String**)
-   **Index name**: `StarredInvoicesIndex`
-   **Projected attributes**: select **All**

![GSI 2](/images/5-Workshop/5.2-create-dynamodb-table/012-gsi2.png)

![GSI 2](/images/5-Workshop/5.2-create-dynamodb-table/013-gsi2.png)

3. Click **Create index**.

![GSI 2](/images/5-Workshop/5.2-create-dynamodb-table/014-gsi2.png)

4. Make sure both GSIs **CustomerName-index** and **StarredInvoicesIndex** are in **ACTIVE** status before continuing with Lambda function configuration.

![Check GSI Status](/images/5-Workshop/5.2-create-dynamodb-table/015-gsistatus.png)

{{% notice warning %}}
⚠️ If the GSI status is still **Creating**, you need to wait a few minutes until it changes to **Active** before making a query or deploying a Lambda to access the GSI.
{{% /notice %}}
