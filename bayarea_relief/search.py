from enum import Enum

from flask import jsonify, make_response
from flask import Response, Blueprint, request

search_bp = Blueprint('search', __name__, url_prefix='/search')


class MimeTypes(Enum):
    JSON = "application/json"

    @classmethod
    def is_supported(cls, content_type):
        return cls.JSON.value == content_type.lower()


@search_bp.route('', methods=["POST"])
def search() -> Response:
    if not MimeTypes.is_supported(request.content_type):
        return make_response(jsonify({}), 400)
    data = request.json
    counties_supported = [c.lower() == "yes" for c in data["counties"]]
    count_coverage = get_county_coverage(counties_supported)
    relief = {
        "name": data["name"],
        "category": data["category"],
        "county": count_coverage,
        **data["counties"]
    }
    return make_response(jsonify(relief), 200)


def get_county_coverage(counties_supported):
    number_counties_supported = sum(counties_supported)
    if number_counties_supported == 0:
        return "Unknown"

    if number_counties_supported == counties_supported:
        county_effectiveness = "All"
    else:
        county_effectiveness = "Some"

    return county_effectiveness
