# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.views.generic.detail import DetailView
from django.http import HttpResponse, JsonResponse
from .models import Image
import requests
import json
from django.utils import timezone
import datetime
from django.views.generic import TemplateView, View
# Create your views here.


# def homepage(request):
#     data = curiosityrover()
#     #data = json.loads(something)
#     image = data['photos'][0]
#     image = image['img_src']
#     context = {
#         'image': image,
#     }

#     return render(request, "wallpaper/index.html", context)


# def curiosityrover():
#     url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=1"
#     app_token = "ApEztOfnuLutAfibTJmSuorcTQMHxQkozbocepVm"
#     payload = {'api_key': app_token}
#     response = requests.get(url, payload)
#     #response = json.dumps(response.json())
#     return response.json()


class HomeView(TemplateView):
    template_name = "wallpaper/index.html"


class Something(View):
    def get(self, request, **kwargs):
        # now = timezone.now()
        # datestart = now - datetime.timedelta(0, 43200, 0)
        # param = Image.objects.filter(date_saved__range=(datestart, now))

        def curiosityrover():
            url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=1"
            app_token = "ApEztOfnuLutAfibTJmSuorcTQMHxQkozbocepVm"
            payload = {'api_key': app_token}
            response = requests.get(url, payload)
            data = response.json()
            image = data['photos'][0]
            return image

        image = curiosityrover()
        mod = Image(sol=image['sol'],
                    earth_date=image['earth_date'],
                    img_src=image['img_src'],
                    date_saved=timezone.now(),
                    )
        mod.save()
        context = {
            'sol': image['sol'],
            'earth_date': image['earth_date'],
            'img_src': image['img_src'],
            'date_saved': timezone.now().isoformat(),
        }
        return HttpResponse(json.dumps(context), content_type="text/json")
        # return JsonResponse(context)
