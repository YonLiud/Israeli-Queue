from dataclasses import dataclass
from typing import Any, List, Optional, TypeVar, Generic, Union

T = TypeVar('T')

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
            self.put(item, friend)
    
    def dequeue(self) -> Item:
        """
        Remove and return the first item from the queue.
        
        Returns:
            The first item in the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        if not self:
            raise IndexError("Cannot dequeue from empty queue")
        return self.pop(0)
    
    def peek(self) -> Item:
        """
        Return the first item without removing it.
        
        Returns:
            The first item in the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        if not self:
            raise IndexError("Cannot peek empty queue")
        return self[0]
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self) == 0
    
    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self)
    
    def get_groups(self) -> List[int]:
        """Get all unique group numbers in the queue."""
        return list(set(item.group for item in self))
    
    def items_in_group(self, group: int) -> List[Item]:
        """Get all items belonging to a specific group."""
        return [item for item in self if item.group == group]


class IsraeliQueueByType(List[List[Any]]):
    """
    A queue that groups items by their type.
    Items of the same type are grouped together in sublists.
    """
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the queue, grouping by type.
        
        Args:
            item: The item to add to the queue
        """
        item_type = type(item)
        for subqueue in self:
            if subqueue and type(subqueue[0]) == item_type:
                subqueue.append(item)
                return
        # No existing subqueue for this type, create new one
        self.append([item])

    def dequeue(self) -> Any:
        """
        Remove and return the first item from the first non-empty subqueue.
        
        Returns:
            The first item from the first subqueue
            
        Raises:
            IndexError: If the queue is empty
        """
        if not self:
            raise IndexError("Cannot dequeue from empty queue")
        
        # Find first non-empty subqueue
        for i, subqueue in enumerate(self):
            if subqueue:
                result = subqueue.pop(0)
                # Remove empty sublists
                if not subqueue:
                    self.pop(i)
                return result
        
        raise IndexError("Cannot dequeue from empty queue")
    
    def peek(self) -> Any:
        """
        Return the first item without removing it.
        
        Returns:
            The first item from the first subqueue
            
        Raises:
            IndexError: If the queue is empty
        """
        if not self:
            raise IndexError("Cannot peek empty queue")
        
        for subqueue in self:
            if subqueue:
                return subqueue[0]
        
        raise IndexError("Cannot peek empty queue")
    
    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return not self or all(not subqueue for subqueue in self)
    
    def size(self) -> int:
        """Return the total number of items across all subqueues."""
        return sum(len(subqueue) for subqueue in self)
    
    def get_types(self) -> List[type]:
        """Get all types present in the queue."""
        types = []
        for subqueue in self:
            if subqueue:
                types.append(type(subqueue[0]))
        return types
    
    def items_of_type(self, item_type: type) -> List[Any]:
        """Get all items of a specific type."""
        for subqueue in self:
            if subqueue and type(subqueue[0]) == item_type:
                return subqueue.copy()
        return []


