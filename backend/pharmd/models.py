from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f'<company_id={self.company_id} company_name={self.company_name}>'

class Pharmacy(models.Model):
    pharmacy_id = models.IntegerField(primary_key=True)
    pharmacy_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'<pharmacy_id={self.pharmacy_id} pharmacy_name={self.pharmacy_name}>' 

class Digital_Health(models.Model):
    digital_health_id = models.IntegerField(primary_key=True)
    digital_health_name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'<digital_health_id={self.digital_health_id} digital_health_name={self.digital_health_name}>'

class Virtual_Pharmacies(models.Model):
    virtual_pharmacy_id = models.IntegerField(primary_key=True)
    virtual_pharmacy_name = models.CharField(max_length=100)
    virtual_pharmacy_logo = models.TextField()
    virtual_pharmacy_url = models.TextField()
    
    def __str__(self):
        return f'<virtual_pharmacy_id={self.virtual_pharmacy_id} virtual_pharmacy_name={self.virtual_pharmacy_name}>'