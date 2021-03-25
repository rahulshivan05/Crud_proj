from django.core import validators
from django import forms
from enroll.models import User2
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentRegistration(forms.ModelForm):

	class Meta:
		model = User2
		fields = ['name', 'email', 'password']
		# exclude = []
		widgets = {
			'password': forms.PasswordInput(render_value=True)
		}







