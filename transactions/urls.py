from django.urls import path
from . import views

urlpatterns = [
    path("", views.form_modelform, name='form_modelform'),
    path('transactions', views.listTransactions, name='transactions')
]
