"""
Israeli Queue - A Python implementation of Israeli Queues.

Israeli Queues are a data structure where items can "join their friends"
in line, creating more realistic simulations of human queuing behavior.
"""

from .IsraeliQueue import Item, IsraeliQueue, IsraeliQueueByType

try:
    from ._version import version as __version__
except ImportError:
    # Fallback for development installs without setuptools_scm
    __version__ = "unknown"

__all__ = [
    "Item",
    "IsraeliQueue",
    "IsraeliQueueByType",
    "__version__",
]
