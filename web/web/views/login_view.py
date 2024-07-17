from django.shortcuts import render
from pymongo import MongoClient

def login(request):
    if 'username' in request.session:
        # Add your dashboard logic here
        return render(request, 'dashboard.html')
    
    # Add your login logic here
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f'Username: {username}')
        print(f'Password: {password}')
        
        is_login_valid = check_user(username, password)

        if(is_login_valid):
            request.session['username'] = username
            request.session.set_expiry(10) 
            return render(request, 'dashboard.html')

    return render(request, 'login.html')

def check_user(email, password):
    client = MongoClient('mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/')
    db = client['CaffeineChronicles']
    users = db['usersdb']

    user = users.find_one({'email': email, 'password': password})

    return user is not None