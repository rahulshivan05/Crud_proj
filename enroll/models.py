from django.db import models


class User2(models.Model):
	image = models.ImageField(upload_to='images/', blank=True, help_text='This is Blank Field')
	name = models.CharField(max_length=100, help_text='Enter your Full Name')
	email = models.EmailField(help_text='Enter valid Email (xyz@gmail.com)')
	password = models.CharField(max_length=100, help_text='Your password must contain at least 8 characters.')
	ip_address = models.CharField(max_length=50, blank=True)
