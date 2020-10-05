#Hashing

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    '''해시 구성하는 노드'''

    def __init__(self, key: Any, value: Any, next: Node) -> None:
        '''Initialize'''
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    '''체인법으로 해시 구현'''
    
    def __init__(self, capacity: int) -> None:
        '''Initialize'''
        self.capacity = capacity
        self.table = [None] * self.capacity

    def hash_value(self, key: Any) -> int:
        '''Get hash value'''
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

    def search(self, key: Any) -> Any:
        '''Return value(key=key)'''
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        return None

    def add(self, key: Any, value: Any) -> bool:
        '''Add value(key=key)'''
        hash = self.hash_value(key)
        p = self.table[hash]
        while p is not None:
            if p.key == key:
                return False
            p = p.next
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True

    def remove(self, key: Any) -> bool:
        '''Delete element(key=key)'''
        hash = self.hash_value(key)
        p = self.table[hash]
        pp = None
        while p is not None:
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return True
            pp = p
            p = p.next
        return False

    def dump(self) -> None:
        '''Dump the hash table'''
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end='')
            while p is not None:
                print(f' ->{p.key} ({p.value})', end='')
                p = p.next
            print()
        