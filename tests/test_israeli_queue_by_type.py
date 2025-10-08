import pytest
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from IsraeliQueue.IsraeliQueue import IsraeliQueueByType


class TestIsraeliQueueByType:
    """Test cases for the IsraeliQueueByType class."""

    def test_empty_queue_creation(self):
        """Test creating an empty type queue."""
        queue = IsraeliQueueByType()
        assert queue.is_empty()
        assert queue.size() == 0

    def test_enqueue_single_type(self):
        """Test enqueuing items of a single type."""
        queue = IsraeliQueueByType()

        queue.enqueue("hello")
        queue.enqueue("world")

        assert queue.size() == 2
        assert not queue.is_empty()
        assert len(queue) == 1  # One subqueue
        assert queue[0] == ["hello", "world"]

    def test_enqueue_multiple_types(self):
        """Test enqueuing items of different types."""
        queue = IsraeliQueueByType()

        queue.enqueue("hello")
        queue.enqueue(42)
        queue.enqueue("world")
        queue.enqueue(100)

        assert queue.size() == 4
        assert len(queue) == 2  # Two subqueues

        # Find string and int subqueues
        str_queue = None
        int_queue = None
        for subqueue in queue:
            if isinstance(subqueue[0], str):
                str_queue = subqueue
            elif isinstance(subqueue[0], int):
                int_queue = subqueue

        assert str_queue == ["hello", "world"]
        assert int_queue == [42, 100]

    def test_dequeue_single_type(self):
        """Test dequeuing from queue with single type."""
        queue = IsraeliQueueByType()
        queue.enqueue("first")
        queue.enqueue("second")

        dequeued = queue.dequeue()
        assert dequeued == "first"
        assert queue.size() == 1
        assert queue[0] == ["second"]

    def test_dequeue_multiple_types(self):
        """Test dequeuing follows FIFO order for first subqueue."""
        queue = IsraeliQueueByType()

        # Add strings first, then ints
        queue.enqueue("hello")
        queue.enqueue(42)
        queue.enqueue("world")

        # Should dequeue from first subqueue (strings)
        assert queue.dequeue() == "hello"
        assert queue.dequeue() == "world"
        # Now should dequeue from second subqueue (ints)
        assert queue.dequeue() == 42

    def test_dequeue_empty_queue(self):
        """Test dequeue from empty queue raises error."""
        queue = IsraeliQueueByType()

        with pytest.raises(IndexError, match="Cannot dequeue from empty queue"):
            queue.dequeue()

    def test_dequeue_removes_empty_subqueues(self):
        """Test that empty subqueues are removed after dequeuing."""
        queue = IsraeliQueueByType()
        queue.enqueue("only_string")
        queue.enqueue(42)

        # Dequeue the only string
        queue.dequeue()

        # String subqueue should be removed
        assert len(queue) == 1
        assert queue[0] == [42]

    def test_peek(self):
        """Test peeking at front item without removing."""
        queue = IsraeliQueueByType()
        queue.enqueue("first")
        queue.enqueue(42)

        peeked = queue.peek()
        assert peeked == "first"
        assert queue.size() == 2  # Size unchanged

    def test_peek_empty_queue(self):
        """Test peek on empty queue raises error."""
        queue = IsraeliQueueByType()

        with pytest.raises(IndexError, match="Cannot peek empty queue"):
            queue.peek()

    def test_get_types(self):
        """Test getting all types present in queue."""
        queue = IsraeliQueueByType()
        queue.enqueue("string")
        queue.enqueue(42)
        queue.enqueue([1, 2, 3])

        types = queue.get_types()
        assert set(types) == {str, int, list}

    def test_items_of_type(self):
        """Test getting all items of a specific type."""
        queue = IsraeliQueueByType()
        queue.enqueue("hello")
        queue.enqueue(42)
        queue.enqueue("world")
        queue.enqueue(100)

        strings = queue.items_of_type(str)
        assert strings == ["hello", "world"]

        ints = queue.items_of_type(int)
        assert ints == [42, 100]

        floats = queue.items_of_type(float)
        assert floats == []

    def test_complex_types(self):
        """Test with complex data types."""
        queue = IsraeliQueueByType()

        # Add various complex types
        queue.enqueue({"name": "Alice"})
        queue.enqueue([1, 2, 3])
        queue.enqueue({"name": "Bob"})
        queue.enqueue((1, 2))
        queue.enqueue([4, 5, 6])

        assert queue.size() == 5
        assert len(queue) == 3  # dict, list, tuple subqueues

        # Check grouping
        dicts = queue.items_of_type(dict)
        lists = queue.items_of_type(list)
        tuples = queue.items_of_type(tuple)

        assert dicts == [{"name": "Alice"}, {"name": "Bob"}]
        assert lists == [[1, 2, 3], [4, 5, 6]]
        assert tuples == [(1, 2)]

    def test_queue_with_none_values(self):
        """Test queue behavior with None values."""
        queue = IsraeliQueueByType()
        queue.enqueue(None)
        queue.enqueue("string")
        queue.enqueue(None)

        assert queue.size() == 3
        nones = queue.items_of_type(type(None))
        assert nones == [None, None]

    def test_dequeue_until_empty(self):
        """Test dequeuing until queue is completely empty."""
        queue = IsraeliQueueByType()
        items = ["a", 1, "b", 2, "c"]

        for item in items:
            queue.enqueue(item)

        dequeued = []
        while not queue.is_empty():
            dequeued.append(queue.dequeue())

        # Should maintain type grouping order
        assert dequeued == ["a", "b", "c", 1, 2]
        assert queue.is_empty()
        assert queue.size() == 0
