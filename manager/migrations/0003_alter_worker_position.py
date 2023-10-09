# Generated by Django 4.2.5 on 2023-10-01 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("manager", "0002_alter_worker_options_alter_worker_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="manager.position",
            ),
        ),
    ]