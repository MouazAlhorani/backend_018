from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render


class RedirectIfNotRegisteredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        device_ip = request.META.get('REMOTE_ADDR')
        print(device_ip)
        if device_ip=='192.168.50.7':
            return render(request,"web_app_018/index.html") 
        else:
            return render(request,"welcome.html") 