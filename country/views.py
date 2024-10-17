from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from country.forms import CountryForm
from country.models import Country
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    page = request.GET.get('page', 1)
    countries = Country.objects.all()
    paginator = Paginator(countries, 3)
    current_page = paginator.page(page)

    try:
        current_page = paginator.page(page)
    except PageNotAnInteger:
        current_page = paginator.page(1)
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)

    context = {
        "countries": current_page,
    }
    return render(request, "country/index.html", context)


def detail(request, country_id):
    country = get_object_or_404(Country, pk=country_id)
    return render(request, "country/details.html", {"country": country})

def countries(request):
    search_query = request.GET.get("search_query", "")

    if search_query:

        countries = Country.objects.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    else:
        countries = Country.objects.all()
    context = {
        "countries": countries,
        "search_query": search_query,
    }
    return render(request, "country/index.html", context)


def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username").lower()
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Пользователь {username} вошел.")
                return redirect("index")
    else:
        form = AuthenticationForm()

    return render(request, "country/login.html", {"form": form})


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
            return redirect("index")
    context = {"form": form}
    return render(request, "country/form.html", context)


def register_user(request):
    page = "register"
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Аккаунт создан")
            login(request, user)
            return redirect("index")
    context = {
        "page": page,
        "form": form,
    }
    return render(request, "country/registration.html", context)


@login_required(login_url="login")
def update_country(request, pk):
    country = Country.objects.get(id=pk)
    form = CountryForm(instance=country)

    if request.method == "POST":
        form = CountryForm(request.POST, request.FILES, instance=country)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        "country": country,
        "form": form,
    }
    return render(request, "country/form-country.html", context)


@login_required(login_url="login")
def delete_country(request, pk):
    country = Country.objects.get(id=pk)

    if request.method == "POST":
        country.delete()
        return redirect("index")
    context = {"country": country}
    return render(request, "country/delete.html", context)
