from django.shortcuts import render
from pymongo import MongoClient

def register(request):
    if 'username' in request.session:
        # Add your dashboard logic here
        return render(request, 'dashboard.html')

    # Add your registration logic here
    if request.method == 'POST':
        full_name = request.POST.get('fullName')
        email_address = request.POST.get('emailAddress')
        phone_number = request.POST.get('phoneNumber')
        password = request.POST.get('password')
        
        print(f'Full Name: {full_name}')
        print(f'Email Address: {email_address}')
        print(f'Phone Number: {phone_number}')
        print(f'Password: {password}')
        
        client = MongoClient('mongodb+srv://volkaneerdogan:volkan1700@caffeinechroniclesclust.xcclxhl.mongodb.net/')
        db = client['CaffeineChronicles']

        users = db['usersdb']

        user_data = {
            'name': full_name,
            'email': email_address,
            'phone': phone_number,
            'password': password
        }

        result = users.insert_one(user_data)
        print(f'User ID: {result.inserted_id}')
        return render(request, 'login.html')
    
    return render(request, 'register.html')