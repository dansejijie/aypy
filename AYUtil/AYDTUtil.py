
import functools

def empty_wrapper(func):
    """
    作用范围：函数装饰器 (模块函数或者类函数)
    功能：空装饰器，为fix版本问题使用，或者分逻辑功能实现使用
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

# noinspection PyUnusedLocal
def empty_wrapper_with_params(*p_args, **p_kwargs):
    """
    作用范围：函数装饰器 (模块函数或者类函数)
    功能：带参数空装饰器，为fix版本问题使用，或者分逻辑功能实现使用
    """

    def decorate(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorate
