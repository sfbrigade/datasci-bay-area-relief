from unittest import TestCase
from bay_area_relief.search import search_bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(search_bp)


class TestSearchApi(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_search(self):
        response = self.app.post("/search")
        self.assertEqual(response.json["hello"], "world")
        self.assertEqual(response.status_code, 200)
