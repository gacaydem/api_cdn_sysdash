from . import views
from rest_framework import routers
from django.urls import path, include
router = routers.DefaultRouter()
router.register('Edge_Info', views.Edge_InfoView)
router.register('Miss', views.MissView)
router.register('Edge_History', views.Edge_HistoryView)
urlpatterns = [
    path('', include(router.urls)),
]
