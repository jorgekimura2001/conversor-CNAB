from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Transaction(models.Model):

    TransactionsChoices = (
        (1, "Débito"),
        (2, "Boleto"),
        (3, "Financiamento"),
        (4, "Crédito"),
        (5, "Recebimento Empréstimo"),
        (6, "Vendas"),
        (7, "Recebimento TED"),
        (8, "Recebimento DOC"),
        (9, "Aluguel"),
    )

    type = models.CharField(choices=TransactionsChoices, max_length=22)
    date = models.DateField()
    # valor em centavos tem de converter
    value = models.PositiveIntegerField()
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    time = models.TimeField()
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19)


class FileModel(models.Model):
    file = models.FileField()
