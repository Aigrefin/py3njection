Advanced usage
==============

I want to create my own instanciation method
--------------------------------------------

By default, an injectable class will be instanciated each time it is injected.

To override this behavior, you have to implement a *@classmethod* named _instance_factory.
If *@inject* sees this method, it calls it instead of creating the instance itself.

.. code-block:: python

    class ToInject:
        @classmethod
        def _instance_factory():
            # Your way of delivering an instance
            return instance

The singleton decorator does the same thing. Except it adds the class method to an existing class.

Take a peek at the `singleton decorator implementation`_ for an example.

.. _singleton decorator implementation: https://github.com/Aigrefin/py3njection
