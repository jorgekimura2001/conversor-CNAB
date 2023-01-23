from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Transaction(models.Model):
    type = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(9),
        ],
    )
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
