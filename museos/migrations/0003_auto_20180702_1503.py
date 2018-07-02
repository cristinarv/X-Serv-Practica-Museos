# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('museos', '0002_auto_20180701_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='configuracion',
            old_name='tamaño',
            new_name='tamano',
        ),
    ]
