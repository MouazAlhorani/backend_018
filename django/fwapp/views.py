from datetime import datetime, timezone
from scapy.all import *
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes,action
from django.views.decorators.csrf import csrf_protect
from rest_framework.permissions import AllowAny
from rest_framework.response import Response as rfresponse
from rest_framework import status
from rest_framework import serializers,renderers
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
import requests
import asyncio
from django.shortcuts import redirect
from app_018.models import *



class LoginViewSet(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'web_app_fw/index.html'
    @action(methods=['get'], detail=False)
    @permission_classes([AllowAny])
    def fwlogin(self, request):
        return rfresponse(template_name=self.template_name)
    


