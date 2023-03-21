# Generated by Django 4.1.3 on 2023-02-20 19:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='sensor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='measurement.sensor'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]