from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_index')
        else:
            messages.error(request, 'Username or password is not correct', extra_tags="Error")
    return render(request, "registration/login.html", {})


def registerView(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully', extra_tags="Info")
            return redirect('login_url')
        else:
            for field, error in f.errors.as_data().items():
                if field == "password1" or field == "password2":
                    field = "Password"

                messages.error(request, str(error[0])[2:-2], extra_tags=str(field).capitalize())
    else:
        f = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': f})


def logoutView(request):
    logout(request)
    return redirect("login_url")
