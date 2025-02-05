from django.db import models

# Create your models here.
class Product(models.Model):
    CAT=((1,"Storybooks"),(2,"Biography"),(3,"Lkg1"),(4,"Firsttofifth"),(5,"Sixthtotenth"),(6,"Writting Instruments"),)
    pname=models.CharField(max_length=50,verbose_name="Product Name")  # verbose_name is a alicing for pname
    price=models.IntegerField()
    category=models.IntegerField(choices=CAT,verbose_name="Category")
    description=models.CharField(max_length=300,verbose_name="Details")
    is_active=models.BooleanField(default=True,verbose_name="Is_Available")
    pimage=models.ImageField(upload_to='images')
    offer_price=models.IntegerField(default=0)
    
    def __str__(self):    
        return self.pname


class Cart(models.Model):
    userid=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='userid')
    pid=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='pid')
    qty=models.IntegerField(default=1)

class Address(models.Model):
    user_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='user_id')
    address=models.CharField(max_length=100)
    fullname=models.CharField(max_length=40)
    city=models.CharField(max_length=30)
    pincode=models.CharField(max_length=10)
    state=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)

class Order(models.Model):
    order_id=models.CharField(max_length=50)
    user_id=models.ForeignKey('auth.User',on_delete=models.CASCADE,db_column='user_id')
    p_id=models.ForeignKey('Product',on_delete=models.CASCADE,db_column='p_id')
    qty=models.IntegerField(default=1)
    amt=models.FloatField()
    payment_status=models.CharField(max_length=20,default="unpaid")
    # if we want to return the character value to the admin interface and user interface
    def __str__(self):
        return self.order_id