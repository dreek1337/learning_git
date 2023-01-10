from request_and_response import Response, Request


def create_response(url, method, params, status, status_text, content=''):
    """
    Создание Response
    """
    return Response(url=url, method=method, params=params,
                    status=status, status_text=status_text, content=content)


def controller(request: Request) -> Response:
    """
    Проверка данных для создания Response
    """
    response_dict = {'url': request.url,
                     'method': request.method,
                     'params': request.params,
                     'status': request.status
                     }
    status_num = {200: 'OK', 201: 'CREATED', 400: 'BAD_REQUEST',
                  401: 'NOT_AUTH', 404: 'NOT_FOUND'}
    try:
        request.timeout
        if request.method in ['GET', 'POST'] and 300 < request.status >= 200:
            response_dict['status_text'] = status_num[request.status]
            response_dict['content'] = status_num[request.status]
            return create_response(**response_dict)
        elif 500 < request.status >= 400:
            response_dict['status_text'] = status_num[request.status]
            return create_response(**response_dict)
        else:
            return 'Ошибка'
    except:
        response_dict['status_text'] = 'TIMEOUT_ERROR'
        response_dict['status'] = 408
        return create_response(**response_dict)
