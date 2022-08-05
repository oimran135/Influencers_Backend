from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from .models import (
    Campaign,
    Brand,
    CampaignDates,
)

class HashtagSerializer(ModelSerializer):

    class Meta:
        model = Campaign
        fields = ['id', 'hashtag']


class ActiveCampaignsSerializer(ModelSerializer):
    
    class Meta:
        model = Campaign
        fields = '__all__'


class BrandSerializer(ModelSerializer):
    
    class Meta:
        model = Brand
        fields = '__all__'


class AllCampaignsSerializer(ModelSerializer):
    brand_set = serializers.ImageField(source = "brand.brand_image")

    class Meta:
        model = Campaign
        fields = ['name', 'hashtag', 'campaign_type', 'campaign_status', 'brand_set']


class CampaignDatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampaignDates
        fields = "__all__"


class CreateCampaignSerializer(ModelSerializer):
    campaign_dates = CampaignDatesSerializer(write_only=True, many=True)

    authentication_classes = [IsAuthenticated]

    class Meta:
        model = Campaign
        fields = ['name', 'hashtag', 'campaign_type', 'campaign_status', 'brand', 'campaign_dates']

    def create(self, validated_data):
        campaignDates_data = validated_data.pop('campaign_dates', None)
        item = Campaign.objects.create(**validated_data)

        campaign_dates = []
        if campaignDates_data is not None:
            for date in campaignDates_data:
                date_id = date.pop('id', None)
                date_data, _ = CampaignDates.objects.get_or_create(id=date_id, defaults=date)
                campaign_dates.append(date_data)
                item.campaign_dates.add(*campaign_dates)
        item.save()
        return item
