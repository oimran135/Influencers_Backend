from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import (
    Campaign,
    Brand,
)

class HashtagSerializer(ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['id', 'hashtag']


class CampaignSerializer(ModelSerializer):
    
    class Meta:
        model = Campaign
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'


class ViewCampaignsSerializer(ModelSerializer):
    brand_set = serializers.ImageField(source = "brand.brand_image")

    class Meta:
        model = Campaign
        fields = ['name', 'hashtag', 'start_date', 'campaign_type', 'campaign_status', 'brand_set']


