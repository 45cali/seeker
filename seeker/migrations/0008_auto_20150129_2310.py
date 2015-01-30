# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0007_auto_20150129_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product',
            field=models.CharField(unique=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
