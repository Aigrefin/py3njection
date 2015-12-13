from functools import wraps


def inject(function_to_wrap):
    """This decorator will inject a new instance of every annotated parameter
    of a function.

    It will use the hinted type of a parameter to create the object (these
    object could have a decorated constructor too).

    More on http://py3njection.readthedocs.org/en/latest/

    :param function_to_wrap: the function that will be injected with instances.
    :return: the new decorated function with its instances

    :Example:

    >>>from some_package import ClassToInject
    >>>from py3njection import inject
    >>>class Demo:
    ...    @inject
    ...    def __init__(self, object_to_use: ClassToInject):
    ...        self.dependency = object_to_use
    ...
    >>> Demo()
    <__main__.Demo object at 0x10136dd30>

    """

    @wraps(function_to_wrap)
    def wrapper(*arguments, **keywords):
        for (function_argument_keyword, dependency) in function_to_wrap.__annotations__.items():
            if function_argument_keyword != 'return' and function_argument_keyword not in keywords:
                keywords[function_argument_keyword] = dependency()
        return function_to_wrap(*arguments, **keywords)

    return wrapper
