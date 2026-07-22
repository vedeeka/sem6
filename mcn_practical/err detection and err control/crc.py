def crc(data, pol):
    original = data
    m = len(data)
    n = len(pol)

    data += "0" * (n - 1)
    data = list(data)

    for i in range(m):
        if data[i] == "1":
            for j in range(n):
                if data[i + j] == pol[j]:
                    data[i + j] = "0"
                else:
                    data[i + j] = "1"

    rem = "".join(data[-(n - 1):])

    print("CRC:", rem)
    print("Codeword:", original + rem)

crc("1101011011", "100000111")