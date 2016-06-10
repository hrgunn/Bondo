from django.shortcuts import render, redirect
from django.views.generic import View
from home.models import Home
from home.forms import HomeForm, LoginForm
from pprint import pprint as p
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
# Create your views here.
class Home(View):
	form = HomeForm
	template = 'home/login.html'

	def get(self, request):
		if request.user.is_authenticated():

			homeUser = request.GET.get('Username', None)
			Username = Url.objects.filter(user=request.user)
			return render(request, self.template, {
				'form': self.form(initial={'user':request.user}),
				
			})
		return render(request, self.template, {'form': HomeForm(), 'login': LoginForm()})
		# return redirect('home/login')
	# def post(self, request):
	# 	form = self.form(request.POST)


	# 	if form.is_valid():
	# 		if Url.objects.filter(url=request.POST['Username']).exists():
	# 			url = Url.objects.get(Username=request.POST['Username'])
	# 		else:
	# 			url = form.save()
	# 			request.session['count'] += 1
	# 		return redirect('/add?shortCode='+ url.shortCode)
	# 	return render(request, self.template, {'form': form, 'show': request.session['new']})

class UserLogin(View):
	template = 'home/login.html'
	form = AuthenticationForm
	def get(self, request):
		print(self.template)
		return HttpResponseRedirect('/home/login')

	def post(self, request):
		
		form = AuthenticationForm( None,request.POST )

		if form.is_valid():
			login(request, form.get_user())
			request.session['count'] = 0
			return HttpResponseRedirect('/home/')
		else:
			return render(request, self.template, {'login': form})

class UserCreate(View):
	template = 'home/user.html'
	form = UserCreationForm

	def get(self, request):

		return render(request, self.template, {'form': self.form()})

	def post(self, request):
		form = self.form(request.POST)

		if form.is_valid():
			user = form.save()
			return redirect('home/login')

		return render(request, self.template, {'form': form})


class UserLogout(View):
	def get(self, request):
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

