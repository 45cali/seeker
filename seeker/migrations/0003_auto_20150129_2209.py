# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0002_auto_20150129_2112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lookup',
            name='updated_by',
        ),
        migrations.AlterField(
            model_name='lookup',
            name='created_by',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
