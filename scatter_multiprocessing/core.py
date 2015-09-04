"""
    scatter_multiprocessing.core
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Asynchronous primitives for multiprocessing.
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('Event', 'Condition', 'Lock', 'RLock', 'Semaphore', 'BoundedSemaphore', 'Queue', 'Signal')


import multiprocessing
import signal

from multiprocessing import synchronize
from scatter.ext.async.core import spin_wait


class ScatterProcessEvent(synchronize.Event):
    """
    """

    def wait(self, timeout=None):
        """
        """
        wait = super(ScatterProcessEvent, self).wait
        return spin_wait(wait, timeout, lambda r: bool(r))


Event = ScatterProcessEvent
Condition = multiprocessing.Condition
Lock = multiprocessing.Lock
RLock = multiprocessing.RLock
Semaphore = multiprocessing.Semaphore
BoundedSemaphore = multiprocessing.BoundedSemaphore
Queue = multiprocessing.Queue
Signal = signal.signal
