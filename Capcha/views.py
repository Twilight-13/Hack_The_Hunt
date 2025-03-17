from django.shortcuts import render

# Create your views here.
def capcha(request):
    return render(request, 'capcha.html')