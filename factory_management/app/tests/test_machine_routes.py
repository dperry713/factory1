def test_create_machine(client, sample_factory):
    """Test creating a new machine"""
    machine_data = {
        "name": "Test Machine",
        "type": "Testing",
        "factory_id": sample_factory.id
    }
    
    response = client.post('/machines/', 
        data=json.dumps(machine_data),
        content_type='application/json'
    )
    
    assert response.status_code == 201
    
    # Verify machine was created in database
    created_machine = Machine.query.filter_by(name="Test Machine").first()
    assert created_machine is not None
    assert created_machine.type == "Testing"

def test_get_machines(client, sample_machine):
    """Test retrieving list of machines"""
    response = client.get('/machines/')
    
    assert response.status_code == 200
    
    machines = json.loads(response.data)
    assert len(machines) > 0
    assert machines[0]['name'] == sample_machine.name
