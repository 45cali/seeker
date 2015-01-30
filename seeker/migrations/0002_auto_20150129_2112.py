# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lookup',
            name='owner_email',
        ),
        migrations.AlterField(
            model_name='lookup',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field=b'username'),
        ),
        migrations.AlterField(
            model_name='lookup',
            name='owner',
            field=models.ForeignKey(to='auth.Group', to_field=b'name'),
        ),
        migrations.AlterField(
            model_name='lookup',
            name='updated_by',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
