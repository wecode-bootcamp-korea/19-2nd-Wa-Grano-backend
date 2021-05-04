from django.db import models

class User(models.Model):
    email        = models.EmailField(max_length=100)
    password     = models.CharField(max_length=500)
    name         = models.CharField(max_length=45)
    last_name    = models.CharField(max_length=45, null=True)
    first_name   = models.CharField(max_length=45, null=True)
    phone_number = models.CharField(max_length=45, null=True)
    image_url    = models.URLField(max_length=2000)
    coupon       = models.ManyToManyField('products.Coupon', through='products.UserCoupon')
    dinning      = models.ManyToManyField('products.Dinning',through='products.Review')

    class Meta:
        db_table = 'users'
