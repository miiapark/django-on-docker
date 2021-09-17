import logging
from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

logger = logging.getLogger("django")


def _get_client_ip(request):
    x_forwared_for = request.META.get("HTTP_X_FORWARDED_FOR")

    if x_forwared_for is not None:
        if x_forwared_for.find("","") != -1:
            ips = x_forwared_for.split("","")
            return ips[0]

        return x_forwared_for

    x_client = request.META.get("HTTP_X_CLIENT")
    if x_client is not None:
        return x_client

    return request.META.get("REMOTE_ADDR")


class DefaultExceptionHandler(object):
    def __new__(cls, exc, context):
        response = exception_handler(exc, context)
        result = {}
        result["errors"] = {}

        if response is None:
            logger.error("There was some crazy error", exc_info=True, extra={
                "request": context["request"],
            })

            if settings.DEBUG is True:
                return response

            error = Error(status.HTTP_500_INTERNAL_SERVER_ERROR)
            result["errors"]["code"] = error.get_error_code()
            result["errors"]["message"] = _("A server error occurred.")
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            data=result)

        result["errors"]["code"] = Error(response.status_code).get_error_code()
        if response.status_code == status.HTTP_400_BAD_REQUEST:
            result["errors"]["detail"] = {}
            result["errors"]["message"] = _("Invalid request parameter.")

            if "detail" not in response.data:
                result["errors"]["detail"] = response.data
            else:
                if not isinstance(response.data["detail"], dict) and\
                   not isinstance(response.data["detail"], list):
                    result["errors"]["detail"] = response.data["detail"]
                else:
                    for key in response.data:
                        result["errors"]["detail"][key] = response.data[key]
        else:
            result["errors"]["message"] = response.data["detail"]

        response.data = result
        return response


class RequiredError(ValidationError):
    """
    RequiredError
    """
    def __init__(self, keys):
        message = [_("This field is required.")]
        details = {}
        for key in keys:
            details[key] = message

        super(RequiredError, self).__init__(details)


class ErrorCodes(object):
    status_400 = "E001"
    status_401 = "E002"
    status_403 = "E003"
    status_404 = "E004"
    status_405 = "E005"
    status_406 = "E006"
    status_409 = "E010"
    status_413 = "E011"
    status_415 = "E007"
    status_429 = "E008"
    status_500 = "E009"


class Error(object):
    def __init__(self, status_code):
        self.status_code = status_code

    def get_error_code(self):
        key = "status_"+str(self.status_code)
        if hasattr(ErrorCodes, key) is True:
            return getattr(ErrorCodes, key)

        return self.status_code


class CustomError(APIException):
    def __init__(self, status, detail):
        self.status_code = status
        self.detail = _(detail)

    def __str__(self):
        return self.detail


class AlreadyExists(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = _("Already exists.")
    default_code = "already_exists"


class RequestTooLarge(APIException):
    status_code = status.HTTP_413_REQUEST_ENTITY_TOO_LARGE
    default_detail = _("Request too large.")
    default_code = "request_too_large"
