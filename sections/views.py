from django.shortcuts import render
from rest_framework import generics
from .serializers import SectionSerializer,WorkerSerializer,WorksSerializer
from .models import Section,Worker, Works
# Create your views here.
class SectionViews(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
class WorkerViews(generics.ListCreateAPIView):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
class SectionDetail(generics.RetrieveUpdateAPIView):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
class WorkerDetail(generics.RetrieveUpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
class WorksDetail(generics.RetrieveUpdateAPIView):
    queryset = Works.objects.all()
    serializer_class = WorksSerializer