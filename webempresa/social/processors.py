from .models import Link

def contexto_dict(request):
    contexto = {}
    links = Link.objects.all()
    for link in links:
        contexto[link.key] = link.url
    return contexto