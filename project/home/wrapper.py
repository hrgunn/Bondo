from django.conf import settings
import requests

class XigniteCorporateBonds:
	def __init__(self):
		self.base_url = "http://bonds.xignite.com/xBonds.json/"
		self.access_token = {"_Token": settings.XIGNITE_BONDS_API_KEY}

	def _get(self, path, **kwargs):
		url = self.base_url+path
		kwargs.update(self.access_token)
		return requests.get(url,params=kwargs)

# Returns Last Sale price for a specific bond as reported by the price source selected in the input.
	def get_last_sale(self,**kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		last_sale = self._get("GetLastSale", **kwargs)
		return last_sale
#Returns Last Sale price for the list of bonds specified in the input, as reported by the price source selected in the input.

	def get_last_sales(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		last_sales = self._get("GetLastSales", **kwargs)
		return last_sales

#Returns price data composite including last sale price, yield and daily and yearly Open, High, Low prices for a specific bond reported by price source selected in the input.

	def get_price_composite(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		price_composite = self._get("GetPriceComposite", **kwargs)
		return price_composite

# Returns price data composite including last sale price, yield and daily and yearly Open, High, Low prices for the list of bonds specified in the input.

	def get_price_composites(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		price_composites = self._get("GetPriceComposites", **kwargs)
		return price_composites

# Returns daily Open, High, Low, Close (OHLC) prices for a specific bond reported by the price source selected in the input. Daily OHLC data is provided for the most recent date for which data is provided by the price source.
	def get_daily_open_high_low_close_price(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		OHLC = self._get("GetDailyOpenHighLowClosePrice", **kwargs)
		return OHLC
#Returns daily Open, High, Low, Close (OHLC) prices for the list of bonds specified in the input. Daily OHLC data is provided for the most recent date for which data is provided by the price source.

	def get_daily_open_high_low_close_prices(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		OHLCs = self._get("GetDailyOpenHighLowClosePrices", **kwargs)
		return OHLCs

#Returns yearly high, low prices for a specific bond reported by the price source selected in the input.

	def get_yearly_high_low_price(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""

		YHLP = self._get("GetYearlyHighLowPrice", **kwargs)
		return YHLP
#Returns yearly high, low prices for a specific bond reported by the price source selected in the input.

	def get_yearly_high_low_prices(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""

		YHLPs = self._get("GetYearlyHighLowPrices", **kwargs)
		return YHLPs

#Returns Yield to maturity for a specific bond reported by the price source selected in the input.

	def get_yield(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		find_yield = self._get("GetYield", **kwargs)
		return find_yield

#Returns Yield to maturity for the list of bonds specified in the input as reported by the price source selected in the input.

	def get_yields(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		find_yields = self._get("GetYields", **kwargs)
		return find_yields

# Returns Accrued Interest for a specific bond reported by the price source selected in the input.


	def get_accrued_interest(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		accrued_interest = self._get("GetAccruedInterest", **kwargs)
		return accrued_interest

# Returns Accrued Interest for the list of bonds specified in the input.


	def get_accrued_interests(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		accrued_interests = self._get("GetAccruedInterests", **kwargs)
		return accrued_interests

# Returns Price, Yield, Accrued Interest and other bond analytics data for a specific bond reported by the price source selected in the input.


	def get_bond_calculation(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		bond_calculation = self._get("GetBondCalculation", **kwargs)
		return bond_calculation


# Returns Price, Yield, Accrued Interest and other bond analytics data for a list of bonds provided in the input.

	def get_bond_calculations(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		bond_calculations = self._get("GetBondCalculations", **kwargs)
		return bond_calculations

# Returns Duration and Convexity for a specific bond reported by the price source selected in the input.

	def get_duration_and_convexity(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		duration_and_convexity = self._get("GetDurationAndConvexity", **kwargs)
		return duration_and_convexity

# Returns Duration and Convexity for a list of bonds provided in the input.


	def get_duration_and_convexities(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		duration_and_convexities = self._get("GetDurationAndConvexities", **kwargs)
		return duration_and_convexities



class XigniteBondMaster:
	def __init__(self):
		self.base_url = "http://bondmaster.xignite.com/xBondMaster.json/"
		self.access_token = {"_Token": settings.XIGNITE_BONDS_API_KEY}

	def _get(self, path, **kwargs):
		url = self.base_url+path
		kwargs.update(self.access_token)
		return requests.get(url,params=kwargs)

	def get_screen_bonds(self, **kwargs):

		"""
		@param
		kwargs=>Issuer, StartMaturityDate, EndMaturityDate, 
		StartCouponRate, EndCouponRate, Callable, Convertible,
		IncludeNonActive, MaxResultCount
		"""
		screen_bonds = self._get("ScreenBonds", **kwargs)
		return screen_bonds

class MoodyAPI:
	def __init__(self):
		self.base_url = "https://www.quandl.com/api/v3/datasets/MOODY/{dataset_code}/data.json"
		self.access_token = {"_api_key": settings.MOODY_BOND_API_KEY}

	def _get(self, path, **kwargs):
		url = self.base_url.format(dataset_code = path)
		kwargs.update(self.access_token)
		return requests.get(url,params=kwargs)

	def get_moody_BAA(self,**kwargs):
		"""
		@param
		kwargs=>DatabaseCode, PerPage, SortBy, Page
		"""
		moody = self._get("DBAAYLD", **kwargs)
		return moody


	def get_moody_AAA(self,**kwargs):
		"""
		@param
		kwargs=>DatabaseCode, PerPage, SortBy, Page
		"""
		moody = self._get("DAAAYLD", **kwargs)
		return moody

class Merrill_Lynch:
	def __init__(self):
		self.base_url = "https://www.quandl.com/api/v3/datasets/ML/{dataset_code}/data.json"
		self.access_token = {"_api_key": settings.MERRILL_LYNCH_BOND_API_KEY}

	def _get(self, path, **kwargs):
		url = self.base_url.format(dataset_code = path)
		kwargs.update(self.access_token)
		return requests.get(url,params=kwargs)

	def get_merrill_A(self,**kwargs):
		"""
		@param
		kwargs=>DatabaseCode, PerPage, SortBy, Page
		"""
		merrill = self._get("ATRI", **kwargs)
		return merrill

	def get_merrill_B(self,**kwargs):
		"""
		@param
		kwargs=>DatabaseCode, PerPage, SortBy, Page
		"""
		merrill = self._get("ML/BOAS", **kwargs)
		return merrill

	def get_merrill_Emerging_Markets_Corporate(self,**kwargs):
		"""
		@param
		kwargs=>DatabaseCode, PerPage, SortBy, Page
		"""
		merrill = self._get("ML/EMCBI", **kwargs)
		return merrill

class FederalReserve:
	def __init__(self):
		self.base_url = "https://www.quandl.com/api/v3/datasets/CME/{dataset_code}/data.json"
		self.access_token = {"_api_key": settings.FEDERAL_RESERVE_ECONOMIC_API_KEY}

	def _get(self, path, **kwargs):
		url = self.base_url+path
		kwargs.update(self.access_token)
		return requests.get(url,params=kwargs)

	def get_chicago(self,**kwargs):
		"""
		@param
		kwargs=>DatabaseCode, PerPage, SortBy, Page
		"""
		chicago = self._get("SSIN2016", **kwargs)
		return chicago

	def get_chicago(self,**kwargs):
		"""
		@param
		kwargs=>DatabaseCode, PerPage, SortBy, Page
		"""
		chicago = self._get("SSIV2016", **kwargs)
		return chicago

	def get_chicago(self,**kwargs):
		"""
		@param
		kwargs=>DatabaseCode, PerPage, SortBy, Page
		"""
		chicago = self._get("YWU2016", **kwargs)
		return chicago



if __name__ == '__main__':
	my_api = XigniteCorportateBonds()
	response = my_api.get_last_sale(IdentifierType="CUSIP",Identifier="459200HU8",PriceSource="FINRA")
	print(response.json())