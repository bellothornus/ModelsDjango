# Generated by Django 3.0.6 on 2020-05-22 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsMaster', '0005_auto_20200522_2139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id_md', models.AutoField(db_column='id_Modelo', primary_key=True, serialize=False)),
                ('str_md_nombre', models.CharField(db_column='Nombre', max_length=256)),
                ('str_md_descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=256, null=True)),
                ('bool_md_eliminado', models.BooleanField(default=False)),
                ('id_md_emp', models.ForeignKey(db_column='id_Empresa', on_delete=django.db.models.deletion.CASCADE, to='ModelsMaster.Empresa')),
            ],
            options={
                'db_table': 'modelos',
            },
        ),
    ]
