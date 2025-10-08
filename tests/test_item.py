import pytest
import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from IsraeliQueue.IsraeliQueue import Item


class TestItem:
    """Test cases for the Item class."""
    
    def test_item_creation(self):
        """Test creating an Item instance."""
        item = Item("test", 1)
        assert item.item == "test"
        assert item.group == 1
    
    def test_item_equality_same_group(self):
        """Test that items with same content and group are considered equal."""
        item1 = Item("Alice", 1)
        item2 = Item("Alice", 1)  # Same content and group
        assert item1 == item2
    
    def test_item_equality_different_content(self):
        """Test that items with different content are not equal even in same group."""
        item1 = Item("Alice", 1)
        item2 = Item("Bob", 1)  # Same group, different content
        assert item1 != item2
    
    def test_item_same_group_method(self):
        """Test the same_group method."""
        item1 = Item("Alice", 1)
        item2 = Item("Bob", 1)   # Different content, same group
        item3 = Item("Charlie", 2)  # Different group
        
        assert item1.same_group(item2)  # Same group
        assert not item1.same_group(item3)  # Different group
    
    def test_item_equality_different_group(self):
        """Test that items with different groups are not equal."""
        item1 = Item("Alice", 1)
        item2 = Item("Alice", 2)  # Same content, different group
        assert item1 != item2
    
    def test_item_equality_non_item(self):
        """Test equality comparison with non-Item objects."""
        item = Item("Alice", 1)
        assert item != "Alice"
        assert item != 1
        assert item != None
    
    def test_item_repr(self):
        """Test string representation of Item."""
        item = Item("Alice", 1)
        expected = "Item(item='Alice', group=1)"
        assert repr(item) == expected
    
    def test_item_str(self):
        """Test string conversion of Item."""
        item = Item("Alice", 1)
        expected = "Item(Alice, group=1)"
        assert str(item) == expected
    
    def test_item_hash(self):
        """Test that items can be hashed (for use in sets/dicts)."""
        item1 = Item("Alice", 1)
        item2 = Item("Alice", 1)
        item3 = Item("Bob", 1)
        
        # Same content should have same hash
        assert hash(item1) == hash(item2)
        # Different content should likely have different hash
        assert hash(item1) != hash(item3)
        
        # Should be able to put in set
        item_set = {item1, item2, item3}
        assert len(item_set) == 2  # item1 and item2 are the same
    
    def test_item_with_different_types_same_group(self):
        """Test items containing different data types in same group."""
        items = [
            Item("string", 1),
            Item(42, 1),
            Item([1, 2, 3], 1),
            Item({"key": "value"}, 1),
        ]
        
        # All should be in same group but not equal (different content)
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                assert items[i].same_group(items[j])  # Same group
                assert items[i] != items[j]  # But not equal (different content)