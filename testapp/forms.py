from django import forms
from testapp.models import EnquiryModel,Jobs
from django.contrib.auth.models import User
class Enquiry(forms.ModelForm):
	class Meta:
		model=EnquiryModel
		fields='__all__'
class JobsForm(forms.ModelForm):
	class Meta:
		model=Jobs
		fields='__all__'
class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['username','password','email','first_name','last_name']
			