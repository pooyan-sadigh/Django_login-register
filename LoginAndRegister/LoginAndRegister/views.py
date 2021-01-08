from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm


def home_page(request):
    return render(request, 'home_page.html', {})


def login_page(request):
    # print(f"is user logged in : {request.user.is_authenticated}")
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
        'error': '',
    }
    if form.is_valid():
        userName = form.cleaned_data.get('userName')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect(to=home_page)
        else:
            context['error'] = 'incorrect username or password'

    return render(request, "login.html", context)


# get user model which relate django to database ( class )
User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        userName = form.cleaned_data.get('userName')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        User.objects.create_user(username=userName, email=email, password=password)
        return redirect(to=login_page)

    return render(request, "register.html", context)
