# Generated by Django 3.1.1 on 2020-09-30 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_auto_20200930_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='man_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myApp.emp'),
        ),
    ]
