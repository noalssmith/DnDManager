from django.shortcuts import render, redirect
from DowntimeTracker.models import Activity

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            return redirect("dashboard", name=name)
    return render(request, "welcome.html")

def dashboard(request, name):
    current_activity = Activity.objects.filter(player=name)
    if len(current_activity) > 0:
        current_activity = current_activity[0]
    else:
        current_activity = None
    return render(request, "dashboard.html", {"name": name, "currentActivity": current_activity},)
