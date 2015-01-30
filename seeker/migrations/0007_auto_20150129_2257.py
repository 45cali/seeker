# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0006_auto_20150129_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=255)),
                ('alert_set', jsonfield.fields.JSONField(default=[])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='AlertList',
            new_name='Alert',
        ),
        migrations.RenameModel(
            old_name='ProductList',
            new_name='Product',
        ),
    ]
