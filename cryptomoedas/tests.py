from django.db import models
import requests
import json
from forex_python.converter import CurrencyCodes, CurrencyRates

# Create your models here.
requisicao = requests.get('https://economia.awesomeapi.com.br/all')
cotacao = requisicao.json()
print (cotacao)