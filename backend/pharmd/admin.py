from django.contrib import admin
from .models import pharmd

class CompanyAdmin(admin.ModelAdmin):
    company_display = ('company name', "company active")

admin.site.register(Company, CompanyAdmin)