from django.views.generic import DetailView
from ..models.Bill import Bill
from ..models.Legislator import Legislator
from ..models.Vote import Vote
from ..models.VoteResults import VoteResult
from itertools import chain

from django.db.models import Count, Q, Subquery


class BillDetailView(DetailView):
    template_name = 'bills.html'
    model = Bill

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_id_bill = self.kwargs['pk']
        
        query_results = VoteResult.objects.filter(Q(vote_type=1) | Q(vote_type=2), vote_id__bill_id=get_id_bill).values('vote_id__bill_id', 'vote_id__bill_id__title', 'vote_id__bill_id__primary_sponsor__name').annotate(count_type_1=Count('legislator_id', filter=Q(vote_type=1)), count_type_2=Count('legislator_id', filter=Q(vote_type=2)))

        context['bills'] = query_results

        return context