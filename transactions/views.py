from django.shortcuts import render
from .forms import FileForm
import ipdb
from rest_framework.views import Request
from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer


data = []

store_transactions = []

transactions_to_render = []

non_repeat_transaction = []

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
        time = hour + ":" + minute + ":" + seconds
        owner = info[48:62]
        store = info[62:81]

        Transaction.objects.create(
            type=type,
            date=date,
            value=value,
            cpf=cpf,
            card=card,
            time=time,
            owner=owner,
            store=store,
        )


def listTransactions(request):

    store_transactions = [transaction for transaction in Transaction.objects.all().values()]

    for item in store_transactions:
        if item['store'] not in non_repeat_transaction:
            non_repeat_transaction.append(item)
        else:
            print('Item já está na lista')
        # for key, value_dict in item.items():
        #     if key == 'value':
        #         value_converted = round(value_dict/100, 2)
                
        #         transactions_to_render.append({'value': value_converted, 'store': item['store']})
        # for transaction in transactions_to_render:
        #     if item["store"] == transaction['store']:
        #         transaction['store'] 

    ipdb.set_trace()

    return render(request, "list/list.html", {"store_transactions": transactions_to_render})
