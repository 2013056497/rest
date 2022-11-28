from django.db import models


class RestUser(models.Model):
    name = models.CharField(max_length=256)
    address = models.TextField()
    mobile = models.CharField(max_length=11)
    date_of_birth = models.DateField()
