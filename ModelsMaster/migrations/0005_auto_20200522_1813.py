# Generated by Django 3.0.6 on 2020-05-22 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsMaster', '0004_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='empresa',
            old_name='id_emp_centro_principal',
            new_name='id_emp_ag',
        ),
    ]
