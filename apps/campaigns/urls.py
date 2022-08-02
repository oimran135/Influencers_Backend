from django.urls import path

from .views import (
    ActiveCampaignsView,
    BrandView,
    AllCampaignsView,
    CountStatistics,
)

urlpatterns = [
    path('brand/all/', BrandView.as_view()),
    path('campaigns/all/', AllCampaignsView.as_view()),
    path('campaigns/active/', ActiveCampaignsView.as_view()),
    path('utils/counts/', CountStatistics.as_view()),
    #path('', .as_view()),
]