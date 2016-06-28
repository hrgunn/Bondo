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
	MoodyBondForm, MerrillLynchForm, ChicagoForm
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
from home.wrapper import XigniteCorporateBonds, XigniteBondMaster, MoodyAPI, ChicagoMercantileExchange, Merrill_Lynch


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
				'merril_lynch_form': MerrillLynchForm(),
				'chicago_form': ChicagoForm(),

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
	template_name = 'home/search.html'
	form = APIForm()

	# def get(self, request):
	# 	content = {
	# 		'search_form': self.form,
	# 	}
	# 	return render(request, self.template_name, content)

	def post(self, request):
		form = APIForm(data=request.POST)
		if form.is_valid():
			wrapper = XigniteCorporateBonds()
			wrapper2 = XigniteBondMaster()
			wrapper3 = MoodyAPI()
			wrapper4 = Merrill_Lynch()
			wrapper5 = ChicagoMercantileExchange()
			# return render(request, self.template_name, {'form': form})
			print (form.data)
			get_screen_bonds = wrapper2.get_screen_bonds(**form.data)
			get_moody = wrapper3.get_moody(**form.data)
			get_merrill = wrapper4.get_merrill(**form.data)
			get_chicago = wrapper5.get_chicago(**form.data)
			return JsonResponse({'get_last_sale': get_last_sale.text, 'get_last_sales': get_last_sales.text,
			'get_price_composite': get_price_composite.text, 'get_price_composites': get_price_composites.text, 'get_daily_open_high_low_close_price' : get_daily_open_high_low_close_price.text,
			'get_daily_open_high_low_close_prices': get_daily_open_high_low_close_prices.text, 'get_yearly_high_low_price': get_yearly_high_low_price.text,
			'get_yearly_high_low_prices': get_yearly_high_low_prices.text, 'get_yield': get_yield.text, 'get_yields' : get_yields.text,
			'get_accrued_interest': get_accrued_interest.text, 'get_accrued_interests': get_accrued_interests.text, 
			'get_bond_calculation': get_bond_calculation.text, 'get_bond_calculations': get_bond_calculations.text,
			'get_duration_and_convexity': get_duration_and_convexity.text, 'get_duration_and_convexities:': get_duration_and_convexities.text,
			'get_screen_bonds': get_screen_bonds.text, 'get_moody': get_moody.text, 'get_merrill': get_merrill.text, 
			'get_chicago': get_chicago.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class QuickSearch(View):
	template_name = 'home/quick_search.html'
	form = QuickSearchForm

	# def get(self, request):
	# 	content = {
	# 		'quick_search_form': self.form,
	# 	}
	# 	return render(request, self.template_name, content)

	def post(self, request):
		form = QuickSearchForm(data=request.POST)
		if form.is_valid():
			data = {}
			wrapper = XigniteCorporateBonds()
			data['get_last_sale'] = wrapper.get_last_sale(**form.data)
			data['get_last_sale'] = data['get_last_sale'].text
			# get_last_sales = wrapper.get_last_sales(**form.data)
			data['get_price_composite'] = wrapper.get_price_composite(**form.data)
			data['get_price_composite'] = data['get_price_composite'].text
			# get_price_composites = wrapper.get_price_composites(**form.data)
			data['get_daily_open_high_low_close_price'] = wrapper.get_daily_open_high_low_close_price(**form.data)
			data['get_daily_open_high_low_close_price'] = data['get_daily_open_high_low_close_price'].text
			# get_daily_open_high_low_close_prices = wrapper.get_daily_open_high_low_close_prices(**form.data)
			data['get_yearly_high_low_price'] = wrapper.get_yearly_high_low_price(**form.data)
			data['get_yearly_high_low_price'] = data['get_yearly_high_low_price'].text
			# get_yearly_high_low_prices = wrapper.get_yearly_high_low_prices(**form.data)
			data['get_yield'] = wrapper.get_yield(**form.data)
			data['get_yield'] = data['get_yield'].text
			# get_yields = wrapper.get_yields(**form.data)
			data['get_accrued_interest'] = wrapper.get_accrued_interest(**form.data)
			data['get_accrued_interest'] = data['get_accrued_interest'].text
			# get_accrued_interests = wrapper.get_accrued_interests(**form.data)
			data['get_bond_calculation'] = wrapper.get_bond_calculation(**form.data)
			data['get_bond_calculation'] = data['get_bond_calculation'].text
			# get_bond_calculations = wrapper.get_bond_calculations(**form.data)
			data['get_duration_and_convexity'] = wrapper.get_duration_and_convexity(**form.data)
			data['get_duration_and_convexity'] = data['get_duration_and_convexity'].text
			# get_duration_and_convexities = wrapper.get_duration_and_convexities(**form.data)

			# return render(request, self.template_name, {'form': form})
			# data = wrapper.get_last_sale(Identifier = form.data['CUSIP'], IdentifierType = 'CUSIP', PriceSource = 'FINRA')

			return JsonResponse({'data': data})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)


class BroadSearch(View):
	template_name = 'home/broad_range.html'
	form = BroadRangeForm

	# def get(self, request):
	# 	content = {
	# 		'bond_range_form': self.form,
	# 	}
	# 	return render(request, self.template_name, content)

	def post(self, request):
		form = BroadRangeForm(data=request.POST)
		if form.is_valid():
			# return render(request, self.template_name, {'form': form})
			return JsonResponse({'data': form.data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class Markets(View):
	template_name = 'home/markets.html'
	form = MarketForm()
	# def get(self, request):
	# 	content = {
	# 		'market_form': self.form,
	# 	}
	# 	return render(request, self.template_name, content)


	def post(self, request):
		form = MarketForm(data=request.POST)
		if form.is_valid():
			# return render(request, self.template_name, {'form': form})
			return JsonResponse({'data': form.data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class Characteristic(View):
	template_name = 'home/characteristics.html'
	form = CharacteristicForm()
	# def get(self, request):
	# 	content = {
	# 		'characteristic_form': self.form,
	# 	}
	# 	return render(request, self.template_name, content)


	def post(self, request):
		form = CharacteristicForm(data=request.POST)
		if form.is_valid():
			# return render(request, self.template_name, {'form': form})
			return JsonResponse({'data':form.data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class ScreenBond(View):
	template_name = 'home/screenbonds.html'
	form = ScreenBondForm()
	# def get(self, request):
	# 	content = {
	# 		'screen_bond_form': self.form,
	# 	}
	# 	return render(request, self.template_name, content)


	def post(self, request):
		form = self.form(data=request.POST)
		if form.is_valid():
			wrapper = XigniteBondMaster()
			# return render(request, self.template_name, {'form': form})
			print (form.data)
			data = wrapper.get_screen_bonds(**form.data)

			return JsonResponse({'data': form.data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class Moodys(View):
	form = MoodyBondForm
	
	# def get(self, request):
	# 	content = {
	# 		'MoodyBondForm': self.form(),
	# 	}
	# 	return render(request, self.template_name, content)

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			wrapper = MoodyAPI()
			# return render(request, self.template_name, {'form': form})
			print (form.data)
			data = wrapper.get_moody(**form.data)
			return JsonResponse({'data': data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)

class Merrill(View):
	form = MerrillLynchForm
	# def get(self, request):
	# 	content = {
	# 		'MerrillLynchForm': self.form(),
	# 	}
	# 	return render(request, self.template_name, content)

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			wrapper = Merrill_Lynch()
			# return render(request, self.template_name, {'form': form})
			print (form.data)
			data = wrapper.get_merrill(**form.data)
			return JsonResponse({'data': data.text})
		return JsonResponse({'error':'shit something went wrong','errors':form.errors.as_json()},status=500)


class Chicago(View):
	form = ChicagoForm

	# def get(self, request):
	# 	content = {
	# 		'ChicagoForm': self.form(),
	# 	}
	# 	return render(request, self.template_name, content)

	def post(self, request):
		form = self.form(request.POST)
		if form.is_valid():
			wrapper = ChicagoMercantileExchange()
			# return render(request, self.template_name, {'form': form})
			print (form.data)
			data = wrapper.get_chicago(**form.data)
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

