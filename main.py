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
    response_dict = {'url': request.url,
                     'method': request.method,
                     'status': request.status
                     }
    try:
        request.timeout
        response_dict['params'] = request.params
        return create_response(**response_dict)
    except Exception as err:
        raise f'Ошибочкаааа: {err} | status: 408, status_text: TIMEOUT_ERROR'


create_request = [Request(url='https;//url.com', method=choice(('GET', 'POST')),
                          params={str(i): i for i in range(choice(range(7)))},
                          status=choice(range(150, 350, 10)), timeout=choice(range(11)))
                  for i in range(10)]

correct_response = None

for i in create_request:
    c = controller(i)
    if c:
        correct_response = c
    else:
        continue
print(create_request[0].timeout, create_request[1].timeout, create_request[2].timeout)
print(correct_response.status)
print(correct_response.method)
print(correct_response.url)
