from django.db import models
import pandas as pd
from .Bill import Bill

class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    bill_id = models.ForeignKey('Bill', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.legislator} - {self.bill} - {self.vote}"
    
    def get_vote_csv_data(file):
        votes = pd.read_csv(file)

        for index, row in votes.iterrows():
            bill_id = row['bill_id']
            bill_instance = Bill.objects.get(id=bill_id)

            vote_instance = Vote.objects.get_or_create(id=row['id'], bill_id=bill_instance)

        return vote_instance