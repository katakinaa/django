from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class SalaryMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            developer_level = request.POST.get('developer_level')

            if developer_level == 'Junior':
                request.salary = 500
            elif developer_level == 'Middle':
                request.salary = 1000
            elif developer_level == 'Senior':
                request.salary = 3000
            else:
                return HttpResponseBadRequest('Неверный уровень разработчика')

        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'level-salary', 'Неверный уровень разработчика')
