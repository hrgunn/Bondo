from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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

class Home(models.Model):
	CUSIP = models.CharField(max_length=9)
	description = models.TextField(max_length=200)
	# spread = bais points?
	# Curve?
	# States
	quantity_min = models.IntegerField()
	quantity_max = models.IntegerField()
	years_min=models.DateTimeField()
	years_max=models.DateTimeField()
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

class Login(models.Model):
	username = models.CharField(max_length=12)
	password = models.CharField(max_length=12)

	# Call Protect


