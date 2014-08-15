import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def snippet(request):
    if request.method == 'GET':
        response_data = {}
        response_data['result'] = 'GET'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    elif request.method == 'POST':
        response_data = {}
        response_data['result'] = 'POST'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

        
        

@api_view(['PUT', 'DELETE'])
def snippet_detail(request, pk):
    if request.method == 'PUT':
        response_data = {}
        response_data['result'] = 'PUT'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    elif request.method == 'DELETE':
        response_data = {}
        response_data['result'] = 'DELETE'
        return HttpResponse(json.dumps(response_data), content_type="application/json")