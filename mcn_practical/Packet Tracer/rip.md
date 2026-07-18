

# What is RIP?

**RIP (Routing Information Protocol)** is a **dynamic routing protocol**.

Instead of manually adding routes, routers **automatically share** their routing tables with each other.

---

# Why use RIP?

Without RIP

```
Router 1 ❌ doesn't know where Network 30.0.0.0 is.
```

With RIP

```
Router 1 ⇄ Router 2

Both routers exchange routing information automatically.
```

---

# Important Points

- RIP = Dynamic Routing Protocol
- Metric = **Hop Count**
- Maximum Hop Count = **15**
- Administrative Distance = **120**
- Routing updates are sent every **30 seconds**
- We generally use **RIPv2** because it supports subnet masks (classless routing). :contentReference[oaicite:1]{index=1}

---

# Network Used

```
PC1
 |
10.0.0.2
 |
R1
10.0.0.1
 |
20.0.0.1 -------- 20.0.0.2
        R1 ----- R2
                  |
               30.0.0.1
                  |
               30.0.0.2
                 PC2
```

---

# Step 1: Configure Router 1

```bash
enable
configure terminal

interface fa0/0
ip address 10.0.0.1 255.0.0.0
no shutdown

interface serial0/0/0
ip address 20.0.0.1 255.0.0.0
no shutdown
```

### What it does

- Gives IP to LAN interface.
- Gives IP to serial link.
- Turns both interfaces ON.

---

# Step 2: Configure Router 2

```bash
enable
configure terminal

interface fa0/0
ip address 30.0.0.1 255.0.0.0
no shutdown

interface serial0/0/0
ip address 20.0.0.2 255.0.0.0
no shutdown
```

---

# Step 3: Configure PCs

## PC1

```
IP Address : 10.0.0.2
Subnet Mask : 255.0.0.0
Gateway : 10.0.0.1
```

## PC2

```
IP Address : 30.0.0.2
Subnet Mask : 255.0.0.0
Gateway : 30.0.0.1
```

---

# Step 4: Configure RIP on Router 1

```bash
router rip
version 2

network 10.0.0.0
network 20.0.0.0
```

### Meaning

```
router rip
```

Starts RIP.

```
version 2
```

Uses RIPv2.

```
network
```

Advertises directly connected networks.

---

# Step 5: Configure RIP on Router 2

```bash
router rip
version 2

network 20.0.0.0
network 30.0.0.0
```

Router 2 now advertises:

- 20.0.0.0
- 30.0.0.0

---

# Step 6: Verify RIP

On Router 1

```bash
show ip route
```

Expected output

```
R 30.0.0.0
```

The letter **R** means:

```
Route learned through RIP
```

You can also type

```bash
show ip route rip
```

to display only RIP routes. :contentReference[oaicite:2]{index=2}

---

# Step 7: Test

From PC1

```
ping 30.0.0.2
```

✅ Ping should be successful.

---

# Commands to Remember

## Router 1

```bash
interface fa0/0
ip address 10.0.0.1 255.0.0.0
no shutdown

interface serial0/0/0
ip address 20.0.0.1 255.0.0.0
no shutdown

router rip
version 2
network 10.0.0.0
network 20.0.0.0
```

---

## Router 2

```bash
interface fa0/0
ip address 30.0.0.1 255.0.0.0
no shutdown

interface serial0/0/0
ip address 20.0.0.2 255.0.0.0
no shutdown

router rip
version 2
network 20.0.0.0
network 30.0.0.0
```

---

# Important Concepts

### Dynamic Routing

Routers automatically exchange routes.

---

### Hop Count

A **hop** is one router.

Example

```
PC1 → R1 → R2 → PC2
```

Hop Count = **1**

---

### RIPv2

Advantages

- Supports subnet masks
- Supports classless routing
- Uses multicast (224.0.0.9) for updates. :contentReference[oaicite:3]{index=3}

---

# Common Mistakes

### Can't ping?

✔ Check IP addresses.

✔ Check interfaces are ON (`no shutdown`).

✔ Check RIP network commands.

✔ Ensure both routers use

```bash
version 2
```

---

### RIP routes not showing?

Use

```bash
show ip route
```

or

```bash
show ip route rip
```

---

# Easy Exam Notes

- RIP = Routing Information Protocol
- Dynamic Routing
- Metric = Hop Count
- Maximum Hop Count = **15**
- Administrative Distance = **120**
- Updates every **30 seconds**
- Configure using:
  - `router rip`
  - `version 2`
  - `network`

---

# 1-Minute Revision

```
Configure IP Addresses
        ↓
Configure PCs
        ↓
router rip
        ↓
version 2
        ↓
network commands
        ↓
show ip route
        ↓
Ping Test
        ↓
RIP Working ✅
```
````
