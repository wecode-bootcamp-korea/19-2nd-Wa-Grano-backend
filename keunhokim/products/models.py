from django.db import models

class Category(models.Model):
    name        = models.CharField(max_length=45)
    image_url   = models.URLField(max_length=2000)
    destination = models.ManyToManyField('Destination', through='CategoryDestination')

    class Meta:
        db_table = 'categories'

class Destination(models.Model):
    name      = models.CharField(max_length=45)
    image_url = models.URLField(max_length=500)

    class Meta:
        db_table = 'destinations'

class CategoryDestination(models.Model):
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)
    destination = models.ForeignKey('Destination', on_delete=models.CASCADE)

    class Meta:
        db_table = 'category_destinations'

class City(models.Model):
    name = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = 'cities'

class District(models.Model):
    name = models.CharField(max_length=45)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'districts'

class RoomType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'room_types'

class Room(models.Model):
    star_rating = models.SmallIntegerField(default=0)
    room_type   = models.ForeignKey('RoomType',on_delete=models.SET_NULL,null=True)
    convenience = models.ManyToManyField('Convenience',through='RoomConvenience')

    class Meta:
        db_table = 'rooms'

class ServiceType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'service_types'

class Convenience(models.Model):
    name         = models.CharField(max_length=45)
    service_type = models.ForeignKey('ServiceType', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'conveniences'

class RoomConvenience(models.Model):
    service_type = models.ForeignKey('ServiceType', on_delete=models.CASCADE)
    convenience  = models.ForeignKey('Convenience', on_delete=models.CASCADE)
    room         = models.ForeignKey('Room',on_delete=models.CASCADE)

    class Meta:
        db_table = 'room_conveniences'

class DinningType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'dinning_types'

class FoodType(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'food_types'


class Dinning(models.Model):
    dinning_type = models.ForeignKey('DinningType',on_delete=models.SET_NULL, null=True)
    food_type    = models.ForeignKey('FoodType',on_delete=models.SET_NULL, null=True)
    description  = models.TextField()

    class Meta:
        db_table = 'dinnings'

class DinningOption(models.Model):
    name        = models.CharField(max_length=45)
    price       = models.DecimalField(max_digits=18, decimal_places=2)
    description = models.TextField()
    dinning     = models.ForeignKey('Dinning', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'dinning_options'

class Product(models.Model):
    name        = models.CharField(max_length=45)
    rating      = models.DecimalField(max_digits=3,decimal_places=1)
    description = models.TextField()
    address     = models.CharField(max_length=200)
    latitude    = models.DecimalField(max_digits=20, decimal_places=17)
    longitude   = models.DecimalField(max_digits=20, decimal_places=17)
    category    = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    destination = models.ForeignKey('Destination',on_delete=models.SET_NULL, null=True)
    city        = models.ForeignKey('City', on_delete=models.SET_NULL, null=True)
    district    = models.ForeignKey('District',on_delete=models.SET_NULL, null=True)
    price       = models.DecimalField(max_digits=18,decimal_places=2)
    is_room     = models.BooleanField()
    room        = models.ForeignKey('Room', on_delete=models.SET_NULL, null=True)
    is_dinning  = models.BooleanField()
    dinning     = models.ForeignKey('Dinning',on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    image_url = models.URLField()
    product   = models.ForeignKey('Product',on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_images'

class Coupon(models.Model):
    name          = models.CharField(max_length=45)
    code          = models.CharField(max_length=45)
    discount_rate = models.DecimalField(max_digits=2,decimal_places=0)
    expire_date   = models.DateField()
    product       = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'coupons'

class User(models.Model):
    email        = models.EmailField(max_length=100)
    password     = models.CharField(max_length=500)
    name         = models.CharField(max_length=45)
    last_name    = models.CharField(max_length=45, null=True)
    first_name   = models.CharField(max_length=45, null=True)
    phone_number = models.CharField(max_length=45, null=True)
    image_url    = models.URLField(max_length=2000)
    coupon       = models.ManyToManyField('Coupon', through='UserCoupon')
    dinning      = models.ManyToManyField('Dinning',through='Review')

    class Meta:
        db_table = 'users'

class Review(models.Model):
    dinning     = models.ForeignKey('Dinning',on_delete=models.CASCADE)
    user        = models.ForeignKey('User',on_delete=models.CASCADE)
    comment     = models.TextField()
    star_rating = models.SmallIntegerField(default=0)

    class Meta:
        db_table = 'reviews'

class UserCoupon(models.Model):
    user   = models.ForeignKey('User',on_delete=models.CASCADE)
    coupon = models.ForeignKey('Coupon', on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_coupons'



    