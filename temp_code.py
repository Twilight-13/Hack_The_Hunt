
def binary_to_text(binary_input):
    if len(binary_input) % 8 != 0:
        raise ValueError("Binary input length must be a multiple of 8.")
    result = ''
    for i in range(0, len(binary_input), 8):
        byte = binary_input[i:i+8]
        result += chr(int(byte, 2))
    return result

binary_input = '01011001011011110111010001011111011100110100000001110110001100110110010001011111011101000110100000110011'
print(binary_to_text(binary_input))
