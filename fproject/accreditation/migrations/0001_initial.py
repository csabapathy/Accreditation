# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('institution_id', models.CharField(max_length=250)),
                ('institution_name', models.CharField(max_length=250)),
                ('institution_address', models.CharField(max_length=250)),
                ('institution_city', models.CharField(max_length=250)),
                ('institution_state', models.CharField(max_length=250)),
                ('institution_zip', models.CharField(max_length=250)),
                ('institution_phone', models.CharField(max_length=250)),
                ('institution_opeid', models.CharField(max_length=250)),
                ('institution_ipeds_united', models.CharField(max_length=250)),
                ('institution_web_address', models.CharField(max_length=250)),
                ('capus_id', models.CharField(max_length=250)),
                ('capus_name', models.CharField(max_length=250)),
                ('capus_address', models.CharField(max_length=250)),
                ('capus_city', models.CharField(max_length=250)),
                ('campus_state', models.CharField(max_length=250)),
                ('capus_zip', models.CharField(max_length=250)),
                ('campus_ipeds_unitid', models.CharField(max_length=250)),
                ('accreditation_type', models.CharField(max_length=250)),
                ('agency_name', models.CharField(max_length=250)),
                ('agency_status', models.CharField(max_length=250)),
                ('program_name', models.CharField(max_length=250)),
                ('accreditation_status', models.CharField(max_length=250)),
                ('accreditation_data_type', models.CharField(max_length=250)),
                ('periods', models.CharField(max_length=250)),
                ('last', models.CharField(max_length=250)),
            ],
        ),
    ]
