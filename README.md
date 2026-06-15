# Israeli Queue

A Python implementation of the Israeli Queue, a priority queue variant where elements join behind the last member of their group rather than at the back of the line.

[![PyPI](https://img.shields.io/pypi/v/IsraeliQueue)](https://pypi.org/project/IsraeliQueue/)
[![License: MIT](https://img.shields.io/github/license/YonLiud/Israeli-Queue)](LICENSE.txt)
[![Coverage](https://img.shields.io/badge/coverage-97%25-brightgreen)](tests/)

![](https://github.com/user-attachments/assets/566e3f91-dfdb-4cad-988e-3622f4535d3e)

## How it works

In a standard queue, new elements always go to the back. In an Israeli Queue, an element's position depends on whether its group is already represented in the queue. If it is, the element joins immediately after the last member of its group. If not, it goes to the back.

This models real-world queuing behavior where people join their friends already in line rather than starting a new position at the back.

## Installation

```bash
pip install IsraeliQueue
```

## Usage

### Basic queue

```python
from IsraeliQueue import Item, IsraeliQueue

queue = IsraeliQueue()

alice = Item("Alice", group=1)
charlie = Item("Charlie", group=2)
bob = Item("Bob", group=1)

queue.enqueue(alice)    # [Alice]
queue.enqueue(charlie)  # [Alice, Charlie]
queue.enqueue(bob)      # [Alice, Bob, Charlie] — Bob joins his group, not the back

print(queue)  # [Alice, Bob, Charlie]
```

### Explicit placement

Use `put()` to place an item directly after a specific friend:

```python
queue.put(bob, alice)  # Bob joins immediately after Alice
```

### Type-based grouping

`IsraeliQueueByType` automatically groups elements by their Python type:

```python
from IsraeliQueue import IsraeliQueueByType

queue = IsraeliQueueByType()

queue.enqueue("hello")
queue.enqueue(42)
queue.enqueue("world")
queue.enqueue(99)

print(queue)  # [["hello", "world"], [42, 99]]
```

## API

| Method | Description | Complexity |
|---|---|---|
| `enqueue(item)` | Add item; joins group if present, else appends | O(n) |
| `put(item, friend)` | Place item directly after `friend` | O(n) |
| `dequeue()` | Remove and return front item | O(1) |
| `peek()` | Return front item without removing | O(1) |
| `size()` | Number of items in queue | O(1) |
| `is_empty()` | True if queue has no items | O(1) |
| `get_groups()` | List of all group IDs currently in queue | O(n) |
| `items_in_group(group)` | All items belonging to a group | O(n) |

## Testing

```bash
pytest --cov=IsraeliQueue --cov-report=term-missing
```

97% coverage across 38 tests covering edge cases, error conditions, and performance.

## Contributing

Issues and pull requests are welcome. For significant changes, open an issue first.

## License

MIT — see [LICENSE.txt](LICENSE.txt)
