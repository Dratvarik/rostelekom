from django.urls import path
from .views import *

urlpatterns=[
    path('', index, name='index'),
    path('api', api, name='api'),
    # path("analysis", analysis, name='analysis'),
]