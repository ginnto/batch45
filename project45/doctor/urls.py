from django.urls import path
from . import views

urlpatterns = [
    path('docsections',views.doctorsec,name='docsection'),
    path('patientreport/<int:Id>', views.patientrepo, name='patientreport'),
    path('paitentlist/<int:ID>', views.patient_list, name='plist'),

    ]