.. p3njection documentation master file, created by
sphinx-quickstart on Thu Dec 10 16:41:40 2015.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

Welcome to p3njection's documentation!
======================================

.. image:: https://travis-ci.org/Aigrefin/py3njection.svg
    :target: https://travis-ci.org/Aigrefin/py3njection
    :alt: Build Status

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


.. toctree::
:maxdepth: 2