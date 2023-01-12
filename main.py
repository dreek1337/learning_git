from random import choice, randint
from request_and_response import Response, Request


def retry(n: int):
    """
    Созданеи декоратора, который отправляет повторные запросы
    """
    def take_func_retry(func):
        def start(*args, **kwargs):
            counter = n
            r = func(*args, **kwargs)
            if r.status < 300:
                return r
            else:
                while counter:
                    print(f'Осталось попыток: {counter}')
                    r = func(*args, **kwargs)
                    print(r.status)
                    if r.status < 300:
                        return r
                    counter -= 1
                raise 'Ошибся чел'

        return start

    return take_func_retry


@retry(n=10)
def controller(
        url: str,
        params: dict,
        status: int,
        method: str,
        timeout: int,
) -> Response:
    """
    Проверка данных для создания Response
    """
    print(f'1. {timeout}')
    print(f'1. {status}')
    if any((timeout > 5, status > 300)):
        timeout = randint(1, 7)
        status = choice([200, 201, 400, 401, 404])
    print(f'2. {timeout}')
    print(f'2. {status}')

    request = Request(
        url=url,
        timeout=timeout,
        status=status,
        method=method,
        params=params
    )

    response_dict = {
        'url': request.url,
        'method': request.method,
        'status': request.status,
        'params': request.params
    }

    return Response(**response_dict)


for i in range(10):
    timeout = randint(1, 10)
    status = choice([200, 201, 400, 401, 404])
    method = choice(["GET", "POST"])

    try:
        print(controller(url='http:/url', params=dict(d=1, b=2), status=status, method=method, timeout=timeout).__dict__)
    except Exception as err:
        print(f'*Данные не прошли валидацию* {err}')
