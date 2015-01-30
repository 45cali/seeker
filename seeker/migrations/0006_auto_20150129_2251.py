# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0005_remove_lookup_updated_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='find',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='lookup',
            name='owner',
            field=models.CharField(max_length=255),
        ),
    ]
