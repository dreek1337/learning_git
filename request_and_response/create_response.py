class Response:
    """
    Создание response для клиента
    """
    def __init__(self, url: str, method: str, params: dict, status: int, status_text: str, content: str):
        self.url = url
        self.method = method
        self.params = params
        self.status = status
        self.status_text = status_text
        self.content = content