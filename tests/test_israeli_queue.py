import pytest
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from IsraeliQueue.IsraeliQueue import Item, IsraeliQueue


class TestIsraeliQueue:
    """Test cases for the IsraeliQueue class."""

    def test_empty_queue_creation(self):
        """Test creating an empty queue."""
        queue = IsraeliQueue()
        assert queue.is_empty()
        assert queue.size() == 0

    def test_enqueue_without_friend(self):
        """Test adding items without specifying a friend."""
        queue = IsraeliQueue()
        item1 = Item("Alice", 1)
        item2 = Item("Bob", 2)

        queue.enqueue(item1)
        queue.enqueue(item2)

        assert queue.size() == 2
        assert queue[0] == item1
        assert queue[1] == item2

    def test_put_with_friend(self):
        """Test the basic put functionality."""
        queue = IsraeliQueue()
        alice = Item("Alice", 1)
        charlie = Item("Charlie", 2)
        bob = Item("Bob", 1)  # Same group as Alice

        queue.append(alice)
        queue.append(charlie)

        # Bob should join Alice (his friend in same group)
        queue.put(bob, alice)

        # Bob should be after Alice
        assert queue.index(alice) < queue.index(bob)
        assert queue.index(bob) < queue.index(charlie)

    def test_put_multiple_friends(self):
        """Test putting item when multiple friends exist."""
        queue = IsraeliQueue()
        alice = Item("Alice", 1)
        bob = Item("Bob", 1)
        charlie = Item("Charlie", 2)
        david = Item("David", 1)  # Same group as Alice and Bob

        queue.extend([alice, charlie, bob])  # Alice, Charlie, Bob

        # David should join after Bob (furthest friend)
        queue.put(david, alice)

        expected_order = [alice, charlie, bob, david]
        assert queue == expected_order

    def test_put_no_existing_friends(self):
        """Test putting item when no friends exist in queue."""
        queue = IsraeliQueue()
        alice = Item("Alice", 1)
        charlie = Item("Charlie", 2)
        bob = Item("Bob", 3)  # Different group

        queue.extend([alice, charlie])

        # Bob has no friends, should be added to end
        queue.put(bob, alice)  # alice is just for validation

        assert queue[-1] == bob

    def test_put_friend_not_in_queue(self):
        """Test error when friend is not in queue."""
        queue = IsraeliQueue()
        alice = Item("Alice", 1)
        bob = Item("Bob", 1)
        charlie = Item("Charlie", 2)

        queue.append(alice)

        with pytest.raises(ValueError, match="Friend not found in queue"):
            queue.put(charlie, bob)  # bob is not in queue

    def test_dequeue(self):
        """Test removing items from front of queue."""
        queue = IsraeliQueue()
        alice = Item("Alice", 1)
        bob = Item("Bob", 2)

        queue.extend([alice, bob])

        dequeued = queue.dequeue()
        assert dequeued == alice
        assert queue.size() == 1
        assert queue[0] == bob

    def test_dequeue_empty_queue(self):
        """Test dequeue from empty queue raises error."""
        queue = IsraeliQueue()

        with pytest.raises(IndexError, match="Cannot dequeue from empty queue"):
            queue.dequeue()

    def test_peek(self):
        """Test peeking at front item without removing."""
        queue = IsraeliQueue()
        alice = Item("Alice", 1)
        bob = Item("Bob", 2)

        queue.extend([alice, bob])

        peeked = queue.peek()
        assert peeked == alice
        assert queue.size() == 2  # Size unchanged

    def test_peek_empty_queue(self):
        """Test peek on empty queue raises error."""
        queue = IsraeliQueue()

        with pytest.raises(IndexError, match="Cannot peek empty queue"):
            queue.peek()

    def test_get_groups(self):
        """Test getting all unique groups in queue."""
        queue = IsraeliQueue()
        items = [
            Item("Alice", 1),
            Item("Bob", 1),
            Item("Charlie", 2),
            Item("David", 3),
            Item("Eve", 2),
        ]
        queue.extend(items)

        groups = queue.get_groups()
        assert set(groups) == {1, 2, 3}

    def test_items_in_group(self):
        """Test getting all items in a specific group."""
        queue = IsraeliQueue()
        alice = Item("Alice", 1)
        bob = Item("Bob", 1)
        charlie = Item("Charlie", 2)

        queue.extend([alice, charlie, bob])

        group1_items = queue.items_in_group(1)
        assert set(group1_items) == {alice, bob}

        group2_items = queue.items_in_group(2)
        assert group2_items == [charlie]

        group3_items = queue.items_in_group(3)
        assert group3_items == []

    def test_enqueue_with_friend(self):
        """Test enqueue with friend parameter."""
        queue = IsraeliQueue()
        alice = Item("Alice", 1)
        bob = Item("Bob", 1)

        queue.enqueue(alice)
        queue.enqueue(bob, alice)  # Bob joins Alice

        assert queue.index(alice) < queue.index(bob)

    def test_complex_queue_scenario(self):
        """Test a complex scenario with multiple groups and operations."""
        queue = IsraeliQueue()

        # Initial queue: [Alice(1), Charlie(2), Eve(3)]
        alice = Item("Alice", 1)
        charlie = Item("Charlie", 2)
        eve = Item("Eve", 3)
        queue.extend([alice, charlie, eve])

        # Bob(1) joins Alice's group
        bob = Item("Bob", 1)
        queue.put(bob, alice)
        # Queue: [Alice(1), Bob(1), Charlie(2), Eve(3)]

        # David(2) joins Charlie's group
        david = Item("David", 2)
        queue.put(david, charlie)
        # Queue: [Alice(1), Bob(1), Charlie(2), David(2), Eve(3)]

        # Frank(1) joins group 1 (should go after Bob)
        frank = Item("Frank", 1)
        queue.put(frank, alice)
        # Queue: [Alice(1), Bob(1), Frank(1), Charlie(2), David(2), Eve(3)]

        expected = [alice, bob, frank, charlie, david, eve]
        assert queue == expected

        # Test dequeue operations
        assert queue.dequeue() == alice
        assert queue.dequeue() == bob
        assert queue.peek() == frank
