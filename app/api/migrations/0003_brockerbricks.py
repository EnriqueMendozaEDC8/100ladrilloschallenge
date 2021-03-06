# Generated by Django 3.1.1 on 2020-09-15 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200914_1539'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrockerBricks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.broker')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.property')),
            ],
        ),
    ]
