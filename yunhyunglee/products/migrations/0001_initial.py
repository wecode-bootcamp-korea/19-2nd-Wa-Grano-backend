# Generated by Django 3.1.4 on 2021-05-04 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Convenience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'conveniences',
            },
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('image_url', models.URLField(max_length=2000)),
            ],
            options={
                'db_table': 'destinations',
            },
        ),
        migrations.CreateModel(
            name='Dinning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'dinnings',
            },
        ),
        migrations.CreateModel(
            name='DinningType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'dinning_types',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.city')),
            ],
            options={
                'db_table': 'districts',
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'food_types',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('latitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('longitude', models.DecimalField(decimal_places=17, max_digits=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('is_room', models.BooleanField(default=False)),
                ('is_dinning', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.city')),
                ('destination', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.destination')),
                ('dinning', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.dinning')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.district')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_rating', models.SmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'room_types',
            },
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'service_types',
            },
        ),
        migrations.CreateModel(
            name='RoomConvenience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('convenience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.convenience')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.room')),
                ('service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.servicetype')),
            ],
            options={
                'db_table': 'room_conveniences',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='convenience',
            field=models.ManyToManyField(through='products.RoomConvenience', to='products.Convenience'),
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.roomtype'),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
            ],
            options={
                'db_table': 'product_images',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.room'),
        ),
        migrations.CreateModel(
            name='DinningOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('description', models.TextField()),
                ('dinning', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.dinning')),
            ],
            options={
                'db_table': 'dinning_options',
            },
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
        migrations.CreateModel(
            name='CategoryDestination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.destination')),
            ],
            options={
                'db_table': 'category_destinations',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='destination',
            field=models.ManyToManyField(through='products.CategoryDestination', to='products.Destination'),
        ),
    ]
