from django.db import models

# Create your models here.
class Company(models.Model):
    PHARMACY = 'PH'
    DIGITAL_HEALTH = 'DH'
    COMPANY_TYPES = [
        (PHARMACY, 'Pharmacy'),
        (DIGITAL_HEALTH, 'Digital Health'),
    ]

    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=100)
    company_active = models.BooleanField(default=True)
    company_type = models.CharField(max_length=100, choices=COMPANY_TYPES)
    
    def __str__(self):
        return f'<company_id={self.company_id} company_name={self.company_name} company_active={self.company_active} company_type={self.company_type} >'

class Pharmacy(models.Model):
    VIRTUAL_PHARMACY = 'VP'
    DIGITAL_THERAPEUTICS = 'DT'
    CHRONIC_DISEASE_MGMT = 'CDM'
    PERSONALIZED_PHARMACY_SERVICES = 'PPS'
    PHARMACOGENOMICS = 'PG'
    VITAMINS_SUPPLEMENTS = 'VS'
    HOME_LAB_TESTING_MONITORING = 'HLTM'
    HOSPITAL_PHARMACY = 'HP'
    NOVEL_PHARMA = 'NP'
    DTC_PHARMACY_SERVICES = 'DTCPS'
    PHARM_SERVICES_WORKFLOW_EXPANSION = 'PSWE'
    PHARMACY_MEDIA = 'PM'
    PHARMACY_TYPES = [  
        (VIRTUAL_PHARMACY, 'Virtual Pharmacy'),
        (DIGITAL_THERAPEUTICS, 'Digital Therapeutics'),
        (CHRONIC_DISEASE_MGMT, 'Chronic Disease Management'),
        (PERSONALIZED_PHARMACY_SERVICES, 'Personalized Pharmacy Services'),
        (PHARMACOGENOMICS, 'Pharmacogenomics'),
        (VITAMINS_SUPPLEMENTS, 'Vitamins & Supplements'),
        (HOME_LAB_TESTING_MONITORING, 'Home Lab Testing & Monitoring'),
        (HOSPITAL_PHARMACY, 'Hospital Pharmacy'),
        (NOVEL_PHARMA, 'Novel Pharma'),
        (DTC_PHARMACY_SERVICES, 'DTC Pharmacy Services'),
        (PHARM_SERVICES_WORKFLOW_EXPANSION, 'Pharm Services Workflow Expansion'),
        (PHARMACY_MEDIA, 'Pharmacy Media'),
    ]

    pharmacy_id = models.IntegerField(primary_key=True)
    pharmacy_name = models.CharField(max_length=100)
    pharmacy_type = models.CharField(max_length=100, choices=PHARMACY_TYPES)
    
    def __str__(self):
        return f'<pharmacy_id={self.pharmacy_id} pharmacy_name={self.pharmacy_name} pharmacy_type={self.pharmacy_type} >' 

class Digital_Health(models.Model):
    digital_health_id = models.IntegerField(primary_key=True)
    digital_health_name = models.CharField(max_length=100)
    digital_health_type = models.CharField(max_length=100)
    
    def __str__(self):
        return f'<digital_health_id={self.digital_health_id} digital_health_name={self.digital_health_name}>'

class Virtual_Pharmacies(models.Model):
    virtual_pharmacy_id = models.IntegerField(primary_key=True)
    virtual_pharmacy_name = models.CharField(max_length=100)
    virtual_pharmacy_logo = models.TextField()
    virtual_pharmacy_url = models.TextField()
    
    def __str__(self):
        return f'<virtual_pharmacy_id={self.virtual_pharmacy_id} virtual_pharmacy_name={self.virtual_pharmacy_name}>'