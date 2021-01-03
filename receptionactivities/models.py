from django.db import models
from django.contrib.auth.models import User
import arrow
# Create your models here.

class Patient(models.Model):
    salutation = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100,null=True)
    lastname = models.CharField(max_length=100,null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10)
    phonenumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=100,null=True)
    addressline1 = models.CharField(max_length=100)
    addressline2 = models.CharField(max_length=100,null=True)
    addressline3 = models.CharField(max_length=10,null=True)
    location = models.CharField(max_length=100,null=True)
    country = models.CharField(max_length=100)
    postcode = models.IntegerField(null=True)
    state = models.CharField(max_length=10)
    city = models.CharField(max_length=100)

class ExistingPatientAppointmentevents(models.Model):
    taskid = models.CharField(max_length=50, blank=True, editable=False)
    title = models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    doctor = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)


    def schedule_reminder(self):
        """Schedule a Dramatiq task to send a reminder for this appointment"""

        # Calculate the correct time to send this reminder
        appointment_time = arrow.get(self.start)
        reminder_time = appointment_time.shift(minutes=-5)
        now = arrow.now()
        milli_to_wait = int(
            (reminder_time - now).total_seconds()) * 1000

        # Schedule the Dramatiq task
        from .tasks import send_sms_reminder
        result = send_sms_reminder.send_with_options(
            args=(self.pk,),
            delay=milli_to_wait)

        return result.options['redis_message_id']

    # def save(self, *args, **kwargs):
    #     """Custom save method which also schedules a reminder"""
    #
    #     # Check if we have scheduled a reminder for this appointment before
    #     if self.taskid:
    #         # Revoke that task in case its time has changed
    #         self.cancel_task()
    #
    #     # Save our appointment, which populates self.pk,
    #     # which is used in schedule_reminder
    #     super(ExistingPatientAppointmentevents, self).save(*args, **kwargs)
    #
    #     # Schedule a new reminder task for this appointment
    #     self.taskid = self.schedule_reminder()
    #     print('save')
    #     # Save our appointment again, with the new task_id
    #     super(ExistingPatientAppointmentevents, self).save(*args, **kwargs)

    def cancel_task(self):
        redis_client = redis.Redis(host=settings.REDIS_LOCAL, port=6379, db=0)
        redis_client.hdel("dramatiq:default.DQ.msgs", self.taskid)

class NewPatientAppointmentevents(models.Model):
    title = models.CharField(max_length=100)
    phonenumber  = models.CharField(max_length=15)
    start = models.DateTimeField()
    end = models.DateTimeField()
    doctor = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)



class CheckedinPatient(models.Model):
    title = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    checkedintime = models.DateTimeField(auto_now_add=True)
    doctor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    checkouttime = models.DateTimeField(null=True)
    status = models.BooleanField(null=True)

class CountryList(models.Model):
    sortname=models.CharField(max_length=10,null=True)
    name=models.CharField(max_length=100,null=True)
    phonecode = models.IntegerField(null=True)

class StateList(models.Model):
    name=models.CharField(max_length=100,null=True)
    country=models.ForeignKey(CountryList, on_delete=models.SET_NULL, null=True)

