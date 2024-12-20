# Generated by Django 5.0.7 on 2024-12-20 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahp', '0002_rename_projet_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comparaison',
            name='value',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='priority',
            name='column_sum',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='priority',
            name='local_weight',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='priority',
            name='nrmal_row_sum',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
        migrations.AlterField(
            model_name='rank',
            name='global_note',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]