#!/usr/bin/python3
'''singly linked list module'''


class Node:
    '''class to define a node of singly linked list
    Args: data: the private attribute of data of the node
          next_node: private instant attribute of next node
          '''
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''property to retrive private attribute data
        Return: retrived data
        '''
        return self.__data

    @data.setter
    def data(self, value):
        '''property setter to private attribute data
        Args:value: value to be setted in data
        '''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''property to retrive private attribute next_node
        Return: retrived next_node
        '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''property setter to private attribute next_node
        Args: value: value to be setted in next node
        '''
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    '''class to define singly linked list'''
    def __init__(self):
        '''initialization'''
        self.head = None

    def __str__(self):
        '''print statement'''
        my_str = ""
        node = self.head
        while node:
            my_str += str(node.data)
            my_str += '\n'
            node = node.next_node
        return my_str[:-1]

    def sorted_insert(self, value):
        '''public instance method that inserts
        a new Node into the correct sorted position
        in the list (increasing order)
        Args:value: Node value
        '''
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        node = self.head
        while node.next_node and node.next_node.data < value:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node
