# Generated by Django 3.2.9 on 2022-01-09 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0007_auto_20220109_2248'),
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
