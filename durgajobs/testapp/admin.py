from django.contrib import admin
from testapp.models import HydJobs,BngJobs,PuneJobs
# Register your models here.

class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company_name','title','eligibility','addrs','email','phone_number']

admin.site.register(HydJobs,HydJobsAdmin)

class BngJobsAdmin(admin.ModelAdmin):
    list_display=['date','company_name','title','eligibility','addrs','email','phone_number']

admin.site.register(BngJobs,BngJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company_name','title','eligibility','addrs','email','phone_number']

admin.site.register(PuneJobs,PuneJobsAdmin)
