# Generated by Django 5.1.3 on 2025-02-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carvilla', '0005_alter_addstock_mileage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addstock',
            name='mileage',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
    ]
