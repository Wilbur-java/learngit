# Generated by Django 2.2.1 on 2019-10-25 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backtrack', '0002_auto_20191025_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmation',
            name='done',
        ),
        migrations.RemoveField(
            model_name='pbi',
            name='sprintNo',
        ),
        migrations.RemoveField(
            model_name='pbi',
            name='status',
        ),
        migrations.AlterField(
            model_name='confirmation',
            name='pbi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backtrack.Pbi'),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backtrack.Productowner'),
        ),
        migrations.AlterField(
            model_name='project',
            name='pb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backtrack.Productbacklog'),
        ),
    ]
