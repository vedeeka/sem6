

# 1. Character Count
def character_count(data, frame_size):
    payload_size = frame_size - 1
    frames = []
    for i in range(0, len(data), payload_size):
        payload = data[i:i + payload_size]
        count = len(payload) + 1
        frame = str(count) + payload
        frames.append(frame)
    return frames

# 2. Byte Stuffing
def byte_stuffing(data):
    FLAG = "FLAG"
    ESC = "ESC"
    stuffed = []
    for ch in data:
        if ch == 'F':
            stuffed.append("ESC")
            stuffed.append("F")
        elif ch == 'E':
            stuffed.append("ESC")
            stuffed.append("E")
        else:
            stuffed.append(ch)
    frame = ["FLAG"] + stuffed + ["FLAG"]
    return " ".join(frame)

# 3. Bit Stuffing
def bit_stuffing(bits):
    FLAG = "01111110"
    stuffed = ""
    count = 0
    for bit in bits:
        stuffed += bit
        if bit == '1':
            count += 1
            if count == 5:
                stuffed += '0'
                count = 0
        else:
            count = 0
    formatted_bits = " ".join(stuffed)
    return FLAG + "   " + formatted_bits + "   " + FLAG

# 4. Physical Layer Coding Violation
def physical_layer_violation(bits):
    START = "VV"
    END = "VV"
    formatted_bits = " ".join(bits)
    return START + "   " + formatted_bits + "   " + END

while True:
    print("\n1. Character Count")
    print("2. Byte Stuffing")
    print("3. Bit Stuffing")
    print("4. Physical Layer Coding Violation")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        data = input("Enter data: ")
        size = int(input("Enter frame size: "))
        frames = character_count(data, size)
        print("\nCharacter Count Frames:")
        for i, frame in enumerate(frames, start=1):
            print("Frame", i, ":", frame)
    elif choice == '2':
        data = input("Enter data: ")
        result = byte_stuffing(data)
        print("\nByte Stuffed Frame:")
        print(result)
    elif choice == '3':
        bits = input("Enter binary data: ")
        result = bit_stuffing(bits)
        print("\nBit Stuffed Frame:")
        print(result)
    elif choice == '4':
        bits = input("Enter binary data: ")
        result = physical_layer_violation(bits)
        print("\nPhysical Layer Coding Violation Frame:")
        print(result)
    elif choice == '5':
        print("Program Exited")
        break
    else:
        print("Invalid Choice")
