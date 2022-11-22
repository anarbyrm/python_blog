from blog.models import WebsiteSetting, Info, Tag


def custom_context(request):
    context = dict()
    context['setting'] = WebsiteSetting.objects.last()
    context['info'] = Info.objects.last()
    context['tags'] = Tag.objects.all()
    return context
