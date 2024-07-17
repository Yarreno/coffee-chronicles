from django.shortcuts import render
    
def about(request):
    if 'username' in request.session:
        return render(request, 'about.html')
    else:
        return render(request, 'login.html')