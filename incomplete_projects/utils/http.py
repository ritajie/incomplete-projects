import json
from datetime import datetime

from django.http import HttpResponse


def http_response(message="", data=None, status_code=200):
    def datetime_to_timestamp(obj: datetime):
        if isinstance(obj, datetime):
            return int(datetime.timestamp(obj))
        return obj

    response = HttpResponse(
        json.dumps(
            {"code": status_code, "message": message, "data": data or {}},
            default=datetime_to_timestamp,
        ),
        "application/json",
    )
    return response
