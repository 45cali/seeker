# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0004_auto_20150129_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lookup',
            name='updated_by',
        ),
    ]
