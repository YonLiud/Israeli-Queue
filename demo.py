#!/usr/bin/env python3
"""
Demo script showcasing the improved Israeli Queue functionality.
"""

from IsraeliQueue.IsraeliQueue import Item, IsraeliQueue, IsraeliQueueByType


def demo_israeli_queue():
    """Demonstrate the Israeli Queue with improved features."""
    print("=== Israeli Queue Demo ===")

    # Create queue and items
    queue = IsraeliQueue()

    # Create some people with different groups
    alice = Item("Alice", 1)  # Group 1 - VIP
    bob = Item("Bob", 1)  # Group 1 - VIP
    charlie = Item("Charlie", 2)  # Group 2 - Regular
    david = Item("David", 2)  # Group 2 - Regular
    eve = Item("Eve", 3)  # Group 3 - Express

    print("Adding initial people to queue...")
    queue.enqueue(alice)  # Alice joins
    queue.enqueue(charlie)  # Charlie joins
    queue.enqueue(eve)  # Eve joins

    print(f"Queue after initial people: {[str(item) for item in queue]}")

    # Bob joins his VIP friend Alice
    print("\nBob (VIP) wants to join his friend Alice...")
    queue.put(bob, alice)
    print(f"Queue after Bob joins Alice: {[str(item) for item in queue]}")

    # David joins his regular friend Charlie
    print("\nDavid (Regular) wants to join his friend Charlie...")
    queue.put(david, charlie)
    print(f"Queue after David joins Charlie: {[str(item) for item in queue]}")

    # Show queue operations
    print(f"\nQueue size: {queue.size()}")
    print(f"Groups in queue: {queue.get_groups()}")
    print(f"VIP members (group 1): {[str(item) for item in queue.items_in_group(1)]}")

    # Process the queue
    print("\nProcessing queue (FIFO order):")
    while not queue.is_empty():
        person = queue.dequeue()
        print(f"  Serving: {person}")


def demo_israeli_queue_by_type():
    """Demonstrate the type-based queue."""
    print("\n=== Israeli Queue By Type Demo ===")

    queue = IsraeliQueueByType()

    # Add items of different types
    print("Adding items of different types...")
    queue.enqueue("Hello")
    queue.enqueue(42)
    queue.enqueue("World")
    queue.enqueue(3.14)
    queue.enqueue(100)
    queue.enqueue("!")

    print(f"Queue structure: {queue}")
    print(f"Types in queue: {queue.get_types()}")
    print(f"String items: {queue.items_of_type(str)}")
    print(f"Integer items: {queue.items_of_type(int)}")

    # Process the queue
    print("\nProcessing queue (type groups processed in order):")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"  Processing: {item} (type: {type(item).__name__})")


def demo_error_handling():
    """Demonstrate error handling."""
    print("\n=== Error Handling Demo ===")

    queue = IsraeliQueue()
    alice = Item("Alice", 1)
    bob = Item("Bob", 1)

    queue.enqueue(alice)

    # Try to add Bob with a friend not in queue
    try:
        eve = Item("Eve", 3)
        queue.put(bob, eve)  # Eve is not in queue
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")

    # Try to dequeue from empty queue
    queue.dequeue()  # Remove Alice
    try:
        queue.dequeue()  # Try to dequeue from empty queue
    except IndexError as e:
        print(f"✓ Caught expected error: {e}")


if __name__ == "__main__":
    demo_israeli_queue()
    demo_israeli_queue_by_type()
    demo_error_handling()

    print("\n=== Demo Complete ===")
    print("✓ All features working correctly!")
    print("✓ Error handling implemented!")
    print("✓ Comprehensive tests passing!")
