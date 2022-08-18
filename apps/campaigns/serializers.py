from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Campaign,
    Brand,
    CampaignDates, CampaignAmbassador,
)


class HashtagSerializer(ModelSerializer):
    class Meta:
        model = Campaign
        fields = ['id', 'hashtag']


class BrandSerializer(ModelSerializer):
    brand_image = serializers.ImageField(required=False)
    class Meta:
        model = Brand
        fields = '__all__'


class CampaignDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignDates
        fields = ("start_date", "end_date")


class CampaignAmbassadorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CampaignAmbassador
        fields = ["user", ]


class CampaignSerializer(ModelSerializer):
    campaign_dates = CampaignDatesSerializer(many=True, required=False)
    ambassadors = CampaignAmbassadorSerializer(many=True, write_only=True, required=False)
    brand_image = serializers.ImageField(source = "brand.brand_image", required=False)
    img = serializers.ImageField(required=False)

    class Meta:
        model = Campaign
        fields = ['name', 'hashtag', 'campaign_type', 'campaign_status', 'brand_image', 'campaign_dates', 'ambassadors', 'img', 'brand']

    def create(self, validated_data):
        campaign_dates_data = validated_data.pop('campaign_dates', None)
        ambassadors_list = validated_data.pop('ambassadors', None)
        item = Campaign.objects.create(**validated_data)
        for ambassador in ambassadors_list:
            CampaignAmbassador.objects.create(campaign=item, **ambassador)
        for date in campaign_dates_data:
            CampaignDates.objects.create(campaign=item, **date)
        return item
