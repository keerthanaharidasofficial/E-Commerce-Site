# Generated by Django 4.2.5 on 2023-09-20 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0006_rename_login_id_ecom_buyer_wishlist_datatable_user_loginid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecom_buyer_wishlist_datatable',
            name='prod_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
