def crc(data, poly):
    n = len(poly) - 1
    data = list(data + "0" * n)

    for i in range(len(data) - n):
        if data[i] == "1":
            for j in range(len(poly)):
                if data[i + j] == poly[j]:
                    data[i + j] = "0"
                else:
                    data[i + j] = "1"

    rem = "".join(data[-n:])
    print("CRC :", rem)
    print("Sent:", "".join(data[:-n]) + rem)

data = input("Enter data bits: ")
poly = input("Enter generator polynomial: ")

crc(data, poly)