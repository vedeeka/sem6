from parity import normalize_bits, group_bits

def checksum_ones_complement(data, word_size=8):
    words = []

    # Divide data into words
    for i in range(0, len(data), word_size):
        word = data[i:i + word_size]

        # Pad last word if needed
        if len(word) < word_size:
            word += "0" * (word_size - len(word))

        words.append(word)

    total = 0
    max_value = 2 ** word_size

    # Add all words
    for word in words:
        total += int(word, 2)

        # Handle carry
        if total >= max_value:
            total = (total - max_value) + 1

    # Take 1's complement
    checksum = format((max_value - 1) - total, f"0{word_size}b")

    transmitted = "".join(words) + checksum

    return words, checksum, transmitted

if __name__ == "__main__":
    data = input("Enter data bits: ")
    word_size = int(input("Enter word size: "))

    words, checksum, transmitted = checksum_ones_complement(data, word_size)

    print("Words       :", words)
    print("Checksum    :", checksum)
    print("Transmitted :", transmitted)