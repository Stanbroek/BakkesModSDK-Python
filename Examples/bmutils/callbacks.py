from typing import Callable, Any, Dict, List

import bakkesmod
from bakkesmod import cvarManager, gameWrapper

__all__ = ['HookEvent', 'HookEventWithCaller', 'UnhookEvent', 'HookEventPost', 'HookEventWithCallerPost', 'UnhookEventPost',
           'SetTimeout', 'Execute', 'RegisterDrawable', 'RegisterNotifier']

_hooks_pre_events: Dict[str, Dict[str, Callable[[str], None]]] = dict()
_hooks_pre_events_with_caller: Dict[str, Dict[str, Callable[[Any, Any, str], None]]] = dict()
_hooks_post_events: Dict[str, Dict[str, Callable[[str], None]]] = dict()
_hooks_post_events_with_caller: Dict[str, Dict[str, Callable[[Any, Any, str], None]]] = dict()


def _pre_event_hook(eventName: str):
    global _hooks_pre_events
    if eventName in _hooks_pre_events:
        for hook in _hooks_pre_events[eventName].values():
            hook(eventName)


def _pre_event_hook_with_caller(caller: Any, params: Any, eventName: str):
    global _hooks_pre_events_with_caller
    if eventName in _hooks_pre_events_with_caller:
        for hook in _hooks_pre_events_with_caller[eventName].values():
            hook(caller, params, eventName)


def _post_event_hook(eventName: str):
    global _hooks_post_events
    if eventName in _hooks_post_events:
        for hook in _hooks_post_events[eventName].values():
            hook(eventName)


def _post_event_hook_with_caller(caller: Any, params: Any, eventName: str):
    global _hooks_post_events_with_caller
    if eventName in _hooks_post_events_with_caller:
        for hook in _hooks_post_events_with_caller[eventName].values():
            hook(caller, params, eventName)


def HookEvent(eventName: str, callback: Callable[[str], None]):
    """TBD."""
    global _hooks_pre_events
    if eventName not in _hooks_pre_events:
        gameWrapper.HookEvent(eventName, _pre_event_hook)
        _hooks_pre_events[eventName] = dict()
    _hooks_pre_events[eventName][callback.__module__] = callback


def HookEventWithCaller(eventName: str, callback: Callable[[Any, Any, str], None]):
    """TBD."""
    global _hooks_pre_events_with_caller
    if eventName not in _hooks_pre_events_with_caller:
        gameWrapper.HookEventWithCaller(eventName, _pre_event_hook_with_caller)
        _hooks_pre_events_with_caller[eventName] = dict()
    _hooks_pre_events_with_caller[eventName][callback.__module__] = callback


def UnhookEvent(eventName: str):
    """TBD."""
    raise NotImplementedError("Need to find out which module called this.")
    global _hooks_post_events
    if eventName in _hooks_post_events:
        _hooks_post_events[eventName].pop(__package__)
        if not _hooks_post_events[eventName]:
            _hooks_post_events.pop(eventName)

    global _hooks_post_events_with_caller
    if eventName in _hooks_post_events_with_caller:
        _hooks_post_events_with_caller[eventName].pop(__package__)
        if not _hooks_post_events_with_caller[eventName]:
            _hooks_post_events_with_caller.pop(eventName)

    if eventName not in _hooks_post_events and eventName not in _hooks_post_events_with_caller:
        gameWrapper.UnhookEvent(eventName)


def HookEventPost(eventName: str, callback: Callable[[str], None]):
    """TBD."""
    global _hooks_post_events
    if eventName not in _hooks_post_events:
        gameWrapper.HookEventPost(eventName, _post_event_hook)
        _hooks_post_events[eventName] = dict()
    _hooks_post_events[eventName][callback.__module__] = callback


def HookEventWithCallerPost(eventName: str, callback: Callable[[Any, Any, str], None]):
    """TBD."""
    global _hooks_post_events_with_caller
    if eventName not in _hooks_post_events_with_caller:
        gameWrapper.HookEventWithCallerPost(eventName, _post_event_hook_with_caller)
        _hooks_post_events_with_caller[eventName] = dict()
    _hooks_post_events_with_caller[eventName][callback.__module__] = callback


def UnhookEventPost(eventName: str):
    """TBD."""
    raise NotImplementedError("Need to find out which package called this.")
    global _hooks_pre_events
    if eventName in _hooks_pre_events:
        _hooks_pre_events[eventName].pop(__package__)
        if not _hooks_pre_events[eventName]:
            _hooks_pre_events.pop(eventName)

    global _hooks_pre_events_with_caller
    if eventName in _hooks_pre_events_with_caller:
        _hooks_pre_events_with_caller[eventName].pop(__package__)
        if not _hooks_pre_events_with_caller[eventName]:
            _hooks_pre_events_with_caller.pop(eventName)

    if eventName not in _hooks_pre_events and eventName not in _hooks_pre_events_with_caller:
        gameWrapper.UnhookEvent(eventName)


def SetTimeout(theLambda: Callable[[bakkesmod.GameWrapper], None], time: float):
    """TBD."""
    return gameWrapper.SetTimeout(theLambda, time)


def Execute(theLambda: Callable[[bakkesmod.GameWrapper], None]):
    """TBD."""
    return gameWrapper.Execute(theLambda)


def RegisterDrawable(theLambda: Callable[[bakkesmod.CanvasWrapper], None]):
    """TBD."""
    return gameWrapper.RegisterDrawable(theLambda)


def RegisterNotifier(cvar: str, notifier: Callable[[List[str]], None], description: str, permissions: int):
    """TBD."""
    return cvarManager.registerNotifier(cvar, notifier, description, permissions)
