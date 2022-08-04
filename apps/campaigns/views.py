from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.authentication.models import Influencer

from .models import (
    Brand,
    Campaign,
)

from .serializers import (
    BrandSerializer,
    CampaignSerializer,
    ViewCampaignsSerializer,
    HashtagSerializer,
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
    @swagger_auto_schema(
    request_body=CampaignSerializer,
        responses={
            201: "Reset Content",
            403: "Forbidden",
            500: "Internal Server Error",
        },
    )

    def post(self, request):
        bool_var = request.user.is_staff

        if bool_var is True:
            serializer = CampaignSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_403_FORBIDDEN)    


class HashtagsView(APIView):

    def get(self, request):
        query = Campaign.objects.all()
        serializer = HashtagSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBrandView(APIView):

    @swagger_auto_schema(
    request_body=BrandSerializer,
        responses={
            201: "Reset Content",
            403: "Forbidden",
            500: "Internal Server Error",
        },
    )

    def post(self, request):
        bool_var = request.user.is_staff

        if bool_var is True:
            serializer = BrandSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_403_FORBIDDEN)