from multiprocessing import RLock

singletons = {}
lock = RLock()


def singleton(original_class):
    """This decorator, used with the inject decorator, ensures only one
    unique instance of an injected object will ever be created.

    It creates an instance if none exists, and set it as the return value of
    the protected class method _instance_factory (the instance memorization
    is thread safe).
    When _instance_factory is detected by the inject decorator, it overrides
    inject default instanciation mechanism (see inject doc).

    More on http://py3njection.readthedocs.org/en/latest/

    :param original_class: the class which needs to be a singleton
    :return: the class as singleton for the inject decorator

    :Example:

    >>>from py3njection import singleton
    >>>@singleton
    ...class Demo:
    ...     pass

    """

    _set_singleton_instance(original_class)

    def singleton_factory(cls):
        return singletons[original_class]

    original_class._instance_factory = classmethod(singleton_factory)
    return original_class


def _set_singleton_instance(original_class):
    lock.acquire()
    if original_class not in singletons:
        singletons[original_class] = original_class()
    lock.release()
