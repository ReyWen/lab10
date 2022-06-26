class Resistor:

    def __init__(self, nominal, power, precision):
        self.nominal = nominal
        self.power = power
        self.precision = precision
        self.next = None
        self.prev = None

    def __str__(self):
        return f'Resistor {self.nominal} Om, {self.power} W, precision {self.precision}'


class LinkedList:
    current = None

    def __init__(self):
        self.head = None

    def __iter__(self):
        return self

    def iterator(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __next__(self):
        if self.current is None:
            self.current = self.head
            return self.current

    def add(self, other):
        node = self.head
        if node is None:
            self.head = other
            return
        while node.next is not None:
            node = node.next
        node.next = other
        other.prev = node

    def print_by_precision(self, precision):
        for node in self.iterator():
            if node.precision >= precision:
                print(node)

    def search_element(self, nominal):
        for node in self.iterator():
            if node.nominal == nominal:
                return node

    def delete_element(self, element):
        if element is self.head:
            self.head = None
        if element.next is None:
            element.prev.next = None
        element.prev.next = element.next
        element.next.prev = element.prev

    def delete_list(self):
        for node in self.iterator():
            node.next, node.prev = None, None
        self.head = None
