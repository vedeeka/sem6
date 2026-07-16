def block_parity(data, cols):
    pad = (cols - len(data) % cols) % cols
    data += "0" * pad

    rows = []

    for i in range(0, len(data), cols):
        rows.append(list(data[i:i+cols]))

    # Row parity
    for row in rows:
        s = 0
        for bit in row:
            s += int(bit)
        row.append(str(s % 2))

    # Column parity
    col_parity = []
    for j in range(cols + 1):
        s = 0
        for row in rows:
            s += int(row[j])
        col_parity.append(str(s % 2))

    print("\nMatrix:")
    for row in rows:
        print(" ".join(row))
    print("-" * (2 * (cols + 1) - 1))
    print(" ".join(col_parity))

    transmitted = ""
    for row in rows:
        transmitted += "".join(row)
    transmitted += "".join(col_parity)

    print("\nTransmitted Stream:", transmitted)

bits = input("Enter data bits: ")
cols = int(input("Enter columns: "))

block_parity(bits, cols)