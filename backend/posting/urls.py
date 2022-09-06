from django.urls import path

from posting import views

urlpatterns = [
    path("", views.PostingListCreateAPIView.as_view()),
    path("<int:id>", views.PostingDeleteUpdateAPIView.as_view()),
]
