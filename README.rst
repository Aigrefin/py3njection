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

.. image:: https://badges.gitter.im/Join%20Chat.svg
    :target: https://gitter.im/Aigrefin/py3njection?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
    :alt: Join the chat at https://gitter.im/Aigrefin/py3njection

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

What if I want a singleton ?
----------------------------

.. code-block:: python

    @singleton
    class ClassToInject:
        pass

That's it ! When *@inject* sees a class with this decorator, it **always** uses the **same** instance.

How to install
--------------

It's available on PyPI !

.. code-block:: bash

    pip install py3injection

Or get it at : https://pypi.python.org/pypi/py3njection

Want to know more ?
-------------------

A more complete documentation is available here : http://py3njection.readthedocs.org/en/latest/

Contact and Contribution
------------------------

Feel free to contribute in any way :

- help, bugs, issues, suggestions : https://github.com/Aigrefin/py3njection/issues
- twitter account : https://twitter.com/Julien_Tellier
- and finally my mail address is in the setup.py

Some Notes
----------

- Unit tests come easy to set up (unless you have too many dependencies, but that would be a code smell, right ?). Just specify mock instances at your object creation. Examples will come later.
- This also means the injected object could also have some of its members injected too at their initialization !
