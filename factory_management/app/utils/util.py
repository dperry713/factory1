import jwt
import datetime
from flask import request, jsonify
from functools import wraps

SECRET_KEY = "your_secret_key"  # Keep this secure and unique

def encode_token(user_id):
    """Generate a JWT token with user_id and expiration."""
    payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        'iat': datetime.datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_token(token):
    """Decode a JWT token and return the payload."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Token has expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'

def token_required(f):
    """Decorator to check if a valid JWT token is provided."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            user_id = decode_token(token)
        except Exception as e:
            return jsonify({'message': str(e)}), 403
        return f(user_id, *args, **kwargs)
    return decorated

def role_required(allowed_roles):
    """Decorator to check if a user has the required role."""
    def decorator(f):
        @wraps(f)
        def decorated(user_id, *args, **kwargs):
            from models import User
            user = User.query.get(user_id)
            if user.role not in allowed_roles:
                return jsonify({'message': 'Access denied!'}), 403
            return f(user_id, *args, **kwargs)
        return decorated
    return decorator
