from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
# Create your views here.
from django.db.utils import IntegrityError
from django.contrib.auth.models import User


def home(request):
    return render(request, 'homepage.html')

def Login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user= authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("dashboard")
        else:

            return redirect("login")
    return render(request, 'login.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            print("user already exists")

        
    return render(request, 'signup.html')

@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')
