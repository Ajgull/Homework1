from django.urls import path
from first.views import RecSecond, RecFirst, RecThird, RecForth

urlpatterns = [
    path('', RecFirst),
    path('Second/', RecSecond),
    path('Third/', RecThird),
    path('Forth/', RecForth)
]

