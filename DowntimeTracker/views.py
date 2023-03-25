from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        if name:
            return redirect("dashboard", name=name)
    return render(request, "welcome.html")

def dashboard(request, name):
    return render(request, "dashboard.html", {"name": name})
