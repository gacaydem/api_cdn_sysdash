from django.contrib import admin
from .models import Edge_Info, Miss, Edge_History

# Register your models here.
@admin.register(Edge_Info)
class Edge_InfoAdmin(admin.ModelAdmin):
    list_display = ('name','build_status','resource_type','status','created_time','updated_time',)
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Miss)
class MissAdmin(admin.ModelAdmin):
    list_display = ('node_cdn','miss_file', 'time_updated','url_file',)
    ordering = ('node_cdn',)
    search_fields = ('node_cdn',)


@admin.register(Edge_History)
class Edge_HistoryAdmin(admin.ModelAdmin):
    list_display = ('edge_id','message', 'updated_time','uuid',)
    ordering = ('edge_id',)
    search_fields = ('edge_id',)