from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('FeMale', 'Female'),
)

ACC_TYPE =(
    ('savings account','savings account'),
    ('current account','current account'),
    ('other','other'),

)

MATERIAL_TYPE =(
    ('debit card','debit card'),
    ('credit card','credit card'),
    ('other','other'),



)
class district(models.Model):
    name=models.CharField(max_length=220,unique=True)


    def __str__(self):
        return '{}'.format(self.name)

class branch(models.Model):
    district = models.ForeignKey(district, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class persondetails(models.Model):
    name = models.CharField(max_length=220, unique=True)
    dob=models.DateField()
    age=models.IntegerField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    phone_no=models.IntegerField()
    mailid=models.EmailField(max_length = 200)
    address = models.CharField(max_length=220, unique=True)
    district = models.ForeignKey(district, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(branch, on_delete=models.SET_NULL, blank=True, null=True)
    account_type=models.CharField(max_length=220, choices=ACC_TYPE)
    material_type=MultiSelectField(choices=MATERIAL_TYPE,default="",max_length=220)

    def __str__(self):
        return self.name

