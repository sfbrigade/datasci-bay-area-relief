from unittest import TestCase
from bayarea_relief.search import search_bp
from flask import Flask

app = Flask(__name__)
app.register_blueprint(search_bp)


class TestSearchApi(TestCase):

    def setUp(self):
        self.data = {
            "name": "Public sector help",
            "category": "Multiple",
            "counties": {
                "sf_county": "Yes",
                "alameda_county": "Yes",
                "san_mateo_county": "Yes",
                "contra_costa_county": "Yes",
                "santa_clara_county": "Yes",
            }
        }
        self.headers = {
            "Content-type": "application/json"
        }
        self.app = app.test_client()

    def test_search(self):
        response = self.app.post("/search", json=self.data, headers=self.headers)
        self.assertEqual(200, response.status_code)

    def test_search_with_invalid_content_type(self):
        response = self.app.post("/search", json=self.data,
                                 headers={
                                     "Content-Type": "text/plain"
                                 })
        self.assertEqual(400, response.status_code)

        response = self.app.post("/search", json=self.data,
                                 headers=self.headers)
        self.assertEqual(200, response.status_code)

        response = self.app.post("/search", json=self.data,
                                 headers={
                                     "Content-Type": "application/x-www-form-urlencoded"
                                 })
        self.assertEqual(400, response.status_code)

        response = self.app.post("/search", json=self.data,
                                 headers={
                                     "Content-Type": "multipart/form-data"
                                 })
        self.assertEqual(400, response.status_code)

    def test_search_county(self):
        response = self.app.post("/search", json=self.data, headers=self.headers)
        expected = {'alameda_county': 'Yes', 'category': 'Multiple',
                    'contra_costa_county': 'Yes', 'county': 'Unknown',
                    'name': 'Public sector help', 'san_mateo_county': 'Yes',
                    'santa_clara_county': 'Yes', 'sf_county': 'Yes'}
        self.assertEqual(expected, response.json)
        self.assertEqual(200, response.status_code)
