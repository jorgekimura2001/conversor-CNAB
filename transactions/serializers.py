from rest_framework import serializers
from .models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    value_in_real = serializers.SerializerMethodField()

    class Meta:
        model = Transaction
        fields = [
            "type",
            "date",
            "value",
            "value",
            "cpf",
            "card",
            "time",
            "owner",
            "store"
        ]
