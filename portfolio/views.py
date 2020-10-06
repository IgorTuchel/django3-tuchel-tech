from django.shortcuts import render
from .models import Project
import random, string

# Create your views here.
def home(request):
	projects = Project.objects.all()
	return render(request, 'portfolio/home.html', {'projects':projects})
def genpass(request):
	return render(request, 'portfolio/passwordgen.html')	

def password(request):

	thepassword = ''

	

	Lcharacters = string.ascii_lowercase
	Hcharacters = string.ascii_uppercase
	Ncharacters = string.digits
	Pcharacters = string.punctuation

	passList = list(Lcharacters)

	if request.GET.get('uppercase'):
		passList.extend(list(Hcharacters))
	if request.GET.get('numbers'):
		passList.extend(list(Ncharacters))
	if request.GET.get('special'):
		passList.extend(list(Pcharacters))	

	length = int(request.GET.get('length', 12))
	

	for x in range(length):
		thepassword += random.choice(passList)

	return render(request, 'portfolio/password.html', {'password':thepassword})