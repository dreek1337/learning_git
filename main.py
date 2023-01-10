from random import random
from request_and_response import Response, Request


def func(url, method, params, status, status_text, content=''):
    return Response(url=url, method=method, params=params,
                    status=status, status_text=status_text, content=content)


def controller(request: Request, timeout=int(random() * 11)) -> Response:
    response_dict = {'url': request.url,
                     'method': request.method,
                     'params': request.params,
                     'status': request.status
                     }
    if request.method == 'GET' and request.status == 200:
        response_dict['status_text'] = 'OK'
        response_dict['content'] = 'OK'
        return func(**response_dict)
    elif request.method == 'POST' and request.status == 201:
        response_dict['status_text'] = 'CREATED'
        response_dict['content'] = 'CREATED'
        return func(**response_dict)
    elif request.status == 400:
        response_dict['status_text'] = 'BAD_REQUEST'
        return func(**response_dict)
    elif request.status == 401:
        response_dict['status_text'] = 'NOT_AUTH'
        return func(**response_dict)
    elif request.status == 404:
        response_dict['status_text'] = 'NOT_FOUND'
        return func(**response_dict)
    else:
        return 'Неизветсная ошибка'
    