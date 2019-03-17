from .models import Visite_num


class Visite_num_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        stack_info = request.get_full_path()
        if stack_info == '/api/base_info/':
            visite_num_obj = Visite_num.objects.get(id=1)
            visite_num_obj.visite_num = visite_num_obj.visite_num + 1
            visite_num_obj.save()
        return response
