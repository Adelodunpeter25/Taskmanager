from django.shortcuts import render

def login_view(request):
    return render(request, 'accounts/login.html')

def signup_view(request):
    return render(request, 'accounts/signup.html')

def logout_view(request):
    # We'll implement logout logic later
    return render(request, 'accounts/logout.html')
