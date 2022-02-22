from asyncore import read
from urllib import response
from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse, HttpRequest

from django.contrib.gis.geoip2 import GeoIP2

# Create your views here.
# class location(viewsets.ModelViewSet):
#     pass
import time 

# import geoip2.database
import os

import time
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f">>> | {repr(func.__name__)} : {round(run_time, 3)} secs | <<<")
        return value
    return wrapper




@timer
def location(request)    :
    t1 = time.time()
    response_string = 'The IP address {} is located at the coordinates {}, which is in the city {}, country{}'.format(
        request.ipinfo.ip,
        request.ipinfo.loc,
        request.ipinfo.city,
        request.ipinfo.country,
    )
    print("Time Taken: " ,time.time()-1)
    return HttpResponse(response_string)
    
   
