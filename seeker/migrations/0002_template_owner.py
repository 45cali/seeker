# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='owner',
            field=models.CharField(default='oneoffdefault', max_length=255),
            preserve_default=False,
        ),
    ]
