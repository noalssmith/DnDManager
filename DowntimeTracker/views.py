from django.shortcuts import render, redirect
from DowntimeTracker.models import Activity, Player

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
    else:
        current_activity = None
    return render(request, "dashboard.html", {"name": name, "currentActivity": current_activity},)
