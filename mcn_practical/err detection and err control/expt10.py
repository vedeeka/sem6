import math

# --- HELPER FUNCTIONS ---
def normalize_bits(bit_string):
    bit_string = bit_string.strip().replace(" ", "")
    if not bit_string or any(ch not in "01" for ch in bit_string):
        raise ValueError("Input must contain only 0 and 1.")
    return bit_string

def group_bits(bit_string, size=8):
    return " ".join(bit_string[i : i + size] for i in range(0, len(bit_string), size))


# --- 1. PARITY METHOD ---
def parity_bit_method(data, parity_type="even"):
    data = normalize_bits(data)
    ones_count = data.count("1")
    
    # Even parity wants an even number of 1s; Odd parity wants an odd number of 1s
    if parity_type == "even":
        parity = "0" if ones_count % 2 == 0 else "1"
    else:
        parity = "1" if ones_count % 2 == 0 else "0"
        
    return parity, data + parity


# --- 2. BLOCK PARITY (2D PARITY) ---
def block_parity_method(data, cols=8):
    data = normalize_bits(data)
    pad_len = (cols - (len(data) % cols)) % cols
    padded_data = data + ("0" * pad_len)
    
    # Break down the padded data into rows
    rows = [list(padded_data[i : i + cols]) for i in range(0, len(padded_data), cols)]
    
    # Calculate row parity bits
    for row in rows:
        row_parity = str(sum(int(bit) for bit in row) % 2)
        row.append(row_parity)
        
    # Calculate column parity bits
    col_count = cols + 1
    col_parity_row = []
    for c in range(col_count):
        col_sum = sum(int(rows[r][c]) for r in range(len(rows)))
        col_parity_row.append(str(col_sum % 2))
        
    # Format the matrix layout string for clean displaying
    matrix_display = "\n".join(" ".join(row) for row in rows)
    matrix_display += "\n" + "-" * (2 * col_count - 1) + "\n" + " ".join(col_parity_row)
    
    transmitted_stream = "".join("".join(row) for row in rows) + "".join(col_parity_row)
    return padded_data, pad_len, matrix_display, transmitted_stream, col_count


# --- 3. CYCLIC REDUNDANCY CHECK (CRC) ---
def crc_remainder(data, poly):
    data, poly = normalize_bits(data), normalize_bits(poly)
    degree = len(poly) - 1
    working_bits = list(data + ("0" * degree))
    
    # Modulo-2 binary division using XOR operations
    for i in range(len(data)):
        if working_bits[i] == "1":
            for j in range(len(poly)):
                working_bits[i + j] = "0" if working_bits[i + j] == poly[j] else "1"
                
    remainder = "".join(working_bits[-degree:])
    return remainder, data + remainder


# --- 4. CHECKSUM (ONE'S COMPLEMENT) ---
def checksum_ones_complement(data, word_size=16):
    data = normalize_bits(data)
    pad_len = (word_size - (len(data) % word_size)) % word_size
    data += "0" * pad_len
    
    mask = (1 << word_size) - 1
    words = [data[i : i + word_size] for i in range(0, len(data), word_size)]
    
    running_total = 0
    steps = []
    for idx, word in enumerate(words, start=1):
        raw_sum = running_total + int(word, 2)
        # Fold the carry bit (One's complement addition step)
        folded = (raw_sum & mask) + (raw_sum >> word_size)
        while folded > mask:
            folded = (folded & mask) + (folded >> word_size)
            
        steps.append((idx, format(running_total, f"0{word_size}b"), word, format(raw_sum, f"0{word_size+1}b"), format(folded, f"0{word_size}b")))
        running_total = folded
        
    checksum_bits = format((~running_total) & mask, f"0{word_size}b")
    return data, pad_len, words, steps, format(running_total, f"0{word_size}b"), checksum_bits, data + checksum_bits


# --- 5. HAMMING CODE ---
def hamming_encode(data):
    data = normalize_bits(data)
    m = len(data)
    
    # Calculate required number of parity bits: 2^r >= m + r + 1
    r = 0
    while 2**r < (m + r + 1):
        r += 1
        
    n = m + r
    code = ["0"] * (n + 1)
    
    # Place data bits skipping power-of-2 positions
    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:  # Not a power of 2
            code[i] = data[j]
            j += 1
            
    # Calculate parity values
    for i in range(r):
        p = 2**i
        parity_val = sum(int(code[k]) for k in range(1, n + 1) if k & p) % 2
        code[p] = str(parity_val)
        
    return "".join(code[1:])

