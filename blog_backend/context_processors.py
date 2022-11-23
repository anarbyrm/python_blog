from blog.models import WebsiteSetting, Info, Tag, Post


def custom_context(request):
    context = dict()
    context['setting'] = WebsiteSetting.objects.last()
    context['info'] = Info.objects.last()
    context['tags'] = Tag.objects.all()
    context['all_posts_count'] = Post.objects.count()
    return context
