import json
from django.views.generic import View
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from coreApi.mixins import JsonResponseMixin

from .models import Update

def detail_view(request):
    return render() #return JSON data or XML 


# Get Request(Retrieve)
def json_model_detail_view(request):
    data = {
        "count": 1000,
        "content": "some new content"
    }
    # return JsonResponse(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')



class JsonCBV(View):
    def get(self, request, *args, **kwargs):

        data = {
            "count": 1000,
            "content": "some new content"
    } 
        return JsonResponse(data)





class JsonCBV2(JsonResponseMixin, View):
     def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "some new content"
    } 
        return self.render_to_json_response(data)