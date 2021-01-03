from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User, Group
from django.db.models.functions import Concat
from django.db.models import Value, CharField
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import datetime
from .forms import NewPatient
from .models import Patient, ExistingPatientAppointmentevents, NewPatientAppointmentevents,CheckedinPatient,CountryList,StateList


# Create your views here.
def newpatient(request):
    patientform = NewPatient()
    today = date.today()
    doctors = User.objects.filter(groups__name='doctor')
    checkedin_count = CheckedinPatient.objects.filter(checkedintime__year=today.year, checkedintime__month=today.month,
                                                      checkedintime__day=today.day).count()
    newappounmentcount = NewPatientAppointmentevents.objects.filter(start__year=today.year, start__month=today.month,
                                                                    start__day=today.day).count()
    existingappcount = ExistingPatientAppointmentevents.objects.filter(start__year=today.year, start__month=today.month,
                                                                       start__day=today.day).count()
    appointment_count = int(newappounmentcount) + int(existingappcount)
    countries = CountryList.objects.all().values('id','name')

    context = {'form': patientform,'doctors':doctors,'checkin': checkedin_count, 'appointment': appointment_count,
               'countries':countries
               }
    return render(request, 'receptionactivities/newpatientregistration.html', context)

def createnewpatient(request):
    dob = datetime.datetime(int(request.POST.get('year')),int(request.POST.get('month')),int(request.POST.get('day')))
    try:
        if request.POST.get('postcode') == '':
            postcode = 0
        else:
            postcode = request.POST.get('postcode')
        p = Patient(
            salutation=request.POST.get('salutation'),
            firstname=request.POST.get('firstname'),
            middlename=request.POST.get('middlename'),
            lastname=request.POST.get('lastname'),
            dob=dob,
            gender=request.POST.get('gender'),
            phonenumber=request.POST.get('phonenumber'),
            email=request.POST.get('email'),
            addressline1=request.POST.get('addressline1'),
            addressline2=request.POST.get('addressline2'),
            addressline3=request.POST.get('addressline3'),
            location=request.POST.get('location'),
            country=request.POST.get('country'),
            postcode=postcode,
            state=request.POST.get('state'),
            city=request.POST.get('city')
            )
        p.save()
        patient_id = p.id
        status='true'
        errmsg=''
    except Exception as e:
        patient_id = 0
        status = 'false'
        errmsg = str(e)
    data = {'status':status,'errmsg':errmsg,'patid':patient_id}
    return JsonResponse(data)

def getstate(request):
    try:
        country = request.GET.get('country')
        states = list(StateList.objects.filter(country_id=country).values('id','name'))
        data={'status':'true','states':states}
    except Exception as e:
        data = {'status': 'false', 'errmsg': str(e)}
    return JsonResponse(data)
def appointment(request):
    if request.method == 'POST':
        newpatientappointmentcheckbox = request.POST.get('newpatientappointmentcheckbox')
        addappointmentpatientname = request.POST.get('addappointmentpatientname')
        addappointmentpatientid = request.POST.get('addappointmentpatientid')
        addappointmentpatientphone = request.POST.get('addappointmentpatientphone')
        addappointmentstartdate = request.POST.get('addappointmentstartdate')
        addappointmentenddate = request.POST.get('addappointmentenddate')
        doctorname = request.POST.get('addappointmentdoctor')

        if newpatientappointmentcheckbox == '1':
            p = NewPatientAppointmentevents(
                title=addappointmentpatientname,
                phonenumber=addappointmentpatientphone,
                start=addappointmentstartdate,
                end=addappointmentenddate,
                doctor_id=doctorname
            )
            p.save()
        else:
            p = ExistingPatientAppointmentevents(
                title=Patient.objects.get(id=addappointmentpatientid),
                start=addappointmentstartdate,
                end=addappointmentenddate,
                doctor_id=doctorname
            )
            p.save()
    existing_patientevents = ExistingPatientAppointmentevents.objects.all() \
        .annotate(eventid=Concat(Value('E-'), 'id', output_field=CharField())) \
        .values('eventid', 'title__firstname', 'title__phonenumber', 'start', 'end', 'doctor__username','title__lastname'
                ,'title__addressline1','title__location','title__city'
                )
    new_patientevents = NewPatientAppointmentevents.objects.all() \
        .annotate(lastname=Value('', CharField()), \
                  city=Value('', CharField()),location=Value('', CharField()),addressline1=Value('', CharField()),eventid=Concat(Value('N-'), 'id', output_field=CharField())) \
        .values('eventid', 'title', 'phonenumber', 'start', 'end', 'doctor__username','lastname','addressline1','location','city')
    events = existing_patientevents.union(new_patientevents)
    doctors = User.objects.filter(groups__name='doctor')
    today = date.today()
    checkedin_count = CheckedinPatient.objects.filter(checkedintime__year=today.year, checkedintime__month=today.month,
                                                      checkedintime__day=today.day).count()
    newappounmentcount = NewPatientAppointmentevents.objects.filter(start__year=today.year, start__month=today.month,
                                                                    start__day=today.day).count()
    existingappcount = ExistingPatientAppointmentevents.objects.filter(start__year=today.year, start__month=today.month,
                                                                       start__day=today.day).count()
    appointment_count = int(newappounmentcount) + int(existingappcount)

    context = {'eventdata': events, 'doctors': doctors,'checkin': checkedin_count, 'appointment': appointment_count}
    return render(request, 'receptionactivities/appointment.html', context)


# draganddrop and resize handled in same view

def draganddrop(request):
    eventid = request.GET.get('eventid')
    eventstart = request.GET.get('eventstart')
    eventend = request.GET.get('eventend')
    if eventid[0] == 'N':
        p = NewPatientAppointmentevents.objects.filter(id=eventid[2:])
        p.update(start=eventstart, end=eventend)
    elif eventid[0] == 'E':
        p = ExistingPatientAppointmentevents.objects.filter(id=eventid[2:])
        p.update(start=eventstart, end=eventend)
    return redirect('appointment')

def checkin(request):
    patid = request.GET.get('id')
    print(patid[2:])
    p = ExistingPatientAppointmentevents.objects.filter(id=patid[2:]).values('title_id','doctor_id').get()

    q=CheckedinPatient(title_id = p['title_id'],doctor_id=p['doctor_id'])
    q.save()
    data={'status':'true'}
    return JsonResponse(data)

def delete(request):
    eventid = request.GET.get('id')
    if eventid[0] == 'N':
        p = NewPatientAppointmentevents.objects.filter(id=eventid[2:])
        p.delete()
    elif eventid[0] == 'E':
        p = ExistingPatientAppointmentevents.objects.filter(id=eventid[2:])
        p.delete()
    data = {'status': 'true'}
    return JsonResponse(data)

def update(request):
    eventid = request.GET.get('id')
    start = request.GET.get('start')
    end = request.GET.get('end')
    doctor = request.GET.get('doctor')
    if eventid[0] == 'N':
        p = NewPatientAppointmentevents.objects.filter(id=eventid[2:])
        p.update(
            start=start,
            end=end,
            doctor_id=doctor
        )
    elif eventid[0] == 'E':
        p = ExistingPatientAppointmentevents.objects.filter(id=eventid[2:])
        p.update(
            start=start,
            end=end,
            doctor_id=doctor
        )

    return redirect('appointment')

def registerafterappointment(request):
    eventid = request.GET.get('id')
    p = NewPatientAppointmentevents.objects.filter(id=eventid[2:]).values('title','phonenumber')

    data ={'url':request.scheme + "://" +request.get_host() }
    return JsonResponse(data)


