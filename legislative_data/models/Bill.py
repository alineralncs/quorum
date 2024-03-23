from django.db import models
import pandas as pd 
from .Legislator import Legislator

class Bill(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=255)
    primary_sponsor = models.ForeignKey('Legislator', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    def get_bill_csv_data(file):
        bills = pd.read_csv(file)

        for index, row in bills.iterrows():
            sponsor_id = row['sponsor_id']
            sponsor_instance = Legislator.objects.get(id=sponsor_id)
            bills_instance = Bill.objects.get_or_create(id=row['id'], title=row['title'], primary_sponsor=sponsor_instance)

        return bills_instance