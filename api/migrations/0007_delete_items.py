# Generated by Django 2.2.6 on 2020-02-17 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_items'),
    ]

    operations = [
        migrations.DeleteModel(
            name='items',
        ),
    ]