# Generated by Django 4.0.6 on 2022-08-27 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_alter_doctor_information_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_information',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
