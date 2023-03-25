from django.shortcuts import render, redirect
from .models import Activity
import datetime

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            return redirect("dashboard", name=name)
    return render(request, "welcome.html")

def dashboard(request, name):
        
    return render(request, "dashboard.html", {"name": name})

def populate(request):
    treasure = Activity(title="Find Treasure", description="Character spends their free time chasing the treasure of a great and feared pirate.", player="Sarah", date_started=datetime.date(2023, 3,25), days=7, days_completed=0, hidden=False)
    treasure.save()
    dragons = Activity(title="Dragon Hunt", description="Character follows rumors of a dragon sighting over a far village.", player="John", date_started=datetime.date(2023, 3,20), days=14, days_completed=5, hidden=False)
    dragons.save()
    tlc = Activity(title="Me time", description="Character spends a day pampering themselves to recover from all of their great adventures.", player="Mike", date_started=datetime.date(2023, 3,24), days=1, days_completed=0, hidden=False)
    tlc.save()
    return redirect('index')