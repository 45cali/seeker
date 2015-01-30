# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0003_auto_20150129_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookup',
            name='updated_by',
            field=models.CharField(default='oneoff', max_length=255, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lookup',
            name='created_by',
            field=models.CharField(max_length=255),
        ),
    ]
