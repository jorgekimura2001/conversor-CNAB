from django.shortcuts import render
from .forms import FileForm
import ipdb
from rest_framework.views import Request
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer


data = []


def form_modelform(request: Request):
    if request.method == "POST":
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            file_values(request.FILES["file"])
    form = FileForm()
    return render(request, "form/form.modelform.html", {"form": form})


def file_values(file):
    for line in file:
        data.append(line.decode("utf-8").strip())

    for info in data:
        type = info[0]
        date_year = info[1:10][0:4]
        date_mounth = info[1:10][4:6]
        date_day = info[1:10][6:8]
        date = date_year + "-" + date_mounth + "-" + date_day
        value = info[9:19]
        cpf = info[19:30]
        card = info[30:42]
        hour = info[42:48][0:2]
        minute = info[42:48][2:4]
        seconds = info[42:48][4:6]
        time = hour + ':' + minute + ':' + seconds
        owner = info[48:62]
        store = info[62:81]

        print(type)
        print('-'*100)
        print(date)
        print('-'*100)
        print(value)
        print('-'*100)
        print(cpf)
        print('-'*100)
        print(card)
        print('-'*100)
        print(time)
        print('-'*100)
        print(owner)
        print('-'*100)
        print(store)
