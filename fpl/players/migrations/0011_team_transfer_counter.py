# Generated by Django 4.0.1 on 2022-02-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0010_alter_players_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='transfer_counter',
            field=models.PositiveBigIntegerField(default=1),
        ),
    ]