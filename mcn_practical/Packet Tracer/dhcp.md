# Simple DHCP Notes (Packet Tracer)

## What is DHCP?

DHCP (Dynamic Host Configuration Protocol) automatically gives a
device: - IP Address - Subnet Mask - Default Gateway - DNS Server

Without DHCP, you must enter these manually.

------------------------------------------------------------------------

# Method 1: Router as DHCP Server

## Step 1: Configure the Router

``` bash
enable
configure terminal

interface fa0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit
```

**What this does** - Sets the router IP to `192.168.1.1` - Turns the
interface ON

------------------------------------------------------------------------

## Step 2: Reserve IP Addresses

``` bash
ip dhcp excluded-address 192.168.1.1 192.168.1.10
```

These IPs will NOT be given to PCs.

Example: - 192.168.1.1 → Router - 192.168.1.2 → Server - 192.168.1.5 →
Printer

------------------------------------------------------------------------

## Step 3: Create the DHCP Pool

``` bash
ip dhcp pool MY_LAN
network 192.168.1.0 255.255.255.0
default-router 192.168.1.1
dns-server 192.168.1.10
```

Meaning: - `ip dhcp pool` → Create a DHCP pool - `network` → Network for
clients - `default-router` → Gateway for clients - `dns-server` → DNS
for clients

------------------------------------------------------------------------

## Step 4: Get IP on PC

Desktop → IP Configuration → DHCP

The PC gets its IP automatically.

------------------------------------------------------------------------

## Step 5: Test

    ping <other_PC_IP>

------------------------------------------------------------------------

# Method 2: Server as DHCP Server

1.  Give the server a static IP.
2.  Open **Server → Services → DHCP**.
3.  Fill:
    -   Pool Name
    -   Gateway
    -   DNS
    -   Start IP
    -   Subnet Mask
4.  Click **Add**.
5.  Turn **DHCP ON**.
6.  On each PC choose **DHCP**.

------------------------------------------------------------------------

# Commands to Remember

``` bash
enable
configure terminal
interface fa0/0
ip address 192.168.1.1 255.255.255.0
no shutdown

ip dhcp excluded-address 192.168.1.1 192.168.1.10

ip dhcp pool MY_LAN
network 192.168.1.0 255.255.255.0
default-router 192.168.1.1
dns-server 192.168.1.10
```
