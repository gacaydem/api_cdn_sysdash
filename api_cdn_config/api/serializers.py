from rest_framework import serializers

from .models import Edge_Info, Miss, Edge_History


class Edge_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge_Info
        fields = '__all__'


class MissSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miss
        fields = '__all__'


class Edge_HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Edge_History
        fields = '__all__'
