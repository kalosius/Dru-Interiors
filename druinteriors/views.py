from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'authentication/signin.html')


def signup(request):
    return render(request, 'authentication/signup.html')


def logout(request):
    return render(request, 'authentication/logout.html')


def furniture(request):
    return render(request, 'furniture.html')

def gadgets(request):
    return render(request, 'gadgets.html')


def phones(request):
    return render(request, 'phones.html')

def product(request):
    return render(request, 'product.html')

def dogs(request):
    return render(request, 'dogs.html')

def fashion(request):
    return render(request, 'fashion.html')






