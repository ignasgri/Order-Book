# Generated by Django 2.1.4 on 2018-12-22 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('turkey_orders', '0002_auto_20181222_0837'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turkey_orders',
            name='description',
        ),
    ]
