from django.db import models
from foods.models import Food


class UserPhones(models.Model):
    user_id = models.BigIntegerField(unique=True)
    phone = models.CharField(max_length=15)
    

# Create your models here.
class User(models.Model):
    user_id = models.BigIntegerField(unique=True)
    lang = models.CharField(max_length=10, null=True, blank=True)
    
    # def __str__(self):
    #     return str(self.user_id)

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    # def __str__(self) -> str:
    #     return str(f"{self.user.phone} x{self.count} {self.food.name_uz}")