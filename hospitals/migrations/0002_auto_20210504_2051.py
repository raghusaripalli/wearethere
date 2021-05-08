# Generated by Django 3.2.1 on 2021-05-05 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='address',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospital',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]