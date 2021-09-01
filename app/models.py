from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class seller(models.Model):
    Shop_name = models.CharField(max_length=255,default="firstname")
    Sname = models.CharField(max_length=255,default="lasttname")
    email = models.EmailField(unique=True)
    mobile = models.IntegerField(default=123)
    address = models.CharField(max_length=255,default="address")
    passwd = models.CharField(max_length=255,default="password")
    OTP = models.CharField(max_length=6,default="1234")
    def __str__(self):
        return self.Sname

class category(models.Model):
    pcategory=models.CharField(max_length=200,default="product category")
    def __str__(self):
        return self.pcategory
    

class product(models.Model):
    pro_name=models.CharField(max_length=255,default="productname")
    pro_image=models.ImageField(upload_to="productimage/",default="xyz.jpg")
    pro_category=models.ForeignKey(category, on_delete=models.CASCADE)
    pro_price=models.FloatField(default=0.0)

    def __str__(self):
        return self.pro_name

class User(models.Model):
    fname = models.CharField(max_length=255,default="firstname")
    lname = models.CharField(max_length=255,default="lasttname")
    email = models.EmailField(unique=True)
    mobile = models.IntegerField(default=123)
    address = models.CharField(max_length=255,default="address")
    passwd = models.CharField(max_length=255,default="password")
    OTP = models.CharField(max_length=6,default="1234")
    
    def __str__(self):
        return self.fname

class AddCart(models.Model):
    usrg = models.ForeignKey(User, on_delete=models.CASCADE)
    prod = models.ForeignKey(product,on_delete=models.CASCADE)
    qun = models.IntegerField(default=1)
    price = models.IntegerField(default=1234)







