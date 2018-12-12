# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='complemento_endereco',
            field=models.CharField(verbose_name='Complemento', max_length=200, default=0),
            preserve_default=False,
        ),
    ]
