import copy
from typing import List, Set



class Prefix:
    """Prefix class to store a sequence of itemsets., ie sequence for each customer
    ex: [[1, 2], [1, 3, 4], [5, 6]]
    """

    def __init__(self, itemsets: List[List[int]] = None):
        self.itemsets: List[List[int]] = []
        if itemsets:
            self.itemsets.append(itemsets)

    def add_item_set(self, itemset: List[int]):
        self.itemsets.append(itemset)

    def clone_sequence(self):
        itemsets = copy.deepcopy(self.itemsets)
        prefix = Prefix()
        prefix.itemsets = itemsets
        return prefix

    def __len__(self):
        return len(self.itemsets)
