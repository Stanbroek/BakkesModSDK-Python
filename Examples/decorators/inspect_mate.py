#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``inspect_mate`` provides more methods to get information about class attribute
than the standard library ``inspect``.

This module is Python2/3 compatible, tested under Py2.7, 3.3, 3.4, 3.5, 3.6.

Includes tester function to check:

- is regular attribute
- is property style method
- is regular method, example: ``def method(self, *args, **kwargs)``
- is static method
- is class method

These are 5-kind class attributes.

and getter function to get each kind of class attributes of a class.

From https://gist.github.com/MacHu-GWU/0170849f693aa5f8d129aa03fc358305
"""

__version__ = "0.0.1"
__author__ = "Sanhe Hu"
__license__ = "MIT"


import inspect
import functools


def is_attribute(klass, attr, value=None):
    """Test if a value of a class is attribute. (Not a @property style
    attribute)

    :param klass: the class
    :param attr: attribute name
    :param value: attribute value
    """
    if value is None:
        value = getattr(klass, attr)
    assert getattr(klass, attr) == value

    if not inspect.isroutine(value):
        if not isinstance(value, property):
            return True
    return False


def is_property_method(klass, attr, value=None):
    """Test if a value of a class is @property style attribute.

    :param klass: the class
    :param attr: attribute name
    :param value: attribute value
    """
    if value is None:
        value = getattr(klass, attr)
    assert getattr(klass, attr) == value

    if not inspect.isroutine(value):
        if isinstance(value, property):
            return True
    return False


def is_regular_method(klass, attr, value=None):
    """Test if a value of a class is regular method.

    example::

        class MyClass(object):
            def to_dict(self):
                ...

    :param klass: the class
    :param attr: attribute name
    :param value: attribute value
    """
    if value is None:
        value = getattr(klass, attr)
    assert getattr(klass, attr) == value

    if inspect.isroutine(value):
        if not is_static_method(klass, attr, value) \
                and not is_class_method(klass, attr, value):
            return True

    return False


def is_static_method(klass, attr, value=None):
    """Test if a value of a class is static method.

    example::

        class MyClass(object):
            @staticmethod
            def method():
                ...

    :param klass: the class
    :param attr: attribute name
    :param value: attribute value
    """
    if value is None:
        value = getattr(klass, attr)
    assert getattr(klass, attr) == value

    for cls in inspect.getmro(klass):
        if inspect.isroutine(value):
            if attr in cls.__dict__:
                binded_value = cls.__dict__[attr]
                if isinstance(binded_value, staticmethod):
                    return True
    return False


def is_class_method(klass, attr, value=None):
    """Test if a value of a class is class method.

    example::

        class MyClass(object):
            @classmethod
            def method(cls):
                ...

    :param klass: the class
    :param attr: attribute name
    :param value: attribute value
    """
    if value is None:
        value = getattr(klass, attr)
    assert getattr(klass, attr) == value

    for cls in inspect.getmro(klass):
        if inspect.isroutine(value):
            if attr in cls.__dict__:
                binded_value = cls.__dict__[attr]
                if isinstance(binded_value, classmethod):
                    return True
    return False


def _get_members(klass, tester_func, return_builtin):
    """

    :param klass: a class.
    :param tester_func: is_xxx function.
    :param allow_builtin: bool, if False, built-in variable or method such as
      ``__name__``, ``__init__`` will not be returned.
    """
    if not inspect.isclass(klass):
        raise ValueError

    pairs = list()
    for attr, value in inspect.getmembers(klass):
        if tester_func(klass, attr, value):
            if return_builtin:
                pairs.append((attr, value))
            else:
                if not (attr.startswith("__") or attr.endswith("__")):
                    pairs.append((attr, value))

    return pairs


get_attributes = functools.partial(
    _get_members, tester_func=is_attribute, return_builtin=False)
get_attributes.__doc__ = "Get all class attributes members."

get_property_methods = functools.partial(
    _get_members, tester_func=is_property_method, return_builtin=False)
get_property_methods.__doc__ = "Get all property style attributes members."

get_regular_methods = functools.partial(
    _get_members, tester_func=is_regular_method, return_builtin=False)
get_regular_methods.__doc__ = "Get all non static and class method members"

get_static_methods = functools.partial(
    _get_members, tester_func=is_static_method, return_builtin=False)
get_static_methods.__doc__ = "Get all static method attributes members."

get_class_methods = functools.partial(
    _get_members, tester_func=is_class_method, return_builtin=False)
get_class_methods.__doc__ = "Get all class method attributes members."


def get_all_attributes(klass):
    """Get all attribute members (attribute, property style method).
    """
    if not inspect.isclass(klass):
        raise ValueError

    pairs = list()
    for attr, value in inspect.getmembers(
            klass, lambda x: not inspect.isroutine(x)):
        if not (attr.startswith("__") or attr.endswith("__")):
            pairs.append((attr, value))
    return pairs


def get_all_methods(klass):
    """Get all method members (regular, static, class method).
    """
    if not inspect.isclass(klass):
        raise ValueError

    pairs = list()
    for attr, value in inspect.getmembers(
            klass, lambda x: inspect.isroutine(x)):
        if not (attr.startswith("__") or attr.endswith("__")):
            pairs.append((attr, value))
    return pairs
