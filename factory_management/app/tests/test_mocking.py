from unittest.mock import patch, MagicMock

def test_factory_creation_mock():
    """Example of mocking database interaction"""
    with patch('app.routes.factory_routes.Factory') as MockFactory:
        # Create a mock factory
        mock_factory = MagicMock()
        mock_factory.id = 1
        mock_factory.name = "Mocked Factory"
        mock_factory.location = "Mocked Location"
        
        # Configure the mock to return our mocked factory
        MockFactory.query.get.return_value = mock_factory
        
        # Perform test
        factory = MockFactory.query.get(1)
        
        assert factory.name == "Mocked Factory"
        assert factory.location == "Mocked Location"