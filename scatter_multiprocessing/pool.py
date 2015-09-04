"""
    scatter_multiprocessing.pool
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('ProcessPoolService',)


from scatter.ext.async.pool import PoolService
from scatter_multiprocessing.worker import ProcessWorkerService


class ProcessPoolService(PoolService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.pool_worker_class = ProcessWorkerService
