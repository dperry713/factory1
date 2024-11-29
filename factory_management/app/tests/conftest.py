import pytest
from app.app import create_app
from app.models.models import db, Factory, Machine, Worker

@pytest.fixture
def app():
    """Create a Flask app configured for testing"""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })
    
    # Create application context
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """Create a test client for API requests"""
    return app.test_client()

@pytest.fixture
def session(app):
    """Create a database session for adding test data"""
    with app.app_context():
        yield db.session
        db.session.rollback()

@pytest.fixture
def sample_factory(session):
    """Create a sample factory for testing"""
    factory = Factory(name="Test Factory", location="Test Location")
    session.add(factory)
    session.commit()
    return factory

@pytest.fixture
def sample_machine(session, sample_factory):
    """Create a sample machine for testing"""
    machine = Machine(
        name="Test Machine", 
        type="Testing", 
        factory_id=sample_factory.id
    )
    session.add(machine)
    session.commit()
    return machine

@pytest.fixture
def sample_worker(session, sample_factory):
    """Create a sample worker for testing"""
    worker = Worker(
        name="Test Worker", 
        role="Tester", 
        factory_id=sample_factory.id
    )
    session.add(worker)
    session.commit()
    return worker
