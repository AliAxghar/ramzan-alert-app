# Generated by Django 2.2.6 on 2019-11-20 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191028_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='dua',
            name='reference',
            field=models.CharField(default='reference', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='quran',
            name='arabic',
            field=models.FileField(upload_to='files/'),
        ),
    ]
