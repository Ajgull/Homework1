from django.urls import path
from second.views import Sport, Country, Town

urlpatterns = [
    path('Sport/', Sport),
    path('Country/', Country),
    path('Town/', Town)
]
