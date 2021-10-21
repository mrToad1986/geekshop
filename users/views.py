from django.shortcuts import render

def login(request):
    context = {'title': 'Geekshop - Авторизация'}
    return render(request, 'users/login.html', context)

def registration(request):
    context = {'title': 'Geekshop - Регистрация'}
    return render(request, 'users/registration.html', context)