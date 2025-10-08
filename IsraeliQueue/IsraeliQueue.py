from dataclasses import dataclass
from typing import Any

@dataclass
class Item:
    item: Any
    group: int

    def __eq__(self, other) -> bool:
        if isinstance(other, Item):
            return self.item == other.item and self.group == other.group
        return False
    
    def same_group(self, other) -> bool:
        """Check if this item is in the same group as another item."""
        if isinstance(other, Item):
            return self.group == other.group
        return False
    
    def __repr__(self) -> str:
        return f"Item(item={self.item!r}, group={self.group})"
    
    def __str__(self) -> str:
        return f"Item({self.item}, group={self.group})"
    
    def __hash__(self) -> int:
        return hash((self.item, self.group))


class IsraeliQueue(List[Item]):
    """
    A queue where items can join their friends (same group) in line.
    Items are inserted after the furthest friend in the queue.
    """
    
    def put(self, item: Item, friend: Item) -> None:
        """
        Add an item to the queue next to its friends.
        
        Args:
            item: The item to add to the queue
            friend: An existing item in the queue (used for validation)
            
        Raises:
            ValueError: If friend is not found in the queue
        """
        if friend not in self:
            raise ValueError("Friend not found in queue")
        
        # Find all friends (items with same group as the new item)
        all_friends = [(index, f) for index, f in enumerate(self) if f.same_group(item)]
        
        if not all_friends:
            # No friends in queue, append to end
            self.append(item)
        else:
            # Find the furthest friend and insert after them
            most_far = max(all_friends, key=lambda f: f[0])
            # Insert after the furthest friend (index + 1)
            self.insert(most_far[0] + 1, item)
    
    def enqueue(self, item: Item, friend: Optional[Item] = None) -> None:
        """
        Add an item to the queue. If friend is provided, joins them in line.
        If no friend provided, adds to the end.
        
        Args:
            item: The item to add
            friend: Optional existing item to join
        """
        if friend is None:
            self.append(item)
        else:
            self.append([a])

    def dequeue(self):
        if not self:
            raise IndexError("Cannot dequeue from empty queue")
        if not self[0]:
            raise IndexError("Cannot dequeue from empty subqueue")
        
        result = self[0].pop(0)
        # Remove empty sublists
        if not self[0]:
            self.pop(0)
        return result


