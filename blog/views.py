from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic.base import View
from django.views.generic import CreateView, ListView, DetailView
from django.contrib import messages
from django.db.models import Q

from . import models, forms


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]

    return request.META.get('REMOTE_ADDR') 


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        context['tutorials'] = models.Tutorial.objects.all()[:3]
        posts = models.Post.objects.all()[:6]

        context['posts'] = posts
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

    def get_queryset(self):
        posts = models.Post.objects.all()

        q = self.request.GET.get('q')
        tag = self.request.GET.get('tag')

        if q is not None:
            posts = models.Post.objects.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q) |
                Q(tags__name__icontains=q)
            )

        if tag is not None:
            posts = models.Post.objects.filter(tags__name__iexact=tag)

        return posts


class PostDetailView(DetailView):
    model = models.Post

    def get_object(self):
        return get_object_or_404(models.Post, slug=self.kwargs.get('slug'))

    def get(self, *args, **kwargs):
        context = dict()
        user_ip = get_client_ip(self.request)

        if not models.IPModel.objects.filter(address=user_ip).exists():
            ip = models.IPModel.objects.create(address=user_ip)
            ip.save()
        else:
            ip = models.IPModel.objects.filter(address=user_ip).first()
        
        obj = self.get_object()

        if not ip in obj.views.all():
            obj.views.add(ip)

        context['post'] = obj
        context['view_count'] = obj.views.count()

        return render(self.request, 'blog/post-detail.html', context)


class TutorialListView(ListView):
    model = models.Tutorial
    template_name = 'blog/tutorials-list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TutorialListView, self).get_context_data(**kwargs)
        context['tutorials'] = models.Tutorial.objects.filter(is_active=True)
        return context


class TutorialDetailView(DetailView):
    model = models.Tutorial
    template_name = 'blog/tutorial-detail.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(models.Tutorial, slug=slug)
        return obj

    def get_context_data(self, **kwargs):
        context = super(TutorialDetailView, self).get_context_data(**kwargs)
        context['tutorial'] = self.get_object()

        user_ip = get_client_ip(self.request)
        context['user_ip'] = str(user_ip)

        return context


class LessonDetailView(DetailView):
    model = models.Lesson

    def get(self, *args, **kwargs):
        context = dict()
        user_ip = get_client_ip(self.request)

        if not models.IPModel.objects.filter(address=user_ip).exists():
            ip = models.IPModel.objects.create(address=user_ip)
            ip.save()
        else:
            ip = models.IPModel.objects.filter(address=user_ip).first()

        obj = self.get_object()

        if not ip in obj.views.all():
            obj.views.add(ip)

        context['lesson'] = obj

        return render(self.request, 'blog/lesson-detail.html', context)

    def get_object(self):
        slug = self.kwargs.get('slug')
        obj = get_object_or_404(models.Lesson, slug=slug)
        return obj


