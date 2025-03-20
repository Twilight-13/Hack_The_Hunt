from django.shortcuts import render

# ✅ Binary string for the challenge
CHALLENGE_BINARY = "01011001011011110111010001011111011100110100000001110110001100110110010001011111011101000110100000110011"
EXPECTED_OUTPUT = "You_s@v3d_th3"


# ✅ Binary decoding function
def binary_to_text(binary_input):
    """ Converts binary to text """
    try:
        if len(binary_input) % 8 != 0:
            return "❌ Error: Binary input length must be a multiple of 8."

        result = ""
        for i in range(0, len(binary_input), 8):
            byte = binary_input[i:i + 8]
            result += chr(int(byte, 2))

        return result
    except Exception as e:
        return f"❌ Error: Invalid binary input."


# ✅ Main decoder view
def decoder_view(request):
    output = ""
    success = False

    if request.method == "POST":
        user_input = request.POST.get("binary_input", "").strip()

        if user_input:
            # Decode the binary input
            output = binary_to_text(user_input)

            # Check if the output matches the expected result
            success = (output == EXPECTED_OUTPUT)

    return render(request, "code.html", {
        "challenge_binary": CHALLENGE_BINARY,
        "output": output,
        "success": success
    })

def next_level_view(request):
    """ Placeholder view for the next level """
    return render(request, "capcha.html")  # Make sure you have this template