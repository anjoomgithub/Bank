from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import AccountApplication


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/new_page')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, )
                user.save();
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def new_page(request):
    return render(request, "new_page.html")


def account_application(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        dob = request.POST.get('dob', )
        age = request.POST.get('age', )
        gender = request.POST.get('gender', )
        phone = request.POST.get('phone', )
        mail = request.POST.get('mail', )
        address = request.POST.get('address', )
        district = request.POST.get('district', )
        branch = request.POST.get('branch', )
        account_type = request.POST.get('account_type', )
        materials = request.POST.get('materials', )

        application = AccountApplication(name=name, dob=dob, age=age, gender=gender, phone=phone, mail=mail,
                                         address=address, district=district, branch=branch,
                                         account_type=account_type, materials=materials)
        application.save()
        messages.info(request, "Application Accepted")
        return render(request, 'application_success.html')
    else:
        return render(request, 'account_application.html')


def application_success(request):
    return render(request, "application_success.html")
