from parity import normalize_bits

def hamming_encode(data):
    data = normalize_bits(data)
    m = len(data)

    r = 0
    while 2**r < (m + r + 1):
        r += 1

    n = m + r
    code = ["0"] * (n + 1)

    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            code[i] = data[j]
            j += 1

    for i in range(r):
        p = 2**i
        count = 0

        for k in range(1, n + 1):
            if k & p:
                count += int(code[k])

        parity_val = count % 2
        code[p] = str(parity_val)

    return "".join(code[1:])

def hamming_detect_correct(codeword):
    codeword = normalize_bits(codeword)
    n = len(codeword)
    code = ["0"] + list(codeword)

    r = 0
    while 2**r <= n:
        r += 1

    error_pos = 0

    for i in range(r):
        p = 2**i
        count = 0

        for k in range(1, n + 1):
            if k & p:
                count += int(code[k])

        if count % 2 != 0:
            error_pos += p

    if 1 <= error_pos <= n:
        if code[error_pos] == "0":
            code[error_pos] = "1"
        else:
            code[error_pos] = "0"

    return error_pos, "".join(code[1:])

# Execution with User Input
if __name__ == "__main__":
    print("--- Test Hamming Code Method ---")
    user_data = input("Enter original data bits (e.g., 1001): ")
    encoded_cw = hamming_encode(user_data)
    print(f"Generated Hamming Codeword: {encoded_cw}")
    
    print("\n--- Testing Error Correction ---")
    received_cw = input(f"Enter received codeword (Flip a bit to test!): ")
    err, corrected = hamming_detect_correct(received_cw)
    if err == 0:
        print("No error detected in codeword.")
    else:
        print(f"Single-bit error detected at position: {err}")
        print(f"Corrected Codeword Layout          : {corrected}")