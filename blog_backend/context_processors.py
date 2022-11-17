from blog.models import WebsiteSetting, Info


def custom_context(request):
    context = dict()
    context['setting'] = WebsiteSetting.objects.last()
    context['info'] = Info.objects.last()

    return context
