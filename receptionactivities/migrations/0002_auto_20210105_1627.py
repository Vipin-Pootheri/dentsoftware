# Generated by Django 3.0 on 2021-01-05 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionactivities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='existingpatientappointmentevents',
            name='ischeckedin',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='newpatientappointmentevents',
            name='ischeckedin',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='newpatientappointmentevents',
            name='isregistered',
            field=models.BooleanField(null=True),
        ),
    ]
