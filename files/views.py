import os

from django.db import transaction
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .forms import GDUploadFileForm, UploadFileForm
from .models import FRecord, GDFile, GDFolder

# Create your views here.

class FilesUploadView(View):

    def get(self, request, folder_id):
        folder = GDFolder.objects.get(folder_id=folder_id)
        if folder != None:
            return render(self.request, 'files/basic-plus.html')

    def post(self, request, folder_id):
        max_file_size = 100 * 1024 * 1024 # 100 MiB
        accepted_file_types = [
            "image/jpeg", "image/png", "application/pdf", "application/msword", "text/plain"
        ]
        folder = GDFolder.objects.get(folder_id=folder_id)
        if folder != None:
            form = GDUploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                file = request.FILES['file']
                if file.content_type not in accepted_file_types:
                    error = "File type is not accepted!"
                    data = {'files': [{'error': error}]}
                    return JsonResponse(data)
                elif file.size > max_file_size:
                    error = "File is too big!"
                    data = {'files': [{'error': error}]}
                    return JsonResponse(data)
                else:
                    with transaction.atomic():
                        model_instance = form.save(commit=False)
                        model_instance.file.field.upload_to = folder.folder_name
                        file = form.save()
                        data = {'files': [{'name': file.file.name}]} 
        else:
            data = {'files': [{'error': "Wrong request"}]}
        return JsonResponse(data)