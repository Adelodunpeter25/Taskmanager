from django.shortcuts import render

def project_home(request):
    return render(request, 'projects/home.html')  # We'll create this template shortly
