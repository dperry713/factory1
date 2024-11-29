def test_create_worker(client, sample_factory):
    """Test creating a new worker"""
    worker_data = {
        "name": "New Worker",
        "role": "Tester",
        "factory_id": sample_factory.id
    }
    
    response = client.post('/workers/', 
        data=json.dumps(worker_data),
        content_type='application/json'
    )
    
    assert response.status_code == 201
    
    # Verify worker was created in database
    created_worker = Worker.query.filter_by(name="New Worker").first()
    assert created_worker is not None
    assert created_worker.role == "Tester"

def test_get_workers(client, sample_worker):
    """Test retrieving list of workers"""
    response = client.get('/workers/')
    
    assert response.status_code == 200
    
    workers = json.loads(response.data)
    assert len(workers) > 0
    assert workers[0]['name'] == sample_worker.name
