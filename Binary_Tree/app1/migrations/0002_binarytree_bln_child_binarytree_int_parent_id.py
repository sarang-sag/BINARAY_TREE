# Generated by Django 5.0.1 on 2024-02-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='binarytree',
            name='bln_child',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='binarytree',
            name='int_parent_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]