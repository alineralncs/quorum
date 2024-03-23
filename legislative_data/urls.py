from django.urls import path
from .views import HomeView, LegislatorDetailView, BillDetailView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("legislator/<int:pk>", LegislatorDetailView.as_view(), name="legislator_detail"),
    path("bills/<int:pk>", BillDetailView.as_view(), name="bills")
    
]