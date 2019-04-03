from django.urls import path
from .views import TimelineList, TimelineDetail

urlpatterns = [
    path("timeline/", TimelineList.as_view(), name=TimelineList.name),
    path("timeline/<int:pk>/", TimelineDetail.as_view(), name=TimelineDetail.name),
]