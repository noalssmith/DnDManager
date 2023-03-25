from django.shortcuts import render, redirect
from .models import Activity, Player

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            return redirect("dashboard", name=name)
    names = Player.objects.all()
    return render(request, "welcome.html", {"names":names})

def dashboard(request, name):
    return render(request, "dashboard.html", {"name": name})
