from django.db import models

# Create your models here.
class Customer(models.Model):
    transid = models.PositiveIntegerField()
    transdate = models.DateField()
    gender = models.CharField(max_length=70)
    age = models.IntegerField(default=0)
    maritalstatus = models.CharField(max_length=70)
    statenames = models.CharField(max_length=70)
    segment = models.CharField(max_length=70)
    employeestatus = models.CharField(max_length=70)
    paymentmode = models.CharField(max_length=70)
    referal = models.IntegerField(default=0)
    amountspent = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.transid}'
