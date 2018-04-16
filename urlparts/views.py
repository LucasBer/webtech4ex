from django.shortcuts import render

# Create your views here.

def index(request, page_alias):
    args = {}
    args['current_path'] = request.META['HTTP_REFERER']
    try:
        active = Page.objects.get(page_alias=page_alias)
        except Page.DoesNotExist:
            raise Http404("Page does not exist")
    return render(request, 'index.html', {'url_path': args['current_path']})
