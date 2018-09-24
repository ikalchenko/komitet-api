from rest_framework.exceptions import APIException


class AlreadyExist(APIException):
    status_code = 409
    default_detail = 'Instance already exist'
    default_code = 'already_exist'
