from random import choice
from request_and_response import Response, Request


def retry(n):
    """
    Созданеи декоратора, который отправляет повторные запросы
    """
    def take_func_retry(func):
        def start(*args, **kwargs):
            counter = n
            while counter:
                counter -= 1
                try:
                    r = func(*args, **kwargs)
                    if 200 <= r.status < 300:
                        return r
                    else:
                        continue
                except Exception as error:
                    print(f'Не удалось получить валидные данные: {error} | Попыток осталось: {counter}')

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
    r = request(url='https;//url.com', method='GET', params={str(i): i for i in range(choice(range(7)))},
                status=choice(range(150, 350, 10)), timeout=choice(range(11)))
    response_dict = {'url': r.url,
                     'method': r.method,
                     'params': r.params,
                     'status': r.status
                     }
    try:
        r.timeout
        return create_response(**response_dict)
    except Exception as err:
        raise f'Ошибочкаааа: {err} | status: 408, status_text: TIMEOUT_ERROR'
