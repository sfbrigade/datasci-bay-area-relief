from unittest import TestCase
import search
import json


class TestPortalSearch(TestCase):

    def test_search(self):
        response = search.app.test_client().post("/search")
        data = json.loads(response.get_data(as_text=True))
        self.assertEquals(data["hello"], "world")



