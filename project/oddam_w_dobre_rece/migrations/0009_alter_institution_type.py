# Generated by Django 5.1 on 2024-08-21 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oddam_w_dobre_rece', '0008_alter_donation_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='type',
            field=models.CharField(choices=[('FN', 'Fundacja'), ('OP', 'Organizacja Pozarządowa'), ('ZL', 'Zbiórka Lokalna')], default='FN', max_length=2),
        ),
    ]
