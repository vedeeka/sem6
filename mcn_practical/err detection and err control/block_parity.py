from parity import normalize_bits, group_bits

def block_parity_method(data, cols=8):
    data = normalize_bits(data)
    pad_len = (cols - (len(data) % cols)) % cols
    padded_data = data + ("0" * pad_len)
    
    rows = [list(padded_data[i : i + cols]) for i in range(0, len(padded_data), cols)]
    
    for row in rows:
        row_parity = str(sum(int(bit) for bit in row) % 2)
        row.append(row_parity)
        
    col_count = cols + 1
    col_parity_row = []
    for c in range(col_count):
        col_sum = sum(int(rows[r][c]) for r in range(len(rows)))
        col_parity_row.append(str(col_sum % 2))
        
    matrix_display = "\n".join(" ".join(row) for row in rows)
    matrix_display += "\n" + "-" * (2 * col_count - 1) + "\n" + " ".join(col_parity_row)
    
    transmitted_stream = "".join("".join(row) for row in rows) + "".join(col_parity_row)
    return padded_data, pad_len, matrix_display, transmitted_stream, col_count

# Execution with User Input
if __name__ == "__main__":
    print("--- Test 2D Block Parity Method ---")
    user_data = input("Enter data bits (e.g., 110011101011): ")
    user_cols = int(input("Enter number of columns [4]: ").strip() or 4)
    
    pad_d, pad_l, disp, tx, g_size = block_parity_method(user_data, user_cols)
    print(f"\nMatrix Layout:\n{disp}")
    print(f"\nTransmitted Stream   : {group_bits(tx, g_size)}")