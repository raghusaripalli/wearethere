# Generated by Django 3.2.1 on 2021-05-11 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0002_auto_20210504_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='pincode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='contact',
            field=models.IntegerField(),
        ),
    ]