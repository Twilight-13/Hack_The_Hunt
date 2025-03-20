from django.shortcuts import render, redirect


def capcha(request):
    """Display the captcha form."""
    return render(request, 'captcha.html')


def verify_captcha(request):
    """Verify the entered captcha code."""
    if request.method == 'POST':
        entered_code = request.POST.get('captcha_code', '').strip().lower()

        # The expected correct code
        correct_code = "go to room 5 1 8"

        if entered_code == correct_code:
            # Show the "SUCCESSFUL" message
            return render(request, 'capcha.html', {
                'success': True  # Flag to display the message
            })
        else:
            # If incorrect, show error message
            return render(request, 'capcha.html', {
                'feedback': "❌ Incorrect code. Try again!",
                'success': False
            })

    return redirect('capcha')
