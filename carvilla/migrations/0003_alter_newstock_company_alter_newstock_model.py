# Generated by Django 5.1.4 on 2025-02-12 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carvilla', '0002_remove_newstock_name_newstock_company_newstock_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newstock',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='newstock',
            name='model',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
