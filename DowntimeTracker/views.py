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
    current_activity = Activity.objects.filter(player=name)
    if len(current_activity) > 0:
        current_activity = current_activity[0]
        percentage = int(round(current_activity.days_completed / current_activity.days, 2) * 100)
    else:
        current_activity = None
    return render(request, "dashboard.html", {"name": name, "currentActivity": current_activity, "percentage": percentage},)
