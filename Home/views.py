from django.shortcuts import render, redirect
from django.contrib import messages

# Dictionary containing team numbers as usernames and answers as passwords
TEAM_CREDENTIALS = {
    "Team1": "Storage",
    "Team2": "RAM",
    "Team3": "Cloud",
    "Team4": "USB",
    "Team5": "CPU",
    "Team6": "Processor",
    "Team7": "OS",
    "Team8": "Code",
    "Team9": "Software",
    "Team10": "Encryption",
    "Team11": "Password",
    "Team12": "Firewall",
    "Team13": "Network",
    "Team14": "Monitor",
    "Team15": "Software",
    "Team16": "Window",
    "Team17": "Program",
    "Team18": "Internet",
    "Team19": "Search-engine",
    "Team20": "Website",
    "Team21": "GPS",
    "Team22": "Camera",
    "Team23": "Keyboard",
    "Team24": "Email",
    "Team25": "Search Engine",
    "Team26": "Smartphone",
    "Team27": "Pixel",
    "Team28": "Data",
    "Team29": "Shortcut",
    "Team30": "Antivirus"
}

def login_view(request):
    """Handles the team login with hardcoded credentials"""
    if request.method == 'POST':
        team_number = request.POST.get('team_number')
        password = request.POST.get('passcode')

        # Verify team number and password
        if team_number in TEAM_CREDENTIALS and TEAM_CREDENTIALS[team_number].lower() == password.lower():
            # ✅ Successful login → Render code.html
            return render(request, 'code.html')
        else:
            # ❌ Invalid credentials
            messages.error(request, 'Invalid team number or answer')
            return redirect('landing')

    return render(request, 'index.html')
