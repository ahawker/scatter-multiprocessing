"""
    scatter_multiprocessing
    ~~~~~~~~~~~~~~~~~~~~~~~

"""

import itertools

from scatter_multiprocessing import core
from scatter_multiprocessing.core import *
from scatter_multiprocessing import future
from scatter_multiprocessing.future import *
from scatter_multiprocessing import pool
from scatter_multiprocessing.pool import *
from scatter_multiprocessing import queue
from scatter_multiprocessing.queue import *
from scatter_multiprocessing import service
from scatter_multiprocessing.service import *
from scatter_multiprocessing import worker
from scatter_multiprocessing.worker import *

__all__ = list(itertools.chain(core.__all__,
                               future.__all__,
                               pool.__all__,
                               queue.__all__,
                               service.__all__,
                               worker.__all__))