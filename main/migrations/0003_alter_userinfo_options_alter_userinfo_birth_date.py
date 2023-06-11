# Generated by Django 4.2.2 on 2023-06-11 19:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_userinfo_birth_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 6, 11, 19, 12, 57, 159346)),
        ),
    ]