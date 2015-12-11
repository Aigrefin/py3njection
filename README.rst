Py3njection
===========

.. image:: https://travis-ci.org/Aigrefin/py3njection.svg
    :target: https://travis-ci.org/Aigrefin/py3njection
    :alt: Build Status

.. image:: https://codecov.io/github/Aigrefin/py3njection/coverage.svg?branch=master
    :target: https://codecov.io/github/Aigrefin/py3njection?branch=master
    :alt: Tests status

.. image:: https://readthedocs.org/projects/py3njection/badge/?version=latest
    :target: http://py3njection.readthedocs.org/en/latest/?badge=latest
    :alt: Documentation Status

How to use
----------

.. code-block:: python

    from py3njection import inject
    from some_package import ClassToInject

    class Demo:
        @inject
        def __init__(self, object_to_use: ClassToInject):
            self.dependency = object_to_use

    demo = Demo()

How does it work ?
------------------

The decorator *@inject* looks for any annotated method/function parameters (*return* annotation excluded).

It creates a **new** object from the specified class **if no** object is already provided.

How to install
--------------

It's available on PyPI !

.. code-block:: bash

    pip install py3injection

Some Notes
----------

- Unit tests come easy to set up (unless you have too many dependencies, but that would be a code smell, right ?). Juste specify mock instances at your object creation. Examples will come later.
- This also means the injected object could also have some of its members injected too at their initialization !
