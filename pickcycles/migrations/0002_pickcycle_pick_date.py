# Generated by Django 2.0.2 on 2018-12-27 13:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pickcycles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickcycle',
            name='pick_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
