from django.shortcuts import render
from testapp.models import *
 # Create your views here.
def Home_Page_view(request):
    return render(request,'testapp/results.html')
def Hyd_Jobs_view(request):
    Hyd_Jobs_list=HydJobs.objects.all()
    return render(request,'testapp/hydjobs.html',{'Hyd_Jobs_list':Hyd_Jobs_list})
def Blore_Jobs_view(request):
    Blore_Jobs_list=BloreJobs.objects.all()
    return render(request,'testapp/blorejobs.html',{'Blore_Jobs_list':Blore_Jobs_list})
def Pune_Jobs_view(request):
    Pune_Jobs_list=PuneJobs.objects.all()
    return render(request,'testapp/punejobs.html',{'Pune_Jobs_list':Pune_Jobs_list})
