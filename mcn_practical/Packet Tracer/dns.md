

---

# What is DNS?

**DNS (Domain Name System)** converts a **domain name** into an **IP address**.

### Example

Without DNS

```
http://192.168.1.2
```

With DNS

```
http://www.google.com
```

Much easier to remember!

---

# What does DNS do?

Suppose you type

```
www.google.com
```

The PC asks the DNS server:

> "What is the IP address of www.google.com?"

The DNS server replies:

```
www.google.com → 142.250.xxx.xxx
```

Then the PC connects using that IP.

---

# Network Used

| Device | IP Address |
|---------|------------|
| Router | 192.168.1.1 |
| DNS Server | 192.168.1.2 |
| PC0 | 192.168.1.3 |
| PC1 | 192.168.1.4 |

Subnet Mask

```
255.255.255.0
```

DNS Server for all devices

```
192.168.1.2
```

:contentReference[oaicite:1]{index=1}

---

# Step 1: Configure the Server

Open

```
Server
→ Desktop
→ IP Configuration
```

Enter

```
IP Address : 192.168.1.2
Subnet Mask : 255.255.255.0
Default Gateway : 192.168.1.1
DNS Server : 192.168.1.2
```

---

# Step 2: Configure PC0

Desktop

```
IP Address : 192.168.1.3
Subnet Mask : 255.255.255.0
Default Gateway : 192.168.1.1
DNS Server : 192.168.1.2
```

---

# Step 3: Configure PC1

Desktop

```
IP Address : 192.168.1.4
Subnet Mask : 255.255.255.0
Default Gateway : 192.168.1.1
DNS Server : 192.168.1.2
```

---

# Step 4: Configure DNS Service

Open

```
Server
→ Services
→ DNS
```

Turn

```
DNS Service → ON
```

---

# Step 5: Add DNS Records

Fill the Name and Address fields.

Example

| Name | IP Address |
|------|------------|
| PC0 | 192.168.1.3 |
| PC1 | 192.168.1.4 |
| Server | 192.168.1.2 |

Click

```
Add
```

Repeat for every device.

Your DNS server now knows:

```
PC0 → 192.168.1.3

PC1 → 192.168.1.4

Server → 192.168.1.2
```

:contentReference[oaicite:2]{index=2}

---

# Step 6: Test DNS

Open

```
Desktop
→ Command Prompt
```

Instead of

```
ping 192.168.1.4
```

Type

```
ping PC1
```

If everything is correct,

```
Reply from 192.168.1.4
```

DNS has successfully converted the name into an IP address.

:contentReference[oaicite:3]{index=3}

---

# Commands to Remember

There are **NO CLI commands** for this experiment.

Everything is configured using the **GUI**.

```
Server
↓
Desktop
↓
IP Configuration
```

and

```
Server
↓
Services
↓
DNS
↓
Turn ON
↓
Add Name
↓
Add IP
```

---

# Important Concepts

### DNS

Converts

```
Name → IP Address
```

Example

```
PC1

↓

192.168.1.4
```

---

### DNS Record

A DNS Record is simply a mapping.

Example

```
PC0 → 192.168.1.3

PC1 → 192.168.1.4

Server → 192.168.1.2
```

---

### Why do we need DNS?

Without DNS

```
192.168.1.4
```

With DNS

```
PC1
```

Names are much easier to remember than IP addresses.

---

# Common Mistakes

### Ping using name doesn't work?

Check:

✔ DNS Service is ON

✔ DNS record is added

✔ Correct IP entered

✔ PC's DNS Server is

```
192.168.1.2
```

✔ Devices can ping each other using IP first.

:contentReference[oaicite:4]{index=4}

---

# Easy Exam Notes

- DNS = Domain Name System.
- Converts **Domain Name → IP Address**.
- Configure a **static IP** on the DNS server.
- Turn **DNS Service ON**.
- Add **Name + IP Address** records.
- Set every PC's **DNS Server** field to the DNS server's IP.
- Test using

```
ping PC1
```

instead of

```
ping 192.168.1.4
```

---

# 1-Minute Revision

```
Assign Static IPs
        ↓
Configure DNS Server
        ↓
Turn DNS ON
        ↓
Add Name + IP Records
        ↓
Set DNS Server on PCs
        ↓
Ping Using Hostname
        ↓
DNS Working ✅
```