import ipaddress
import math

def flsm():
    network = ipaddress.IPv4Network(input("Enter Network (Ex: 192.168.1.0/24): "), strict=False)
    n = int(input("Enter Number of Subnets: "))

    new_prefix = network.prefixlen + math.ceil(math.log2(n))

    print("\nFLSM Subnets\n")

    for i, subnet in enumerate(network.subnets(new_prefix=new_prefix), 1):
        if i > n:
            break

        print(f"Subnet {i}")
        print("Network   :", subnet.network_address)
        print("Broadcast :", subnet.broadcast_address)
        print("Mask      :", subnet.netmask)

        if subnet.num_addresses > 2:
            print("First Host:", subnet.network_address + 1)
            print("Last Host :", subnet.broadcast_address - 1)
            print("Hosts     :", subnet.num_addresses - 2)
        else:
            print("No usable hosts")
        print()


def vlsm():
    network = ipaddress.IPv4Network(input("Enter Base Network (Ex: 192.168.10.0/24): "), strict=False)
    n = int(input("Enter Number of Subnets: "))

    data = []

    for i in range(n):
        name = input(f"Subnet {i+1} Name: ")
        hosts = int(input("Required Hosts: "))
        data.append((name, hosts))

    data.sort(key=lambda x: x[1], reverse=True)

    current = int(network.network_address)

    print("\nVLSM Subnets\n")

    for name, hosts in data:
        bits = math.ceil(math.log2(hosts + 2))
        prefix = 32 - bits

        subnet = ipaddress.IPv4Network((current, prefix), strict=False)

        print(f"Subnet : {name}")
        print("Network   :", subnet.network_address)
        print("Broadcast :", subnet.broadcast_address)
        print("Mask      :", subnet.netmask)

        if subnet.num_addresses > 2:
            print("First Host:", subnet.network_address + 1)
            print("Last Host :", subnet.broadcast_address - 1)
            print("Hosts     :", subnet.num_addresses - 2)
        else:
            print("No usable hosts")
        print()

        current += subnet.num_addresses


while True:
    print("1. FLSM")
    print("2. VLSM")
    print("3. Exit")

    ch = input("Enter Choice: ")

    if ch == "1":
        flsm()
    elif ch == "2":
        vlsm()
    elif ch == "3":
        break
    else:
        print("Invalid Choice\n")