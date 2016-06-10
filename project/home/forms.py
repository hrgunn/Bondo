from django import forms
from .models import Home, Login

class HomeForm(forms.ModelForm):
  class Meta:
    model = Home
    widgets = {'user': forms.HiddenInput()}
    fields = [
      "CUSIP", 
      "description",
      # "Spread",
      # "States",
      "quantity_min",
      "quantity_max",
      "years_min",
      "years_max",
      # "Maturity Minimum",
      # "Maturity Maximum",
      "coupon_min",
      "coupon_max",
      "price_min",
      "price_max",
      # "YTW Minimum",
      # "YTW Maximum",
      # "OID Yield Minimum",
      # "OID Yield Maximum",
      "Moodys_Rating_Minimum",
      "Moodys_Rating_Maximum",
      "SandP_Rating_Minimum",
      "SandP_Rating_Maximum",
      "Fitch_Ratings_Minimum",
      "Fitch_Ratings_Maximum",
      # "Call Protect Maximum",
      ]

class LoginForm(forms.ModelForm):
	class Meta:
		model = Login
		widgets = {
					'password': forms.PasswordInput(),}
		fields = ('username','password')



