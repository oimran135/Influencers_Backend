from django.db import models

from apps.authentication.models import User


def BrandImages(instance, filename):
    return '/'.join(['images', 'Brands', str(instance.id), filename])


def CampaignImages(instance, filename):
    return '/'.join(['images', 'Campaigns', str(instance.id), filename])


class Brand(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    brand_image = models.ImageField(upload_to=BrandImages, blank=True, null=False,
                                    default='/images/Brands/None/index.jpeg')

    def __str__(self):
        return self.name


class Campaign(models.Model):
    campaignType_choices = (
        ("Periodic", "Periodic"),
        ("Single", "Single"),
    )

    campaignStatus_choices = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Completed", "Completed"),
        ("Periodic-Break", "PRD"),  # Only for preodic
    )

    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    hashtag = models.CharField(max_length=20, unique=True, blank=False, null=False)
    img = models.ImageField(upload_to=CampaignImages, blank=True, null=False,
                            default='/images/Brands/None/index.jpeg')
    campaign_type = models.CharField(max_length=10, choices=campaignType_choices, blank=False, null=False)
    campaign_status = models.CharField(max_length=20, choices=campaignStatus_choices, blank=True, null=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, related_name="brand_set", on_delete=models.CASCADE)
    ambassadors = models.ManyToManyField(User, through='CampaignAmbassador', related_name="campaign_user")

    def __str__(self):
        return self.name


class CampaignDates(models.Model):
    campaign = models.ForeignKey(Campaign, related_name="campaign_dates", blank=True, on_delete=models.CASCADE,
                                 default=0)
    start_date = models.DateField()
    end_date = models.DateField()


class CampaignAmbassador(models.Model):
    user = models.ForeignKey(User, related_name="user_ambassadors", on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, related_name="campaign_ambassadors", on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    influencer = models.ManyToManyField("authentication.Influencer", blank=True, related_name="influencer_category")

    def __unicode__(self):
        return self.name


class Interest(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    influencer = models.ManyToManyField("authentication.Influencer", blank=True, related_name="influencer_interests")
