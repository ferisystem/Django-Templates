from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.shortcuts import (
    render,
    redirect,
)
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def signin_view(request):
    if request.method == "POST":
        username = request.POST.get("user")
        password = request.POST.get("pass")
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {"error": "Invalid username or password"}
            return render(request, "accounts/signin.html", context=context)
        login(request, user)
        return redirect('/')
    return render(request, "accounts/signin.html", {})


def signout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/signout.html", {})


def signup_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login/")
    context = {"form": form}
    return render(request, "accounts/signup.html", context)