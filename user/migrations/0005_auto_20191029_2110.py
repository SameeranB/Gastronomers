# Generated by Django 2.2.5 on 2019-10-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_follows'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]