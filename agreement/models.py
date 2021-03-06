import datetime
from django.db import models
from django.contrib.auth.models import User


class Period(models.Model):
    choice = ((1,"New"), (2,"Active"), (3,"Reconciliation"), (4,"Closed"))
    data_start = models.DateField()
    data_end = models.DateField()
    status = models.IntegerField(choices=choice)
    
    def __str__(self):
        return str(self.data_start) + '/' + str(self.data_end)


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Negotiator(models.Model):
    name = models.ForeignKey(User)

    def __str__(self):
        return str(self.name)


class Agreement(models.Model):
    data_start = models.DateField()
    data_end = models.DateField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    negotiator = models.ForeignKey(Negotiator, on_delete=models.CASCADE)
    loan_turnover = models.FloatField(blank=True, default=0)
    debit_turnover_import = models.FloatField(blank=True, default=0)
    debit_turnover_export = models.FloatField(blank=True, default=0)
    periods = models.ManyToManyField(Period)