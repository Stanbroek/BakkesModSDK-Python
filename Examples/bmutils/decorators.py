import sys
import asyncio
import inspect
from typing import Callable, Any, Dict
from functools import wraps

from bakkesmod import cvarManager, gameWrapper, BakkesModPlugin

from . import inspect_mate
from .bmasync import BMEventLoopPolicy

__all__ = ["bmasync", "PLUGINTYPE_NORMAL", "PLUGINTYPE_ASYNC",
           "plugin", "onLoad", "onUnload"]

PLUGINTYPE_NORMAL = 0
PLUGINTYPE_ASYNC = 1

_loadedPlugins: Dict[str, Any] = {}
_loop: asyncio.AbstractEventLoop = None


def _setup_loop() -> None:
    global _loop
    if not _loop:
        asyncio.set_event_loop_policy(BMEventLoopPolicy())
        _loop = asyncio.new_event_loop()
        asyncio.set_event_loop(_loop)
        _loop.start()


def bmasync(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """async function decorator"""
    _setup_loop()

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return asyncio.ensure_future(func(*args, **kwargs))

    return wrapper


def _named_plugin(name: str, mode: int) -> Callable[[Any], Callable[[Any], type]]:
    def decorator(cls: type) -> Callable[[Any], type]:
        global _loadedPlugins
        _loadedPlugins[cls.__module__] = {
            'class': cls,
            'class_mode': mode,
            'class_name_override': name,
            'class_instance': None
        }

        @wraps(cls)
        def wrapper(*args, **kwargs) -> type:
            return cls(*args, **kwargs)
        return wrapper
    return decorator


def _plugin(cls: type) -> Callable[[Any], type]:
    @wraps(cls)
    def wrapper(*args, **kwargs) -> type:
        return cls(*args, **kwargs)
    return wrapper


def plugin(*args) -> type:
    """plugin class decorator"""
    types = tuple(arg.__class__ for arg in args)
    if types == (str, int):
        return _named_plugin(args[0], args[1])
    elif types == (type,):
        return _plugin(types[0])
    else:
        raise RuntimeError(types)


def _call_func(func: Callable[[Any], Any], *args, **kwargs) -> Any:
    if inspect.iscoroutinefunction(func):
        return bmasync(func)(*args, **kwargs)
    return func(*args, **kwargs)


def onLoad(func: Callable[[None], None]) -> Callable[[None], None]:
    """onLoad function decorator"""
    @wraps(func)
    def wrapper() -> None:
        global _loadedPlugins
        if func.__module__ in _loadedPlugins:
            plugin_class = _loadedPlugins[func.__module__]['class']
            plugin_instance = plugin_class()
            _loadedPlugins[func.__module__]['class_instance'] = plugin_instance
            if issubclass(plugin_class, BakkesModPlugin):
                plugin_instance.cvarManager = cvarManager
                plugin_instance.gameWrapper = gameWrapper
            if inspect_mate.is_regular_method(plugin_class, func.__name__):
                return _call_func(func, plugin_instance)
            if inspect_mate.is_class_method(plugin_class, func.__name__):
                return _call_func(func, plugin_class)
        return _call_func(func)

    sys.modules[func.__module__].onLoad = wrapper
    return wrapper


def onUnload(func: Callable[[None], None]) -> Callable[[None], None]:
    """onUnload function decorator"""
    @wraps(func)
    def wrapper() -> None:
        global _loadedPlugins
        if func.__module__ in _loadedPlugins:
            plugin_class = _loadedPlugins[func.__module__]['class']
            if inspect_mate.is_regular_method(plugin_class, func.__name__):
                plugin_class_instance_tmp = _loadedPlugins[func.__module__]['class_instance']
                _loadedPlugins[func.__module__]['class_instance'] = None
                return _call_func(func, plugin_class_instance_tmp)
            if inspect_mate.is_class_method(plugin_class, func.__name__):
                return _call_func(func, plugin_class)
        return _call_func(func)

    sys.modules[func.__module__].onUnload = wrapper
    return wrapper
