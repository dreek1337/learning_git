from pydantic import BaseModel
from enum import Enum


class BaseRequest(BaseModel):
    """
    Получение запроса от клиента
    """
    get_url: str
    get_method: str
    get_params: dict = None
    get_status: int = None

    valid_methods = [
        'GET',
        'POST',
    ]
    
    def __init__(self, **data) -> None:
        super().__init__(**data)


class Request(BaseRequest):
    """
    Проверка валидности, полученых данных
    """
    get_timeout: int

    class ValidMethods(Enum):
        GET = 'GET'
        POST = 'POST'
        PUT = 'PUT'
        PATCH = 'PATCH'

    def __init__(
            self,
            **data
    ) -> None:
        super().__init__(**data)

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
        valid_methods = [i.value for i in self.ValidMethods]
        if self.get_method in valid_methods:
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
