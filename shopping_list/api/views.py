# Adding generic views to handle writable nested data.

# 1. Listing and creating ShoppingList resources
# 2. Retrieving, updating, deleting a single ShoppingList resource.

from rest_framework import generics

from shopping_list.api.serializers import ShoppingListSerializer, ShoppingItemSerializer
from shopping_list.models import ShoppingList, ShoppingItem

# provides list and create actions.
class ListAddShoppingList(generics.ListCreateAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer

# provides actions related to a single resource ie retrieve, update and destroy.
class ShoppingListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
    

# No need to list endpoint og ShoppingItem since it is already listed via
#  nested serializer for ShoppingList
class AddShoppingItem(generics.CreateAPIView):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer

class ShoppingItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShoppingItemSerializer
    # Have to tell the view to look for a different primary key.
    # Using lookup_url_kwarg for object lookup.
    lookup_url_kwarg = "item_pk"