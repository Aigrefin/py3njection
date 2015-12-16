from functools import wraps


def inject(function_to_wrap):
    """This decorator will inject an instance of every annotated function
    parameter.

    It will use the hinted type of a parameter, its class, to create the object
    (these object could have a decorated constructor too !).

    If the object to inject has a callable attribute '_instance_factory',
    inject will call it to get the instance. Otherwise, a new instance is
    created.

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
    >>>Demo()
    <__main__.Demo object at 0x10136dd30>

    """

    @wraps(function_to_wrap)
    def wrapper(*arguments, **actual_keywords):
        for (function_argument_key, dependency) in function_to_wrap.__annotations__.items():
            no_instance_is_provided = function_argument_key not in actual_keywords
            if no_instance_is_provided and function_argument_key != 'return':
                actual_keywords[function_argument_key] = __use_instance_factory(dependency)
        return function_to_wrap(*arguments, **actual_keywords)

    return wrapper


def __use_instance_factory(dependency):
    if hasattr(dependency, '_instance_factory') and callable(getattr(dependency, '_instance_factory')):
        return dependency._instance_factory()
    return dependency()
