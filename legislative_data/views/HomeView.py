from django.views.generic import TemplateView
from ..models.VoteResults import VoteResult
from ..models.Vote import Vote
from ..models.Bill import Bill
from ..models.Legislator import Legislator


BILLS = 'data/bills.csv'
VOTE = 'data/votes.csv'
VOTE_RESULTS = 'data/vote_results.csv'
LEGISLATOR = 'data/legislators.csv'

class HomeView(TemplateView):
    template_name = 'index.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        Legislator.get_legislator_csv_data(LEGISLATOR)
        Bill.get_bill_csv_data(BILLS)
        Vote.get_vote_csv_data(VOTE)
        VoteResult.get_vote_result_csv_data(VOTE_RESULTS)

        context['bills'] = Bill.objects.all().values('id', 'title', 'primary_sponsor__name')

        context['legislators'] = Legislator.objects.all().values('id', 'name') 
        
        return context