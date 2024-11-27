from flask_limiter.util import get_remote_address

DEFAULT_LIMIT = "5 per minute"

def configure_rate_limiter(limiter):
    limiter.key_func = get_remote_address
    limiter.default_limits = [DEFAULT_LIMIT]
