# Generated by Django 2.0.1 on 2018-09-25 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reward',
            name='on_item',
        ),
        migrations.AddField(
            model_name='reward',
            name='total_points',
            field=models.IntegerField(default=0),
        ),
    ]
