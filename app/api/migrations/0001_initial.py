# Generated by Django 3.1.1 on 2020-09-14 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('existence', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Broker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.TextField()),
                ('detail', models.TextField()),
                ('highProfitability', models.FloatField()),
                ('lowProfitability', models.FloatField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('checkout', models.BooleanField()),
                ('brick', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.brick')),
                ('broker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.broker')),
            ],
        ),
        migrations.AddField(
            model_name='brick',
            name='broker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.broker'),
        ),
        migrations.AddField(
            model_name='brick',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.property'),
        ),
    ]
