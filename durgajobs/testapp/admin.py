from django.contrib import admin
from testapp.models import HydJobs,BloreJobs,PuneJobs
class HydJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonno']
class BloreJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonno']
class PuneJobsAdmin(admin.ModelAdmin):
    list_display=['date','company','title','eligibility','address','email','phonno']
admin.site.register(HydJobs,HydJobsAdmin)
admin.site.register(BloreJobs,BloreJobsAdmin)
admin.site.register(PuneJobs,PuneJobsAdmin)
