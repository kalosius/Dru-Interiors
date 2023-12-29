from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import SignUpForm, SignInForm
from  django.contrib import messages


# Create your views here.
def index(request):
    furniture = Furniture.objects.all()
    gadgets = Gadget.objects.all()
    shirt = Shirt.objects.all()
    trouser = Trouser.objects.all()
    sneaker = Sneaker.objects.all()
    attire = Attire.objects.all()
    pet = Dog.objects.all()
    phones = Phone.objects.all()

    context = {"furniture":furniture, "gadgets":gadgets, "shirt":shirt, "trouser":trouser, "sneaker":sneaker, "attire":attire, "pet":pet, "phones":phones}

    return render(request, 'index.html', context)

# User login View
def signin(request):
    form = SignInForm
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {username}!')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
        
    return render(request, 'authentication/signin.html')

# Registration view
def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # messages.success(request, f"Welcome {user}! to Dru-Interiors-Limited")
            return redirect('index') #redirect to home page
        else:
            messages.warning(request, "Username or Password Incorrect!")     #else reload to the registration page displaying an error message
    return render(request, 'authentication/signup.html', {"form": form})


def logout(request):
    return render(request, 'authentication/logout.html')


def furniture(request):
    furniture = Furniture.objects.all()
    context = {"furniture":furniture}
    return render(request, 'furniture.html', context)

def gadgets(request):
    gadgets = Gadget.objects.all()
    context = {"gadgets":gadgets}
    return render(request, 'gadgets.html', context)


def phones(request):
    phones = Phone.objects.all()
    context = {"phones":phones}
    return render(request, 'phones.html', context)

def product(request):
    return render(request, 'product.html')

def dogs(request):
    pet = Dog.objects.all()
    context = {"pet":pet}
    return render(request, 'dogs.html', context)

def fashion(request):
    shirt = Shirt.objects.all()
    trouser = Trouser.objects.all()
    sneaker = Sneaker.objects.all()
    attire = Attire.objects.all()
    context = {"shirt":shirt, "trouser":trouser, "sneaker":sneaker, "attire":attire}
    return render(request, 'fashion.html', context)
