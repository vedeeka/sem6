

import math
def normalize_bits(bit_string):
    bit_string=bit_string.strip().replace(" ","")
    if bit_string=="" or any(ch not in "01" for ch in bit_string):
        raise ValueError("Input must contain only 0 and 1.")
    return bit_string


def group_bits(bit_string,size=8):
    return " ".join(bit_string[i:i+size] for i in range(0,len(bit_string),size))

#1. Parity Method
def parity_bit_method(data_bits,parity_type="even"):
    data_bits=normalize_bits(data_bits)
    ones_count=data_bits.count("1")
    if parity_type=="even":
        parity="0" if ones_count%2==0 else "1"
    elif parity_type=="odd":
        parity="1" if ones_count%2==0 else "0"
    else:
        raise ValueError("parity_type must be 'even' or 'odd'.")
    transmitted=data_bits+parity
    return parity,transmitted

#2. Block Parity Method (2D Parity)
def block_parity_method(data_bits,cols=8):
    data_bits=normalize_bits(data_bits)
    if cols<=1:
        raise ValueError("cols must be greater than 1.")
    pad_len=(cols-(len(data_bits)%cols))%cols
    padded=data_bits+("0"*pad_len)
    rows=[list(padded[i:i+cols]) for i in range(0,len(padded),cols)]
    for row in rows:
        row_parity=str(sum(int(b) for b in row)%2)
        row.append(row_parity)
    col_count=cols+1
    col_parity_row=[]
    for c in range(col_count):
        col_sum=sum(int(rows[r][c]) for r in range(len(rows)))
        col_parity_row.append(str(col_sum%2))
    matrix_lines=[" ".join(row) for row in rows]
    matrix_lines.append("-"*(2*col_count-1))
    matrix_lines.append(" ".join(col_parity_row))
    transmitted_stream="".join("".join(row) for row in rows)+"".join(col_parity_row)
    return {
        "padded_data":padded,
        "pad_len":pad_len,
        "display":"\n".join(matrix_lines),
        "transmitted_stream":transmitted_stream,
        "stream_group_size":col_count,
    }

#3. CRC - 8
def crc_remainder(data_bits,polynomial_bits):
    data_bits=normalize_bits(data_bits)
    poly=normalize_bits(polynomial_bits)
    degree=len(poly)-1
    working=list(data_bits+("0"*degree))
    for i in range(len(data_bits)):
        if working[i]=="1":
            for j in range(len(poly)):
                working[i+j]="0" if working[i+j]==poly[j] else "1"
    remainder="".join(working[-degree:])
    codeword=data_bits+remainder
    return remainder,codeword

#4. Checksum
def checksum_ones_complement(data_bits,word_size=16):
    data_bits=normalize_bits(data_bits)
    if len(data_bits)%word_size!=0:
        pad_len=word_size-(len(data_bits)%word_size)
        data_bits+="0"*pad_len
    else:
        pad_len=0
    mask=(1<<word_size)-1
    words=[data_bits[i:i+word_size] for i in range(0,len(data_bits),word_size)]
    running_total=0
    for word in words:
        word_val=int(word,2)
        raw_sum=running_total+word_val
        folded=(raw_sum & mask)+(raw_sum>>word_size)
        while folded>mask:
            folded=(folded & mask)+(folded>>word_size)
        running_total=folded
    checksum_val=(~running_total)&mask
    checksum_bits=format(checksum_val,f"0{word_size}b")
    transmitted=data_bits+checksum_bits
    return checksum_bits,transmitted,words,pad_len

#5. Hamming Code
def hamming_encode(data_bits):
    data_bits=normalize_bits(data_bits)
    m=len(data_bits)
    r=0
    while 2**r<(m+r+1):
        r+=1
    n=m+r
    code=["0"]*(n+1)
    j=0
    for i in range(1,n+1):
        if (i & (i-1))!=0:
            code[i]=data_bits[j]
            j+=1
    for i in range(r):
        p=2**i
        parity=0
        for k in range(1,n+1):
            if k & p:
                parity^=int(code[k])
        code[p]=str(parity)
    return "".join(code[1:])

