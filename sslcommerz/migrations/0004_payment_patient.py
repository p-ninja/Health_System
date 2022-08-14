# Generated by Django 4.0.6 on 2022-08-14 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0004_alter_hospital_information_address'),
        ('sslcommerz', '0003_remove_payment_patient_payment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hospital.patient'),
        ),
    ]
