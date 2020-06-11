from flask import jsonify, make_response, Response, Blueprint

search_bp = Blueprint('search', __name__, url_prefix='/search')


@search_bp.route('', methods=["POST"])
def search() -> Response:
    data = {"hello": "world"}
    return make_response(jsonify(data), 200)
