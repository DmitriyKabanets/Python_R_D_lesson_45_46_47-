# Generated by Django 5.0.2 on 2024-04-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='begin_at',
            field=models.DateField(blank=True),
        ),
    ]
