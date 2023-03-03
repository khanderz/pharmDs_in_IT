from django.contrib import admin
from .models import Company, Pharmacy, Digital_Health, Virtual_Pharmacies

class CompanyAdmin(admin.ModelAdmin):
    company_display = ('company name', "company active")

admin.site.register(Company, CompanyAdmin)