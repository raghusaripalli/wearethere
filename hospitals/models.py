from django.core.validators import MinValueValidator, MaxLengthValidator, MinLengthValidator
from django.db import models


class Hospital(models.Model):
    name = models.CharField(max_length=50, null=False)
    district = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    address = models.CharField(max_length=100, null=False)
    gmap_link = models.CharField(max_length=2048, null=False)
    pincode = models.IntegerField(validators=[MaxLengthValidator(6), MinLengthValidator(6)], null=False)
    total_icu_beds = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    total_o2_beds = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    total_normal_beds = models.IntegerField(default=0, validators=[MinValueValidator(0)])


class History(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    last_updated = models.DateTimeField()
    icu_beds = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    o2_beds = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    normal_beds = models.IntegerField(null=False, validators=[MinValueValidator(0)])


class Staff(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20, null=False)
    contact = models.IntegerField(validators=[MaxLengthValidator(10), MinLengthValidator(10)], null=False)
