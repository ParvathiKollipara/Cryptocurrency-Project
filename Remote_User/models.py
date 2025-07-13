from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address= models.CharField(max_length=3000)
    gender= models.CharField(max_length=30)

class financial_risk_type(models.Model):

    volume_usd_24h= models.CharField(max_length=3000)
    available_supply= models.CharField(max_length=3000)
    idn= models.CharField(max_length=3000)
    last_updated= models.CharField(max_length=3000)
    market_cap_usd= models.CharField(max_length=3000)
    max_supply= models.CharField(max_length=3000)
    name= models.CharField(max_length=3000)
    percent_change_1h= models.CharField(max_length=3000)
    percent_change_24h= models.CharField(max_length=3000)
    percent_change_7d= models.CharField(max_length=3000)
    price_btc= models.CharField(max_length=3000)
    price_usd= models.CharField(max_length=3000)
    rank= models.CharField(max_length=3000)
    symbol= models.CharField(max_length=3000)
    total_supply= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



