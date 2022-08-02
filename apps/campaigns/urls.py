from django.urls import path

from .views import (
    ActiveCampaignsView,
    BrandView,
    AllCampaignsView,
    CountStatistics,
    CreateCampaignView,
    HashtagsView,
    CreateBrandView,
)

urlpatterns = [
    path('brand/all/', BrandView.as_view()),
    path('campaigns/all/', AllCampaignsView.as_view()),
    path('campaigns/active/', ActiveCampaignsView.as_view()),
    path('utils/counts/', CountStatistics.as_view()),
    path('campaigns/create/', CreateCampaignView.as_view()),
    path('campaigns/hashtags/all/', HashtagsView.as_view()),
    path('brand/create/', CreateBrandView.as_view()),
]