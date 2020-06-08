# Generated by Django 3.0.6 on 2020-05-24 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsMaster', '0006_modelo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objetivo',
            fields=[
                ('id_ob', models.AutoField(db_column='id_ob', primary_key=True, serialize=False)),
                ('str_ob_nombre', models.CharField(blank=True, db_column='Nombre', max_length=256, null=True)),
                ('str_ob_descripcion', models.CharField(db_column='Descripcion', max_length=256)),
                ('str_ob_codificacion', models.CharField(blank=True, db_column='Codificacion', max_length=256, null=True)),
                ('num_ob_any', models.IntegerField(blank=True, db_column='Año', null=True)),
                ('bool_ob_eliminado', models.BooleanField(db_column='eliminado', default=False)),
            ],
            options={
                'db_table': 'objetivos',
            },
        ),
        migrations.CreateModel(
            name='PuntosCapitulo',
            fields=[
                ('id_pc', models.AutoField(db_column='id_Bench', primary_key=True, serialize=False)),
                ('str_pc_nombre', models.CharField(blank=True, db_column='Nombre', max_length=256, null=True)),
                ('str_pc_descripcion', models.CharField(blank=True, db_column='Descripcion', max_length=256, null=True)),
                ('bool_pc_eliminado', models.BooleanField(db_column='eliminado', default=False)),
                ('id_pc_am', models.ForeignKey(blank=True, db_column='id_Ambito', null=True, on_delete=django.db.models.deletion.PROTECT, to='ModelsMaster.Ambito')),
                ('id_pc_md', models.ForeignKey(blank=True, db_column='id_Modelo', null=True, on_delete=django.db.models.deletion.PROTECT, to='ModelsMaster.Modelo')),
            ],
            options={
                'db_table': 'puntos_capitulo',
            },
        ),
        migrations.CreateModel(
            name='ObjetivoRelacionado',
            fields=[
                ('id_or', models.AutoField(db_column='id_Objetivo_relacionado', primary_key=True, serialize=False)),
                ('str_or_nombre', models.CharField(blank=True, db_column='Nombre', max_length=256, null=True)),
                ('bool_or_eliminado', models.BooleanField(db_column='eliminado', default=False)),
                ('id_or_ob', models.ForeignKey(blank=True, db_column='id_Objetivo', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Id_Objetivo', to='ModelsMaster.Objetivo')),
                ('id_or_ob_asociado', models.ForeignKey(blank=True, db_column='id_Objetivo_Asociado', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Id_Objetivo_Asociado', to='ModelsMaster.Objetivo')),
            ],
            options={
                'db_table': 'objetivo_relacionado',
            },
        ),
        migrations.AddField(
            model_name='objetivo',
            name='id_ob_pc',
            field=models.ForeignKey(blank=True, db_column='id_Capitulo', null=True, on_delete=django.db.models.deletion.PROTECT, to='ModelsMaster.PuntosCapitulo'),
        ),
        migrations.AddField(
            model_name='objetivo',
            name='id_ob_to',
            field=models.ForeignKey(db_column='id_Tipo_Objetivo', on_delete=django.db.models.deletion.PROTECT, to='ModelsMaster.TipoObjetivo'),
        ),
    ]