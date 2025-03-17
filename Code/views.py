import subprocess
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Dummy function to generate unique code per team
def generate_code(language):
    if language == "python":
        return (
            "def binary_to_text(binary_input):\n"
            "    result = ''\n"
            "    for i in range(0, len(binary_input), 8):\n"
            "        byte = binary_input[i:i+8]\n"
            "        # Fix the error here\n"
            "        result += chr(int(byte, 2))\n"
            "    return result\n\n"
            "binary_input = '0100100001100101011011000110110001101111'\n"
            "print(binary_to_text(binary_input))"
        )
    else:  # C code
        return (
            "#include <stdio.h>\n"
            "#include <string.h>\n"
            "\n"
            "void binary_to_text(char *binary_input) {\n"
            "    char result[100];\n"
            "    int index = 0;\n"
            "    for (int i = 0; i < strlen(binary_input); i += 8) {\n"
            "        char byte[9] = {0};\n"
            "        strncpy(byte, binary_input + i, 8);\n"
            "        result[index++] = strtol(byte, NULL, 2);\n"
            "    }\n"
            "    result[index] = '\\0';\n"
            "    printf(\"%s\\n\", result);\n"
            "}\n"
            "\n"
            "int main() {\n"
            "    char binary_input[] = \"0100100001100101011011000110110001101111\";\n"
            "    binary_to_text(binary_input);\n"
            "    return 0;\n"
            "}"
        )

def code_editor(request):
    language = request.POST.get('language', 'python')
    initial_code = generate_code(language)
    return render(request, 'code.html', {
        'initial_code': initial_code,
        'language': language
    })

def check_code(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        code = request.POST.get('code')

        try:
            # Save code to a temp file and execute
            file_extension = 'py' if language == 'python' else 'c'
            file_name = f'temp_code.{file_extension}'
            with open(file_name, 'w') as file:
                file.write(code)

            # Run the code securely
            if language == 'python':
                result = subprocess.run(['python', file_name], capture_output=True, text=True, timeout=5)
            else:
                # Compile and run C code
                subprocess.run(['gcc', file_name, '-o', 'temp_code'], check=True)
                result = subprocess.run(['./temp_code'], capture_output=True, text=True, timeout=5)

            output = result.stdout
            feedback = 'Code executed successfully!' if result.returncode == 0 else 'There was an error executing your code.'
        except Exception as e:
            output = str(e)
            feedback = 'An error occurred while processing your code.'

        return render(request, 'code.html', {
            'initial_code': code,
            'language': language,
            'output': output,
            'feedback': feedback
        })

    return redirect('/')