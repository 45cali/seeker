# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seeker', '0003_auto_20150205_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookup',
            name='email',
            field=models.EmailField(default='coresys.ticketmaster.com', max_length=75),
            preserve_default=False,
        ),
    ]
