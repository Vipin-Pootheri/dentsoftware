from django.http import HttpResponse
from django.shortcuts import redirect


def user_access(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'admin':
            return redirect('adminhomepage')

        if group == 'receptionist' or group=='doctor':
            return view_func(request, *args, **kwargs)

    return wrapper_function


def admin_access(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'doctor':
            return HttpResponse('You are not authorised to view this page')
        if group == 'receptionist':
            return HttpResponse('You are not authorised to view this page')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
    return wrapper_function


def doctor_access(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'receptionist':
            return HttpResponse('You are not authorised to view this page')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_function
