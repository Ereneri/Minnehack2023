# Generated by Django 4.1.5 on 2023-01-29 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thegarden', '0003_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
