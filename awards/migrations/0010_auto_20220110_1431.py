# Generated by Django 3.2.9 on 2022-01-10 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0009_auto_20220109_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='website',
            name='content',
        ),
        migrations.RemoveField(
            model_name='website',
            name='design',
        ),
        migrations.RemoveField(
            model_name='website',
            name='usability',
        ),
    ]
