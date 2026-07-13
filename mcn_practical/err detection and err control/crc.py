from parity import normalize_bits, group_bits

def crc_remainder(data, poly):
    data, poly = normalize_bits(data), normalize_bits(poly)
    degree = len(poly) - 1
    working_bits = list(data + ("0" * degree))
    
    for i in range(len(data)):
        if working_bits[i] == "1":
            for j in range(len(poly)):
                working_bits[i + j] = "0" if working_bits[i + j] == poly[j] else "1"
                
    remainder = "".join(working_bits[-degree:])
    return remainder, data + remainder

# Execution with User Input
if __name__ == "__main__":
    print("--- Test CRC Method ---")
    user_data = input("Enter data bits (e.g., 110100111): ")
    # CRC-8 Polynomial standard: 100000111
    user_poly = input("Enter generator polynomial [100000111]: ").strip() or "100000111"
    
    rem, codeword = crc_remainder(user_data, user_poly)
    print(f"CRC Remainder   : {rem}")
    print(f"Transmitted Bits: {group_bits(codeword)}")