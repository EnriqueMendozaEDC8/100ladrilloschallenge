# Generated by Django 3.1.1 on 2020-09-14 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='brick',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='brick',
            name='existence',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='broker',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='checkout',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='property',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
