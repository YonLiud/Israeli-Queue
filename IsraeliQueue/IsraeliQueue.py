from dataclasses import dataclass
from typing import Any

@dataclass
class Item:
    item: any
    group: int

    def __eq__(self, other):
        return self.group == other


class IsraeliQueue(list):
    def put(self, item, friend):
        assert friend in self
        all_friends = [(index, f) for index, f in enumerate(self) if f.group == item.group]
        most_far = max(all_friends, key=lambda f: f[0])
        self.insert(most_far[0], item)


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


