# All the API related code will be in this folder.

from rest_framework import serializers
from shopping_list.models import ShoppingItem

class ShoppingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ["id", "name", "purchased"]
        read_only_fields = ("id",)