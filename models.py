# models.py
from django.db import models

class TaxPayments(models.Model):
    COMPANY_CHOICES = [
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    ]

    company = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=COMPANY_CHOICES, default='Paid')
    due_date = models.CharField(max_length=100)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2, help_text="Enter tax rate (e.g., 0.06)")

    def __str__(self):
        return self.company
