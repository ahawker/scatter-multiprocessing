"""
    scatter_multiprocessing.service
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('ProcessAsyncService',)


from scatter.ext.async import AsyncService
from scatter_multiprocessing.queue import ProcessQueueService
from scatter_multiprocessing.pool import ProcessPoolService
from scatter_multiprocessing.future import ProcessFutureService


class ProcessAsyncService(AsyncService):
    """

    """

    def on_initializing(self, *args, **kwargs):
        """

        """
        self.response_queue_class = ProcessQueueService
        self.worker_pool_class = ProcessPoolService
        self.futures_class = ProcessFutureService
