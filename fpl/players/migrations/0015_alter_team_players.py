# Generated by Django 4.0.1 on 2022-02-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0014_team_captain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(null=True, related_name='team', to='players.Players'),
        ),
    ]