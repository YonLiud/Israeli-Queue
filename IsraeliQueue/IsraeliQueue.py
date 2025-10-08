from dataclasses import dataclass
from typing import Any

@dataclass
class Item:
    item: Any
    group: int

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.group == other.group
        return False


class IsraeliQueue(list):
    def put(self, item, friend):
        if friend not in self:
            raise ValueError("Friend not found in queue")
        
        # Find all friends (items with same group as the new item)
        all_friends = [(index, f) for index, f in enumerate(self) if f.group == item.group]
        
        if not all_friends:
            # No friends in queue, append to end
            self.append(item)
        else:
            # Find the furthest friend and insert after them
            most_far = max(all_friends, key=lambda f: f[0])
            # Insert after the furthest friend (index + 1)
            self.insert(most_far[0] + 1, item)


class IsraeliQueueByType(list):
    def enqueue(self, a):
        for i in range(len(self)):
            if type(self[i][0]) == type(a):
                self[i].append(a)
                break
        else:
            self.append([a])

    def dequeue(self):
        return self.pop(0)


