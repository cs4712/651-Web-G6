# Generated by Django 2.1.2 on 2018-11-05 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo_blog', '0004_auto_20181023_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
