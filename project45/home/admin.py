from django.contrib import admin
from . models import *
# Register your models here.

class dep(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Department,dep)


class doc(admin.ModelAdmin):
    list_display = ['name','img','contact']
    list_editable = ['img','contact']
admin.site.register(Doctors,doc)



admin.site.register(Patients)



admin.site.register(Discharge)

admin.site.register(DoctorReport)
