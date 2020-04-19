"""
PyQt AND OpenCV
By LiNYoUBiAo
2020/4/19 19:49
"""
from functools import wraps

can_run = True


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated


@decorator_name
def func():
    return("Function is running")


print(func())
can_run = False
print(func())
