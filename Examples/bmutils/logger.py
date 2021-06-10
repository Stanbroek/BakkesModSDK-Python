import sys
from io import StringIO

from bakkesmod import cvarManager

__all__ = ['redirectStandardStreams', 'log', 'debug', 'info', 'warning', 'error', 'critical']


class StringIOCallbackStream(object):
    """TDB."""
    def __init__(self, prefix):
        self._io = StringIO()
        self.prefix = prefix

    def write(self, b, *args, **kwargs):
        ret = self._io.write(b, *args, **kwargs)
        if b[-1] == '\n':
            self._io.seek(0)
            for line in self._io.read().strip().split('\n'):
                log(self.prefix, line)
            self._io.seek(self._io.truncate(0))

        return ret

    def __getattr__(self, attr):
        debug(self.prefix, attr)
        return getattr(self._io, attr)


_swapped = False


def redirectStandardStreams():
    """Redirects stdout and strerr to cvarManager log."""
    global _swapped
    if not _swapped:
        sys.stdout = StringIOCallbackStream('stdout')
        sys.stderr = StringIOCallbackStream('stderr')
        _swapped = True


def log(prefix, *args, **kwargs):
    """Logs a message with no level on this logger."""
    cvarManager.log(f"[{prefix}] {' '.join([str(arg) for arg in args])} "
                    f"{' '.join([f'{key}: {value}' for key, value in kwargs])}")


def debug(*args, **kwargs):
    """Logs a message with level DEBUG on this logger."""
    log("[DEBUG]", *args, **kwargs)


def info(*args, **kwargs):
    """Logs a message with level INFO on this logger."""
    log("[INFO]", *args, **kwargs)


def warning(*args, **kwargs):
    """Logs a message with level WARNING on this logger."""
    log("[WARNING]", *args, **kwargs)


def error(*args, **kwargs):
    """Logs a message with level ERROR on this logger"""
    log("[ERROR]", *args, **kwargs)


def critical(*args, **kwargs):
    """Logs a message with level CRITICAL on this logger."""
    log("[CRITICAL]", *args, **kwargs)
