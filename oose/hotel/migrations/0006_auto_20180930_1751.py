# Generated by Django 2.0.1 on 2018-09-30 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_remove_reward_reward_claimed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerreview',
            name='menu_item',
        ),
        migrations.RemoveField(
            model_name='customerreview',
            name='overall_rating',
        ),
        migrations.RemoveField(
            model_name='reward',
            name='reward_value',
        ),
    ]
