from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'welcome.html')

def dashboard(request):
    return render(request, 'dashboard.html')