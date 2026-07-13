from parity import normalize_bits, group_bits

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
        folded = (raw_sum & mask) + (raw_sum >> word_size)
        while folded > mask:
            folded = (folded & mask) + (folded >> word_size)
            
        steps.append((idx, format(running_total, f"0{word_size}b"), word, format(raw_sum, f"0{word_size+1}b"), format(folded, f"0{word_size}b")))
        running_total = folded
        
    checksum_bits = format((~running_total) & mask, f"0{word_size}b")
    return data, pad_len, words, steps, format(running_total, f"0{word_size}b"), checksum_bits, data + checksum_bits

# Execution with User Input
if __name__ == "__main__":
    print("--- Test Checksum Method ---")
    user_data = input("Enter data bits (e.g., 1001100111100010): ")
    user_wsize = int(input("Enter segment word size [8]: ").strip() or 8)
    
    pad_d, pad_l, words, steps, final_sum, chk, tx = checksum_ones_complement(user_data, user_wsize)
    print(f"\nDivided Words   : {words}")
    print("Steps Calculation:")
    for step in steps:
        print(f" Word {step[0]}: {step[1]} + {step[2]} = {step[3]} -> folded: {step[4]}")
    print(f"Checksum Bits   : {chk}")
    print(f"Transmitted Bits: {group_bits(tx, user_wsize)}")