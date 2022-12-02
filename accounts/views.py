from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.shortcuts import (
    render,
    redirect,
)
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)


# Create your views here.
def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm(request)
    context = {"form": form}
    return render(request, "accounts/signin.html", context)


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