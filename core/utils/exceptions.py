from rest_framework.exceptions import APIException

class ValidationError(APIException):
    status_code = 400
    default_detail = "Parameters Invalid to request"
    default_code = "validation_error"
