from django import forms
from .models import BroadRange, QuickSearch, Market, Characteristic, Bond_Type

class BroadRangeForm(forms.ModelForm):
  class Meta:
    model = BroadRange
    widgets = {"user" : forms.HiddenInput(),
               "description" : forms.TextInput(),
               }
    fields = [
    # "quantity_min",
    # "quantity_max",
    # "years_min",
    # "years_max",
    # # "Maturity Minimum",
    # # "Maturity Maximum",
    # "coupon_min",
    # "coupon_max",
    # "price_min",
    # "price_max",
    # "YTW Minimum",
    # "YTW Maximum",
    # "OID Yield Minimum",
    # "OID Yield Maximum",
    "Moodys_Rating_Minimum",
    "Moodys_Rating_Maximum",
    "Merrill_Lynch_Minimum",
    "Merrill_Lynch_Maximum",
    # "SandP_Rating_Minimum",
    # "SandP_Rating_Maximum",
    # "Fitch_Ratings_Minimum",
    # "Fitch_Ratings_Maximum",
  ]

class QuickSearchForm(forms.Form):
  
    Identifier = forms.CharField(required = False)
    IdentifierType = forms.ChoiceField(choices=( ('Symbol','Symbol'), ('CIK','CIK'), ('CUSIP','CUSIP'), ('ISIN','ISIN'), ('Valoren','Valoren'), ('SEDOL','SEDOL') ))
    PriceSource = forms.ChoiceField(choices=(('FINRA','FINRA'),))
  


class CharacteristicForm(forms.ModelForm):
  class Meta:
    model = Characteristic
    fields = [
      "bond_type","sectors","prerefund",
      "escrowed","insured","insurable",
      "taxable","amt","bank_q",
      "callable","putable","float_var_rt",
      "sinking_fund","convertible","zero_coupon"
    ]
    widgets = { 
                "bond_type":  forms.RadioSelect(attrs = {'class' : 'inline'}),
                "prerefund": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "escrowed": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "insured": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "insurable": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "taxable": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "amt": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "bank_q": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "callable": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "putable": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "float_var_rt": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "sinking_fund": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "convertible": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "zero_coupon": forms.RadioSelect(attrs = {'class' : 'inline'}),



                }
class MarketForm(forms.ModelForm):
  class Meta:
    model = Market

    fields = ["inventory_choices", "include_choices", 
    "limit_offerings_choices", "window",]
    widgets = { "window": forms.RadioSelect(attrs = {'class' : 'inline'}),
                "inventory_choices" : forms.CheckboxSelectMultiple(),
                "include_choices" : forms.CheckboxSelectMultiple(),
                "limit_offerings_choices": forms.RadioSelect(attrs = {'class' : 'inline'}),



              }
# class APIForm(forms.Form):
#     Identifier = forms.CharField(required = False)
#     IdentifierType = forms.ChoiceField(choices=( ('Symbol','Symbol'), ('CIK','CIK'), ('CUSIP','CUSIP'), ('ISIN','ISIN'), ('Valoren','Valoren'), ('SEDOL','SEDOL') ))
#     PriceSource = forms.ChoiceField(choices=(('FINRA','FINRA'),))
     

class ScreenBondForm(forms.Form):
    Issuer = forms.CharField(required = False)
    StartMaturityDate = forms.DateField()
    EndMaturityDate = forms.DateField()
    StartCouponRate = forms.CharField()
    EndCouponRate = forms.CharField()
    Callable = forms.ChoiceField(choices=( ('Any', 'Any'), ('True', 'True'), ('False', 'False')))
    Convertible = forms.ChoiceField(choices=( ('Any', 'Any'), ('True', 'True'), ('False', 'False')))
    IncludeNonactive = forms.ChoiceField(choices=( ('True', 'True'), ('False', 'False')))
    MaxResultCount = forms.CharField()

class MoodyBondForm(forms.Form):
  id = forms.CharField(required= False)
  dataset_code = forms.CharField()
  database_code = forms.CharField()
  name = forms.CharField()
  description = forms.CharField()
  frequency = forms.ChoiceField(choices= (('Daily', 'Daily'), ('Monthly', 'Monthly'), ('Annually', 'Annually')))
  type = forms.CharField()
  premium = forms.ChoiceField(choices= (('All', 'All'), ('True', 'True'), ('False', 'False')))
  database_id = forms.CharField()

class MerrillLynchForm (forms.Form):
  id = forms.CharField(required= False)
  dataset_code = forms.CharField()
  database_code = forms.CharField()
  name = forms.CharField()
  description = forms.CharField()
  frequency = forms.ChoiceField(choices= (('Daily', 'Daily'), ('Monthly', 'Monthly'), ('Annually', 'Annually')))
  type = forms.CharField()
  premium = forms.ChoiceField(choices= (('All', 'All'), ('True', 'True'), ('False', 'False')))
  database_id = forms.CharField()

class ChicagoForm (forms.Form):
  id = forms.CharField(required= False)
  dataset_code = forms.CharField()
  database_code = forms.CharField()
  name = forms.CharField()
  description = forms.CharField()
  frequency = forms.ChoiceField(choices= (('Daily', 'Daily'), ('Monthly', 'Monthly'), ('Annually', 'Annually')))
  type = forms.CharField()
  premium = forms.ChoiceField(choices= (('All', 'All'), ('True', 'True'), ('False', 'False')))
  database_id = forms.CharField()



























      # "CUSIP", 
      # "description",
      # "state",
      # "quantity_min",
      # "quantity_max",
      # "years_min",
      # "years_max",
      # # "Maturity Minimum",
      # # "Maturity Maximum",
      # "coupon_min",
      # "coupon_max",
      # "price_min",
      # "price_max",
      # # "YTW Minimum",
      # # "YTW Maximum",
      # # "OID Yield Minimum",
      # # "OID Yield Maximum",
      # "Moodys_Rating_Minimum",
      # "Moodys_Rating_Maximum",
      # "SandP_Rating_Minimum",
      # "SandP_Rating_Maximum",
      # "Fitch_Ratings_Minimum",
      # "Fitch_Ratings_Maximum",
      # # "Call Protect Maximum",
      # "Inventory_Choices",
      # "Include_Choices",
      # "Limit_Offerings_Choices",
      # "View",
      # "Spread",
      # "Bond_Type",
      # "Sectors",

  

# class LoginForm(forms.ModelForm):
# 	class Meta:
# 		model = Login
# 		widgets = {
# 					'Password': forms.PasswordInput(),}
# 		fields = ('Username','Password')



