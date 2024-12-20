# Generated by Django 5.0.7 on 2024-12-18 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id_node', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=45)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Projet',
            fields=[
                ('id_projet', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=45)),
                ('date_creation', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id_node', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='rank', serialize=False, to='ahp.node')),
                ('global_note', models.DecimalField(decimal_places=0, max_digits=5)),
                ('rank', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comparaison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=0, max_digits=5)),
                ('compared_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comparisons_to', to='ahp.node')),
                ('id_node1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comparisons_node1', to='ahp.node')),
                ('id_node2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comparisons_node2', to='ahp.node')),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_sum', models.DecimalField(decimal_places=0, max_digits=5)),
                ('nrmal_row_sum', models.DecimalField(decimal_places=0, max_digits=5)),
                ('parent_id', models.IntegerField()),
                ('local_weight', models.DecimalField(decimal_places=0, max_digits=5)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='priorities', to='ahp.node')),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='id_projet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nodes', to='ahp.projet'),
        ),
    ]