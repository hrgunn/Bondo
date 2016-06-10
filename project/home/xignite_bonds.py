import requests

class XigniteCorportateBonds:
	def __init__(self):
		self.base_url = "http://bonds.xignite.com/xBonds.json/"
		self.access_token = {"_Token":"CB0BBEC6941D444194532D22B2ACD5F7"}

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
		OHLC = self._get("GetDailyOpenHighLowClosePrice")
		return OHLC
#Returns daily Open, High, Low, Close (OHLC) prices for the list of bonds specified in the input. Daily OHLC data is provided for the most recent date for which data is provided by the price source.

	def get_daily_open_high_low_close_prices(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		OHLCs = self._get("GetDailyOpenHighLowClosePrices")
		return OHLCs

#Returns yearly high, low prices for a specific bond reported by the price source selected in the input.

	def get_yearly_high_low_price(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""

		YHLP = self._get("GetYearlyHighLowPrice")
		return YHLP
#Returns yearly high, low prices for a specific bond reported by the price source selected in the input.

	def get_yearly_high_low_prices(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""

		YHLPs = self._get("GetYearlyHighLowPrices")
		return YHLPs

#Returns Yield to maturity for a specific bond reported by the price source selected in the input.

	def get_yield(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		find_yield = self._get("GetYield")
		return find_yield

#Returns Yield to maturity for the list of bonds specified in the input as reported by the price source selected in the input.

	def get_yields(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		find_yields = self._get("GetYields")
		return find_yields

# Returns Accrued Interest for a specific bond reported by the price source selected in the input.


	def get_accrued_interest(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		accrued_interest = self._get("GetAccruedInterest")
		return accrued_interest

# Returns Accrued Interest for the list of bonds specified in the input.


	def get_accrued_interests(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		accrued_interests = self._get("GetAccruedInterests")
		return accrued_interests

# Returns Price, Yield, Accrued Interest and other bond analytics data for a specific bond reported by the price source selected in the input.


	def get_bond_calculation(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		bond_calculation = self._get("GetBondCalculation")
		return bond_calculation


# Returns Price, Yield, Accrued Interest and other bond analytics data for a list of bonds provided in the input.

	def get_bond_calculations(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		bond_calculations = self._get("GetBondCalculations")
		return bond_calculations

# Returns Duration and Convexity for a specific bond reported by the price source selected in the input.

	def get_duration_and_convexity(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		duration_and_convexity = self._get("GetDurationAndConvexity")
		return duration_and_convexity

# Returns Duration and Convexity for a list of bonds provided in the input.


	def get_duration_and_convexities(self, **kwargs):
		"""
		@param
		kwargs=>IdentifierType, Identifier, PriceSource
		"""
		duration_and_convexities = self._get("GetDurationAndConvexities")
		return duration_and_convexities










if __name__ == '__main__':
	my_api = XigniteCorportateBonds()
	response = my_api.get_last_sale(IdentifierType="CUSIP",Identifier="459200HU8",PriceSource="FINRA")
	print(response.json())