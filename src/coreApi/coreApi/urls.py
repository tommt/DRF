
from django.contrib import admin
from django.urls import path

from updates.views import json_model_detail_view, JsonCBV, JsonCBV2, SerializedListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('update/', json_model_detail_view, name='update'),
    path('cbv/json', json_model_detail_view, name='cbv'),
    path('cbv2/json/', json_model_detail_view, name='cbv'),
    path('serialize/json/', SerializedListView.as_view(), name='list'),
]