def hamming_detect_correct(codeword_bits):
    codeword_bits=normalize_bits(codeword_bits)
    n=len(codeword_bits)
    code=["0"]+list(codeword_bits)
    r=0
    while 2**r<=n:
        r+=1
    error_pos=0
    for i in range(r):
        p=2**i
        parity=0
        for k in range(1,n+1):
            if k & p:
                parity^=int(code[k])
        if parity!=0:
            error_pos+=p
    corrected=code[:]
    if 1<=error_pos<=n:
        corrected[error_pos]="1" if corrected[error_pos]=="0" else "0"
    return error_pos,"".join(corrected[1:])

#6. Reed Solomon Code
def reed_solomon_demo(text,nsym=8):
    codec=reedsolo.RSCodec(nsym)
    encoded=codec.encode(text.encode("utf-8"))
    decoded=codec.decode(encoded)
    decoded_bytes=decoded[0] if isinstance(decoded,tuple) else decoded
    return encoded,decoded_bytes.decode("utf-8"),nsym
    
    while True:
        print("\n1. Parity Bit Method            2. Block Parity Method\n3. CRC                          4. Checksum\n5. Hamming Code                 6. Reed-Solomon Code\n7. Exit")
        choice=input("Enter choice: ").strip()
        match choice:
                case "1":
                    bits=input("Enter data bits: ")
                    ptype=input("Enter parity type (even/odd): ").strip().lower()
                    parity,transmitted=parity_bit_method(bits,ptype)
                    print("Data bits        :",group_bits(normalize_bits(bits)))
                    print("Parity bit       :",parity)
                    print("Transmitted bits :",group_bits(transmitted))
                case "2":
                    bits=input("Enter data bits: ")
                    cols=int(input("Enter columns per row: "))
                    result=block_parity_method(bits,cols)
                    print("Padded data      :",group_bits(result["padded_data"]))
                    print("Pad bits added   :",result["pad_len"])
                    print("\nRows with parity:")
                    print(result["display"])
                    print("\nTransmitted stream :")
                    print(group_bits(result["transmitted_stream"],result["stream_group_size"]))
                case "3":
                    bits=input("Enter data bits: ")
                    crc_type=input("Choose CRC type (8/16/32): ").strip()
                    if crc_type not in crc_polys:
                        raise ValueError("CRC type must be 8,16 or 32.")
                    remainder,codeword=crc_remainder(bits,crc_polys[crc_type])
                    print("Data bits        :",group_bits(normalize_bits(bits)))
                    print("Generator poly   :",crc_polys[crc_type])
                    print("CRC remainder    :",remainder)
                    print("Transmitted bits :",group_bits(codeword))
                case "4":
                    bits=input("Enter data bits: ")
                    word_size=int(input("Enter word size: "))
                    checksum_bits,transmitted,words,pad_len=checksum_ones_complement(bits,word_size)
                    print("Words:")
                    for word in words:
                        print(word)
                    print("\nPad bits added :",pad_len)
                    print("Checksum       :",checksum_bits)
                    print("Transmitted    :",group_bits(transmitted,word_size))
                case "5":
                    data=input("Enter data bits: ")
                    encoded=hamming_encode(data)
                    print("Data bits       :",normalize_bits(data))
                    print("Encoded codeword:",encoded)
                    ans=input("Check error detection? (y/n): ").strip().lower()
                    if ans=="y":
                        recv=input("Enter received codeword: ")
                        error_pos,corrected=hamming_detect_correct(recv)
                        if error_pos==0:
                            print("No single-bit error detected.")
                        else:
                            print("Error at position :",error_pos)
                            print("Corrected codeword:",corrected)
                case "6":
                    text=input("Enter text: ")
                    nsym=int(input("Enter parity symbols count: "))
                    encoded,decoded,parity_symbols=reed_solomon_demo(text,nsym)
                    print("Original text :",text)
                    print("Parity symbols:",parity_symbols)
                    print("Encoded bytes :",list(encoded))
                    print("Decoded text  :",decoded)
                case "7":
                    print("Exiting...")
                    break
                case _:
                    print("Invalid choice.")
