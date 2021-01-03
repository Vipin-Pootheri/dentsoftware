from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import json,sys,os
from datetime import date
from .models import Alerts,Radilogy,Prescription,Billing,Medicine,Diagnosis,Treatment,Treatmentdetails
from receptionactivities.models import CheckedinPatient

# Create your views here.

def doctorhomepage(request):
    return render(request,'doctoractivities/alert.html')

def alerts(request):
    patid = request.session['patid']
    if request.method == "POST":
        if request.POST.get('alertbloodpreessure') == 'on':
            alertbloodpreessure=True
            alertbloodpreessuretext = request.POST.get('alertbloodpreessuretext')
        else:
            alertbloodpreessure = False
            alertbloodpreessuretext=None
        if request.POST.get('alertheartalignment') == 'on':
            alertheartalignment=True
            alertheartalignmenttext = request.POST.get('alertheartalignmenttext')
        else:
            alertheartalignment = False
            alertheartalignmenttext=None
        if request.POST.get('alertheumaticfever') == 'on':
            alertheumaticfever=True
            alertheumaticfevertext = request.POST.get('alertheumaticfevertext')
        else:
            alertheumaticfever = False
            alertheumaticfevertext=None
        if request.POST.get('alertasthma') == 'on':
            alertasthma=True
            alertasthmatext = request.POST.get('alertasthmatext')
        else:
            alertasthma = False
            alertasthmatext=None
        if request.POST.get('alerttuberculosis') == 'on':
            alerttuberculosis=True
            alerttuberculosistext = request.POST.get('alerttuberculosistext')
        else:
            alerttuberculosis = False
            alerttuberculosistext=None
        if request.POST.get('alertheart') == 'on':
            alertheart=True
            alerthearttext = request.POST.get('alerthearttext')
        else:
            alertheart = False
            alerthearttext=None
        if request.POST.get('alertdentalissues') == 'on':
            alertdentalissues=True
            alertdentalissuestext = request.POST.get('alertdentalissuestext')
        else:
            alertdentalissues = False
            alertdentalissuestext=None
        if request.POST.get('alertpreviousillness') == 'on':
            alertpreviousillness=True
            alertpreviousillnesstext = request.POST.get('alertpreviousillnesstext')
        else:
            alertpreviousillness = False
            alertpreviousillnesstext=None
        if request.POST.get('alertpresentmedicalcare') == 'on':
            alertpresentmedicalcare=True
            alertpresentmedicalcaretext = request.POST.get('alertpresentmedicalcaretext')
        else:
            alertpresentmedicalcare = False
            alertpresentmedicalcaretext=None
        if request.POST.get('alertanydrugs') == 'on':
            alertanydrugs=True
            alertanydrugstext = request.POST.get('alertanydrugstext')
        else:
            alertanydrugs = False
            alertanydrugstext=None
        if request.POST.get('alertfemalepatients') == 'on':
            alertfemalepatients=True
            alertfemalepatientstext = request.POST.get('alertfemalepatientstext')
        else:
            alertfemalepatients = False
            alertfemalepatientstext=None
        if request.POST.get('alertallergies') == 'on':
            alertallergies=True
            alertallergiestext = request.POST.get('alertallergiestext')
        else:
            alertallergies = False
            alertallergiestext=None
        alertremarks = request.POST.get('alertremarks')

        pat = Alerts.objects.filter(patient_id = patid)
        if pat.exists():
            pat.update(
                bloodpressure=alertbloodpreessure,
                bloodpressuretext=alertbloodpreessuretext,
                heartalignment=alertheartalignment,
                heartalignmenttext=alertheartalignmenttext,
                heumaticfever=alertheumaticfever,
                heumaticfevertext=alertheumaticfevertext,
                asthma=alertasthma,
                asthmatext=alertasthmatext,
                tuberculosis=alerttuberculosis,
                tuberculosistext=alerttuberculosistext,
                heart=alertheart,
                hearttext=alerthearttext,
                dentalissues=alertdentalissues,
                dentalissuestext=alertdentalissuestext,
                previousillness=alertpreviousillness,
                previousillnesstext=alertpreviousillnesstext,
                presentmedicalcare=alertpresentmedicalcare,
                presentmedicalcaretext=alertpresentmedicalcaretext,
                anydrugs=alertanydrugs,
                anydrugstext=alertanydrugstext,
                femalepatients=alertfemalepatients,
                femalepatientstext=alertfemalepatientstext,
                alertallergies=alertallergies,
                alertallergiestext=alertallergiestext,
                remarks=alertremarks,
                doctor_id=request.user.id

            )
        else:
            p = Alerts(
                patient_id=patid,
                bloodpressure=alertbloodpreessure,
                bloodpressuretext=alertbloodpreessuretext,
                heartalignment=alertheartalignment,
                heartalignmenttext=alertheartalignmenttext,
                heumaticfever=alertheumaticfever,
                heumaticfevertext=alertheumaticfevertext,
                asthma=alertasthma,
                asthmatext=alertasthmatext,
                tuberculosis=alerttuberculosis,
                tuberculosistext=alerttuberculosistext,
                heart=alertheart,
                hearttext=alerthearttext,
                dentalissues=alertdentalissues,
                dentalissuestext=alertdentalissuestext,
                previousillness=alertpreviousillness,
                previousillnesstext=alertpreviousillnesstext,
                presentmedicalcare=alertpresentmedicalcare,
                presentmedicalcaretext=alertpresentmedicalcaretext,
                anydrugs=alertanydrugs,
                anydrugstext=alertanydrugstext,
                femalepatients=alertfemalepatients,
                femalepatientstext=alertfemalepatientstext,
                alertallergies=alertallergies,
                alertallergiestext=alertallergiestext,
                remarks=alertremarks,
                doctor_id=request.user.id

            )
            p.save()

    alert = Alerts.objects.filter(patient_id = patid).values('bloodpressure','bloodpressuretext','heartalignment','heartalignmenttext',
                                                              'heumaticfever','heumaticfevertext','asthma','asthmatext','tuberculosis',
                                                              'tuberculosistext','heart','hearttext','dentalissues','dentalissuestext',
                                                              'previousillness','previousillnesstext','presentmedicalcare','presentmedicalcaretext',
                                                              'anydrugs','anydrugstext','femalepatients','femalepatientstext','alertallergies',
                                                               'alertallergiestext','remarks'
                                                              )
    if alert.exists():
        alert=alert.get()
    context={'alert':alert}
    print(context)
    return render(request,'doctoractivities/alert.html',context)

