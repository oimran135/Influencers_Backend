# Generated by Django 4.0.6 on 2022-08-04 12:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaigns', '0006_alter_brand_brand_image_alter_campaign_brand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='days',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='influencers_count',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='start_date',
        ),
        migrations.AddField(
            model_name='campaign',
            name='ambassadors',
            field=models.ManyToManyField(blank=True, related_name='campaign_ambassadors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CampaignDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('campaign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='campaign_dates', to='campaigns.campaign')),
            ],
        ),
    ]