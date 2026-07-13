#no need for this if u give input in correct format
def normalize_bits(bit_string):
    bit_string = bit_string.strip().replace(" ", "")
    if not bit_string or any(ch not in "01" for ch in bit_string):
        raise ValueError("Input must contain only 0 and 1.")
    return bit_string


#no need for this also if u want formating then only its good to use
def group_bits(bit_string, size=8):
    return " ".join(bit_string[i : i + size] for i in range(0, len(bit_string), size))

def parity_bit_method(data, parity_type="even"):
    data = normalize_bits(data)
    ones_count = data.count("1")
    
    if parity_type == "even":
        parity = "0" if ones_count % 2 == 0 else "1"
    else:
        parity = "1" if ones_count % 2 == 0 else "0"
        
    return parity, data + parity

# Execution with User Input
if __name__ == "__main__":
    print("--- Test Parity Bit Method ---")
    user_data = input("Enter data bits (e.g., 1011001): ")
    user_type = input("Enter parity type (even/odd) [even]: ").strip().lower() or "even"
    
    p_bit, tx_data = parity_bit_method(user_data, user_type)
    print(f"Calculated Parity Bit: {p_bit}")
    print(f"Transmitted Data     : {group_bits(tx_data)}")
    print(f"Transmitted Data     : {tx_data}") 