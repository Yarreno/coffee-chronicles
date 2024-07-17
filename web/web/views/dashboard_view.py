from django.shortcuts import render
    
def dashboard(request):
    if 'username' in request.session:
        return render(request, 'dashboard.html')
    else:
        return render(request, 'login.html')