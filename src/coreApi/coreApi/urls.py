
from django.contrib import admin
from django.urls import path

from updates.views import update_model_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
     path('update/', update_model_detail_view, name='update'),
]
