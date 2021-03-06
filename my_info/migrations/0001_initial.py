# Generated by Django 4.0.3 on 2022-03-24 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('Org', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=20)),
                ('NID', models.IntegerField(max_length=20)),
                ('Phone_No', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='room_info',
            fields=[
                ('room_number', models.IntegerField(primary_key=True, serialize=False)),
                ('room_name', models.CharField(max_length=20)),
                ('room_size', models.IntegerField(max_length=20)),
            ],
        ),
    ]
