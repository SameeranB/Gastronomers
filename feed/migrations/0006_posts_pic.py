# Generated by Django 2.2.5 on 2019-10-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0005_auto_20191029_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
