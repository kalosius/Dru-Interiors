from django.shortcuts import render
from . models import *

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

def signin(request):
    return render(request, 'authentication/signin.html')


def signup(request):
    return render(request, 'authentication/signup.html')


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
