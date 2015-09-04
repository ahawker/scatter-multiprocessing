"""
    scatter_multiprocessing.worker
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('ProcessWorkerService',)


import multiprocessing

from scatter.ext.async import spin_wait, Worker, WorkerService
from scatter.exceptions import ScatterExit
from scatter_multiprocessing.core import Event


class ScatterProcess(multiprocessing.Process):
    """

    """

    def __init__(self, func, *args, **kwargs):
        super(ScatterProcess, self).__init__(target=func, args=args, kwargs=kwargs)
        self.daemon = True
        self._seconds = 0
        self._started = Event()
        self._completed = Event()
        self._cancelled = Event()

    @property
    def id(self):
        return self.ident

    def start(self):
        """
        """
        return super(ScatterProcess, self).start()

    def start_later(self, seconds):
        """
        """
        self._seconds = seconds
        self.start()

    def started(self):
        """
        """
        return self._started.is_set()

    def running(self):
        """
        """
        return self.is_alive()

    def completed(self):
        """
        """
        return self._completed.is_set()

    def wait_for_start(self, timeout=None):
        """
        """
        return self._started.wait(timeout)

    def wait_for_completion(self, timeout=None):
        """
        """
        return self._completed.wait(timeout)

    def run(self):
        """
        """
        cancelled = self._cancelled.wait(self._seconds)
        if cancelled:
            return
        self._started.set()
        try:
            super(ScatterProcess, self).run()
        finally:
            self._completed.set()

    def cancel(self):
        """
        """
        self._cancelled.set()
        return not self.started()

    def stop(self, exception=ScatterExit, timeout=None):
        """
        """
        self.terminate()
        return self.join(timeout)

    def join(self, timeout=None):
        """
        """
        join = super(ScatterProcess, self).join
        return spin_wait(join, timeout, lambda r: not self.is_alive())

    def get(self, block=True, timeout=None):
        """
        """
        return self._result.get(block, timeout)

    def is_current(self):
        """
        """
        return multiprocessing.current_process() is self


class ProcessWorker(Worker):
    """
    """

    worker_cls = ScatterProcess


class ProcessWorkerService(WorkerService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.worker_class = ProcessWorker