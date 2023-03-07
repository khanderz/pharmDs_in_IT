from django.db import models



# one to many
class Company(models.Model):
    PHARMACY = 'PH'
    DIGITAL_HEALTH = 'DH'
    COMPANY_TYPES = [
        (PHARMACY, 'Pharmacy'),
        (DIGITAL_HEALTH, 'Digital Health'),
    ]

    company_id = models.IntegerField(primary_key=True)
    company_name = models.CharField(max_length=100, unique=True, default="Company Name")
    company_active = models.BooleanField(default=True)
    company_type = models.CharField(max_length=100, choices=COMPANY_TYPES, default=DIGITAL_HEALTH)
    
    def __str__(self):
        return f'<company_id={self.company_id} company_name={self.company_name} company_active={self.company_active} company_type={self.company_type} >'

# one to many
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

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    pharmacy_id = models.IntegerField(primary_key=True)
    pharmacy_type = models.CharField(max_length=100, choices=PHARMACY_TYPES)
    pharmacy_logo = models.TextField(default=" ")
    pharmacy_url = models.URLField(default=" ")
    pharmacy_description = models.TextField(default=" ")
    
    def __str__(self):
        return f'<pharmacy_id={self.pharmacy_id} pharmacy_name={self.company.company_name} pharmacy_type={self.pharmacy_type} >' 

# one to many
class Digital_Health(models.Model):
    MENTAL_HEALTH = 'MH'
    GENETICS = 'G'
    PROVIDER_DIRECTORIES_AND_CARE_NAVIGATION = 'PDACN'
    HYBRID_VIRTUAL_INPERSON_CARE = 'HVIC'
    DIGITAL_THERAPEUTICS = 'DT'
    BILLING_AND_PAYMENTS = 'BAP'
    APP_DEPLOYMENT = 'AD'
    SCREENING_MONITORING_DIAGNOSTICS = 'SMD'
    DATA_INTEGRATION_ANALYTICS = 'DIA'
    CLINICAL_INTELLIGENCE = 'CI'
    HOME_HEALTH_TECH = 'HHT'
    VIRTUAL_CARE = 'VC'
    PATIENT_ENGAGEMENT = 'PE'
    CARE_COORDINATION_COLLABORATION = 'CCC'
    WORKFLOW_DIGITIZATION_AND_AUTOMATION = 'WDA'
    COMPUTER_AIDED_IMAGING = 'CAI'
    CLINICAL_TRIALS = 'CT'
    DIGITAL_HEALTH_TYPES = [
        (MENTAL_HEALTH, 'Mental Health'),
        (GENETICS, 'Genetics'),
        (PROVIDER_DIRECTORIES_AND_CARE_NAVIGATION, 'Provider Directories & Care Navigation'),
        (HYBRID_VIRTUAL_INPERSON_CARE, 'Hybrid Virtual In-Person Care'),
        (DIGITAL_THERAPEUTICS, 'Digital Therapeutics'),
        (BILLING_AND_PAYMENTS, 'Billing & Payments'),
        (APP_DEPLOYMENT, 'App Deployment'),
        (SCREENING_MONITORING_DIAGNOSTICS, 'Screening, Monitoring, Diagnostics'),
        (DATA_INTEGRATION_ANALYTICS, 'Data Integration & Analytics'),
        (CLINICAL_INTELLIGENCE, 'Clinical Intelligence'),
        (HOME_HEALTH_TECH, 'Home Health Tech'),
        (VIRTUAL_CARE, 'Virtual Care'),
        (PATIENT_ENGAGEMENT, 'Patient Engagement'),
        (CARE_COORDINATION_COLLABORATION, 'Care Coordination & Collaboration'),
        (WORKFLOW_DIGITIZATION_AND_AUTOMATION, 'Workflow Digitization & Automation'),
        (COMPUTER_AIDED_IMAGING, 'Computer-Aided Imaging'),
        (CLINICAL_TRIALS, 'Clinical Trials'),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    digital_health_id = models.IntegerField(primary_key=True)
    digital_health_type = models.CharField(max_length=100, choices=DIGITAL_HEALTH_TYPES)
    digital_health_logo = models.TextField(default=" ")
    digital_health_url = models.URLField(default=" ")
    digital_health_description = models.TextField(default=" ")

    def __str__(self):
        return f'<digital_health_id={self.digital_health_id} digital_health_name={self.company.company_name} digital_health_type={self.digital_health_type} >'