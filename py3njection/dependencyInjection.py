from functools import wraps


def inject(function_to_wrap):
    @wraps(function_to_wrap)
    def wrapper(*arguments, **keywords):
        for (function_argument_keyword, dependency) in function_to_wrap.__annotations__.items():
            if function_argument_keyword != 'return' and function_argument_keyword not in keywords:
                keywords[function_argument_keyword] = dependency()
        return function_to_wrap(*arguments, **keywords)

    return wrapper
