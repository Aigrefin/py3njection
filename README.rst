Py3njection
===========

How to use
----------

.. code-block:: python

    from py3njection import inject
    from some_package import ClassToInject

    class Demo:
        @inject
        def __init__(self, object_to_use: ClassToInject):
            object_to_use.call_method()

    demo = Demo()

How does it work ?
------------------

The decorator *@inject* looks for any annotated method/function parameters (*return* annotation excluded).

It creates a new object from the specified class if no object is already provided.

How to install
--------------

It's available on PyPI !

.. code-block::

    pip install py3injection

Some Notes
----------

- Unit tests come easy to set up (unless you have too many dependencies, but that would be a code smell, right ?). Juste specify mock instances at your object creation. Examples will come later.
- This also means the injected object could also have some of its members injected too at their initialization !
