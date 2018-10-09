from django.db import models

# Create your models here.

from gdstorage.storage import GoogleDriveStorage, GoogleDrivePermissionType, GoogleDrivePermissionRole, GoogleDriveFilePermission

permission = GoogleDriveFilePermission(
    GoogleDrivePermissionRole.READER,
    GoogleDrivePermissionType.USER,
    "jzhou@example.com"
)

gd_storage = GoogleDriveStorage(permissions=(permission, ))

class GDFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField(upload_to='Safe', storage=gd_storage)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class LocalFile(models.Model):
    id = models.AutoField(primary_key=True)
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

class GDFolder(models.Model):
    id = models.AutoField(primary_key=True)
    folder_id = models.CharField(max_length=200, unique=True)
    folder_name = models.CharField(max_length=200, default=None)
    folder_email = models.EmailField(default=None)
    updated_at = models.DateTimeField(auto_now_add=True)

class FRecord(models.Model):
    id = models.AutoField(primary_key=True)
    folder_id = models.CharField(max_length=200)
    folder_name = models.CharField(max_length=200, default=None)
    folder_email = models.EmailField(default=None)
    file_name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
