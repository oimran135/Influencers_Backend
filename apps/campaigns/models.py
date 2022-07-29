from email.policy import default
from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    img = models.ImageField(blank=True, null=True)


class Campaign(models.Model):

    campaignType_choices = (
        ("Preodic", "Preodic"),
        ("Single", "Single"),
    )

    campaignStatus_choices = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("On Break", "BRK"), #Only for preodic
    )

    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    hashtag = models.CharField(max_length=20, unique=True, blank=False, null=False)
    img = models.ImageField()
    campaign_type = models.CharField(max_length=10, choices=campaignType_choices, blank=False, null=False)
    start_date = models.DateField(auto_now=True)
    days = models.IntegerField(blank=True, null=True)
    influencers_count = models.IntegerField(blank=True, null=True)
    campaign_status = models.CharField(max_length=10, choices= campaignStatus_choices,blank=True, null=True)
    total_posts = models.IntegerField(blank=True, null=True)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)


class Interest(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)



