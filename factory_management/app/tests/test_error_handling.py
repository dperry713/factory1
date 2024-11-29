def test_create_factory_missing_data(client):
    """Test creating a factory with missing data"""
    invalid_data = {
        "name": "Incomplete Factory"
    }
    
    response = client.post('/factories/', 
        data=json.dumps(invalid_data),
        content_type='application/json'
    )
    
    assert response.status_code == 400

def test_get_nonexistent_factory(client):
    """Test retrieving a nonexistent factory"""
    response = client.get('/factories/9999')
    
    assert response.status_code == 404
