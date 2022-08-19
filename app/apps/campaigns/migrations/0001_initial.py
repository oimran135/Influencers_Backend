# Generated by Django 4.1 on 2022-08-05 14:29

import apps.campaigns.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("authentication", "0003_influencer_img_user_img"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "brand_image",
                    models.ImageField(
                        blank=True,
                        default="media/images/Brands/None/index.jpeg",
                        upload_to=apps.campaigns.models.BrandImages,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Campaign",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                ("hashtag", models.CharField(max_length=20, unique=True)),
                (
                    "img",
                    models.ImageField(
                        blank=True,
                        default="media/images/Brands/None/index.jpeg",
                        upload_to=apps.campaigns.models.CampaignImages,
                    ),
                ),
                (
                    "campaign_type",
                    models.CharField(
                        choices=[("Periodic", "Periodic"), ("Single", "Single")],
                        max_length=10,
                    ),
                ),
                (
                    "campaign_status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Active", "Active"),
                            ("Inactive", "Inactive"),
                            ("Completed", "Completed"),
                            ("Periodic-Break", "PRD"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Interest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "influencer",
                    models.ManyToManyField(
                        blank=True,
                        related_name="influencer_interests",
                        to="authentication.influencer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "influencer",
                    models.ManyToManyField(
                        blank=True,
                        related_name="influencer_category",
                        to="authentication.influencer",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CampaignDates",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "campaign",
                    models.ForeignKey(
                        blank=True,
                        default=0,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="campaign_dates",
                        to="campaigns.campaign",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CampaignAmbassador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "campaign_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="campaign_ambassadors",
                        to="campaigns.campaign",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_ambassadors",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="campaign",
            name="ambassadors",
            field=models.ManyToManyField(
                through="campaigns.CampaignAmbassador", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="campaign",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="brand_set",
                to="campaigns.brand",
            ),
        ),
    ]