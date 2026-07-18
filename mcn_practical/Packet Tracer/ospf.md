

# What is OSPF?

**OSPF (Open Shortest Path First)** is a **dynamic routing protocol**.

It allows routers to **automatically exchange routing information** and always chooses the **shortest path** to the destination.

---

# Why use OSPF?

Without OSPF

```
Router 1 ❌ doesn't know where Network 30.0.0.0 is.
```

With OSPF

```
Router 1 ⇄ Router 2

Both routers automatically exchange routes.
```

---

# Important Points

- OSPF = Open Shortest Path First
- Dynamic Routing Protocol
- Metric = **Cost**
- Administrative Distance = **110**
- Uses **Area 0** as the backbone area.
- Uses multicast addresses:
  - **224.0.0.5**
  - **224.0.0.6**
- Routers exchange **Hello Packets** to become neighbors. :contentReference[oaicite:1]{index=1}

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
20.0.0.1 ------- 20.0.0.2
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

- Assigns IP addresses.
- Turns interfaces ON.

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

# Step 4: Configure OSPF on Router 1

```bash
router ospf 1

network 10.0.0.0 0.255.255.255 area 0
network 20.0.0.0 0.255.255.255 area 0
```

### Meaning

```
router ospf 1
```

Starts the OSPF process.

```
network
```

Advertises the connected networks.

```
area 0
```

Adds the networks to OSPF Area 0.

---

# Step 5: Configure OSPF on Router 2

```bash
router ospf 2

network 20.0.0.0 0.255.255.255 area 0
network 30.0.0.0 0.255.255.255 area 0
```

> **Note:** The **process ID (1 or 2)** can be different on each router, but the **Area ID must be the same** for neighboring routers. :contentReference[oaicite:2]{index=2}

---

# Step 6: Verify OSPF

Check if routers became neighbors.

```bash
show ip ospf neighbor
```

Expected:

```
Neighbor State = FULL
```

---

Check routing table

```bash
show ip route ospf
```

Expected

```
O 30.0.0.0
```

The letter **O** means

```
Route learned through OSPF.
```

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

router ospf 1

network 10.0.0.0 0.255.255.255 area 0
network 20.0.0.0 0.255.255.255 area 0
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

router ospf 2

network 20.0.0.0 0.255.255.255 area 0
network 30.0.0.0 0.255.255.255 area 0
```

---

# Important Concepts

### OSPF Neighbor

Routers first become **neighbors** before exchanging routes.

---

### Hello Packet

Used to discover neighboring routers.

---

### Area

An Area is a logical group of routers.

For basic Packet Tracer labs, use:

```
Area 0
```

---

### Wildcard Mask

OSPF uses a **Wildcard Mask**, not a subnet mask.

Example

```
Subnet Mask

255.0.0.0

↓

Wildcard Mask

0.255.255.255
```

---

### Cost

OSPF selects the route with the **lowest cost**.

Unlike RIP, OSPF **does not use hop count**. :contentReference[oaicite:3]{index=3}

---

# Common Mistakes

### Routers not becoming neighbors?

✔ Same Area ID

✔ Interfaces are ON (`no shutdown`)

✔ Correct IP addresses

✔ Correct network statements

---

### No OSPF routes?

Check

```bash
show ip ospf neighbor
```

Then

```bash
show ip route ospf
```

---

# Easy Exam Notes

- OSPF = Open Shortest Path First
- Dynamic Routing Protocol
- Metric = Cost
- Administrative Distance = **110**
- Backbone = **Area 0**
- Uses **Hello Packets**
- Uses multicast:
  - **224.0.0.5**
  - **224.0.0.6**
- Configure using:
  - `router ospf`
  - `network`
  - `area`

---

# 1-Minute Revision

```
Configure IP Addresses
        ↓
Configure PCs
        ↓
router ospf
        ↓
network + wildcard mask
        ↓
area 0
        ↓
show ip ospf neighbor
        ↓
show ip route ospf
        ↓
Ping Test
        ↓
OSPF Working ✅
```