def prescription(request):
    patid = request.session['patid']
    if request.method == 'POST':
        p=Prescription(patient_id = patid,
                      medicine_id = request.POST.get('prescriptionmedicine'),
                      pattern = request.POST.get('prescriptionpattern'),
                      days = request.POST.get('prescriptiondays'),
                      instructions = request.POST.get('prescriptioninstruction'),
                      doctor_id =request.user.id
                     )
        p.save()
    prescription = Prescription.objects.filter(patient_id= patid).values('id','medicine__medicine','pattern','days','instructions','doctor__username','created_at')
    medicine =Medicine.objects.all().values('medicine','id')
    context = {'medicines':medicine,'prescriptions':prescription}
    return render(request,'doctoractivities/prescription.html',context)

def radiologyimages(request):
    print(request.FILES)
    patid = request.session['patid']
    if request.method == 'POST':
        type= request.POST.get('radilogycategorytype')
        if type== 'request':
            p = Radilogy(patient_id=patid,
                         documenttype=request.POST.get('radilogycategory'),
                         toothno=request.POST.get('radilogytoothno'),
                         instructions=request.POST.get('radiologyinstruction'),
                         doctor_id=request.user.id,
                         requesttype=request.POST.get('radilogycategorytype')
                         )
            p.save()
        else:
            myfile = request.FILES['radilogyuploadfile']
            fs = FileSystemStorage()
            filename = fs.save('radiology/' + myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            p = Radilogy(patient_id=patid,
                     uploadedfile=uploaded_file_url,
                     documenttype=request.POST.get('radilogycategory'),
                     toothno=request.POST.get('radilogytoothno'),
                     instructions=request.POST.get('radiologyinstruction'),
                     doctor_id=request.user.id,
                     requesttype=request.POST.get('radilogycategorytype')
                     )
            p.save()


    radiology = Radilogy.objects.filter(patient_id= patid).values('documenttype','toothno','uploadedfile','id','doctor__username','requesttype').order_by('-created_at')

    context ={'radiologyimages':radiology}
    return render(request,'doctoractivities/radiologyimages.html',context)

def billing(request):
    patid = request.session['patid']
    if request.method == 'POST':
        p = Billing(patient_id=patid,
                         billdate=request.POST.get('billingdate'),
                         mode=request.POST.get('paymentmode'),
                         transactionamount=request.POST.get('transactionamount'),
                         createdby_id=request.user.id
                         )
        p.save()
    billing=Billing.objects.filter(patient_id=patid).values('id','billdate','mode','transactionamount','createdby__username')
    context ={'billings':billing}
    return render(request, 'doctoractivities/billing.html',context)

def checkout(request):
    patid=request.session['patid']

    p= CheckedinPatient.objects.filter(title_id = patid)
    p.update(status=False,checkouttime = date.today())

    return redirect('/home')

def dentalchart(request):
    patid = request.session['patid']
    diagnosises = Diagnosis.objects.all().values('id','diagnosis')
    treatments = Treatment.objects.all().values('id','treatment','amount','taxpercentage')
    treatmentdetails = Treatmentdetails.objects.filter(patient_id =patid ).values('id','updated_date','teeth','diagnosis__id','diagnosis__diagnosis','treatment__treatment','treatment__id','fee','discount',
                                                                                  'payable','clinical_notes','doctor__username','status'
                                                                                  )
    context={'diagnosises':diagnosises,'treatments':treatments,'treatmentdetails':treatmentdetails}
    return render(request, 'doctoractivities/dentalchart.html',context)

@csrf_exempt
def savetreatment(request):
    try:
        patid = request.session['patid']
        details = request.POST.getlist('detail[]')

        for detail in details:
            data = json.loads(detail)
            treatmentid = data['id']
            p = Treatmentdetails.objects.filter(id=treatmentid,patient_id=patid)

            if data['treatment'] =='' or data['treatment'] == 'None':

                treatmentmentdata = None
            else:
                treatmentmentdata = data['treatment']
            if data['fee'] == '':
                fee = 0
            else:
                fee = data['fee']
            if data['discount'] == '':
                discount = 0
            else:
                discount = data['discount']
            if data['payable'] == '':
                payable = 0
            else:
                payable = data['payable']

            if p.exists():

                p.update(
                    teeth=data['teethno'],
                    diagnosis_id=Diagnosis.objects.filter(diagnosis=data['diagnosis']).values('id').get()['id'],
                    treatment=treatmentmentdata,
                    fee=fee,
                    discount=discount,
                    payable=payable,
                    clinical_notes='hello',
                    doctor_id=request.user.id,
                    status=data['statustreatment']
                )
            else:

                p=Treatmentdetails(
                    patient_id=patid,
                    teeth = data['teethno'],
                    diagnosis_id = Diagnosis.objects.filter(diagnosis =data['diagnosis']).values('id').get()['id'],
                    treatment = treatmentmentdata,
                    fee = fee,
                    discount = discount,
                    payable = payable,
                    clinical_notes = data['clinicalnotes'],
                    doctor_id = request.user.id,
                    status = data['statustreatment']
                )
                p.save()

        data = {'status':'true'}
    except Exception as e:
        print(str(e))
        data = {'status': 'true'}
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
    return JsonResponse(data)
@csrf_exempt
def getfee(request):
    treatmentid = request.POST.get('treatmentid')
    treatmentdata = Treatment.objects.filter(id=treatmentid).values('amount','taxpercentage').get()

    data={'status':'true','amount':treatmentdata['amount'],'tax':treatmentdata['taxpercentage']}
    return JsonResponse(data)

@csrf_exempt
def saveeditedtreatment(request):
    patid = request.session['patid']
    id = request.POST.get('id')
    teethno = request.POST.get('teethno')
    diagnosis = request.POST.get('diagnosis')
    treatment = request.POST.get('treatment')
    fee = request.POST.get('fee')
    discount = request.POST.get('discount')
    payable = request.POST.get('payable')
    status = request.POST.get('status')
    clinicalnotes = request.POST.get('clinicalnotes')
    p = Treatmentdetails.objects.filter(id=id, patient_id=patid)
    if p.exists():
        p.update(
            teeth=teethno,
            diagnosis_id=diagnosis,
            treatment_id=treatment,
            fee=fee,
            discount=discount,
            payable=payable,
            clinical_notes=clinicalnotes,
            doctor_id=request.user.id,
            status=status
        )
    else:
        p = Treatmentdetails(
            patient_id=patid,
            teeth=teethno,
            diagnosis_id=diagnosis,
            treatment_id=treatment,
            fee=fee,
            discount=discount,
            payable=payable,
            clinical_notes=clinicalnotes,
            doctor_id=request.user.id,
            status=status
        )
        p.save()
    data={'status':'true'}
    return JsonResponse(data)