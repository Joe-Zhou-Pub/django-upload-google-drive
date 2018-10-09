# django-upload-google-drive

Google Drive requires login to upload file ( download does not require ). For company to utilize Google Suite for workflow to collect external customer/user files who do not have google account, it will be hard. This program is trying to address the problem, also have Google app script part working along with Google form to collect the other data, at the end of submit the google form, automatically generate a link for the external customer/user to upload file without login. This program is just upload part of whole project.

The service is running on Google Kubernetes Engine. Tried on Google App Engine but it limits the file size to 32MB. Kubernetes Engine with containerized application is the way for application agile develop/integration/deployment.

This is example setup, tested and verified on GKE, you need setup your own GCP project, cloudsql, service account etc.
