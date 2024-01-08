from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class expense(models.Model):
    user=models.ForeignKey(user, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    description=models.CharField(max_length=255)