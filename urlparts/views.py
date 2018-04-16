from django.shortcuts import render

# Create your views here.

def index(request):
    args = {}
    args['current_path'] = request.META['HTTP_REFERER']
    return render(request, 'index.html', {'url_path': args['current_path']})
    
