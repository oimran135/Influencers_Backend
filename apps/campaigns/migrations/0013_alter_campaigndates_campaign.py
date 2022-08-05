# Generated by Django 4.1 on 2022-08-05 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("campaigns", "0012_remove_campaign_campaign_dates_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="campaigndates",
            name="campaign",
            field=models.ForeignKey(
                blank=True,
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="campaign_dates",
                to="campaigns.campaign",
            ),
        ),
    ]
