# Generated by Django 3.0 on 2022-12-27 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20221227_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='section',
            old_name='subManager_id',
            new_name='sub_manager_id',
        ),
    ]