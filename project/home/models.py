from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
Ratings_Choices =(
	('AAA','AAA'),
	('AA','AA'),
	('A','A'),
	('BBB','BBB'),
	('BB','BB'),
	('B','B'),
	('CCC','CCC'),
	('CC','CC'),
	('C','C'),
	('D','D'),


)

Inventory_Choices=(
	('All', 'All'),
	('Street', 'Street'),
	('Internal', 'Internal'),

)

Include_Choices=(
	('Secondary', 'Secondary'), 
	('New Issues', 'New Issues'),
	('Bids Wanted', 'Bids Wanted'),
	
)

Limit_Offerings_Choices=(
	('All', 'All'),
	('Only New', 'Only New'),
	('Only with a Quoted Bid Side', 'Only with a Quoted Bid Side')
)
View=(
	('Collapsed', 'Collapsed'),
	('Expanded', 'Expanded'),
)

Spread=(
	('bps', 'bps'),
	('10', '10'),
	('20', '20'),
	('30', '30'),
	('40', '40'),
	('50', '50'),
	('60', '60'),
	('70', '70'),
	('80', '80'),
	('90', '90'),
	('100', '100'),
)

Bond_Type=(
	("GO's", "GO's"),
	("Rev's", "Rev's"),
	("Double Brl", "Double Brl"),
)

Sectors=(
	('All', 'All'),
	('US Government', 'US Government'),
	('Mortgage', 'Mortgage'),
	('Credit', 'Credit'),
	('Non-US', 'Non-US'),
	('Cash', 'Cash')
)

def years():
	return [(year,year)for year in range(2000, 2016)]


class Home(models.Model):
	CUSIP = models.CharField(max_length=9)
	description = models.TextField(max_length=200)
	# spread = bais points?
	# Curve?
	state = USStateField()
	quantity_min = models.IntegerField()
	quantity_max = models.IntegerField()
	years_min=models.CharField(max_length = 4, choices=years())
	years_max=models.CharField(max_length = 4, choices=years())
	# maturity pulldown min/max
	coupon_min=models.IntegerField()
	coupon_max=models.IntegerField()
	price_min=models.IntegerField()
	price_max=models.IntegerField()
	# YTW min/max
	# OID min/max
	
	Moodys_Rating_Minimum = models.CharField(max_length = 4, choices=Ratings_Choices, default = "AAA")
	Moodys_Rating_Maximum = models.CharField(max_length = 4, choices=Ratings_Choices, default = "AAA")
	SandP_Rating_Minimum = models.CharField(max_length = 4, choices=Ratings_Choices, default = "AAA")
	SandP_Rating_Maximum = models.CharField(max_length = 4, choices=Ratings_Choices, default = "AAA")
	Fitch_Ratings_Minimum = models.CharField(max_length = 4, choices=Ratings_Choices, default = "AAA")
	Fitch_Ratings_Maximum = models.CharField(max_length = 4, choices=Ratings_Choices, default = "AAA")
	Inventory_Choices = models.BooleanField(max_length = 3, choices=Inventory_Choices, default = "All")
	Include_Choices = models.BooleanField(max_length = 3, choices=Include_Choices, default = "Secondary")
	Limit_Offerings_Choices = models.BooleanField(max_length = 3, choices=Limit_Offerings_Choices, default = "All")
	View = models.BooleanField(max_length = 2, choices=View, default = "Collapsed")
	Spread = models.CharField(max_length = 100, choices=Spread, default= "bps")
	Bond_Type = models.BooleanField(max_length = 3, choices=Bond_Type, default = "GO's")
	Sectors = models.BooleanField(max_length = 20, choices=Sectors, default="All")


	# Call Protect


