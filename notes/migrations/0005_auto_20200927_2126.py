# Generated by Django 3.1 on 2020-09-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20200927_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='labels',
            field=models.CharField(choices=[('primary', 'primary'), ('success', 'success'), ('secondary', 'secondary'), ('danger', 'danger'), ('warning', 'warning'), ('info', 'info'), ('light', 'light'), ('dark', 'dark')], default='success', max_length=50),
        ),
    ]
