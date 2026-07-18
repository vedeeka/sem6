

# What is Telnet?

**Telnet** allows you to **remotely access and configure** a router or switch using another computer.

Instead of sitting in front of the router/switch, you can manage it from a PC.

> **Note:** Telnet sends data in plain text (not secure). SSH is the secure alternative. :contentReference[oaicite:1]{index=1}

---

# Requirements

Before Telnet works, you need:

- Router/Switch must have an IP address.
- PC and Router/Switch must be in the same network.
- Configure a Telnet password.
- Configure an Enable password.

---

# Method 1: Configure Telnet on a Switch

## Step 1: Configure Enable Password

```bash
enable
configure terminal

enable password admin
```

### What it does

Allows access to **Privileged EXEC Mode (`#`)** after logging in.

---

## Step 2: Assign an IP Address to VLAN 1

```bash
interface vlan 1
ip address 10.0.0.20 255.0.0.0
no shutdown
exit
```

### What it does

Gives the switch an IP address so it can be accessed remotely.

---

## Step 3: Configure Telnet Password

```bash
line vty 0 15
password cisco
login
```

### Meaning

- `line vty 0 15` → Configure all Telnet lines.
- `password cisco` → Password used for Telnet.
- `login` → Enables password checking.

---

## Step 4: Configure the PC

```
IP Address : 10.0.0.10
Subnet Mask: 255.0.0.0
Gateway    : (Not required for same network)
```

---

## Step 5: Test

Open **Desktop → Command Prompt**

```
telnet 10.0.0.20
```

Enter:

```
Password: cisco
```

Then type

```
enable
```

Enter

```
Password: admin
```

You are now managing the switch remotely.

---

# Method 2: Configure Telnet on a Router

## Step 1: Configure Enable Password

```bash
enable
configure terminal

enable password admin
```

---

## Step 2: Configure Router IP

```bash
interface fa0/0
ip address 10.0.0.1 255.0.0.0
no shutdown
```

---

## Step 3: Configure Telnet Password

```bash
line vty 0 15
password cisco
login
```

---

## Step 4: Configure the PC

```
IP Address : 10.0.0.10
Subnet Mask: 255.0.0.0
Default Gateway : 10.0.0.1
```

---

## Step 5: Test

Command Prompt

```
telnet 10.0.0.1
```

Enter

```
Password: cisco
```

Then

```
enable
```

Password

```
admin
```

Now you can configure the router remotely.

---

# Commands to Remember

## Switch

```bash
enable
configure terminal

enable password admin

interface vlan 1
ip address 10.0.0.20 255.0.0.0
no shutdown

line vty 0 15
password cisco
login
```

---

## Router

```bash
enable
configure terminal

enable password admin

interface fa0/0
ip address 10.0.0.1 255.0.0.0
no shutdown

line vty 0 15
password cisco
login
```

---

# Important Concepts

### What is VTY?

**VTY (Virtual Terminal)** lines allow remote login using Telnet.

```
line vty 0 15
```

Means the device allows up to **16 remote Telnet sessions (0–15).** :contentReference[oaicite:2]{index=2}

---

### Why do we need an Enable Password?

There are **two passwords**:

### Telnet Password

```
password cisco
```

Used to log into the device.

---

### Enable Password

```
enable password admin
```

Used to enter **Privileged EXEC Mode (`#`)** after login.

---

# Troubleshooting

### Can't ping the router/switch?

✔ Check IP addresses.

✔ Check cables.

✔ Check interface status.

---

### Telnet doesn't connect?

Check:

```bash
line vty 0 15
password cisco
login
```

Without `login`, Telnet authentication won't work. :contentReference[oaicite:3]{index=3}

---

### Interface is down?

Use

```bash
no shutdown
```

---

# Easy Exam Notes

- Telnet = Remote management protocol.
- Device must have an IP address.
- Configure **Enable Password**.
- Configure **VTY Password**.
- Enable **login** on VTY lines.
- Use **telnet <IP Address>** from the PC.
- Telnet is **not secure** because passwords are sent in plain text; SSH is preferred for secure remote access. :contentReference[oaicite:4]{index=4}

---

# 1-Minute Revision

```
Configure IP
        ↓
Enable Password
        ↓
VTY Password
        ↓
login
        ↓
PC → Command Prompt
        ↓
telnet <IP>
        ↓
Password
        ↓
enable
        ↓
Remote Access Successful
```