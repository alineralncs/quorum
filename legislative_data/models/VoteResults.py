from django.db import models
from .Legislator import Legislator
from .Vote import Vote
import pandas as pd

class VoteResult(models.Model):
    id = models.AutoField(primary_key=True)
    vote_id = models.ForeignKey('Vote', on_delete=models.CASCADE)
    legislator_id = models.ForeignKey('Legislator', on_delete=models.CASCADE)
    vote_type = models.IntegerField()

    def __str__(self):
        return f"{self.legislator} - {self.vote}"

    
    def get_vote_result_csv_data(file):
        vote_results = pd.read_csv(file)

        for index, row in vote_results.iterrows():
            id = row['id']
            vote_id = row['vote_id']
            legislator_id = row['legislator_id']
            vote_type = row['vote_type']

            vote_instance = Vote.objects.get(id=vote_id)
            legislator_instance = Legislator.objects.get(id=legislator_id)
            vote_result_instance = VoteResult.objects.get_or_create(id=id, vote_id=vote_instance, legislator_id=legislator_instance, vote_type=vote_type)

        return vote_result_instance