# Generated by Django 4.2.5 on 2023-09-21 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0007_ecom_buyer_wishlist_datatable_prod_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ecom_buyer_cart_datatable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_loginid', models.IntegerField()),
                ('prod_id', models.IntegerField()),
                ('prod_name', models.CharField(max_length=50)),
                ('imgfile', models.FileField(upload_to='')),
                ('prod_category', models.CharField(max_length=40)),
                ('prod_size', models.CharField(max_length=10)),
                ('prod_price', models.IntegerField()),
                ('prod_details', models.CharField(max_length=1000)),
                ('prod_quantity', models.IntegerField()),
            ],
        ),
    ]
