# Generated by Django 4.0.4 on 2022-12-06 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onestop', '0021_alter_seller_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='password',
            field=models.CharField(default='', max_length=200),
        ),
    ]