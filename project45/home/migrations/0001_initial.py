# Generated by Django 5.0.6 on 2024-07-03 04:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Discharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discharged', models.BooleanField(default=False)),
                ('admitted_date', models.DateField()),
                ('discharged_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='picture')),
                ('name', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=50)),
                ('department', models.ManyToManyField(to='home.department')),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Address', models.TextField()),
                ('Contact', models.CharField(max_length=50)),
                ('Symptoms', models.TextField()),
                ('Status', models.CharField(max_length=50)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.doctors')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
                ('update_date', models.DateField()),
                ('medicine', models.TextField()),
                ('conclusion', models.TextField()),
                ('admission_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.discharge')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.patients')),
            ],
        ),
        migrations.AddField(
            model_name='discharge',
            name='patient',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.patients'),
        ),
    ]
