from django.db import models
from receptionactivities.models import  Patient
from django.contrib.auth.models import User
# Create your models here.

class Diagnosis(models.Model):
    diagnosis = models.CharField(max_length=1000)
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=10)

class Treatment(models.Model):
    treatment = models.CharField(max_length=1000)
    description = models.CharField(max_length=4000,null=True)
    code = models.CharField(max_length=10,null=True)
    amount = models.FloatField()
    taxpercentage = models.FloatField()
    type=models.CharField(max_length=100)

class Medicine(models.Model):
    genericname = models.CharField(max_length=100)
    medicine = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.genericname + self.medicine

class Alerts(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True)
    bloodpressure = models.BooleanField()
    bloodpressuretext = models.CharField(max_length=1000,null=True)
    heartalignment = models.BooleanField()
    heartalignmenttext = models.CharField(max_length=1000,null=True)
    heumaticfever = models.BooleanField()
    heumaticfevertext = models.CharField(max_length=1000,null=True)
    asthma = models.BooleanField()
    asthmatext = models.CharField(max_length=1000,null=True)
    tuberculosis = models.BooleanField()
    tuberculosistext = models.CharField(max_length=1000,null=True)
    heart = models.BooleanField()
    hearttext = models.CharField(max_length=1000,null=True)
    dentalissues = models.BooleanField()
    dentalissuestext = models.CharField(max_length=1000,null=True)
    previousillness = models.BooleanField()
    previousillnesstext = models.CharField(max_length=1000,null=True)
    presentmedicalcare = models.BooleanField()
    presentmedicalcaretext = models.CharField(max_length=1000,null=True)
    anydrugs = models.BooleanField()
    anydrugstext = models.CharField(max_length=1000,null=True)
    femalepatients = models.BooleanField()
    femalepatientstext = models.CharField(max_length=1000,null=True)
    alertallergies = models.BooleanField()
    alertallergiestext = models.CharField(max_length=1000,null=True)
    remarks = models.CharField(max_length=4000,null=True)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)

class Radilogy(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    uploadedfile = models.FileField(null=True)
    documenttype = models.CharField(max_length=10,null=True)
    toothno = models.IntegerField(null=True)
    instructions= models.CharField(max_length = 4000,null=True)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    requesttype= models.CharField(max_length=10,null=True)

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    medicine = models.ForeignKey(Medicine,on_delete = models.SET_NULL, null=True)
    pattern = models.IntegerField()
    days = models.CharField(max_length=10)
    instructions= models.CharField(max_length = 4000,null=True)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateField(auto_now_add=True, null=True)

class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    billdate = models.DateField(auto_now_add=True)
    mode = models.CharField(max_length=100)
    transactionamount = models.FloatField()
    createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Treatmentdetails(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    teeth = models.CharField(max_length=10)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.SET_NULL, null=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.SET_NULL, null=True)
    fee = models.FloatField()
    discount = models.FloatField()
    payable = models.FloatField()
    clinical_notes = models.CharField(max_length=4000)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=50,null=True)
