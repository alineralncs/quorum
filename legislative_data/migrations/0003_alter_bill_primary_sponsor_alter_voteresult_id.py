# Generated by Django 5.0.3 on 2024-03-22 23:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("legislative_data", "0002_alter_bill_id_alter_legislator_id_alter_vote_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bill",
            name="primary_sponsor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="legislative_data.legislator",
            ),
        ),
        migrations.AlterField(
            model_name="voteresult",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
