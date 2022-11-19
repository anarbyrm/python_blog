from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.base import View
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages

from . import models, forms


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


class ContactView(CreateView):
    model = models.Contact
    form_class = forms.ContactForm
    template_name = 'blog/contact.html'

    def form_valid(self, form):
        form = form.save()
        messages.success(self.request, f"{form.full_name}, mesajınız bizə göndərildi.")
        return redirect(reverse('home-page'))


class PostListView(ListView):
    model = models.Post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'

