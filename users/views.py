from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Profile
from django.contrib import messages
from .forms import CustomUserCreationForm
# Create your views here.


def loginUser(request):
	page = 'login'
	context = {'page':page}
	if request.user.is_authenticated:
		return redirect('profiles')

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		try:
			user = User.objects.get(username = username )

		except:
			messages.error(request, 'User does not exist')
		user = authenticate(request,username= username, password = password)

		if user is not None:
			login(request,user)
			return redirect('profiles')
		else:
			messages.error(request, 'User name or password is not correct')


	return render(request,'users/login_register.html',context)

def logoutUser(request):
	logout(request)
	messages.error(request, 'successfully logged out')
	return redirect('login')
def registerUser(request):
	page = 'register'
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username.lower()
			user.save()
			messages.success(request,'User account was created');
			login(request,user)
			return redirect('profiles')
		else:
			messages.error(request,'Error occured during registration');
	context = {'page':page,'form':form}
	return render(request,'users/login_register.html',context)
@login_required(login_url = 'login')
def profiles(request):
	profiles = Profile.objects.all()
	context = {'profiles':profiles}
	return render(request,'users/profiles.html',context)