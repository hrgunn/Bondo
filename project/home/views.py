from django.shortcuts import render, redirect
from django.views.generic import View
from home.models import (
	Market, BroadRange, 
	Characteristic, QuickSearch
)
from home.forms import (
	BroadRangeForm, QuickSearchForm, 
	CharacteristicForm
	, MarketForm, APIForm, ScreenBondForm,
	MoodyBondForm
)
from pprint import pprint as p
from django.contrib.auth import (
	authenticate, login, logout
)
from django.contrib.auth.forms import (
	UserCreationForm, AuthenticationForm
)
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from home.xignite_bonds import XigniteCorporateBonds, XigniteBondMaster


# Create your views here.
class Home(View):
	form = BroadRangeForm
	template_name = 'home/home.html'

	def get(self, request):
		if request.user.is_authenticated():
			return render(request, self.template_name, {
				'bond_range_form': self.form(),
				'quick_search_form': QuickSearchForm(),
				'characteristic_form': CharacteristicForm(),
				'market_form': MarketForm(),
				'search_form': APIForm(),
				'screen_bond_form': ScreenBondForm(),
				'moody_bond_form': MoodyBondForm(),
			})
		return redirect('/home/login')
		# return redirect('home/login')
	def post(self, request):
		form = self.form(request.POST)
		print(form)
		# if form.is_valid():

		# 	else:
		# 	url = form.save()
				
		return render(request, self.template_name, {'form': form})

class UserLogin(View):
	template_name = 'home/login.html'
	form = AuthenticationForm
	def get(self, request):
		print('UserLogin')
		return render(request, self.template_name, {'login': self.form()})

	def post(self, request):
		
		form = AuthenticationForm( None,request.POST )

		if form.is_valid():
			login(request, form.get_user())
			request.session['count'] = 0
			return HttpResponseRedirect('/home/')
		else:
			return render(request, self.template_name, {'login': form, })

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

class SearchForm(View):
	form = APIForm

	def get(self, request):
		form = self.form(request.GET)
		if form.is_valid():
			wrapper = XigniteCorporateBonds()
			# return render(request, self.template_name, {'form': form})
			print (form.data)
			data = wrapper.get_last_sale(**form.data)
			return JsonResponse({'data': data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class QuickSearch(View):
	template_name = 'home/quick_search'
	form = QuickSearchForm

	def get(self, request):
		form = QuickSearchForm(request.GET)
		if form.is_valid():
			wrapper = XigniteCorporateBonds()
			# return render(request, self.template_name, {'form': form})
			print (form.data['CUSIP'])
			data = wrapper.get_last_sale(Identifier = form.data['CUSIP'], IdentifierType = 'CUSIP', PriceSource = 'FINRA')
			return JsonResponse({'data': data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)


class BroadSearch(View):
	template_name = 'home/broad_search'
	form = BroadRangeForm

	def get(self, request):
		form = BroadRangeForm(request.GET)
		if form.is_valid():
			# return render(request, self.template_name, {'form': form})
			return JsonResponse({'data':form.data})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class Markets(View):
	template_name = 'home/markets'
	form = MarketForm

	def get(self, request):
		form = MarketForm(request.GET)
		if form.is_valid():
			# return render(request, self.template_name, {'form': form})
			return JsonResponse({'data':form.data})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class Characteristic(View):
	template_name = 'home/characteristic'
	form = CharacteristicForm

	def get(self, request):
		form = CharacteristicForm(request.GET)
		if form.is_valid():
			# return render(request, self.template_name, {'form': form})
			return JsonResponse({'data':form.data})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class ScreenBond(View):
	form = ScreenBondForm

	def get(self, request):
		form = self.form(request.GET)
		if form.is_valid():
			wrapper = XigniteBondMaster()
			# return render(request, self.template_name, {'form': form})
			print (form.data)
			data = wrapper.get_screen_bonds(**form.data)
			return JsonResponse({'data': data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class Moodys(View):
	form = MoodyBondForm
	
	def get(self, request):
		form = self.form(request.GET)
		if form.is_valid():
			wrapper = MoodyAPI()
			# return render(request, self.template_name, {'form': form})
			print (form.data)
			data = wrapper.get_moody(**form.data)
			return JsonResponse({'data': data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)


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

