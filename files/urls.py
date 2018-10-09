from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    #url(r'^upload/(?P<folder_id>.*)', views.FilesUploadView.as_view(), name='files_upload_url_name'),
    path('upload/<str:folder_id>', views.FilesUploadView.as_view(), name='files_upload_url_name'),
]
