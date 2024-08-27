from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.

def index(request):
    obj = Doctors.objects.all()   # select * from doctors
    # -------------------------------------------
    var = Paginator(obj,1)
    pgnum = int(request.GET.get('page', 1))

    try:
        doc = var.page(pgnum)
    except(InvalidPage, EmptyPage):
        doc = var.page(var.num_pages)
   #----------------------------------------------
    return render(request,'index.html',{'var':doc})
