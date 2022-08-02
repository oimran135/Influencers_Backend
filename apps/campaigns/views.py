from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.authentication.models import Influencer

from .models import (
    Brand,
    Campaign,
)

from .serializers import (
    BrandSerializer,
    CampaignSerializer,
    ViewCampaignsSerializer,
)


class BrandView(APIView):
    
    def get_queryset(request):
        queryset = Brand.objects.all()
        return queryset

    def get(self, request):
        queryset = BrandView.get_queryset(request)
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ActiveCampaignsView(APIView):

    def get_queryset(request):
        queryset = Campaign.objects.filter(campaign_status="Active")
        return queryset

    def get(self, request):
        queryset = ActiveCampaignsView.get_queryset(request)
        serializer = ViewCampaignsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CountStatistics(APIView):

    def get(self, request):
        query1 = Campaign.objects.all().count()
        query2 = Campaign.objects.filter(campaign_status="Completed").count()
        query3 = Campaign.objects.filter(campaign_status="Active").count()
        query4 = Influencer.objects.all().count()

        data = {
            "Total Campaigns":query1,
            "Successful Campaigns":query2,
            "In Progress Campaigns":query3,
            "Total Ifluencers":query4,
        }

        return Response(data, status=status.HTTP_200_OK)

class AllCampaignsView(APIView):

    def get_queryset(request):
        queryset = Campaign.objects.all()
        return queryset

    def get(self, request):
        queryset = AllCampaignsView.get_queryset(request)
        serializer = ViewCampaignsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCampaignView(APIView):

    def post(self, request):
        pass
       