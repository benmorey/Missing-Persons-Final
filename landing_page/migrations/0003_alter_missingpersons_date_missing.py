# Generated by Django 4.2.2 on 2023-06-20 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0002_alter_missingpersons_date_missing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingpersons',
            name='date_missing',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 20, 18, 26, 8, 105844)),
        ),
    ]
