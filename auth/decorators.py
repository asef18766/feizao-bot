from . import AuthFailure

def require_role(target_role:str):
    def func_wrapper(func):
        def wrapper(*args, **kwargs):
            if  "user_line_id" in kwargs.keys() and target_role == "":
                return func(*args, **kwargs)
            raise AuthFailure()
        return wrapper
    return func_wrapper