from django.shortcuts import render, redirect
from .models import Activity, Player
import datetime
import json

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            return redirect("dashboard", name=name)
    names = Player.objects.all()
    return render(request, "welcome.html", {"names":names})

def dashboard(request, name):
    current_activitys = Activity.objects.filter(player=name)
    all_activities = Activity.objects.all()
    status = [a.player == name for a in all_activities]

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        days = request.POST.get("days")
        new_activity = Activity(title=title, description=description, days=days, player="", days_completed=0, hidden=True, date_started=None)
        new_activity.save()

    if len(current_activitys) > 0:
        current_activity = current_activitys[0]
        days_completed = (datetime.date.today() - current_activity.date_started).days + current_activity.days_completed
        percentage = int(round(days_completed / current_activity.days, 2) * 100)
    else:
        current_activity = None
        percentage = 0
        days_completed = 0
    return render(request, "dashboard.html",
                   {"name": name, 
                    "currentActivity": current_activity,
                    "daysCompleted": days_completed, 
                    "percentage":  percentage, 
                    "allActivities":zip(all_activities,status)})


def begin_activity(request):
    print('Checkpoint: Begin_activity')
    title = request.POST.get('title')
    name = request.POST.get('name')
    acts = Activity.objects.filter(player=name)
    for act in acts:
        act.player = '';
        act.days_completed = (datetime.date.today() - act.date_started).days + act.days_completed
        act.date_started = None
        act.save()

    acts = Activity.objects.filter(title=title)
    if(len(acts)>0):
        acts[0].player = name
        acts[0].date_started = datetime.date.today()
        acts[0].save()
    else:
        print("ERROR: No activite called",title)

    print('\t',title)
    print('\t',name)
    return redirect("dashboard", name=name)




def populate(request):
    ...
#     treasure = Activity(title="Find Treasure", description="Character spends their free time chasing the treasure of a great and feared pirate.", player="Sarah", date_started=datetime.date(2023, 3,25), days=7, days_completed=0, hidden=False)
#     treasure.save()
#     dragons = Activity(title="Dragon Hunt", description="Character follows rumors of a dragon sighting over a far village.", player="John", date_started=datetime.date(2023, 3,20), days=14, days_completed=5, hidden=False)
#     dragons.save()
#     tlc = Activity(title="Me time", description="Character spends a day pampering themselves to recover from all of their great adventures.", player="Mike", date_started=datetime.date(2023, 3,24), days=1, days_completed=0, hidden=False)
#     tlc.save()
#     return redirect('index')
