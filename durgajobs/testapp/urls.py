from django.urls import path
from . import views

urlpatterns=[
path('', views.Homepage_view),
path('HydJobs/', views.HydJobs_view),
path('BngJobs/', views.BngJobs_view),
path('PuneJobs/', views.PuneJobs_view),
]
