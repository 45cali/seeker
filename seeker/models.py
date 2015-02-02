from django.db import models
import jsonfield
from django.contrib.auth.models import User, Group


class LookUp(models.Model):
    pattern = models.CharField(max_length=255)
    product = models.CharField(max_length=50)
    created_by = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    alert_set = jsonfield.JSONField(default=[], null=True, blank=True)

    class Meta:
        unique_together = (("pattern", "owner"),)


class Alert(models.Model):
    alert = models.CharField(max_length=50, unique=True)


class Product(models.Model):
    product = models.CharField(max_length=50, unique=True)


class Template(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255)
    alert_set = jsonfield.JSONField(default=[])
    owner = models.CharField(max_length=255)

