import sys
from . import inspect_mate
from typing import Callable
from functools import wraps
from bakkesmod import cvarManager, gameWrapper, BakkesModPlugin

__all__ = ["plugin", "onLoad", "onUnload"]

_plugin_class = None
_plugin_class_instance = None


def plugin(*args):
    """plugin class decorator"""
    types = tuple(arg.__class__ for arg in args)
    if types == (str, int):
        return _named_plugin(args[0], args[1])
    elif types == (type,):
        return _plugin(types[0])
    else:
        raise RuntimeError(types)


def _named_plugin(name: str, mode: int):
    def decorator(cls: type):
        global _plugin_class
        _plugin_class = cls

        @wraps(cls)
        def wrapper(*args, **kwargs):
            return cls(*args, **kwargs)
        return wrapper
    return decorator


def _plugin(cls: type):
    @wraps(cls)
    def wrapper(*args, **kwargs):
        return cls(*args, **kwargs)
    return wrapper


def onLoad(func: Callable[[None], None]):
    """onLoad function decorator"""
    @wraps(func)
    def wrapper():
        global _plugin_class_instance
        if _plugin_class:
            _plugin_class_instance = _plugin_class()
            if issubclass(_plugin_class, BakkesModPlugin):
                _plugin_class_instance.cvarManager = cvarManager
                _plugin_class_instance.gameWrapper = gameWrapper
        if inspect_mate.is_regular_method(_plugin_class, func.__name__):
            return func(_plugin_class_instance)
        if inspect_mate.is_class_method(_plugin_class, func.__name__):
            return func(_plugin_class)
        return func()

    sys.modules[func.__module__].onLoad = wrapper
    return wrapper


def onUnload(func: Callable[[None], None]):
    """onUnload function decorator"""
    @wraps(func)
    def wrapper():
        if inspect_mate.is_regular_method(_plugin_class, func.__name__):
            global _plugin_class_instance
            plugin_class_instance_tmp = _plugin_class_instance
            _plugin_class_instance = None
            return func(plugin_class_instance_tmp)
        if inspect_mate.is_class_method(_plugin_class, func.__name__):
            return func(_plugin_class)
        return func()

    sys.modules[func.__module__].onUnload = wrapper
    return wrapper
