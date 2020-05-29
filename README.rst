###################################################################
marso - A Move(Libra) Parser (Not Ready)
###################################################################


.. image:: https://img.shields.io/pypi/v/marso.svg
    :target: https://pypi.org/project/marso/
    :alt: Marso

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: ./LICENSE
    :alt: MIT licensed

.. image:: https://github.com/yuan-xy/marso/workflows/Python%20package/badge.svg
    :target: https://github.com/yuan-xy/marso/actions
    :alt: Python package



Marso is a Move language parser that supports error recovery and round-trip parsing
. Marso is also able to list multiple syntax errors in your move source file.

Marso has been battle-tested by jedi_. 

Marso consists of a small API to parse Move language and analyse the syntax tree.

A simple example:

.. code-block:: python

    >>> import marso
    >>> module = marso.parse('hello + 1', version="3.6")
    >>> expr = module.children[0]
    >>> expr
    PythonNode(arith_expr, [<Name: hello@1,0>, <Operator: +>, <Number: 1>])
    >>> print(expr.get_code())
    hello + 1
    >>> name = expr.children[0]
    >>> name
    <Name: hello@1,0>
    >>> name.end_pos
    (1, 5)
    >>> expr.end_pos
    (1, 9)

To list multiple issues:

.. code-block:: python

    >>> grammar = marso.load_grammar()
    >>> module = grammar.parse('foo +\nbar\ncontinue')
    >>> error1, error2 = grammar.iter_errors(module)
    >>> error1.message
    'SyntaxError: invalid syntax'
    >>> error2.message
    "SyntaxError: 'continue' not properly in loop"

Resources
=========

- `Testing <https://marso.readthedocs.io/en/latest/docs/development.html#testing>`_
- `PyPI <https://pypi.python.org/pypi/marso>`_
- `Docs <https://marso.readthedocs.org/en/latest/>`_
- Uses `semantic versioning <https://semver.org/>`_

Installation
============

    pip install marso



Acknowledgements
================

- David Halter (@davidhalter) for the original `Parso <https://github.com/davidhalter/parso>`_ project.
- Guido van Rossum (@gvanrossum) for creating the parser generator pgen2
  (originally used in lib2to3).


.. _jedi: https://github.com/yuan-xy/jedi
