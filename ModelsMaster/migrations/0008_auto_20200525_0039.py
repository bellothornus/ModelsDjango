# Generated by Django 3.0.6 on 2020-05-24 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ModelsMaster', '0007_auto_20200525_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benchmarking',
            name='id_bench_sc',
            field=models.ForeignKey(db_column='id_Sector', on_delete=django.db.models.deletion.PROTECT, to='ModelsMaster.Sector'),
        ),
        migrations.AlterField(
            model_name='benchmarking',
            name='str_bench_descripcion',
            field=models.CharField(blank=True, db_column='Descripcion', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='benchmarking',
            name='str_bench_nombre',
            field=models.CharField(db_column='Nombre', max_length=256),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='id_ob',
            field=models.AutoField(db_column='id_Objetivo', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='id_ob_pc',
            field=models.ForeignKey(db_column='id_Capitulo', on_delete=django.db.models.deletion.PROTECT, to='ModelsMaster.PuntosCapitulo'),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='str_ob_codificacion',
            field=models.CharField(db_column='Codificacion', max_length=256),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='str_ob_descripcion',
            field=models.CharField(blank=True, db_column='Descripcion', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='str_ob_nombre',
            field=models.CharField(db_column='Nombre', max_length=256),
        ),
        migrations.AlterField(
            model_name='objetivorelacionado',
            name='id_or',
            field=models.AutoField(db_column='id_ObjetivoRelacionado', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='objetivorelacionado',
            name='id_or_ob',
            field=models.ForeignKey(db_column='id_Objetivo', on_delete=django.db.models.deletion.PROTECT, related_name='Id_Objetivo', to='ModelsMaster.Objetivo'),
        ),
        migrations.AlterField(
            model_name='objetivorelacionado',
            name='id_or_ob_asociado',
            field=models.ForeignKey(db_column='id_Objetivo_Asociado', on_delete=django.db.models.deletion.PROTECT, related_name='Id_ObjetivoAsociado', to='ModelsMaster.Objetivo'),
        ),
        migrations.AlterField(
            model_name='puntoscapitulo',
            name='id_pc',
            field=models.AutoField(db_column='id_Capitulo', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='puntoscapitulo',
            name='id_pc_am',
            field=models.ForeignKey(db_column='id_Ambito', on_delete=django.db.models.deletion.PROTECT, to='ModelsMaster.Ambito'),
        ),
        migrations.AlterField(
            model_name='puntoscapitulo',
            name='id_pc_md',
            field=models.ForeignKey(db_column='id_Modelo', on_delete=django.db.models.deletion.PROTECT, to='ModelsMaster.Modelo'),
        ),
        migrations.AlterField(
            model_name='puntoscapitulo',
            name='str_pc_nombre',
            field=models.CharField(db_column='Nombre', max_length=256),
        ),
    ]
