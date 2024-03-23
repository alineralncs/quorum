from django.db import models
import pandas as pd

class Legislator(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_legislator_csv_data(file):
        legislators = pd.read_csv(file)

        for index, row in legislators.iterrows():
           legislator_instance =  Legislator.objects.get_or_create(id=row['id'], name=row['name'])

        return legislator_instance