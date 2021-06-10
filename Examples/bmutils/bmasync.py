# Modified asyncio.BaseEventLoop for BakkesMod.
import sys
import time
import heapq
import asyncio
import logging
import traceback
import collections

from bakkesmod import cvarManager, gameWrapper

__all__ = ['BMEventLoop', 'BMEventLoopPolicy']

# Name the logger after the package.
_logger = logging.getLogger(__package__)

# Maximum timeout passed to select to avoid OS limitations
_MAXIMUM_SELECT_TIMEOUT = 24 * 3600


class BMEventLoop(asyncio.AbstractEventLoop):
    def __init__(self):
        self._debug = False
        self._closed = False
        self._running = False
        self._stopping = False
        self._idle = False
        self._ready = collections.deque()
        self._scheduled = []
        self._clock_resolution = time.get_clock_info('monotonic').resolution

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} running={self.is_running()} "
            f"closed={self.is_closed()} idle={self.is_idle()} "
            f"debug={self.get_debug()}>"
        )

    def set_debug(self, debug):
        self._debug = debug

    def get_debug(self):
        return self._debug

    def time(self):
        """Return the time according to the event loop's clock.

        This is a float expressed in seconds since an epoch, but the
        epoch, precision, accuracy and drift are unspecified and may
        differ per event loop.
        """
        return time.monotonic()

    def _debug_log(self, text):
        """Logs event loop info when in debug mode."""
        if self._debug:
            cvarManager.log(f"[async] DEBUG: {text}")

    def _check_closed(self):
        """Throws runtime error if the event is closed"""
        if self._closed:
            raise RuntimeError("Event loop is closed")

    def _wakeup(self):
        """Will wake up the idle event loop."""
        self._check_closed()
        if not self.is_idle():
            raise RuntimeError("Event loop is not idle")
        self._debug_log("resume event loop")
        gameWrapper.SetTimeout(lambda gw: self._run_once(), 0)

    def _timer_handle_cancelled(self, handle):
        """Notification that a TimerHandle has been cancelled."""
        pass

    # Methods for running the event loop.

    def _run_once(self):
        """Run one full iteration of the event loop.

        This calls all currently ready callbacks, schedules the
        resulting callbacks, and finally schedules "call_later"
        callbacks.
        """
        if self._stopping:
            self._running = False
            self._debug_log("stopped event loop")
            return

        self._debug_log(f"_scheduled={self._scheduled}")

        # Remove delayed calls that were cancelled from head of queue.
        while self._scheduled and self._scheduled[0]._cancelled:
            handle = heapq.heappop(self._scheduled)
            self._debug_log(f"cancelled handle={handle}")
            handle._scheduled = False

        timeout = None
        if self._ready or self._stopping:
            timeout = 0
        elif self._scheduled:
            # Compute the desired timeout.
            when = self._scheduled[0]._when
            timeout = min(max(0, when - self.time()), _MAXIMUM_SELECT_TIMEOUT)

        # Handle 'later' callbacks that are ready.
        end_time = self.time() + self._clock_resolution
        while self._scheduled:
            handle = self._scheduled[0]
            self._debug_log(f"_when={handle._when} >= end_time={end_time}")
            if handle._when >= end_time:
                break
            handle = heapq.heappop(self._scheduled)
            handle._scheduled = False
            self._ready.append(handle)

        self._debug_log(f"_ready={self._ready}")

        # Call the callbacks that are ready.
        ntodo = len(self._ready)
        for i in range(ntodo):
            handle = self._ready.popleft()
            if handle._cancelled:
                self._debug_log(f"cancelled handle={handle}")
                continue
            self._debug_log(f"run handle={handle}")
            handle._run()
        handle = None

        if timeout is not None:
            # self._debug_log(f"next tick in {timeout} seconds")
            # gameWrapper.SetTimeout(lambda gw: self._run_once(), timeout)
            gameWrapper.SetTimeout(lambda gw: self._run_once(), max(timeout, 1))
        else:
            self._debug_log("pause event loop")
            self._idle = True

    def start(self):
        """Run the event loop until stop() is called.
        This function is non blocking."""
        self._debug_log("start")
        self._check_closed()
        if self.is_running():
            raise RuntimeError("This event loop is already running")
        self._running = True
        self._debug_log("started event loop")
        self._run_once()

    def run_forever(self):
        """Run the event loop until stop() is called."""
        self._debug_log("run_forever")
        raise NotImplementedError("run_forever")

    def run_until_complete(self, future):
        """Run the event loop until a Future is done."""
        self._debug_log(f"run_until_complete, future={future}")
        raise NotImplementedError(f"run_until_complete, future={future}")

    def is_running(self):
        """Return whether the event loop is currently running."""
        self._debug_log("is_running")
        return self._running

    def is_closed(self):
        """Returns True if the event loop was closed."""
        self._debug_log("is_closed")
        return self._closed

    def is_idle(self):
        """Returns True if the event loop is idle."""
        self._debug_log("is_idle")
        return self._idle

    def stop(self):
        """Stop running the event loop.

        Every callback already scheduled will still run. This simply informs
        run_forever to stop looping after a complete iteration.
        """
        self._debug_log("stop")
        self._stopping = True

    def close(self):
        """Close the event loop.

        This clears the queues and shuts down the executor,
        but does not wait for the executor to finish.

        The event loop must not be running.
        """
        self._debug_log("close")
        if self.is_running():
            raise RuntimeError("Cannot close a running event loop")
        if self._closed:
            return
        self._closed = True
        self._ready.clear()
        self._scheduled.clear()

    async def shutdown_asyncgens(self):
        """Shutdown all active asynchronous generators."""
        self._debug_log("shutdown_asyncgens")
        # We don"t have any asynchronous generators.

    def call_exception_handler(self, context):
        """Call the current event loop's exception handler.

        The context argument is a dict containing the following keys:

        - 'message': Error message;
        - 'exception' (optional): Exception object;
        - 'future' (optional): Future instance;
        - 'task' (optional): Task instance;
        - 'handle' (optional): Handle instance;
        - 'protocol' (optional): Protocol instance;
        - 'transport' (optional): Transport instance;
        - 'socket' (optional): Socket instance;
        - 'asyncgen' (optional): Asynchronous generator that caused
                                 the exception.

        New keys maybe introduced in the future.

        Note: do not overload this method in an event loop subclass.
        For custom exception handling, use the
        `set_exception_handler()` method.
        """
        self._debug_log(f"call_exception_handler, context={context}")
        message = context.get('message')
        if not message:
            message = "Unhandled exception in event loop"

        exception = context.get('exception')
        if exception is not None:
            exc_info = (type(exception), exception, exception.__traceback__)
        else:
            exc_info = False

        log_lines = [message]
        for key in sorted(context):
            if key in {'message', 'exception'}:
                continue
            value = context[key]
            if key == 'source_traceback':
                tb = "".join(traceback.format_list(value))
                value = "Object created at (most recent call last):\n"
                value += tb.rstrip()
            elif key == 'handle_traceback':
                tb = "".join(traceback.format_list(value))
                value = "Handle created at (most recent call last):\n"
                value += tb.rstrip()
            else:
                value = repr(value)
            log_lines.append(f"{key}: {value}")

        _logger.error("\n".join(log_lines), exc_info=exc_info)
        # Logger writes to stderr, so we steal it.
        sys.stderr.seek(0)
        for line in sys.stderr.read().split('\n'):
            cvarManager.log(f"[async] ERROR: {line}")
        sys.stderr.seek(sys.stderr.truncate(0))

    # Methods for scheduling jobs.

    def call_soon(self, callback, *args, context=None):
        """Arrange for a callback to be called as soon as possible.

        This operates as a FIFO queue: callbacks are called in the
        order in which they are registered.  Each callback will be
        called exactly once.

        Any positional arguments after the callback will be passed to
        the callback when it is called.
        """
        self._debug_log(f"call_soon, callback={callback}, args={args}, "
                        f"context={context}")
        self._check_closed()
        handle = asyncio.Handle(callback, args, self, context)
        self._ready.append(handle)

        if self.is_running() and self.is_idle():
            self._wakeup()

        return handle

    def call_later(self, delay, callback, *args, context=None):
        """Arrange for a callback to be called at a given time.

        Return a Handle: an opaque object with a cancel() method that
        can be used to cancel the call.

        The delay can be an int or float, expressed in seconds.  It is
        always relative to the current time.

        Each callback will be called exactly once.  If two callbacks
        are scheduled for exactly the same time, it undefined which
        will be called first.

        Any positional arguments after the callback will be passed to
        the callback when it is called.
        """
        self._debug_log(f"call_later, delay={delay}, callback={callback}, "
                        f"args={args}, context={context}")
        return self.call_at(self.time() + delay, callback, *args,
                            context=context)

    def call_at(self, when, callback, *args, context=None):
        """Like call_later(), but uses an absolute time.

        Absolute time corresponds to the event loop's time() method.
        """
        self._debug_log(f"call_at, when={when}, callback={callback}, "
                        f"args={args}, context={context}")
        self._check_closed()
        timer = asyncio.TimerHandle(when, callback, args, self, context)
        heapq.heappush(self._scheduled, timer)
        timer._scheduled = True

        if self.is_running() and self.is_idle():
            self._wakeup()

        return timer

    def create_task(self, coro):
        """Schedule a coroutine object.

        Return a task object.
        """
        self._debug_log(f"create_task, coro={coro}")
        self._check_closed()
        return asyncio.Task(coro, loop=self)

    def create_future(self):
        """Create a Future object attached to the loop."""
        self._debug_log("create_future")
        return asyncio.Future(loop=self)


class BMEventLoopPolicy(asyncio.events.BaseDefaultEventLoopPolicy):
    _loop_factory = BMEventLoop
