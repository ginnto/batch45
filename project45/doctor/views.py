from django.shortcuts import render, get_object_or_404
from home . models import *
# Create your views here.

def doctorsec(request):
    doc= Doctors.objects.all()
    return render(request,'docsection.html',{'j':doc})

def patientrepo(request,Id):
    pat = get_object_or_404(Discharge,patient=Id)
    return render(request,'patientreport.html',{'dr':pat})

def patient_list(request,ID):
    pat = Patients.objects.all().filter(Doctor=ID)                                                                                                # select * from patients where doctor = id;
    return render(request, 'patientList.html',{'p':pat})
