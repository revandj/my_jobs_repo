from django.shortcuts import render
from testapp.models import HydJobs,BngJobs,PuneJobs
# Create your views here.

def Homepage_view(request):
    return render(request,'testapp/index.html')

def HydJobs_view(request):
    job_list=HydJobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/HydJobs.html',context=my_dict)

def BngJobs_view(request):
    job_list=BngJobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/BngJobs.html',context=my_dict)

def PuneJobs_view(request):
    job_list=PuneJobs.objects.all()
    my_dict={'job_list':job_list}
    return render(request,'testapp/PuneJobs.html',context=my_dict)
