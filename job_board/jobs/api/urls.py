from django.urls import path
from jobs.api.views import (JobOfferListCreateAPIView, JobOfferDetailAPIView)
# from news.api.views import (article_detail_api_view,
#                             article_list_create_api_view)

urlpatterns = [
    path("jobs/",
         JobOfferListCreateAPIView.as_view(),
         name="jobs-list"),

    path("jobs/<int:pk>/",
         JobOfferDetailAPIView.as_view(),
         name="job-detail"),
    ]
