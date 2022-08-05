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


class BrandSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CampaignDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignDates
        fields = ("start_date", "end_date")


class CampaignSerializer(ModelSerializer):
    campaign_dates = CampaignDatesSerializer(many=True)

    class Meta:
        model = Campaign
        fields = ['name', 'hashtag', 'campaign_type', 'campaign_status', 'brand', 'campaign_dates']

    def create(self, validated_data):
        campaign_dates_data = validated_data.pop('campaign_dates', None)
        item = Campaign.objects.create(**validated_data)
        for date in campaign_dates_data:
            CampaignDates.objects.create(campaign=item, **date)
        return item
