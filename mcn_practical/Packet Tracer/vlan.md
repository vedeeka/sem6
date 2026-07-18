

# What is a VLAN?

**VLAN (Virtual Local Area Network)** is a way to divide one physical network into multiple logical networks.

Example:

- VLAN 10 → Sales Department
- VLAN 20 → IT Department

Even though all PCs are connected to the same switch, they behave as if they are on different networks.

### Benefits
- Better Security
- Less Broadcast Traffic
- Easier Network Management

---

# Network Used

| VLAN | Name | Network |
|------|------|----------------|
| 10 | SALES | 192.168.1.0/24 |
| 20 | IT | 192.168.2.0/24 |

---

# Step 1: Create VLANs

```bash
enable
configure terminal

vlan 10
name SALES

vlan 20
name IT
```

### What these commands do

- `vlan 10` → Creates VLAN 10
- `name SALES` → Gives VLAN 10 the name SALES
- `vlan 20` → Creates VLAN 20
- `name IT` → Gives VLAN 20 the name IT

---

# Step 2: Assign Ports to VLANs

### VLAN 10

```bash
interface fa0/1
switchport mode access
switchport access vlan 10

interface fa0/2
switchport mode access
switchport access vlan 10
```

### VLAN 20

```bash
interface fa0/3
switchport mode access
switchport access vlan 20

interface fa0/4
switchport mode access
switchport access vlan 20
```

### Meaning

`switchport mode access`
- Makes the port connect to only one VLAN.

`switchport access vlan 10`
- Assigns the port to VLAN 10.

---

# Step 3: Configure Trunk Port

```bash
interface fa0/5
switchport mode trunk
```

### What is a Trunk?

A trunk carries traffic for **multiple VLANs**.

Usually used between:
- Switch ↔ Switch
- Switch ↔ Router

---

# Step 4: Assign IP Addresses

## VLAN 10

PC1

```
IP : 192.168.1.10
Mask : 255.255.255.0
Gateway : 192.168.1.1
```

PC2

```
IP : 192.168.1.20
Mask : 255.255.255.0
Gateway : 192.168.1.1
```

---

## VLAN 20

PC3

```
IP : 192.168.2.10
Mask : 255.255.255.0
Gateway : 192.168.2.1
```

PC4

```
IP : 192.168.2.20
Mask : 255.255.255.0
Gateway : 192.168.2.1
```

---

# Step 5: Test

### Same VLAN

```
PC1 → ping PC2
```

✅ Works

---

### Different VLAN

```
PC1 → ping PC3
```

❌ Doesn't work

Reason:
Inter-VLAN Routing is not configured yet. :contentReference[oaicite:1]{index=1}

---

# Step 6: Configure Router (Inter-VLAN Routing)

Enable the router interface.

```bash
enable
configure terminal

interface fa0/0
no shutdown
```

---

## Create Sub-interface for VLAN 10

```bash
interface fa0/0.10
encapsulation dot1q 10
ip address 192.168.1.1 255.255.255.0
```

---

## Create Sub-interface for VLAN 20

```bash
interface fa0/0.20
encapsulation dot1q 20
ip address 192.168.2.1 255.255.255.0
```

---

### Meaning

`fa0/0.10`
- Sub-interface for VLAN 10

`encapsulation dot1q 10`
- Connects this interface to VLAN 10

`ip address`
- Gateway for VLAN 10

Same for VLAN 20.

---

# Step 7: Test Again

```
PC1 → ping PC3
```

✅ Works

Now devices in different VLANs can communicate.

---

# Important Commands to Remember

## Create VLAN

```bash
vlan 10
name SALES

vlan 20
name IT
```

---

## Access Port

```bash
interface fa0/1
switchport mode access
switchport access vlan 10
```

---

## Trunk Port

```bash
interface fa0/5
switchport mode trunk
```

---

## Router Configuration

```bash
interface fa0/0
no shutdown

interface fa0/0.10
encapsulation dot1q 10
ip address 192.168.1.1 255.255.255.0

interface fa0/0.20
encapsulation dot1q 20
ip address 192.168.2.1 255.255.255.0
```

---

# Easy Exam Notes

- VLAN = Logical Network
- Access Port = One VLAN
- Trunk Port = Multiple VLANs
- Same VLAN → Communication works
- Different VLAN → Need Router
- Router-on-a-Stick = One router interface divided into multiple sub-interfaces
- `encapsulation dot1q` identifies the VLAN on each sub-interface. :contentReference[oaicite:2]{index=2}

---

# 1-Minute Revision

```
Create VLAN
↓
Assign Ports
↓
Configure Trunk
↓
Assign IPs
↓
Ping (Same VLAN ✔)
↓
Configure Router
↓
Ping (Different VLAN ✔)
```