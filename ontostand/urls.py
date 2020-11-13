from django.conf.urls import url
from . import views
from django.urls import path


app_name = 'ontostand'
urlpatterns = [
    # ex: /mysample/
    url(r'^$', views.index),
    url(r'^extractors', views.extractors, name='extractors'),
    url(r'^getFileList', views.getFileList, name='getFileList'),
    url(r'^verbalize', views.verbalize, name='verbalize'),
    url(r'^upload', views.upload, name='upload'),
    url(r'^clean_temp_files', views.clean_temp_files, name='clean_temp_files'),
]
