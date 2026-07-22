Web Server Configuration 

## Step 1: Build the Network

-   Place the following devices:
    -   1 × Server-PT
    -   1 × 2960 Switch
    -   2 × PCs
-   Connect all devices to the switch using **Copper Straight-Through**
    cables.

------------------------------------------------------------------------

## Step 2: Configure the Server IP

1.  Click **Server**.
2.  Go to **Desktop → IP Configuration**.
3.  Select **Static**.
4.  Enter:
    -   **IP Address:** `192.168.1.10`
    -   **Subnet Mask:** `255.255.255.0`
    -   **Default Gateway:** `192.168.1.1`

------------------------------------------------------------------------

## Step 3: Configure PC IPs

Configure the PCs manually.

### PC0

-   IP Address: `192.168.1.2`
-   Subnet Mask: `255.255.255.0`
-   Default Gateway: `192.168.1.1`

### PC1

-   IP Address: `192.168.1.3`
-   Subnet Mask: `255.255.255.0`
-   Default Gateway: `192.168.1.1`

------------------------------------------------------------------------

## Step 4: Enable HTTP Service

1.  Click the **Server**.
2.  Open the **Services** tab.
3.  Select **HTTP**.
4.  Set **HTTP = On**.
5.  (Optional) Set **HTTPS = On**.

------------------------------------------------------------------------

## Step 5: Edit the Web Page

Select **index.html** and replace its contents with:

``` html
<html>
<head><title>My Web Server</title></head>
<body>
<h1>Welcome to My Network</h1>
<p>Web Server Configuration Successful</p>
</body>
</html>
```

Click **Save**.

------------------------------------------------------------------------

## Step 6: Test Connectivity

On **PC0**:

1.  Open **Desktop → Command Prompt**.
2.  Execute:

``` text
ping 192.168.1.10
```

Expected output:

``` text
Reply from 192.168.1.10: bytes=32 time<1ms TTL=128
```

------------------------------------------------------------------------

## Step 7: Test the Web Server

1.  Open **Desktop → Web Browser** on PC0.
2.  Enter:

``` text
http://192.168.1.10
```

3.  Click **Go**.

------------------------------------------------------------------------

## Expected Output

``` text
Welcome to My Network

Web Server Configuration Successful
```

------------------------------------------------------------------------

## Verification

-   Ping from the PC to the server is successful (0% packet loss).
-   The custom web page loads successfully in the browser.
