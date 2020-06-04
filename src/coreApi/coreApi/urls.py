
from django.contrib import admin
from django.urls import path

from updates.views import json_model_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
     path('update/', json_model_detail_view, name='update'),
]
