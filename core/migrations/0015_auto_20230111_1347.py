# Generated by Django 3.0 on 2023-01-11 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20230104_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='user2',
        ),
        migrations.AddField(
            model_name='friend',
            name='player1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='player11', to='core.Player'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='player2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='player22', to='core.Player'),
            preserve_default=False,
        ),
    ]