from dataclasses import dataclass
from typing import Any

@dataclass
class Item:
    item: any
    group_id: int

    def __eq__(self, other):
        return self.group == other


class IsraeliQueue(list):
    def put(self, item, friend):
        assert friend in self
        all_friends = [(index, f) for index, f in enumerate(self) if f.group == item.group]
        most_far = max(all_friends, key=lambda f: f[0])
        self.insert(most_far[0], item)

