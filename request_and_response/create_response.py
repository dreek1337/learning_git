from typing import Any
from pydantic import BaseModel
from enum import Enum


class Response(BaseModel):
    """
    Создание response для клиента
    """
    url: str
    method: str
    params: dict
    status: int
    content = 'random'

    class StatusNum(Enum):
        OK = 200
        CREATED = 201
        BAD_REQUEST = 400
        NOT_AUTH = 401
        NOT_FOUND = 404
        TIMEOUT_ERROR = 408

    def __init__(self, **data: Any):
        super().__init__(**data)

    @property
    def status_text(self):
        return [i.name for i in self.StatusNum if i.value == self.status][0]
