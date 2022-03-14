from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def index(request):
    return render(request, 'index.html', {
        'message': 'Testing h2',
        'services': [
            {'service':'Financial Statements', 'price':500, 'Available':True},
            {'service':'Financial Consulting', 'price':1000, 'Available':True},
            {'service':'Financial Advice', 'price':2000, 'Available':True}
        ]
    })

def login_view(request):
    if request.method == 'POST' or 'GET':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user: 
            login(request, user)
            return redirect('profile')


    return render(request, 'users/login.html', {

    })

def profile(request):
    account_status = False
    return render(request, 'users/profile.html', {
        'accountStatus': account_status,
        'menu': [
            {'company':'companyName'},
            {'services':'Services'},
            {'industry':'Industry'}
        ]
    })