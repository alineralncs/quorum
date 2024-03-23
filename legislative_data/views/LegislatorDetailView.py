from django.shortcuts import render
from django.views.generic import DetailView
from ..models.Legislator import Legislator
from ..models.VoteResults import VoteResult
import pandas
from django.db.models import Count, Q
from ..models.Bill import Bill
from ..models.Legislator import Legislator
from ..models.Vote import Vote
from ..models.VoteResults import VoteResult

LEGISLATOR_PATH = 'data/legislators.csv'
VOTE = 'data/votes.csv'
VOTE_RESULTS = 'data/vote_results.csv'
BILLS = 'data/bills.csv'

class LegislatorDetailView(DetailView):
    template_name = 'legislator.html'
    model = Legislator

    def get_context_data(self, **kwargs):
        get_id_legislator = self.kwargs['pk']

        context = super().get_context_data(**kwargs)
        
        query = VoteResult.objects.filter(legislator_id=get_id_legislator).values('legislator_id__name', 'legislator_id').annotate(support=Count('vote_type', filter=Q(vote_type=1)), opposition=Count('vote_type', filter=Q(vote_type=2)))

        context['data'] = query

        return context
    
