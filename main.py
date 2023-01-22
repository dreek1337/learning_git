from random import choice, randint
from request_and_response import Response, Request


def retry(n: int):
    """
    Созданеи декоратора, который отправляет повторные запросы
    """
    def take_func_retry(func):
        def start(*args, **kwargs):

            for _ in range(n):
                r = func(*args, **kwargs)
                if r.status < 300:
                    return r

        return start
    return take_func_retry


@retry(n=10)
def controller(
        url: str,
        method: str,
        params: dict,
        status: int,
        timeout: int,
) -> Response:
    """
    Проверка данных для создания Response
    """
    if any((timeout > 5, status > 300)):
        timeout = randint(1, 10)
        status = choice([200, 201, 400, 401, 404])

    request = Request(
        get_url=url,
        get_timeout=timeout,
        get_status=status,
        get_method=method,
        get_params=params
    )

    response_dict = {
        'url': request.url,
        'method': request.method,
        'status': request.status,
        'params': request.params
    }

    return Response(**response_dict)


for i in range(20):
    timeout = randint(1, 10)
    status = choice([200, 201, 400, 401, 404])
    method = choice(["GET", "POST"])

    try:
        resp = controller(url='http://url', params=dict(d=1, b=2), status=status,
                          method=method, timeout=timeout)
        print(resp.__dict__)
        print(resp.status_text)
    except Exception as err:
        print(f'*Данные не прошли валидацию* {err}')
