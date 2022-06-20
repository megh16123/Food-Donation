from django.db import models

# Create your models here.

class Donor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class FoodDetail(models.Model):
    donor = models.ForeignKey(Donor,on_delete=models.CASCADE,default=None)
    foodname = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    prepared_at = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.foodname