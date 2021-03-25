from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User2
import socket
from ipware import get_client_ip
import httpagentparser
import platform
import ipapi


def add_show(request):
	error_message = None
	data = ipapi.location(output='json')
	# print(data)
	# print(request.get_host())
	# print(socket.gethostname())
	# user.ipaddress = get_ip(request)
	# print(user.ipaddress)
	# ipaddress=get_ip(request) 
	# print(request.build_absolute_uri())
	# print(request.META['HTTP_USER_AGENT'])
	# print(request.headers)

	# Only find the user agent in (request.headers)
	# print(request.headers['User-Agent'])

	agent = request.environ.get('HTTP_USER_AGENT')
	browser = httpagentparser.detect(agent)
	os = platform.system()

	if not browser:
	    browser = agent.split('/')[0]
	else:
	    browser = browser['browser']['name']  


	if request.method == 'POST':
		form = StudentRegistration(request.POST)
		if form.is_valid():
			nm = form.cleaned_data['name']
			em = form.cleaned_data['email']
			pw = form.cleaned_data['password']
			reg = User2(name=nm, email=em, password=pw)
			reg.save()
			form = StudentRegistration()
	else:
		form = StudentRegistration()
	stud = User2.objects.all()

	context = {
		'form': form,
		'stu': stud,
		'browser': browser,
		'os': os,
		'data': data,
	}

	return render(request, 'enroll/addandshow.html', context)

def update_data(request, id):
	if request.method == 'POST':
		pi = User2.objects.get(pk=id)
		form = StudentRegistration(request.POST, instance=pi)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')

	pi = User2.objects.get(pk=id)
	form = StudentRegistration(instance=pi)
	context = {
		'form': form,
	}	
	return render(request, 'enroll/update.html', context)



def delete_data(request, id):
	if request.method == 'POST':
		pi = User2.objects.get(pk=id)
		pi.delete()
		return HttpResponseRedirect('/')






