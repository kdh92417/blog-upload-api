from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posting import views

router_v1 = DefaultRouter()
router_v1.register("v1", views.PostingViewSet)

urlpatterns = [
    path("", include(router_v1.urls))
]
