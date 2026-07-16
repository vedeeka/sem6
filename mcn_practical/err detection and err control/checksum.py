def checksum(data, size):
    words = []

    while len(data) % size != 0:
        data += "0"

    for i in range(0, len(data), size):
        words.append(data[i:i+size])

    total = 0
    for word in words:
        total += int(word, 2)
        if total >= 2**size:
            total = (total - 2**size) + 1

    checksum = ""
    binary = bin(total)[2:].zfill(size)

    for bit in binary:
        if bit == "0":
            checksum += "1"
        else:
            checksum += "0"

    transmitted = "".join(words) + checksum

    print("Words      :", words)
    print("Checksum   :", checksum)
    print("Transmitted:", transmitted)

data = input("Enter data bits: ")
size = int(input("Enter word size: "))

checksum(data, size)