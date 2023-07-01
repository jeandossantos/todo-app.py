from django.db import models

import uuid
# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=65)
    email = models.CharField(max_length=65,  unique=True)
    password = models.CharField(max_length=255)
 