from rest_framework import generics

from .models import Timeline
from .serializers import TimelineSerializer


class TimelineList(generics.ListCreateAPIView):

    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    name = 'timeline-list'

class TimelineDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer
    name = 'timeline-detail'