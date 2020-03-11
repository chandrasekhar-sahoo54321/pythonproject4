from django.contrib import admin
from testapp.models import EnquiryModel,Jobs,Apply

# Register your models here.
class EnquiryAdmin(admin.ModelAdmin):
	list_display=['name','email','phone','message']
admin.site.register(EnquiryModel,EnquiryAdmin)
class JobsAdmin(admin.ModelAdmin):
	list_display=['date','company','title','eligibility','address','email','phone']
admin.site.register(Jobs,JobsAdmin)
class ApplyAdmin(admin.ModelAdmin):
	list_display=['Name','Email','Mobile','Gender','Designation','Location','DOB','Qualification','Experience','Language','Nationality','year_of_passout','job_type','current_ctc','expected_ctc']
admin.site.register(Apply,ApplyAdmin)
