# Generated by Django 2.2.5 on 2019-10-29 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_auto_20191029_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
