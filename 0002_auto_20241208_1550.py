# Generated by Django 3.0 on 2024-12-08 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TaxPayment',
            new_name='TaxPayments',
        ),
    ]
