from django.db import models

# Create your models here.

import uuid

class ShoppingItem(models.Model):
    # Adding own UUID to help prevent people from  easily accessing records.
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    purchased = models.BooleanField()

    def __str__(self):
        return f"{self.name}"
