# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0002_template_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookup',
            name='info',
            field=models.TextField(default='default text'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lookup',
            name='oncall',
            field=models.URLField(default='oncall.com'),
            preserve_default=False,
        ),
    ]
