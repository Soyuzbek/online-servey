from rest_framework.exceptions import APIException


class ObjectNotFoundException(APIException):
    status_code = 404


class IncorrectPasswordException(APIException):
    status_code = 400


class ObjectAlreadyExistException(APIException):
    status_code = 400


class RequiredObjectException(APIException):
    status_code = 400
