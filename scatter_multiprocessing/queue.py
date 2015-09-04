"""
    scatter_multiprocessing.queue
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
"""
__author__ = 'Andrew Hawker <andrew.r.hawker@gmail.com>'
__all__ = ('ProcessQueue',)


import multiprocessing
import Queue as queue

from scatter.ext.async import Queue, QueueService


class ProcessQueue(Queue):
    """
    """

    queue_cls = multiprocessing.Queue


class ProcessQueueService(QueueService):
    """
    """

    def on_initializing(self, *args, **kwargs):
        """
        """
        self.queue_class = ProcessQueue
        self.queue_max_size = None
        self.queue_empty_exception = queue.Empty
        self.queue_full_exception = queue.Full
