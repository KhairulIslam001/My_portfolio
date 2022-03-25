from django.db import models

# Create your models here.
class customer_information(models.Model):
    Customer_ID=models.IntegerField
    customer_name=models.CharField(max_length=20)
    Org=models.CharField(max_length=15)
    Email=models.CharField(max_length=20)
    NID=models.IntegerField(max_length=20)
    Phone_No=models.CharField(max_length=20)

class room_info(models.Model):
    room_number=models.IntegerField(primary_key=True)
    room_name=models.CharField(max_length=20)
    room_size=models.IntegerField(max_length=20)
