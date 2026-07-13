def reed_solomon_demo(text, nsym=8):
    import reedsolo
    codec = reedsolo.RSCodec(nsym)
    encoded = codec.encode(text.encode("utf-8"))
    decoded = codec.decode(encoded)
    decoded_bytes = decoded[0] if isinstance(decoded, tuple) else decoded
    return encoded, decoded_bytes.decode("utf-8")

# Execution with User Input
if __name__ == "__main__":
    print("--- Test Reed-Solomon Code Method ---")
    user_text = input("Enter a text message string: ")
    user_nsym = int(input("Enter count of parity check symbols [8]: ").strip() or 8)
    
    enc_bytes, dec_text = reed_solomon_demo(user_text, user_nsym)
    print(f"Encoded Symbol Array Bytes: {list(enc_bytes)}")
    print(f"Decoded Message Output    : {dec_text}")