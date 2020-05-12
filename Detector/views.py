from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('/signup/')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already taken')
                return redirect('/signup/')
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                user.save()
                print('user created')
                return redirect('/login/')
        else:
            messages.info(request, 'password not matching...')
            return redirect('/signup/')
        # return redirect('/home/')

    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/home/')
        else:
            messages.info(request, 'invalid username')
            return redirect('/login/')

    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/Index/')