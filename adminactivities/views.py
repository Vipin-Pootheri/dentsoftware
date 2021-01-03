from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.http import JsonResponse
from .forms import Adduser

from homepage.decorators import admin_access


# Create your views here.
@admin_access
def adduser(request):
    form = Adduser(request.POST or None)
    userlist = User.objects.all().values('id', 'username', 'email', 'groups__name').order_by('-id')
    if request.method == "POST":
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(data['name'], data['email'], data['password'])
            user = new_user.save()
            print(new_user)
            group = Group.objects.get(name=data['usertype'])
            new_user.groups.add(group)

    context = {'form': form, 'userlist': userlist}

    return render(request, 'adminactivities/adduser.html', context=context)


@admin_access
def edituser(request):
    id = request.GET.get('userid', None)
    user = User.objects.filter(id=id).values('username', 'email','groups__name').get()
    return JsonResponse(user)


@admin_access
def deleteuser(request, id):
    u = User.objects.get(id=id)
    u.delete()
    return redirect('adminadduser')


@admin_access
def addprescription(request):
    return render(request, 'adminactivities/addprescription.html')


@admin_access
def addtreatmentplan(request):
    return render(request, 'adminactivities/addtreatmentplan.html')
