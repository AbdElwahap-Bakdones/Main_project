# Generated by Django 3.0 on 2023-01-14 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20230111_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='core.Player'),
        ),
    ]