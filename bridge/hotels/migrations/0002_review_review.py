# Generated by Django 4.0.1 on 2022-01-10 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review',
            field=models.TextField(default='Great', null=True),
        ),
    ]
