def test_factory_machine_relationship(client, session, sample_factory):
    """Test relationship between factory and machines"""
    machine1 = Machine(name="Machine 1", type="Type A", factory_id=sample_factory.id)
    machine2 = Machine(name="Machine 2", type="Type B", factory_id=sample_factory.id)
    
    session.add(machine1)
    session.add(machine2)
    session.commit()
    
    factory = Factory.query.get(sample_factory.id)
    assert len(factory.machines) == 2
    assert {machine.name for machine in factory.machines} == {"Machine 1", "Machine 2"}

def test_factory_worker_relationship(client, session, sample_factory):
    """Test relationship between factory and workers"""
    worker1 = Worker(name="Worker 1", role="Role A", factory_id=sample_factory.id)
    worker2 = Worker(name="Worker 2", role="Role B", factory_id=sample_factory.id)
    
    session.add(worker1)
    session.add(worker2)
    session.commit()
    
    factory = Factory.query.get(sample_factory.id)
    assert len(factory.workers) == 2
    assert {worker.name for worker in factory.workers} == {"Worker 1", "Worker 2"}
