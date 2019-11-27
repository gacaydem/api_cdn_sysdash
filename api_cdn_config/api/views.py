from rest_framework import viewsets
from .models import Edge_Info, Miss, Edge_History
from .serializers import Edge_HistorySerializer, MissSerializer, Edge_InfoSerializer


class Edge_InfoView(viewsets.ModelViewSet):
    queryset = Edge_Info.objects.all()
    serializer_class = Edge_InfoSerializer


class MissView(viewsets.ModelViewSet):
    queryset = Miss.objects.all()
    serializer_class = MissSerializer


class Edge_HistoryView(viewsets.ModelViewSet):
    queryset = Edge_History.objects.all()
    serializer_class = Edge_HistorySerializer

