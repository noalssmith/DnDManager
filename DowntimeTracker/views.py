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
    current_activitys = Activity.objects.filter(player=name)
    all_activities = Activity.objects.all()
    if len(current_activitys) > 0:
        current_activity = current_activitys[0]
        percentage = int(round(current_activity.days_completed / current_activity.days, 2) * 100)
    else:
        current_activity = None
        percentage = 0
    return render(request, "dashboard.html", {"name": name, "currentActivity": current_activity, "percentage":  percentage, "allActivities":all_activities})

def populate(request):
    ...
#     treasure = Activity(title="Find Treasure", description="Character spends their free time chasing the treasure of a great and feared pirate.", player="Sarah", date_started=datetime.date(2023, 3,25), days=7, days_completed=0, hidden=False)
#     treasure.save()
#     dragons = Activity(title="Dragon Hunt", description="Character follows rumors of a dragon sighting over a far village.", player="John", date_started=datetime.date(2023, 3,20), days=14, days_completed=5, hidden=False)
#     dragons.save()
#     tlc = Activity(title="Me time", description="Character spends a day pampering themselves to recover from all of their great adventures.", player="Mike", date_started=datetime.date(2023, 3,24), days=1, days_completed=0, hidden=False)
#     tlc.save()
#     return redirect('index')