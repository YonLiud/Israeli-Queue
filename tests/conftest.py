import pytest
import sys
import os

# Add the parent directory to the path so we can import IsraeliQueue
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from IsraeliQueue.IsraeliQueue import Item, IsraeliQueue, IsraeliQueueByType


@pytest.fixture
def sample_items():
    """Create sample items for testing."""
    return [
        Item("Alice", 1),
        Item("Bob", 1),
        Item("Charlie", 2),
        Item("David", 2),
        Item("Eve", 3),
    ]


@pytest.fixture
def basic_queue():
    """Create a basic Israeli queue with some items."""
    queue = IsraeliQueue()
    queue.append(Item("Alice", 1))
    queue.append(Item("Charlie", 2))
    queue.append(Item("Eve", 3))
    return queue


@pytest.fixture
def type_queue():
    """Create a type-based queue with some items."""
    queue = IsraeliQueueByType()
    queue.enqueue("hello")
    queue.enqueue(42)
    queue.enqueue("world")
    queue.enqueue(100)
    return queue