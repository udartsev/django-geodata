class BaseServerException(Exception):
    def __init__(self, detail, status_code, message):
        super().__init__(message)
        self.detail = detail
        self.status_code = status_code


class SearchFieldRequiered(BaseServerException):
    def __init__(self):
        super().__init__(detail='entity', status_code=404, message='Search field required')
