from django.db import models

# Create your models here.

class Invoice(models.Model):
    date = models.DateField()
    invoice_customer_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}'

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    descrption = models.CharField(max_length=200)
    quantity = models.IntegerField()
    unit_price  = models.FloatField()
    price = models.FloatField()



