# Generated by Django 2.2.6 on 2019-10-28 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191028_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quran',
            name='arabic',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='quran',
            name='urdu_arabic',
            field=models.FileField(upload_to=''),
        ),
    ]
