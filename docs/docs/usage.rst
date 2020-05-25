.. include:: ../global.rst

Usage
=====

|marso| works around grammars. You can simply create Python grammars by calling
:py:func:`marso.load_grammar`. Grammars (with a custom tokenizer and custom parser trees)
can also be created by directly instantiating :py:func:`marso.Grammar`. More information
about the resulting objects can be found in the :ref:`parser tree documentation
<parser-tree>`.

The simplest way of using marso is without even loading a grammar
(:py:func:`marso.parse`):

.. sourcecode:: python

   >>> import marso
   >>> marso.parse('foo + bar')
   <Module: @1-1>

Loading a Grammar
-----------------

Typically if you want to work with one specific Python version, use:

.. autofunction:: marso.load_grammar

Grammar methods
---------------

You will get back a grammar object that you can use to parse code and find
issues in it:

.. autoclass:: marso.Grammar
    :members:
    :undoc-members:


Error Retrieval
---------------

|marso| is able to find multiple errors in your source code. Iterating through
those errors yields the following instances:

.. autoclass:: marso.normalizer.Issue
    :members:
    :undoc-members:


Utility
-------

|marso| also offers some utility functions that can be really useful:

.. autofunction:: marso.parse
.. autofunction:: marso.split_lines
.. autofunction:: marso.python_bytes_to_unicode


Used By
-------

- jedi_ (which is used by IPython and a lot of editor plugins).
- mutmut_ (mutation tester)


.. _jedi: https://github.com/yuan_xy/jedi
.. _mutmut: https://github.com/boxed/mutmut
