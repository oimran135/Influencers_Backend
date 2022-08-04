# Generated by Django 4.0.6 on 2022-08-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0007_remove_campaign_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='influencers_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='campaign',
            name='start_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='CampaignDates',
        ),
    ]
