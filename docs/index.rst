Welcome to p3njection's documentation!
======================================

.. include:: badges.rst

Table of content
----------------

.. toctree::
    :maxdepth: 2

    index
    advanced_usage

How to use
----------

Put inject on top of the method. All annotated parameters will be injected with an instance matching the annotation type.

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

**If no** object is already provided, that is if no parameter is given and no default parameter exists, *@inject* will provide and instance. This instance is either a new object, or the result of the class factory (see :doc:`advanced_usage`)

What if I want a singleton ?
----------------------------

Put it on top of the class to mark as singleton.

.. code-block:: python

    @singleton
    class ClassToInject:
        pass

That's it ! When *@inject* sees a class with this decorator, it **always** uses the **same** instance.

**Note** : It stays a singleton as long as your using *@inject* to get the instance.

How to install
--------------

It's available on PyPI !

.. code-block:: bash

    pip install py3injection

Or get it at : https://pypi.python.org/pypi/py3njection

Contact and Contribution
------------------------

Feel free to contribute in any way :

- help, bugs, issues, suggestions : https://github.com/Aigrefin/py3njection/issues
- twitter account : https://twitter.com/Julien_Tellier
- and finally my mail address is in the setup.py

Some Notes
----------

- Unit tests come easy to set up (unless you have too many dependencies, but that would be a code smell, right ?). Juste specify mock instances at your object creation. Examples will come later.
- This also means the injected object could also have some of its members injected too at their initialization !
