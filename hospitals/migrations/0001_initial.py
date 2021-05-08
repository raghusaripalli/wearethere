# Generated by Django 3.2.1 on 2021-05-04 20:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=100)),
                ('gmap_link', models.CharField(max_length=2048)),
                ('pincode', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(6), django.core.validators.MinLengthValidator(6)])),
                ('total_icu_beds', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_o2_beds', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('total_normal_beds', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20)),
                ('contact', models.IntegerField(validators=[django.core.validators.MaxLengthValidator(10), django.core.validators.MinLengthValidator(10)])),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.hospital')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField()),
                ('icu_beds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('o2_beds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('normal_beds', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospitals.hospital')),
            ],
        ),
    ]