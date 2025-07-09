import os
from django.http import FileResponse, Http404

class MediaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/media/'):
            file_path = os.path.join('media', request.path.replace('/media/', '', 1))
            if os.path.isfile(file_path):
                return FileResponse(open(file_path, 'rb'))
            raise Http404("Media file not found.")
        return self.get_response(request)
