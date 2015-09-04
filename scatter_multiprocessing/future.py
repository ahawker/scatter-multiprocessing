"""
    scatter_multiprocessing.future
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('ProcessFuture',)


from scatter.ext.async.future import Future, FutureService, ScatterFuture


class ProcessAsyncResult(object):
    """

    """

    def __init__(self):
        pass

    def get(self, block=True, timeout=None):
        pass

    def get_nowait(self):
        """
        """
        return self.get(block=False)

    def completed(self):
        pass

    def successful(self):
        pass

    def set_result(self, result):
        pass

    def set_exception(self, exc_info):
        pass


class ProcessFuture(Future):
    """
    """

    future_cls = ScatterFuture


class ProcessFutureService(FutureService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.future_class = ProcessFuture