# Generated by Django 4.2.5 on 2023-09-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ecom_seller_register_datatable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('pw', models.CharField(max_length=15)),
                ('imgfile', models.ImageField(upload_to='ecom_app/static')),
            ],
        ),
    ]