def hamming_detect_correct(codeword):
    codeword = normalize_bits(codeword)
    n = len(codeword)
    code = ["0"] + list(codeword)
    
    r = 0
    while 2**r <= n:
        r += 1
        
    # Recalculate parity to pinpoint error position (Syndrome calculation)
    error_pos = 0
    for i in range(r):
        p = 2**i
        if sum(int(code[k]) for k in range(1, n + 1) if k & p) % 2 != 0:
            error_pos += p
            
    # Correct error if found
    if 1 <= error_pos <= n:
        code[error_pos] = "1" if code[error_pos] == "0" else "0"
        
    return error_pos, "".join(code[1:])


# --- 6. REED-SOLOMON CODE ---
def reed_solomon_demo(text, nsym=8):
    import reedsolo
    codec = reedsolo.RSCodec(nsym)
    encoded = codec.encode(text.encode("utf-8"))
    decoded = codec.decode(encoded)
    decoded_bytes = decoded[0] if isinstance(decoded, tuple) else decoded
    return encoded, decoded_bytes.decode("utf-8")


# --- MAIN MENU USER INTERFACE ---
def main():
    crc_polys = {"8": "100000111", "16": "11000000000000101", "32": "100000100110000010001110110110111"}
    
    while True:
        print("\n=== Experiment 10: Error Detection/Correction ===")
        print("1. Parity Bit      2. 2D Block Parity  3. CRC")
        print("4. Checksum        5. Hamming Code     6. Reed-Solomon")
        print("7. Exit")
        
        choice = input("Enter choice (1-7): ").strip()
        if choice == "7":
            print("Exiting...")
            break
            
        try:
            if choice == "1":
                bits = input("Enter data bits: ")
                ptype = input("Parity type (even/odd) [even]: ").strip().lower() or "even"
                parity, tx = parity_bit_method(bits, ptype)
                print(f"Data Bits   : {group_bits(normalize_bits(bits))}\nParity Bit  : {parity}\nTransmitted : {group_bits(tx)}")
                
            elif choice == "2":
                bits = input("Enter data bits: ")
                cols = int(input("Columns per row [8]: ").strip() or 8)
                pad_d, pad_l, disp, tx, g_size = block_parity_method(bits, cols)
                print(f"Padded Data : {group_bits(pad_d)}\nPad Added   : {pad_l}\n\nMatrix Layout:\n{disp}\n\nTransmitted : {group_bits(tx, g_size)}")
                
            elif choice == "3":
                bits = input("Enter data bits: ")
                ctype = input("CRC type (8/16/32): ").strip()
                if ctype not in crc_polys: raise ValueError("Invalid CRC type choice.")
                rem, cw = crc_remainder(bits, crc_polys[ctype])
                print(f"Data Bits   : {group_bits(normalize_bits(bits))}\nGenerator   : {crc_polys[ctype]}\nRemainder   : {rem}\nTransmitted : {group_bits(cw)}")
                
            elif choice == "4":
                bits = input("Enter data bits: ")
                w_size = int(input("Word size [16]: ").strip() or 16)
                pad_d, pad_l, words, steps, raw_sum, chk, tx = checksum_ones_complement(bits, w_size)
                print(f"Padded Data : {group_bits(pad_d, w_size)}\nPad Added   : {pad_l}\nWords       : {words}\n\nSteps:")
                for step in steps:
                    print(f" Step {step[0]}: {step[1]} + {step[2]} = {step[3]} -> fold = {step[4]}")
                print(f"Final Sum   : {raw_sum}\nChecksum    : {chk}\nTransmitted : {group_bits(tx, w_size)}")
                
            elif choice == "5":
                bits = input("Enter data bits: ")
                encoded = hamming_encode(bits)
                print(f"Data Bits   : {normalize_bits(bits)}\nEncoded CW  : {encoded}")
                if input("Test error correction? (y/n): ").strip().lower() == "y":
                    recv = input("Enter received codeword: ")
                    pos, corrected = hamming_detect_correct(recv)
                    print(f"Error at Position: {pos}\nCorrected Code   : {corrected}" if pos else "No single-bit error detected.")
                    
            elif choice == "6":
                text = input("Enter text: ")
                nsym = int(input("Parity symbols [8]: ").strip() or 8)
                enc, dec = reed_solomon_demo(text, nsym)
                print(f"Original Text  : {text}\nEncoded Bytes  : {list(enc)}\nDecoded Text   : {dec}")
                
            else:
                print("Invalid choice. Try again.")
        except Exception as exc:
            print(f"Error: {exc}")

if __name__ == "__main__":
    main()