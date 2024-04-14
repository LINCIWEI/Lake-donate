# Generated by Django 4.1.2 on 2024-04-06 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ObjectID', models.IntegerField()),
                ('LochCode', models.TextField()),
                ('SurfaceArea', models.FloatField()),
                ('AuthID', models.TextField()),
                ('LochAuth', models.TextField()),
                ('IslandName', models.TextField()),
                ('LochName', models.TextField()),
                ('Price', models.IntegerField()),
            ],
        ),
    ]
