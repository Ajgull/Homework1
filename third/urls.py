from django.urls import path
from third.views import Hobby, Univercity, Work

urlpatterns = [
    path('Hobby/', Hobby),
    path('Univercity/', Univercity),
    path('Work/', Work)
]
