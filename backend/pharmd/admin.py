from django.contrib import admin
from .models import Company, Pharmacy, Digital_Health, Virtual_Pharmacies

class CompanyAdmin(admin.ModelAdmin):
    company_display = ('company name', "company active")

class PharmacyAdmin(admin.ModelAdmin):
    pharmacy_display = ('pharmacy name')

class Digital_HealthAdmin(admin.ModelAdmin):
    digital_health_display = ('digital health name')

class        

admin.site.register(Company, CompanyAdmin)