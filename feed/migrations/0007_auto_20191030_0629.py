# Generated by Django 2.2.5 on 2019-10-30 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0006_posts_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
