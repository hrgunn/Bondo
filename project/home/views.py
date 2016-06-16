from django.shortcuts import render, redirect
from django.views.generic import View
from home.models import Home
from home.forms import HomeForm
from pprint import pprint as p
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect


# Create your views here.
class Home(View):
	form = HomeForm
	template = 'home/home.html'

	def get(self, request):
		if request.user.is_authenticated():

			return render(request, self.template, {
				'form': self.form(),
				
			})
		return redirect('/home/login')
		# return redirect('home/login')
	def post(self, request):
		form = self.form(request.POST)
		print(form)
		# if form.is_valid():

		# 	else:
		# 	url = form.save()
				
		return render(request, self.template, {'form': form})

class UserLogin(View):
	template = 'home/login.html'
	form = AuthenticationForm
	def get(self, request):
		return render(request, self.template, {'login': self.form()})

	def post(self, request):
		
		form = AuthenticationForm( None,request.POST )

		if form.is_valid():
			login(request, form.get_user())
			request.session['count'] = 0
			return HttpResponseRedirect('/home/')
		else:
			return render(request, self.template, {'login': form, })

class UserCreate(View):
	template_name = 'home/create.html'
	form = UserCreationForm

	def get(self, request):

		return render(request, self.template_name, {'form': self.form()})

	def post(self, request):
		form = self.form(request.POST)

		if form.is_valid():
			form = form.save()
			print (form)
			return redirect('/home/login')

		return render(request, self.template_name, {'form': form})

class Created(View):
	template_name = 'home/user_created'
	form = AuthenticationForm

	def get(self, request):

		return render(request, self.template_name, {'form': form})

class UserLogout(View):
	def post(self, request):
		logout( request )

		return redirect('/home/login')
# def home(request):
#   return render(request, "Home/home.html", {"form": HomeForm()})

# def create(request):
#   if request.method == "GET":
#     context = {
#       "form": HomeForm(),
#     }
#     return render(request, '/create.html', context)
#   elif request.method == "POST":
#     form = TodoForm(request.POST)
#     if form.is_valid():
#       form.save()
#     return redirect("/")

