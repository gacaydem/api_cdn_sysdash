from django.db import models
from datetime import datetime


class Edge_Info(models.Model):
    name = models.TextField(max_length=50)
    build_status = models.IntegerField(default=2) #(1: Building, 2: Done, 3: OK, -1: Error)
    resource_type = models.CharField(max_length=50, default='vod')
    status = models.IntegerField(default=1)
    created_time = models.DateTimeField(default=datetime.now, blank=True)
    updated_time = models.DateTimeField(default=datetime.now, blank=True)


    # @property
    def __str__(self):
        return self.name


class Miss(models.Model):
    node_cdn = models.TextField(max_length=50)
    miss_file = models.TextField(max_length=50)
    time_updated = models.DateTimeField(default=datetime.now, blank=True)
    url_file = models.TextField(max_length=50,default='/usr/local/nginx-1.10.1/conf/sites-enabled/')

    
    # @property
    def __str__(self):
        return self.miss_file


class Edge_History(models.Model):
    edge_id = models.ForeignKey(Edge_Info, related_name='Edge_Histories', on_delete=models.CASCADE)
    message = models.TextField(max_length=50)
    updated_time = models.DateTimeField(default=datetime.now, blank=True)
    uuid = models.TextField(max_length=50)
    
    # @property
    def __str__(self):
        return self.edge_id