#How to create a doubly linked list

class DoubleLinkedLink(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None
        self.prevNode = None

# a = DoubleLinkedLink(1)
# b = DoubleLinkedLink(2)
# c = DoubleLinkedLink(3)

# a.nextNode = b
# b.prevNode = a
# b.nextNode = c
# c.prevNode = b
