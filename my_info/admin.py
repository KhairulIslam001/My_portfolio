from django.contrib import admin
from .models import customer_information

# Register your models here.

@admin.register(customer_information)

class UserAdmin(admin.ModelAdmin):
    list_display=['Customer_ID','customer_name','Org','Email','NID','Phone_No']

