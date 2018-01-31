from django import test


class GetPublicViewTest(test.SimpleTestCase):
    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
