import unittest
from unittest.mock import patch, MagicMock
from app.app import create_app


class MainRouteTestCase(unittest.TestCase):

    @patch('app.models.db.init_app')
    @patch('flask_migrate.Migrate')
    @patch('app.models.Acronym.query')
    def setUp(self, mock_migrate, mock_init_app, mock_db_query):  # pylint: disable=arguments-differ
        self.mock_migrate = mock_migrate
        self.mock_init_app = mock_init_app
        self.mock_db_query = mock_db_query
        self.app = create_app(False)
        self.app.config["SECRET_KEY"] = "test_flask"
        self.app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://test_user:test_password@localhost:5432/test_db"
        self.client = self.app.test_client()

    def test_index(self):
        
        mock_acronyms = [
            MagicMock(id=1, abbreviation='MOJ', definition='Ministry of Justice'),
            MagicMock(id=2, abbreviation='CPS )', definition='Crown Prosecution Service')
        ]
        self.mock_db_query.all.return_value = mock_acronyms

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
