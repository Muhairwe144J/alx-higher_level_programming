#!/usr/bin/python3


class Node:
    
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
    
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
            
    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
