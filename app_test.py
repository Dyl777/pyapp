import unittest
from app import app

class APITestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a Flask test client
        cls.client = app.test_client()
        cls.client.testing = True

    def test_create_resource(self):
        """Test creating a resource, expecting a 201 status code."""
        response = self.client.post('/api/resource', json={"key": "value"})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())

    def test_get_resource(self):
        """Test fetching an existing resource, expecting a 200 status code."""
        # First, create a resource
        post_response = self.client.post('/api/resource', json={"key": "value"})
        resource_id = post_response.get_json()["id"]

        # Then, retrieve it
        get_response = self.client.get(f'/api/resource/{resource_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(get_response.get_json(), {"key": "value"})

    def test_get_nonexistent_resource(self):
        """Test fetching a non-existent resource, expecting a 404 status code."""
        response = self.client.get('/api/resource/99999')  # Non-existent ID
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
