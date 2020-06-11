from unittest import TestCase
from bay_area_relief.search import search_bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(search_bp)


class TestSearchApi(TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_search(self):
        response = self.app.post("/search", data={"hello": "world"})
        self.assertEqual(response.status_code, 200)

    def test_search_with_invalid_content_type(self):
        response = self.app.post("/search", data={"hello": "world"},
                                 headers={
                                     "Content-Type": "text/plain"
                                 })
        self.assertEqual(response.status_code, 400)

        response = self.app.post("/search", json={"hello": "world"},
                                 headers={
                                     "Content-Type": "application/json"
                                 })
        self.assertEqual(response.status_code, 200)

        response = self.app.post("/search", data={"hello": "world"},
                                 headers={
                                     "Content-Type": "application/x-www-form-urlencoded"
                                 })
        self.assertEqual(response.status_code, 200)

    def test_search_county(self):
        data = {"counties": ["Alameda", "Contra Costa", "Marin", "Napa",
                             "San Francisco", "San Mateo", "Santa Clara",
                             "Solano", "Sonoma"]
                }
        response = self.app.post("/search", data=data)
        self.assertEqual(response.json,
                         {'Alameda': 'yes', 'Contra Costa': 'yes', 'Marin': 'yes',
                          'Napa': 'yes', 'San Francisco': 'yes', 'San Mateo': 'yes',
                          'Santa Clara': 'yes', 'Solano': 'yes', 'Sonoma': 'yes'})
        self.assertEqual(response.status_code, 200)
