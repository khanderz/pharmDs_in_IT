from django.contrib import admin
from .models import Company, Pharmacy, Digital_Health

class CompanyAdmin(admin.ModelAdmin):
    company_display = ('company name', "company active")

class PharmacyAdmin(admin.ModelAdmin):
    pharmacy_display = ('pharmacy name')

class Digital_HealthAdmin(admin.ModelAdmin):
    digital_health_display = ('digital health name')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Pharmacy, PharmacyAdmin)
admin.site.register(Digital_Health, Digital_HealthAdmin)