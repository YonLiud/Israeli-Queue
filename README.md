[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/YonLiud/Israeli-Queue">
    <img src="https://i.ibb.co/bgJQ792/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Israeli Queue</h3>

  <p align="center">
    A high-performance Python implementation of Israeli Queues - where social relationships affect queuing order
    <br />
    <strong>Now with comprehensive testing, type safety, and improved API!</strong>
  </p>
</p>

## 🎯 About Israeli Queue

Israeli Queues are a fascinating data structure that simulates real-world queuing behavior where **social relationships matter**. Unlike traditional FIFO queues, Israeli Queues allow items to "join their friends" in line, creating more realistic simulations of human queuing behavior.

### ✨ Key Features

- **🤝 Social Queuing**: Items can join their friends (same group) in the queue
- **🔄 Dynamic Priority**: Queue order changes based on relationships between elements  
- **🎭 Type-Based Grouping**: Alternative queue that groups items by their data type
- **🛡️ Type Safety**: Full type hints and comprehensive error handling
- **🧪 Well Tested**: 97% test coverage with comprehensive test suite
- **⚡ High Performance**: Optimized algorithms with O(n) insertion complexity

### 🏗️ Architecture

- **`Item`**: Container with data and group membership
- **`IsraeliQueue`**: Main queue where items join friends in their group
- **`IsraeliQueueByType`**: Queue that automatically groups items by type

## 🚀 Installation

### From PyPI
```bash
pip install IsraeliQueue
```

### From Source (Development)
```bash
git clone https://github.com/YonLiud/Israeli-Queue.git
cd Israeli-Queue
pip install -r requirements-dev.txt
```

## 📚 Quick Start

### Basic Israeli Queue Usage

```python
from IsraeliQueue import Item, IsraeliQueue

# Create queue and items
queue = IsraeliQueue()
alice = Item("Alice", group=1)    # VIP group
bob = Item("Bob", group=1)        # VIP group  
charlie = Item("Charlie", group=2) # Regular group

# Add initial people
queue.enqueue(alice)
queue.enqueue(charlie)

# Bob joins his VIP friend Alice
queue.put(bob, alice)  # Bob will be placed after Alice

print(queue)  # [Alice, Bob, Charlie]
```

### Type-Based Queue Usage

```python
from IsraeliQueue import IsraeliQueueByType

queue = IsraeliQueueByType()

# Items are automatically grouped by type
queue.enqueue("Hello")
queue.enqueue(42)
queue.enqueue("World")
queue.enqueue(100)

print(queue)  # [["Hello", "World"], [42, 100]]

# Process items by type groups
while not queue.is_empty():
    item = queue.dequeue()
    print(f"Processing: {item}")
# Output: Hello, World, 42, 100
```

## 🔧 Advanced Usage

### Queue Operations

```python
from IsraeliQueue import Item, IsraeliQueue

queue = IsraeliQueue()
alice = Item("Alice", 1)
bob = Item("Bob", 1)

# Standard queue operations
queue.enqueue(alice)              # Add to end
queue.enqueue(bob, alice)         # Add near friend
item = queue.dequeue()            # Remove from front
first = queue.peek()              # Look at front without removing

# Queue inspection
print(f"Size: {queue.size()}")                    # Get queue size
print(f"Empty: {queue.is_empty()}")               # Check if empty
print(f"Groups: {queue.get_groups()}")            # Get all group IDs
print(f"VIPs: {queue.items_in_group(1)}")        # Get items by group
```

### Error Handling

```python
from IsraeliQueue import IsraeliQueue, Item

queue = IsraeliQueue()
alice = Item("Alice", 1)
bob = Item("Bob", 1)

try:
    # This will raise ValueError - bob not in queue
    queue.put(alice, bob)
except ValueError as e:
    print(f"Error: {e}")

try:
    # This will raise IndexError - empty queue
    empty_queue = IsraeliQueue()
    empty_queue.dequeue()
except IndexError as e:
    print(f"Error: {e}")
```

## 🎬 Real-World Examples

### Event Management System

```python
# VIP ticketing system
queue = IsraeliQueue()

# Regular attendees arrive first
regular1 = Item("John", group=2)
regular2 = Item("Jane", group=2)
queue.enqueue(regular1)
queue.enqueue(regular2)

# VIP arrives and joins their group
vip1 = Item("Alice", group=1)
vip2 = Item("Bob", group=1)
queue.enqueue(vip1)           # VIP goes to back initially
queue.put(vip2, vip1)         # Second VIP joins first VIP

# Result: [John, Jane, Alice, Bob] - VIPs together at back
```

### Task Processing by Type

```python
# Process different types of tasks
task_queue = IsraeliQueueByType()

# Add mixed tasks
task_queue.enqueue("send_email")
task_queue.enqueue(42)           # Database ID to process
task_queue.enqueue("send_sms") 
task_queue.enqueue({"task": "backup"})
task_queue.enqueue(99)

# Tasks are grouped: [["send_email", "send_sms"], [42, 99], [{"task": "backup"}]]
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=IsraeliQueue --cov-report=term-missing

# Run specific test file
pytest tests/test_israeli_queue.py -v
```

### Test Coverage
- **38 comprehensive tests**
- **97% code coverage**
- Edge cases and error conditions covered
- Performance and integration testing

## 🎯 Applications

1. **🎪 Event Management**: VIP queuing, group ticket processing
2. **🏪 Customer Service**: Loyalty program priorities, group handling  
3. **🎮 Game Development**: Player queuing with clan/guild relationships
4. **📊 Simulation**: Realistic modeling of human queuing behavior
5. **⚙️ Task Processing**: Grouping tasks by type or priority

## 📈 Performance

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| `enqueue()` | O(1) | O(1) |
| `put()` | O(n) | O(1) |
| `dequeue()` | O(1) | O(1) |
| `peek()` | O(1) | O(1) |
| `items_in_group()` | O(n) | O(k) |

## 🛠️ Development

### Setup Development Environment

```bash
git clone https://github.com/YonLiud/Israeli-Queue.git
cd Israeli-Queue
pip install -r requirements-dev.txt
```

### Run Demo

```bash
python demo.py
```

### Code Quality

The project follows modern Python best practices:
- **Type hints** throughout the codebase
- **Comprehensive docstrings** for all public APIs
- **Error handling** with meaningful messages
- **Test-driven development** with high coverage

## 🗺️ Roadmap

- [ ] **Performance optimizations** for large queues
- [ ] **Async/await support** for concurrent operations  
- [ ] **Serialization support** (JSON, pickle)
- [ ] **Priority queue variant** with weighted groups
- [ ] **Visual queue representation** tools
- [ ] **Benchmarking suite** for performance analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE.txt` for more information.

## 📞 Contact & Links

- **Project Link**: [https://github.com/YonLiud/Israeli-Queue](https://github.com/YonLiud/Israeli-Queue)
- **PyPI Package**: [https://pypi.org/project/IsraeliQueue/](https://pypi.org/project/IsraeliQueue/)
- **Issues**: [Report bugs or request features](https://github.com/YonLiud/Israeli-Queue/issues)

## 🏆 Changelog

### v2.0 (Latest)
- ✨ **New**: Comprehensive type hints and improved API
- ✨ **New**: 97% test coverage with robust test suite
- ✨ **New**: Enhanced error handling and validation
- ✨ **New**: Additional utility methods (`peek`, `size`, `get_groups`, etc.)
- 🐛 **Fixed**: Item equality logic and queue insertion behavior
- 📚 **Improved**: Documentation and usage examples

### v1.1
- Initial stable release with basic functionality

---

<p align="center">
  <strong>⭐ Star this repo if you found it useful! ⭐</strong>
</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/YonLiud/Israeli-Queue.svg?style=for-the-badge
[contributors-url]: https://github.com/YonLiud/Israeli-Queue/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/YonLiud/Israeli-Queue.svg?style=for-the-badge
[forks-url]: https://github.com/YonLiud/Israeli-Queue/network/members
[stars-shield]: https://img.shields.io/github/stars/YonLiud/Israeli-Queue.svg?style=for-the-badge
[stars-url]: https://github.com/YonLiud/Israeli-Queue/stargazers
[issues-shield]: https://img.shields.io/github/issues/YonLiud/Israeli-Queue.svg?style=for-the-badge
[issues-url]: https://github.com/YonLiud/Israeli-Queue/issues
[license-shield]: https://img.shields.io/github/license/YonLiud/Israeli-Queue.svg?style=for-the-badge
[license-url]: https://github.com/YonLiud/Israeli-Queue/blob/master/LICENSE.txt
