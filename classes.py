class Request:
    def __init__(self, http_method, path) -> None:
        self.http_method: str = http_method
        self.path: str = path
