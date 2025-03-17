def binary_to_text(binary_input):
    result = ''
    for i in range(0, len(binary_input), 8):
        byte = binary_input[i:i+8]
        # Fix the error here
        result += chr(int(byte, 2))
    return result

binary_input = '0100100001100101011011000110110001101111'
print(binary_to_text(binary_input))