# Generated by Django 2.1.4 on 2018-12-25 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('turkey_orders', '0007_auto_20181223_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turkey_orders',
            name='collection_date',
            field=models.TextField(choices=[('21', '21ST'), ('22', '22ND'), ('23', '23RD'), ('24', '24TH'), ('29', '29ND'), ('30', '22ED'), ('31', '22ST')], default='24TH', max_length=10),
        ),
        migrations.AlterField(
            model_name='turkey_orders',
            name='phone_number',
            field=models.IntegerField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='turkey_orders',
            name='t_type',
            field=models.CharField(choices=[('farm_fresh', 'FARM FRESH'), ('free_range', 'FREE RANGE'), ('organic', 'ORGANIC')], default='FARM FRESH', max_length=14),
        ),
        migrations.AlterField(
            model_name='turkey_orders',
            name='turkey',
            field=models.CharField(choices=[('whole_turkey', 'WHOLE TURKEY'), ('boned_and_rolled', 'B + R'), ('boneed_rolled_stuffed', 'B + R + S'), ('boned_rolled_own_stuffing', 'B + R + OWN STUFFING'), ('crown', 'CROWN'), ('crown_boned_rolled', 'B + R CROWN'), ('crown_boned_rolled_stuffed', 'B + R + STUFFED'), ('turkey_breast', 'TURKEY BREAST')], default='WHOLE TURKEY', max_length=14),
        ),
        migrations.AlterField(
            model_name='turkey_orders',
            name='weight',
            field=models.CharField(choices=[('2kg', '2KG'), ('2_5kg', '2.5 KG'), ('3kg', '3KG'), ('3_5kg', '3.5KG'), ('4kg', '4kg'), ('4_5kg', '4.5KG'), ('5kg', '5KG'), ('5_5kg', '5.5KG'), ('6_5kg', '6.5KG'), ('7_5kg', '7.5KG'), ('8_5kg', '8.5KG'), ('9_5kg', '9.5KG'), ('10_5kg', '10.5KG')], default='5.5KG', max_length=14),
        ),
    ]
