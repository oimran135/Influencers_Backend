import traceback
from django.db import transaction, IntegrityError
from rest_framework import status, permissions
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

    def get_queryset(self):
        queryset = Campaign.objects.filter(campaign_status="Active")
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = CampaignSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CountStatistics(APIView):

    def get(self, request):
        query1 = Campaign.objects.all().count()
        query2 = Campaign.objects.filter(campaign_status="Completed").count()
        query3 = Campaign.objects.filter(campaign_status="Active").count()
        query4 = Influencer.objects.all().count()

        data = {
            "Total Campaigns": query1,
            "Successful Campaigns": query2,
            "In Progress Campaigns": query3,
            "Total Ifluencers": query4,
        }

        return Response(data, status=status.HTTP_200_OK)


class AllCampaignsView(APIView):

    def get_queryset(self):
        queryset = Campaign.objects.all()
        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = CampaignSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCampaignView(APIView):
    # permission_classes = [permissions.IsAdminUser]

    @swagger_auto_schema(
        request_body=CampaignSerializer,
        responses={
            201: "Created",
            403: "Forbidden",
            500: "Internal Server Error",
        },
    )
    def post(self, request):
        try:
            with transaction.atomic():
                serializer = CampaignSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
            return Response({"message": e.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # def get_permissions(self):
    #     if self.request.user.is_staff:
    #         pass


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

        if request.user.is_staff:
            serializer = BrandSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_403_FORBIDDEN)


class AmbassadorActiveCampaingsView(APIView):

    def get(self, request):
        user_id = request.user.id
        queryset = Campaign.objects.filter(ambassadors=user_id, campaign_status="Active")
        serializer = CampaignSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

