from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View

from . import models


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        context['tutorials'] = models.Tutorial.objects.all()[:3]
        context['posts'] = models.Post.objects.all()[:6]

        return render(request, 'blog/index.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        context['about'] = models.About.objects.last()

        return render(request, 'blog/about.html', context)




