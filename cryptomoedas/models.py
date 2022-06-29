from django.db import models
from forex_python.converter import CurrencyCodes, CurrencyRates
# Create your models here.

c = CurrencyRates
cd = CurrencyCodes

class Moedas(models.Model):
    escolher_moeda = models.Field.choices(cd = CurrencyCodes)
    nome = models.CharField(max_length= 50)
    cotacao_atual = models.DateField(blank=True, null=True)
    pontuacao = models.IntegerField(blank=True, null=True)
    habilitado = models.BooleanField(blank=True, null=True)
    observacao = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.nome
    