from rest_framework import serializers
from .models import Transaction
import ipdb


class TransactionSerializer(serializers.ModelSerializer):

    value_in_real = serializers.SerializerMethodField()

    def get_value_in_real(self, obj: Transaction) -> str:
        return f'R$ {round(obj.value/100, 2)}'

    class Meta:
        model = Transaction
        fields = [
            "type",
            "date",
            "value_in_real",
            "cpf",
            "card",
            "time",
            "owner",
            "store"
        ]
