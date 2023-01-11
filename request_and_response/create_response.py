from enum import Enum


class Response:
    """
    Создание response для клиента
    """
    status_num = {200: 'OK', 201: 'CREATED', 400: 'BAD_REQUEST',
                  401: 'NOT_AUTH', 404: 'NOT_FOUND'}

    def __init__(self, url: str, method: str, params: dict, status: int, content='random'):
        self.url = url
        self.method = method
        self.params = params
        self.status = status
        self.content = content

    @property
    def status_text(self):
        return self.status_num.get(self.status)