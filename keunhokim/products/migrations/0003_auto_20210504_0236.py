# Generated by Django 3.2 on 2021-05-04 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210503_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='dinning',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='user',
            name='dinning',
        ),
        migrations.RemoveField(
            model_name='usercoupon',
            name='coupon',
        ),
        migrations.RemoveField(
            model_name='usercoupon',
            name='user',
        ),
        migrations.DeleteModel(
            name='Coupon',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserCoupon',
        ),
    ]
