# Generated by Django 4.1.6 on 2023-03-03 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                ("company_id", models.IntegerField(primary_key=True, serialize=False)),
                ("company_name", models.CharField(max_length=100)),
                ("company_active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Digital_Health",
            fields=[
                (
                    "digital_health_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("digital_health_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Pharmacy",
            fields=[
                ("pharmacy_id", models.IntegerField(primary_key=True, serialize=False)),
                ("pharmacy_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Virtual_Pharmacies",
            fields=[
                (
                    "virtual_pharmacy_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("virtual_pharmacy_name", models.CharField(max_length=100)),
                ("virtual_pharmacy_logo", models.TextField()),
                ("virtual_pharmacy_url", models.TextField()),
            ],
        ),
    ]