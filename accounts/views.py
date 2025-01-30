from django.shortcuts import render

# Create your views here.
def user_signup(request);
    return render(request, 'account/signup.html')

def user_login(request);
    return render(request, 'account/login.html')