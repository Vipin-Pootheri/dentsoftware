from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from django.contrib.auth.models import User, Group
from datetime import date
from .decorators import user_access, admin_access, doctor_access
from receptionactivities.models import Patient,ExistingPatientAppointmentevents,NewPatientAppointmentevents,CheckedinPatient


# Create your views here.

@user_access
def homepage(request):
    today = date.today()
    checkedin_count = CheckedinPatient.objects.filter(checkedintime__year = today.year,checkedintime__month=today.month,checkedintime__day=today.day).count()
    newappounmentcount = NewPatientAppointmentevents.objects.filter(start__year = today.year,start__month=today.month,start__day=today.day).count()
    existingappcount = ExistingPatientAppointmentevents.objects.filter(start__year = today.year,start__month=today.month,start__day=today.day).count()
    appointment_count = int(newappounmentcount) + int(existingappcount)
    doctors = User.objects.filter(groups__name='doctor')
    context = {'checkin':checkedin_count, 'appointment':appointment_count,'doctors':doctors}

    return render(request, 'receptionactivities/receptionpage.html',context)


@admin_access
def adminhomepage(request):
    return render(request, 'homepage/adminhomepage.html')


@doctor_access
def doctorhomepage(request):
    return render(request, 'homepage/doctorhomepage.html')


def searchpatient(request):
    searchfield = request.GET.get('name')
    patients = []
    if len(searchfield) > 0:
        patients = list(
            Patient.objects.filter(Q(firstname__icontains=searchfield) | Q(middlename__icontains=searchfield) | Q(
                lastname__icontains=searchfield) | Q(phonenumber__icontains=searchfield)).values('id', 'firstname',
                                                                                                 'lastname',
                                                                                                 'phonenumber',
                                                                                                 'addressline1',
                                                                                                 'location'))

    return JsonResponse(patients, safe=False)
def checkinwalkin(request):
    patid = request.session['patid']
    doctorid = request.GET.get('doctorid')
    ischeckedin = CheckedinPatient.objects.filter(title_id=patid, doctor_id=doctorid, status=None)

    if ischeckedin.exists():
        pass
    else:
        q = CheckedinPatient(title_id=patid, doctor_id=doctorid)
        q.save()
    data = {'status': 'true'}
    return JsonResponse(data)
def appointmentcheckin(request):
    patid = request.GET.get('patid')
    doctorid = request.GET.get('doctorid')
    appid=request.GET.get('appid')
    ischeckedin = CheckedinPatient.objects.filter(title_id=patid, doctor_id=doctorid, status=None)
    p=NewPatientAppointmentevents.objects.filter(id=appid[2:])
    p.update(ischeckedin=True)
    if ischeckedin.exists():
        pass
    else:
        q = CheckedinPatient(title_id=patid, doctor_id=doctorid)
        q.save()
    data = {'status': 'true','url': request.scheme + "://" + request.get_host()+'/home/'}
    return JsonResponse(data)

def setpatient(request):
    patid = request.GET.get('patid')

    print('set the session key')
    request.session['patid'] = patid
    patient=Patient.objects.filter(id=patid).values('firstname','phonenumber','location').get()
    request.session['firstname'] = patient['firstname']
    request.session['phonenumber'] = patient['phonenumber']
    request.session['location'] = patient['location']

    data = {'status':'true'}
    return JsonResponse(data)