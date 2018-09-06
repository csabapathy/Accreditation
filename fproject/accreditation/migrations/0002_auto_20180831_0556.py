# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accreditation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='school',
            old_name='capus_address',
            new_name='campus_address',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='capus_city',
            new_name='campus_city',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='capus_id',
            new_name='campus_id',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='capus_name',
            new_name='campus_name',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='capus_zip',
            new_name='campus_zip',
        ),
    ]
