# Generated by Django 2.2.5 on 2019-10-29 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_auto_20191029_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='dish',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Dish'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='rating',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='shares',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
