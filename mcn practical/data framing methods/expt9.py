# Framing Methods

def character_count(data, frame_size):
    if frame_size <= 1:
        raise ValueError("Frame size must be greater than 1")
    payload = frame_size - 1
    frames = []
    for i in range(0, len(data), payload):
        part = data[i:i + payload]
        frames.append(str(len(part) + 1) + part)
    return frames


def byte_stuffing(data):
    stuffed = ""
    i = 0
    while i < len(data):
        if data[i:i+4] == "FLAG":
            stuffed += "ESCFLAG"
            i += 4
        elif data[i:i+3] == "ESC":
            stuffed += "ESCESC"
            i += 3
        else:
            stuffed += data[i]
            i += 1
    return "FLAG " + stuffed + " FLAG"


def bit_stuffing(bits):
    if any(b not in "01" for b in bits):
        raise ValueError("Enter only 0 and 1")

    FLAG = "01111110"
    stuffed = ""
    count = 0

    for b in bits:
        stuffed += b
        if b == "1":
            count += 1
            if count == 5:
                stuffed += "0"
                count = 0
        else:
            count = 0

    return f"{FLAG} {stuffed} {FLAG}"


def physical_layer_violation(bits):
    if any(b not in "01" for b in bits):
        raise ValueError("Enter only 0 and 1")

    return f"VV {bits} VV"


def main():
    while True:
        print("\n=== Framing Methods ===")
        print("1. Character Count")
        print("2. Byte Stuffing")
        print("3. Bit Stuffing")
        print("4. Physical Layer Coding Violation")
        print("5. Exit")

        choice = input("Enter choice: ")

        try:
            if choice == "1":
                data = input("Enter data: ")
                size = int(input("Enter frame size: "))
                frames = character_count(data, size)

                print("\nFrames:")
                for i, frame in enumerate(frames, 1):
                    print(f"Frame {i}: {frame}")

            elif choice == "2":
                data = input("Enter data: ")
                print("\nByte Stuffed Frame:")
                print(byte_stuffing(data))

            elif choice == "3":
                bits = input("Enter binary data: ")
                print("\nBit Stuffed Frame:")
                print(bit_stuffing(bits))

            elif choice == "4":
                bits = input("Enter binary data: ")
                print("\nPhysical Layer Coding Violation Frame:")
                print(physical_layer_violation(bits))

            elif choice == "5":
                print("Program Exited")
                break

            else:
                print("Invalid Choice")

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()