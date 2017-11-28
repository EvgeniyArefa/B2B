import datetime
from django.contrib import admin
from agreement.models import Period, Country, Company, Negotiator, Agreement
from django import forms


class AgreementForm(forms.ModelForm):

    def clean(self):
        start_date = self.cleaned_data.get('data_start')
        end_date = self.cleaned_data.get('data_end')
        if start_date > end_date:
            raise forms.ValidationError\
                ("The end date must be later than the start date")
        return self.cleaned_data


class PeriodForm(forms.ModelForm):

    def clean(self):
        start_date = self.cleaned_data.get('data_start')
        end_date = self.cleaned_data.get('data_end')
        if start_date > end_date:
            raise forms.ValidationError\
                ("The end date must be later than the start date")
        return self.cleaned_data


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    list_filter = ['name', 'code']
    search_fields = ['name', 'code']
    

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    list_filter = ['name', 'country']
    search_fields = ['name', 'country']
    

class NegotiatorAdmin(admin.ModelAdmin):
    list_filter = ['name']
    search_fields = ['name']


class PeriodsInline(admin.TabularInline):
    model =  Agreement.periods.through


class PeriodAdmin(admin.ModelAdmin):
    form = PeriodForm
    list_display = ('status', 'data_start', 'data_end')
    list_filter = ['status', 'data_start', 'data_end']
    search_fields = ['status']
    date_hierarchy = 'data_end'


class AgreementAdmin(admin.ModelAdmin):
    form = AgreementForm
    inlines = [
        PeriodsInline,
    ]
    exclude = ('periods',)
    list_display = ('company', 'data_start', 'data_end', 'negotiator', 
        'loan_turnover', 'debit_turnover_import', 'debit_turnover_export')
    list_filter = ['company', 'data_start', 'data_end','negotiator', 
        'periods']
    search_fields = ['company', 'negotiator']
    date_hierarchy = 'data_end'
    

admin.site.register(Period, PeriodAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Negotiator, NegotiatorAdmin)
admin.site.register(Agreement, AgreementAdmin)