# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse

import requests
import json
# Create your views here.


def homepage(request):
    something = curiosityrover().content
    
    data = json.loads(something)
    image = data['photos'][0]
    image = image['img_src']
    print(image)
    context = {
        'image': image,
    }

    return render(request, "wallpaper/index.html", context)


def curiosityrover():
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=1"
    app_token = "ApEztOfnuLutAfibTJmSuorcTQMHxQkozbocepVm"
    payload = {'api_key': app_token}
    response = requests.get(url, payload)
    response = json.dumps(response.json())
    return HttpResponse(response)



# class HomeView(TemplateView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)


#         def curiosityrover():
#             url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=1"
#             app_token = "ApEztOfnuLutAfibTJmSuorcTQMHxQkozbocepVm"
#             payload = {'api_key': app_token}
#             print(payload)
#             return requests.get(url, payload,))

#         context['image_url'] = 