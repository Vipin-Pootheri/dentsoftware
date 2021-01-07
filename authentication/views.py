from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm


# Create your views here.

def loginpage(request):
    loginform = LoginForm(request.POST or None)
    if request.method == "POST":
        if loginform.is_valid():
            username = loginform.cleaned_data.get("username")
            password = loginform.cleaned_data.get("password")
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                print('here')
                return redirect('homepage')
            else:
                messages.error(request,"Username or password is incorrect")
                return redirect('loginpage')
    loginform = LoginForm()
    context = {"loginform": loginform}
    return render(request, 'authentication/loginpage.html', context)

def logout_view(request):
    if 'firstname' in request.session:
        del request.session['patid']
        del request.session['firstname']
        del request.session['phonenumber']
        del request.session['location']
    logout(request)
    loginform = LoginForm()
    return redirect('loginpage')

