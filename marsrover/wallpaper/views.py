# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import wallpaper
# Create your views here.


def homepage(request):
    data = wallpaper.curiosityrover()['photos'][0]
    image = data['img_src']

    context = {
        'image': image,
    }

    return render(request, "wallpaper/index.html", context)
