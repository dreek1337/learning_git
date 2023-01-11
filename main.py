from random import choice
from request_and_response import Response, Request


def retry(n):
    """
    Созданеи декоратора, который отправляет повторные запросы
    """
    def take_func_retry(func):
        def start(*args, **kwargs):
            for i in range(n):
                r = func(*args, **kwargs)
                print(r.status)
                if 200 <= r.status < 300:
                    return func(*args, **kwargs)
                else:
                    continue
            raise 'Oшибка'

        return start

    return take_func_retry


def create_response(url, method, params, status):
    """
    Создание Response
    """
    return Response(url=url, method=method, params=params, status=status)


@retry(n=10)
def controller(request: Request) -> Response:
    """
    Проверка данных для создания Response
    """
    response_dict = {'url': request.url,
                     'method': request.method,
                     'params': request.params,
                     'status': request.status
                     }
    try:
        request.timeout
        return create_response(**response_dict)
    except:
        response_dict['status'] = 408
        return create_response(**response_dict)
