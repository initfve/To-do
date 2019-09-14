from django.shortcuts import render


# Create your views here.
def loginView(request):
    return render(request, "registration/login.html", {})


def registerView(request):
    return render(request, "registration/register.html", {})


def logoutView(request):
    pass