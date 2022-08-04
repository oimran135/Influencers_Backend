from email.policy import default
from django.db import models


def BrandImages(instance, filename):
    return '/'.join( ['images', 'Brands', str(instance.id), filename] )

def CampaignImages(instance, filename):
    return '/'.join( ['images', 'Campaigns', str(instance.id), filename] )

class Brand(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    brand_image = models.ImageField(upload_to=BrandImages, blank=True, null=False, default='media/images/Brands/None/index.jpeg')

    def __str__(self):
      return self.name


class Campaign(models.Model):

    campaignType_choices = (
        ("Preodic", "Preodic"),
        ("Single", "Single"),
    )

    campaignStatus_choices = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Completed", "Completed"),
        ("Periodic-Break", "PRD"), #Only for preodic
    )

    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    hashtag = models.CharField(max_length=20, unique=True, blank=False, null=False)
    img = models.ImageField(upload_to=CampaignImages, blank=True, null=False, default='media/images/Brands/None/index.jpeg')
    campaign_type = models.CharField(max_length=10, choices=campaignType_choices, blank=False, null=False)
    campaign_status = models.CharField(max_length=20, choices= campaignStatus_choices,blank=True, null=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, related_name="brand_set", on_delete=models.CASCADE)
    ambassadors = models.ManyToManyField('authentication.User', blank=True, related_name="campaign_ambassadors")

    def __str__(self):
      return self.name


class CampaignDates(models.Model):
    campaign = models.ForeignKey(Campaign, null=True, blank=True, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    influencer = models.ManyToManyField("authentication.Influencer", blank=True, related_name="influencer_category")

    def __unicode__(self):
      return self.name

class Interest(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    influencer = models.ManyToManyField("authentication.Influencer", blank=True, related_name="influencer_interests")



