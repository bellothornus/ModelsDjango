# Generated by Django 3.0.6 on 2020-06-01 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsMaster', '0007_auto_20200601_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicadoraccionproceso',
            name='IdProc',
            field=models.ForeignKey(blank=True, db_column='IA_Id_Proceso', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ModelsMaster.Proceso'),
        ),
    ]
