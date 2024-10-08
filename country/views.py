from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from country.forms import CountryForm
from country.models import Country
from django.contrib import messages


def index(request):
    countries = Country.objects.all()
    return render(request, 'country/index.html', {'countries': countries})


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username').lower()
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Пользователь {username} вошел.")
                return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, "country/login.html", {'form': form})

def logout_user(request):
    username = request.user.username
    logout(request)
    messages.info(request, f"Пользователь {username} вышел.")
    return redirect("login")


@login_required(login_url="login")
def create_country(request):
    form = CountryForm()
    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'country/form.html', context)

def register_user(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Аккаунт создан")
            login(request, user)
            return redirect('index')
    context = {
        'page': page,
        'form': form,
    }
    return render(request, "country/registration.html", context)