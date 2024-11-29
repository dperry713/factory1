import pytest
import json
from app.models.models import Factory

def test_create_factory(client, session):
    """Test creating a new factory"""
    factory_data = {
        "name": "New Factory",
        "location": "New Location"
    }
    
    response = client.post('/factories/', 
        data=json.dumps(factory_data),
        content_type='application/json'
    )
    
    assert response.status_code == 201
    
    # Verify factory was created in database
    created_factory = Factory.query.filter_by(name="New Factory").first()
    assert created_factory is not None
    assert created_factory.location == "New Location"

def test_get_factories(client, sample_factory):
    """Test retrieving list of factories"""
    response = client.get('/factories/')
    
    assert response.status_code == 200
    
    factories = json.loads(response.data)
    assert len(factories) > 0
    assert factories[0]['name'] == sample_factory.name

def test_get_single_factory(client, sample_factory):
    """Test retrieving a single factory by ID"""
    response = client.get(f'/factories/{sample_factory.id}')
    
    assert response.status_code == 200
    
    factory_data = json.loads(response.data)
    assert factory_data['name'] == sample_factory.name
    assert factory_data['location'] == sample_factory.location

def test_update_factory(client, sample_factory):
    """Test updating an existing factory"""
    update_data = {
        "name": "Updated Factory Name",
        "location": "Updated Location"
    }
    
    response = client.put(
        f'/factories/{sample_factory.id}', 
        data=json.dumps(update_data),
        content_type='application/json'
    )
    
    assert response.status_code == 200
    
    # Verify database was updated
    updated_factory = Factory.query.get(sample_factory.id)
    assert updated_factory.name == "Updated Factory Name"
    assert updated_factory.location == "Updated Location"

def test_delete_factory(client, sample_factory):
    """Test deleting a factory"""
    response = client.delete(f'/factories/{sample_factory.id}')
    
    assert response.status_code == 204
    
    # Verify factory was deleted from database
    deleted_factory = Factory.query.get(sample_factory.id)
    assert deleted_factory is None
