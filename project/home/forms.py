from django import forms
from .models import Home

class HomeForm(forms.ModelForm):
  class Meta:
    model = Home
    widgets = {"user" : forms.HiddenInput(),
               "description" : forms.TextInput(),
               "Inventory_Choices" : forms.CheckboxSelectMultiple(),
               "Include_Choices" : forms.CheckboxSelectMultiple(),
               "Limit_Offerings_Choices": forms.CheckboxSelectMultiple(),
               "View": forms.CheckboxSelectMultiple(),
               "Bond_Type":  forms.CheckboxSelectMultiple(),
               }

    fields = [
      "CUSIP", 
      "description",
      "state",
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
      "Inventory_Choices",
      "Include_Choices",
      "Limit_Offerings_Choices",
      "View",
      "Spread",
      "Bond_Type",
      "Sectors",

      ]

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = Login
# 		widgets = {
# 					'Password': forms.PasswordInput(),}
# 		fields = ('Username','Password')



