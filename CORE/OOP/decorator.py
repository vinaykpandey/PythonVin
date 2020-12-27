from functools import wraps

def message(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print("Start Decorator")
        return fn(*args, **kwargs)
    return wrapper