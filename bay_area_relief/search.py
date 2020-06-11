from enum import Enum

from flask import jsonify, make_response
from flask import Response, Blueprint, request

search_bp = Blueprint('search', __name__, url_prefix='/search')


class MimeTypes(Enum):
    FORM_ENCODED = "application/x-www-form-urlencoded"
    JSON = "application/json"

    @classmethod
    def is_supported(cls, content_type):
        is_form = cls.FORM_ENCODED.value == content_type.lower()
        is_json = cls.JSON.value == content_type.lower()
        return is_form or is_json


class CountyResponse(str, Enum):
    YES = "yes"
    NO = "no"
    UNKNOWN = "unknown"


@search_bp.route('', methods=["POST"])
def search() -> Response:
    if not MimeTypes.is_supported(request.content_type):
        return make_response(jsonify({}), 400)

    response = {}

    data = request.form.to_dict(flat=False) or request.json

    counties = data.get("counties") or []
    for county in counties:
        response[county] = CountyResponse.YES.value

    return make_response(jsonify(response), 200)
