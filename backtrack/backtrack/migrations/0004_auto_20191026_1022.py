# Generated by Django 2.2.1 on 2019-10-26 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backtrack', '0003_auto_20191026_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirmation',
            name='pbi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backtrack.Pbi'),
        ),
        migrations.AlterField(
            model_name='pbi',
            name='conversation',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pbi',
            name='storypoints',
            field=models.IntegerField(blank=True),
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
