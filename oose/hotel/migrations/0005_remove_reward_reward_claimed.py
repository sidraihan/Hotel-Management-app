# Generated by Django 2.0.1 on 2018-09-30 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_order_claimed_reward'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reward',
            name='reward_claimed',
        ),
    ]
