# Django
from django.conf.urls import url
from django.urls import path, include

# Local
#from . import views

urlpatterns=[
    url(r'^api-auth/', include('rest_framework.urls'))
]