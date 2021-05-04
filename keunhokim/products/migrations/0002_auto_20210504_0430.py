# Generated by Django 3.1.4 on 2021-05-04 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.city'),
        ),
        migrations.AddField(
            model_name='product',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.destination'),
        ),
        migrations.AddField(
            model_name='product',
            name='dinning',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.dinning'),
        ),
        migrations.AddField(
            model_name='product',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.district'),
        ),
        migrations.AddField(
            model_name='product',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.room'),
        ),
        migrations.AddField(
            model_name='district',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.city'),
        ),
        migrations.AddField(
            model_name='dinningoption',
            name='dinning',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.dinning'),
        ),
        migrations.AddField(
            model_name='dinning',
            name='dinning_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.dinningtype'),
        ),
        migrations.AddField(
            model_name='dinning',
            name='food_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.foodtype'),
        ),
        migrations.AddField(
            model_name='convenience',
            name='service_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.servicetype'),
        ),
        migrations.AddField(
            model_name='categorydestination',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.AddField(
            model_name='categorydestination',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.destination'),
        ),
        migrations.AddField(
            model_name='category',
            name='destination',
            field=models.ManyToManyField(through='products.CategoryDestination', to='products.Destination'),
        ),
    ]
