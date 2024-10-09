import unittest
from unittest.mock import patch
from app.app import create_app


class MainRouteTestCase(unittest.TestCase):

    @patch('app.models.db.init_app')
    @patch('flask_migrate.Migrate')
    def setUp(self, mock_migrate, mock_init_app):
        self.mock_migrate = mock_migrate  # Store the mock_migrate instance
        self.mock_init_app = mock_init_app
        self.app = create_app(False)
        self.app.config["SECRET_KEY"] = "test_flask"
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test_user:test_password@localhost:5432/test_db"
        self.client = self.app.test_client()

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
