# Generated by Django 2.1.2 on 2018-11-08 18:54

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo_blog', '0006_auto_20181105_0314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='post',
            name='longitude',
        ),
        migrations.AlterField(
            model_name='post',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]
