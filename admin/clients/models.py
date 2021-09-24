from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Clients(models.Model):
    businessName = models.CharField(
        'Business Name', max_length=100, db_column='b_name')
    businessAddress = models.CharField(
        'Business Address', max_length=255, db_column='b_address')
    businessPhone = PhoneNumberField(
        'Business Phone', max_length=16, unique=True, db_column='b_phone')
    personName = models.CharField(
        'Person Name', max_length=100, db_column='cp_name')
    personEmail = models.EmailField(
        "Person Email", unique=True, db_column='cp_email')
    personPhone = PhoneNumberField(
        'Person Phone', max_length=16, unique=True, db_column='cp_phone')
    username = models.CharField(
        max_length=50, unique=True)
    password = models.CharField(max_length=128)
    emailStatus = models.BooleanField(
        'Email Status', db_column='mail_status', default=False)
    status = models.BooleanField(db_column='status', default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "clients"
        ordering = ('businessName',)

    def __str__(self):
        return str(self.businessName)
