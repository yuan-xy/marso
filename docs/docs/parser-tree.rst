.. include:: ../global.rst

.. _parser-tree:

Parser Tree
===========

The parser tree is returned by calling :py:meth:`marso.Grammar.parse`.

.. note:: Note that marso positions are always 1 based for lines and zero
   based for columns. This means the first position in a file is (1, 0).

Parser Tree Base Classes
------------------------

Generally there are two types of classes you will deal with:
:py:class:`marso.tree.Leaf` and :py:class:`marso.tree.BaseNode`.

.. autoclass:: marso.tree.BaseNode
    :show-inheritance:
    :members:

.. autoclass:: marso.tree.Leaf
    :show-inheritance:
    :members:

All nodes and leaves have these methods/properties:

.. autoclass:: marso.tree.NodeOrLeaf
    :members:
    :undoc-members:
    :show-inheritance:


Python Parser Tree
------------------

.. currentmodule:: marso.python.tree

.. automodule:: marso.python.tree
    :members:
    :undoc-members:
    :show-inheritance:


Utility
-------

.. autofunction:: marso.tree.search_ancestor
