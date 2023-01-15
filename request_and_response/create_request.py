from typing import Final
from random import choice


class BaseRequest:
    """
    Получение запроса от клиента
    """
    valid_methods = [
        'GET',
        'POST',
    ]

    def __init__(
            self,
            url: str,
            method: str,
            params: dict = None,
            status: int = None,
    ) -> None:
        self.get_url = url
        self.get_method = method
        self.get_params = params
        self.get_status = status


class Request(BaseRequest):
    """
    Проверка валидности, полученых данных
    """
    valid_methods: Final = [
        'GET',
        'POST',
        'PUT',
        'PATCH',
    ]

    def __init__(
            self,
            timeout: int,
            *args,
            **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.get_timeout = timeout

    @property
    def url(self):
        """
        Проверка валидности url
        """
        if self.get_params and self.get_method == 'GET':
            end_of_url = '&'.join(f'{i}={j}' for i, j in self.get_params.items())
            complete_url = f'{self.get_url}?{end_of_url}/'
            return complete_url
        else:
            return self.get_url

    @property
    def method(self):
        """
        Проверка валидности method
        """
        if self.get_method in self.valid_methods:
            return self.get_method
        else:
            raise 'Неподходящий метод request_and_response'

    @property
    def params(self):
        """
        Проверка валидности params
        """
        if not self.get_params or 5 < len(self.get_params):
            raise 'Количество параметров, больше 5 или меньще 1'
        else:
            return self.get_params

    @property
    def timeout(self):
        """
        Проверка валидности timeout
        """
        if self.get_timeout <= 5:
            return self.get_timeout
        else:
            raise 'Параметр больше значения 5'

    @property
    def status(self):
        """
        Проверка валидности timeout
        """
        if self.get_timeout <= 5:
            return self.get_status
        else:
            return 408
